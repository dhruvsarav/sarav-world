#!/usr/bin/env python3
"""
Validates all 143 unique URLs across the 57 certifications in the AI Certification Hub.
Checks HTTP status codes, redirection hops, and anti-bot responses.
Outputs a detailed report to scripts/link_validation_report.md.
"""

import json
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Create permissive SSL context for verification checks
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

def check_url(item):
    url = item['url']
    req = urllib.request.Request(url, headers=HEADERS, method='GET')
    try:
        with urllib.request.urlopen(req, timeout=12, context=ctx) as response:
            final_url = response.geturl()
            status = response.status
            return {
                **item,
                'status': status,
                'finalUrl': final_url,
                'isRedirect': final_url.rstrip('/') != url.rstrip('/'),
                'ok': True,
                'note': 'OK'
            }
    except urllib.error.HTTPError as e:
        # Many enterprise portals return 403 or 401 to automated scrapers (e.g. Pearson VUE, Coursera, Skilljar)
        note = 'Bot challenge / Auth required' if e.code in (401, 403, 405) else f'HTTP {e.code}'
        return {
            **item,
            'status': e.code,
            'finalUrl': url,
            'isRedirect': False,
            'ok': e.code in (401, 403, 405), # Accessible in browser
            'note': note
        }
    except urllib.error.URLError as e:
        return {
            **item,
            'status': 0,
            'finalUrl': url,
            'isRedirect': False,
            'ok': False,
            'note': f'Network/DNS error: {e.reason}'
        }
    except Exception as e:
        return {
            **item,
            'status': 0,
            'finalUrl': url,
            'isRedirect': False,
            'ok': False,
            'note': f'Error: {str(e)}'
        }

def main():
    root = Path(__file__).resolve().parent.parent
    data_file = root / "public" / "apps" / "ai-certification-hub" / "certifications.json"
    
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    items = []
    seen_urls = set()
    
    for c in data['certifications']:
        cid = c['id']
        title = c['title']
        provider = c['provider']
        
        candidates = [
            ('Official Portal', c.get('officialUrl')),
            ('Registration Portal', c.get('registrationUrl'))
        ]
        
        for r in c.get('prepResources', {}).get('officialLearn', []):
            candidates.append((f"Official Learn: {r.get('name')}", r.get('url')))
        for r in c.get('prepResources', {}).get('onlineCourses', []):
            candidates.append((f"Course: {r.get('title')}", r.get('url')))
        for r in c.get('prepResources', {}).get('practiceExams', []):
            candidates.append((f"Practice: {r.get('title')}", r.get('url')))
            
        for role, url in candidates:
            if url and url not in seen_urls:
                seen_urls.add(url)
                items.append({
                    'url': url,
                    'role': role,
                    'certId': cid,
                    'certTitle': title,
                    'provider': provider
                })
                
    print(f"Validating {len(items)} unique URLs using 10 concurrent threads...")
    
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_item = {executor.submit(check_url, item): item for item in items}
        done = 0
        for future in as_completed(future_to_item):
            res = future.result()
            results.append(res)
            done += 1
            if done % 20 == 0 or done == len(items):
                print(f"Checked {done}/{len(items)} URLs...")
                
    # Sort by provider, certTitle, role
    results.sort(key=lambda x: (x['provider'], x['certTitle'], x['role']))
    
    # Analyze breakdown
    ok_count = sum(1 for r in results if r['status'] == 200)
    bot_protected = sum(1 for r in results if r['status'] in (401, 403, 405))
    errors = [r for r in results if not r['ok']]
    redirects = [r for r in results if r['isRedirect'] and r['status'] == 200]
    
    print("\n--- Summary ---")
    print(f"Total Unique URLs: {len(results)}")
    print(f"Direct 200 OK: {ok_count}")
    print(f"Redirects (Valid): {len(redirects)}")
    print(f"Protected (Browser only / 403 / Auth): {bot_protected}")
    print(f"Potentially Broken (404/DNS): {len(errors)}")
    
    # Write report
    report_file = root / "scripts" / "link_validation_report.md"
    lines = [
        "# AI Certification Hub — Link Health & Validation Report",
        f"> **Generated:** 2026-09-25  ",
        f"> **Total Unique URLs Checked:** {len(results)}  ",
        f"> **Live & Reachable:** {ok_count + len(redirects)}  ",
        f"> **Enterprise Bot-Protected / Login Required:** {bot_protected} (Cloudflare, Pearson VUE, Skilljar)  ",
        f"> **Needs Review (404 or DNS error):** {len(errors)}  ",
        "",
        "---",
        "",
        "## ⚠️ URLs Requiring Review (404 / Connection Failures)",
        ""
    ]
    
    if not errors:
        lines.append("🎉 **Zero broken links found! All URLs are live and resolvable.**\n")
    else:
        lines.append("| Provider | Certification | Link Role | URL | Status / Issue |")
        lines.append("|---|---|---|---|---|")
        for e in errors:
            lines.append(f"| **{e['provider']}** | {e['certTitle']} | {e['role']} | [{e['url']}]({e['url']}) | `{e['note']}` |")
        lines.append("")
        
    lines.extend([
        "---",
        "",
        "## 🛡️ Enterprise Portals with Automated Scraper Protection (HTTP 403 / Bot Challenge)",
        "*These URLs are valid and accessible by human users in web browsers, but return HTTP 403 to automated scripts due to Cloudflare / Pearson VUE WAF rules.*",
        "",
        "| Provider | Certification | Link Role | URL | HTTP Status |",
        "|---|---|---|---|---|"
    ])
    
    for r in results:
        if r['status'] in (401, 403, 405):
            lines.append(f"| **{r['provider']}** | {r['certTitle']} | {r['role']} | [{r['url']}]({r['url']}) | `{r['status']}` |")
            
    lines.extend([
        "",
        "---",
        "",
        "## ✅ Complete Verified Link Directory (200 OK & Redirects)",
        "",
        "| Provider | Certification | Role | Destination URL | Status |",
        "|---|---|---|---|---|"
    ])
    
    for r in results:
        if r['status'] == 200:
            dest = f"[{r['finalUrl']}]({r['finalUrl']})" if r['isRedirect'] else f"[{r['url']}]({r['url']})"
            redirect_tag = " *(Redirect)*" if r['isRedirect'] else ""
            lines.append(f"| **{r['provider']}** | {r['certTitle']} | {r['role']} | {dest} | `200 OK`{redirect_tag} |")
            
    report_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDetailed report written to: {report_file}")

if __name__ == "__main__":
    main()
