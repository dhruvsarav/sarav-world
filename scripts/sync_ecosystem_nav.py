#!/usr/bin/env python3
"""
Standardize the Ecosystem Menu across all Sarav's World pages.

Structural block replacement using depth-counted <div> parsing:
locates the exact <div class="ecosystem-links">...</div> span by brace-depth counting,
so nested divs or surrounding code/styles can NEVER corrupt or truncate the file.
Renders shared Jinja macros per page composition, runs maker-checker integrity checks,
and writes to disk only when 100% of checks pass.
"""
import json, re, sys, urllib.parse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parent.parent
PUBLIC = REPO_ROOT / "public"
DATA_FILE = REPO_ROOT / "scripts" / "ecosystem_nav" / "nav.json"
TEMPLATES_DIR = REPO_ROOT / "scripts" / "ecosystem_nav"

nav = json.loads(DATA_FILE.read_text(encoding="utf-8"))
env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
tpl = env.get_template("menus.html.jinja")
ecosystem_links = tpl.module.ecosystem_links

GROUP_SECTIONS = ["apps", "games", "projects"]

PAGES = []
def add(path, mode, sections=None, current_id=None):
    PAGES.append({"path": path, "mode": mode, "sections": sections or [], "current_id": current_id})

# 1. EApps section (12 pages) — mode=['eapps'], single E-Apps dropdown
add("eapps/index.html", ["eapps"], current_id="eapps-hub")
for app_id, dirn in [("dwssharedworkspace","dwssharedworkspace"),
                      ("tokenomics","tokenomics"), ("sdoptimizer","sdoptimizer"),
                      ("fsoptimizer","fsoptimizer"), ("desksidestaffing","desksidestaffing"),
                      ("dexadvisor","dexadvisor"), ("itsmadvisor","itsmadvisor"),
                      ("rfpscorer","rfpscorer"), ("aiinitsm","aiinitsm"),
                      ("automationscore","automationscore"),
                      ("dwpassessment","dwpassessment")]:
    add(f"apps/{dirn}/index.html", ["eapps"], current_id=app_id)

# 2. Apps section (14 pages) — mode=['group'], sections=[apps,games,projects]
add("apps/index.html", ["group"], GROUP_SECTIONS, current_id="apps-hub")
for app_id, dirn in [("genzalphaslang","genzalphaslang"), ("salary-planner","salary-planner"),
                      ("home-budget-planner","home-budget-planner"), ("retirement-planner","retirement-planner"),
                      ("gold-price-estimator","gold-price-estimator"), ("gold-loan-calculator","gold-loan-calculator"),
                      ("digigold-calculator","digigold-calculator"), ("fd-calculator","fd-calculator"),
                      ("rd-calculator","rd-calculator"), ("glow-up-grid","glow-up-grid"),
                      ("lunchbox-planner","lunchbox-planner"), ("study-sprint","study-sprint"),
                      ("piggy-bank-ledger","piggy-bank-ledger"),
                      ("chore-quest-board","chore-quest-board"),
                      ("screen-time-passes","screen-time-passes")]:
    add(f"apps/{dirn}/index.html", ["group"], GROUP_SECTIONS, current_id=app_id)

# 3. Games section (10 pages with navbar) — mode=['group'], sections=[apps,games,projects]
# Note: samosasnatch has no ecosystem bar (designed as 2-player split-screen tap battle)
add("games/index.html", ["group"], GROUP_SECTIONS, current_id="games-hub")
for g in ["familywinner","sentimeter","secretbox","cuptoss","bottleflip",
          "chitcharades","snackroulette","dialoguedetective","gulelstrike"]:
    add(f"games/{g}/index.html", ["group"], GROUP_SECTIONS, current_id=g)

# 4. 4-quadrant gateways (2 pages: playground and projects) — all 4 dropdowns
add("playground/index.html", ["eapps", "group"], GROUP_SECTIONS, current_id=None)
add("projects/index.html", ["eapps", "group"], GROUP_SECTIONS, current_id="projects-hub")

assert len(PAGES) == 40, f"expected 40 pages, got {len(PAGES)}"

# Build the set of internally-resolvable URLs
INTERNAL_OK = set()
for cat, items in nav.items():
    for it in items:
        if not it.get("external"):
            INTERNAL_OK.add(it["url"])
INTERNAL_OK.add("https://iamsaravofficial.com/")

def url_resolves(url):
    if url in INTERNAL_OK:
        if url == "https://iamsaravofficial.com/":
            return True
        path = urllib.parse.urlparse(url).path.strip("/")
        candidate = PUBLIC / path / "index.html"
        return candidate.is_file()
    for cat, items in nav.items():
        for it in items:
            if it["url"] == url and it.get("external"):
                return True
    return False

def find_div_block(html, class_needle):
    """Depth-counted div finder — ensures 100% boundary safety."""
    m = re.search(r'<div class="[^"]*\b' + re.escape(class_needle) + r'\b[^"]*"[^>]*>', html)
    if not m:
        return None
    outer_start = m.start()
    inner_start = m.end()
    depth = 1
    tag_re = re.compile(r'<(/?)div\b[^>]*>')
    for tm in tag_re.finditer(html, inner_start):
        if tm.group(1) == '':
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                inner_end = tm.start()
                outer_end = tm.end()
                return (outer_start, outer_end, inner_start, inner_end)
    return None

def check_rendered(inner_html, cfg):
    errs = []
    current_count = len(re.findall(r'class="current"', inner_html))
    expected_current = 0 if cfg["current_id"] is None else 1
    if current_count != expected_current:
        errs.append(f'expected {expected_current} "current" link(s), found {current_count}')

    if cfg["path"] in ("playground/index.html", "projects/index.html"):
        expected_dropdowns = 4
    elif "eapps" in cfg["mode"]:
        expected_dropdowns = 1
    else:
        expected_dropdowns = 3

    actual_dropdowns = len(re.findall(r'class="eco-dropdown"', inner_html))
    if actual_dropdowns != expected_dropdowns:
        errs.append(f'expected {expected_dropdowns} dropdown(s), found {actual_dropdowns}')

    for am in re.finditer(r'<a href="([^"]+)"[^>]*>([^<]*)</a>', inner_html):
        url, label = am.group(1), am.group(2)
        if url == "https://iamsaravofficial.com/":
            continue
        if not label.strip() or label.strip()[0].isalnum():
            errs.append(f'missing icon on menu item: {url}')
        if not url_resolves(url):
            errs.append(f'broken link: {url}')

    return errs

def main():
    write_changes = "--write" in sys.argv
    report = []
    pending_writes = []

    for cfg in PAGES:
        src_path = PUBLIC / cfg["path"]
        if not src_path.exists():
            report.append((cfg["path"], "FAIL", [f"File not found: {src_path}"]))
            continue

        html = src_path.read_text(encoding="utf-8")
        block = find_div_block(html, "ecosystem-links")
        if not block:
            report.append((cfg["path"], "FAIL", ["ecosystem-links block not found"]))
            continue
        outer_start, outer_end, inner_start, inner_end = block

        active_dropdown = "games" if cfg["path"] == "games/index.html" else None

        if cfg["path"] in ("playground/index.html", "projects/index.html"):
            brand = '<a href="https://iamsaravofficial.com/" class="eco-brand">← Sarav\'s World</a>\n<span class="eco-divider">│</span>\n'
            d = '\n<span class="eco-divider">│</span>\n'
            rendered_inner = (
                brand
                + tpl.module.ecosystem_menu(nav, ["apps"], cfg["current_id"], None) + d
                + tpl.module.eapps_menu(nav, cfg["current_id"]) + d
                + tpl.module.ecosystem_menu(nav, ["games", "projects"], cfg["current_id"], None)
            )
        else:
            rendered_inner = ecosystem_links(
                nav, cfg["mode"], sections=cfg["sections"],
                current_id=cfg["current_id"], active_dropdown=active_dropdown,
            )

        errs = check_rendered(rendered_inner, cfg)
        if errs:
            report.append((cfg["path"], "FAIL", errs))
            continue

        indented = "\n".join(("      " + ln if ln.strip() else ln) for ln in rendered_inner.split("\n"))
        rendered_crlf = indented.replace("\r\n", "\n").replace("\n", "\r\n")
        new_html = html[:inner_start] + "\r\n" + rendered_crlf + "\r\n    " + html[inner_end:]

        pending_writes.append((src_path, new_html))
        report.append((cfg["path"], "OK", []))

    ok_count = sum(1 for _, s, _ in report if s == "OK")
    fail_count = sum(1 for _, s, _ in report if s == "FAIL")
    print(f"\n{ok_count} OK, {fail_count} FAIL out of {len(report)} pages")

    if fail_count > 0:
        for path, status, errs in report:
            if status == "FAIL":
                print(f"  FAIL {path}")
                for e in errs:
                    print(f"       - {e}")
        print("\nIntegrity check failed. ZERO files were written.")
        sys.exit(1)

    if write_changes:
        for path, content in pending_writes:
            path.write_text(content, encoding="utf-8", newline="")
        print(f"Successfully synchronized all {len(pending_writes)} pages in-place.")
    else:
        print("Dry run complete. Pass --write to apply changes in-place.")

if __name__ == "__main__":
    main()
