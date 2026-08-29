"""
generate_factdrop.py — builds iamsaravofficial.com/factdrop

Can be run locally:
    python scripts/factdrop/generate_factdrop.py
Or automatically via GitHub Actions every Thursday.

Preview a future week without publishing anything (dry run):
    python scripts/factdrop/generate_factdrop.py --as-of 2026-09-10
"""

import json, os, sys, html, argparse, shutil
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------------------------
# Config & Path Resolution
# ---------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

SITE_ROOT = os.path.join(REPO_ROOT, "public", "factdrop")
BASE_URL = "https://iamsaravofficial.com/factdrop"
DATA_FILE = os.path.join(SCRIPT_DIR, "factdrop_facts.json")
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")

IST = timezone(timedelta(hours=5, minutes=30))
EPOCH = datetime(2026, 1, 1, 11, 11, tzinfo=IST)          # Post #1's exact publish moment
WEEK = timedelta(days=7)

CATEGORIES = {
    "love":    "Love & Relationships",
    "tech":    "Tech & Internet",
    "history": "History",
    "science": "Science & Space",
    "language":"Language & Words",
    "money":   "Money & Business",
    "mind":    "Mind & Body",
    "food":    "Food & Culture",
    "wild":    "Wild Facts",
}

CATEGORY_DESC = {
    "love":     "The science, history, and odd trivia of who we love and why.",
    "tech":     "How the digital world actually got built \u2014 accidents, hacks, and all.",
    "history":  "Wars, kings, and moments stranger than fiction.",
    "science":  "Space, biology, physics \u2014 the universe's fine print.",
    "language": "Where words actually came from.",
    "money":    "The strange origin stories behind brands, markets, and cash.",
    "mind":     "How your brain quietly runs the show.",
    "food":     "The backstory behind what's on your plate.",
    "wild":     "Doesn't fit anywhere else. Still true.",
}

POLICY_LAST_UPDATED = "28 Aug 2026"

PRIVACY_HTML = f"""<h2>Privacy Policy</h2>
<p>This section (iamsaravofficial.com/factdrop) does not collect any personal information from visitors. No sign-up, no forms, no tracking cookies are currently used.</p>
<p>The like button stores an anonymous count of likes per fact \u2014 no personal or device-identifying information is attached to it. Your browser locally remembers which facts you've already liked, so the button doesn't reset on your next visit; that stays on your device and is never sent to us.</p>
<p>In future, analytics tools (e.g. Google Analytics) or ads (e.g. Google AdSense) may be added to understand site usage. If added, they'll collect aggregate usage data only \u2014 you won't be individually identified. This policy will be updated to reflect that.</p>
<p>External links, including to other parts of iamsaravofficial.com, may be present; we aren't responsible for their privacy practices.</p>
<p class="modal-meta">Last updated: {POLICY_LAST_UPDATED}</p>"""

TERMS_HTML = f"""<h2>Terms</h2>
<p>Facts on this site are original writing \u2014 researched and rewritten in our own words, even when based on someone else's reporting or research. See the Disclaimer for the limits of that process.</p>
<p>The design, layout, and code of this section belong to iamsaravofficial.com.</p>
<p>This section is provided "as is"; no uptime or accuracy guarantee is made.</p>
<p>These terms may change without prior notice.</p>
<p class="modal-meta">Last updated: {POLICY_LAST_UPDATED}</p>"""

DISCLAIMER_HTML = """<h2>Disclaimer</h2>
<p>Fact Drop posts are written for general interest and quick reading \u2014 not as professional, medical, financial, or legal advice.</p>
<p>Facts are researched and checked at the time of writing, then kept deliberately short and simplified for a quick read. Some nuance is necessarily left out.</p>
<p>Understanding of any topic can evolve over time, and mistakes are possible despite best efforts.</p>
<p>Spotted something inaccurate? <a href="https://iamsaravofficial.com/feedback/">Let us know</a>.</p>"""

ABOUT_HTML = """<h2>About Fact Drop</h2>
<p>A weekly dose of genuinely interesting, fact-checked trivia \u2014 one new drop every Thursday, across love, tech, history, science, and more.</p>
<p>Part of <a href="https://iamsaravofficial.com">iamsaravofficial.com</a>, built and maintained by Saravanakumar Murugan.</p>"""

MODALS = {
    "privacy-modal":    PRIVACY_HTML,
    "terms-modal":      TERMS_HTML,
    "disclaimer-modal": DISCLAIMER_HTML,
    "about-modal":      ABOUT_HTML,
}

# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------
def esc(s):
    return html.escape(s or "", quote=True)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def publish_dt(date_str):
    y, m, d = map(int, date_str.split("-"))
    return datetime(y, m, d, 11, 11, tzinfo=IST)

def fail(msg):
    print(f"\n✗ BUILD REFUSED\n{msg}\n", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--as-of", help="Simulate a date (YYYY-MM-DD) instead of using real now(). "
                                     "For previewing a future week. Never use this for a real publish run.")
args = parser.parse_args()

if args.as_of:
    y, m, d = map(int, args.as_of.split("-"))
    now_ist = datetime(y, m, d, 12, 0, tzinfo=IST)  # midday on that date, avoids same-day 11:11 edge ambiguity
    print(f"*** SIMULATED RUN — pretending now = {now_ist.strftime('%a %d %b %Y')} — nothing here is real ***\n")
else:
    now_ist = datetime.now(IST)

# ---------------------------------------------------------------------
# STEP 1 — load + validate schedule integrity
# ---------------------------------------------------------------------
if not os.path.exists(DATA_FILE):
    fail(f"{DATA_FILE} not found at {DATA_FILE}")

facts = json.load(open(DATA_FILE, encoding="utf-8"))
if not facts:
    fail(f"{DATA_FILE} is empty.")

seen_ids, seen_slugs = set(), set()
for i, f in enumerate(facts):
    for field in ("id", "slug", "category", "headline", "body", "publish_date"):
        if field not in f:
            fail(f"Fact at position {i+1} missing required field '{field}'.")
    if f["category"] not in CATEGORIES:
        fail(f"Fact #{i+1} (slug={f['slug']}) has unknown category '{f['category']}'. "
             f"Valid: {', '.join(CATEGORIES)}")

    expected = EPOCH + i * WEEK
    actual = publish_dt(f["publish_date"])
    if actual != expected:
        fail(
            f"SCHEDULE BROKEN at fact #{i+1} (id={f['id']}, slug={f['slug']}):\n"
            f"  publish_date in JSON : {f['publish_date']}  ->  {actual.isoformat()}\n"
            f"  should be            : {expected.date()}  ->  {expected.isoformat()}\n"
            f"  Post {i+1} must land exactly {i} week(s) after post 1 ({EPOCH.date()}).\n"
            f"  Fix {DATA_FILE} — check for a copy-paste date error or a reordered/inserted fact."
        )
    if f["id"] in seen_ids:
        fail(f"Duplicate id '{f['id']}' at position {i+1}.")
    if f["slug"] in seen_slugs:
        fail(f"Duplicate slug '{f['slug']}' at position {i+1}.")
    seen_ids.add(f["id"]); seen_slugs.add(f["slug"])

print(f"[OK] Schedule integrity — {len(facts)} facts, ids/slugs unique, "
      f"every publish_date exactly matches its week position from {EPOCH.date()}")

# ---------------------------------------------------------------------
# Copy static assets (style.css, script.js) into output tree
# ---------------------------------------------------------------------
if not os.path.isdir(ASSETS_DIR):
    fail(f"{ASSETS_DIR} not found at {ASSETS_DIR}")
shutil.copytree(ASSETS_DIR, os.path.join(SITE_ROOT, "assets"), dirs_exist_ok=True)
print(f"[OK] Copied assets -> {SITE_ROOT}/assets/")

# ---------------------------------------------------------------------
# STEP 2 — how many are due
# ---------------------------------------------------------------------
due = [f for f in facts if publish_dt(f["publish_date"]) <= now_ist]

due_by_formula = 0 if now_ist < EPOCH else (now_ist - EPOCH).days // 7 + 1
due_by_formula = min(due_by_formula, len(facts))

if len(due) != due_by_formula:
    fail(
        f"COUNT MISMATCH as of {now_ist.isoformat()}:\n"
        f"  facts.json filter says {len(due)} due\n"
        f"  calendar formula says  {due_by_formula} due\n"
        f"  These must always agree."
    )

print(f"[OK] Due as of {now_ist.strftime('%a %d %b %Y, %H:%M IST')}: "
      f"{len(due)} of {len(facts)} facts (week {len(due)})")

if not due:
    print("Nothing due yet — nothing to build. Exiting clean.")
    sys.exit(0)

due_by_category = {}
for f in due:
    due_by_category.setdefault(f["category"], []).append(f)

# ---------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------
def head(title, description, canonical_path, asset_prefix):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{BASE_URL}{canonical_path}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="article">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset_prefix}assets/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="{asset_prefix}">Fact <span>Drop</span></a>
  <nav>
    <a href="{asset_prefix}">All facts</a>
    <a href="{asset_prefix}categories/">Categories</a>
  </nav>
</header>
"""

def foot(asset_prefix):
    modals_html = "\n".join(
        f"""<div class="modal-overlay" id="{mid}" hidden>
  <div class="modal-box" role="dialog" aria-modal="true">
    <button type="button" class="modal-close" aria-label="Close">&times;</button>
    {content}
  </div>
</div>"""
        for mid, content in MODALS.items()
    )
    return f"""<footer class="site-footer">
  <span>A new drop every Thursday</span>
  <nav class="footer-nav">
    <button type="button" data-modal-target="privacy-modal">Privacy</button>
    <button type="button" data-modal-target="terms-modal">Terms</button>
    <button type="button" data-modal-target="disclaimer-modal">Disclaimer</button>
    <button type="button" data-modal-target="about-modal">About</button>
  </nav>
  <a href="https://iamsaravofficial.com">iamsaravofficial.com</a>
</footer>

{modals_html}

<script src="{asset_prefix}assets/script.js"></script>
</body>
</html>
"""

def share_block(f, url):
    text = f"{f['headline']} — Fact Drop #{f['id']}"
    from urllib.parse import quote
    wa = quote(f"{text}\n{url}")
    xt = quote(text)
    eu = quote(url)
    return f"""<div class="share-row">
  <button class="share-icon share-native" id="share-native" data-url="{esc(url)}" data-text="{esc(text)}" hidden aria-label="Share">Share</button>
  <a class="share-icon" href="https://wa.me/?text={wa}" target="_blank" rel="noopener" aria-label="Share on WhatsApp">WhatsApp</a>
  <a class="share-icon" href="https://twitter.com/intent/tweet?text={xt}&url={eu}" target="_blank" rel="noopener" aria-label="Share on X">X</a>
  <a class="share-icon" href="https://www.facebook.com/sharer/sharer.php?u={eu}" target="_blank" rel="noopener" aria-label="Share on Facebook">Facebook</a>
  <button class="share-icon share-copy" id="share-copy" data-url="{esc(url)}" aria-label="Copy link">Copy link</button>
</div>
"""

# ---------------------------------------------------------------------
# Fact pages: /factdrop/fact/<slug>/
# ---------------------------------------------------------------------
count_fact_pages = 0
for idx, f in enumerate(due):
    ap = "../../"
    url = f"{BASE_URL}/fact/{f['slug']}/"
    cat_label = CATEGORIES[f["category"]]
    prev_f = due[idx - 1] if idx > 0 else None
    next_f = due[idx + 1] if idx < len(due) - 1 else None

    related = [x for x in due_by_category[f["category"]] if x["id"] != f["id"]][:3]
    related_html = "\n".join(
        f'<a class="mini" href="{ap}fact/{r["slug"]}/"><span class="n">#{r["id"]}</span>'
        f'<span class="t">{esc(r["headline"])}</span></a>' for r in related
    ) or '<p class="muted">More in this category coming soon.</p>'

    prev_html = (f'<a class="nav-btn prev" href="{ap}fact/{prev_f["slug"]}/">&larr; #{prev_f["id"]}</a>'
                 if prev_f else '<a class="nav-btn prev disabled" href="#">&larr; Start</a>')
    next_html = (f'<a class="nav-btn next" href="{ap}fact/{next_f["slug"]}/">#{next_f["id"]} &rarr;</a>'
                 if next_f else '<a class="nav-btn next disabled" href="#">Latest &rarr;</a>')

    body = f"""<div class="wrap">
  <div class="eyebrow">
    <a href="{ap}">Fact Drop</a><span class="sep">/</span>
    <a class="cur" href="{ap}category/{f['category']}/">{esc(cat_label)}</a>
  </div>
  <div class="ticket">
    <div class="ticket-stub">
      <span class="stub-num">TIL #{f['id']}</span>
      <span class="stub-cat">{esc(cat_label)}</span>
    </div>
    <div class="ticket-perf"><i></i><i></i></div>
    <div class="ticket-body">
      <h1 class="headline">{esc(f['headline'])}</h1>
      <p class="fact-text">{esc(f['body'])}</p>
      <button type="button" class="like-btn" data-slug="{esc(f['slug'])}" aria-label="Like this fact">
        <span class="like-icon">\U0001F90D</span><span class="like-count">\u2013</span>
      </button>
    </div>
  </div>
  {share_block(f, url)}
  <div class="nav-row">{prev_html}{next_html}</div>
  <div class="section-title">More in {esc(cat_label)}</div>
  {related_html}
</div>
"""
    page = head(f"{f['headline']} — Fact Drop", f['body'][:155], f"/fact/{f['slug']}/", ap) + body + foot(ap)
    write(os.path.join(SITE_ROOT, "fact", f["slug"], "index.html"), page)
    count_fact_pages += 1

print(f"[OK] Fact pages written: {count_fact_pages}")

# ---------------------------------------------------------------------
# Category hub pages
# ---------------------------------------------------------------------
count_hub_pages = 0
for cat_key, cat_facts in due_by_category.items():
    ap = "../../"
    cards = "\n".join(
        f'<a class="fact-card" href="{ap}fact/{f["slug"]}/"><span class="n">TIL #{f["id"]}</span>'
        f'<h2>{esc(f["headline"])}</h2></a>'
        for f in sorted(cat_facts, key=lambda x: -int(x["id"]))
    )
    body = f"""<div class="wrap">
  <div class="eyebrow"><a href="{ap}">Fact Drop</a><span class="sep">/</span><span class="cur">{esc(CATEGORIES[cat_key])}</span></div>
  <h1 class="headline">{esc(CATEGORIES[cat_key])}</h1>
  <div class="fact-grid">{cards}</div>
</div>
"""
    page = head(f"{CATEGORIES[cat_key]} — Fact Drop", f"All Fact Drop posts in {CATEGORIES[cat_key]}.", f"/category/{cat_key}/", ap) + body + foot(ap)
    write(os.path.join(SITE_ROOT, "category", cat_key, "index.html"), page)
    count_hub_pages += 1

print(f"[OK] Category hub pages written: {count_hub_pages}")

# ---------------------------------------------------------------------
# Landing page
# ---------------------------------------------------------------------
ap = ""
recent = sorted(due, key=lambda x: -int(x["id"]))[:12]
recent_html = "\n".join(
    f'<a class="fact-card" href="{ap}fact/{f["slug"]}/"><span class="n">TIL #{f["id"]}</span>'
    f'<h2>{esc(f["headline"])}</h2></a>' for f in recent
)
cat_html = "\n".join(
    f'<a class="cat-card" href="{ap}category/{k}/"><h2>{esc(v)}</h2>'
    f'<span class="count-pill">{len(due_by_category[k])} facts</span></a>'
    for k, v in CATEGORIES.items() if k in due_by_category
)
body = f"""<div class="hero-landing">
  <h1>Fact Drop</h1>
  <p>One fact a week. Every Thursday.</p>
</div>
<div class="wrap">
  <div class="cat-grid">{cat_html}</div>
  <div class="section-title">Latest drops</div>
  <div class="fact-grid">{recent_html}</div>
</div>
"""
page = head("Fact Drop — a new fact every Thursday", "Fact Drop: bite-sized, verified facts across love, tech, history, science and more. New drop every Thursday.", "/", ap) + body + foot(ap)
write(os.path.join(SITE_ROOT, "index.html"), page)
print("[OK] Landing page written")

# ---------------------------------------------------------------------
# All-categories page
# ---------------------------------------------------------------------
ap = "../"
cat_cards_full = "\n".join(
    f'<a class="cat-card" href="{ap}category/{k}/"><h2>{esc(v)}</h2>'
    f'<p class="cat-desc">{esc(CATEGORY_DESC[k])}</p>'
    f'<span class="count-pill">{len(due_by_category[k])} facts</span></a>'
    for k, v in CATEGORIES.items() if k in due_by_category
)
body = f"""<div class="wrap">
  <div class="eyebrow"><a href="{ap}">Fact Drop</a><span class="sep">/</span><span class="cur">Categories</span></div>
  <h1 class="headline">Categories</h1>
  <div class="cat-grid cat-grid-full">{cat_cards_full}</div>
</div>
"""
page = head("Categories — Fact Drop", "Every Fact Drop category, all in one place.", "/categories/", ap) + body + foot(ap)
write(os.path.join(SITE_ROOT, "categories", "index.html"), page)
print(f"[OK] All-categories page written ({len(due_by_category)} categories)")

# ---------------------------------------------------------------------
# sitemap.xml
# ---------------------------------------------------------------------
urls = [f"{BASE_URL}/", f"{BASE_URL}/categories/"]
urls += [f"{BASE_URL}/category/{k}/" for k in due_by_category]
urls += [f"{BASE_URL}/fact/{f['slug']}/" for f in due]

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sitemap.append(f"  <url><loc>{u}</loc></url>")
sitemap.append("</urlset>")
write(os.path.join(SITE_ROOT, "sitemap.xml"), "\n".join(sitemap))
print(f"[OK] sitemap.xml written with {len(urls)} urls")

# ---------------------------------------------------------------------
# FINAL CROSS-CHECK
# ---------------------------------------------------------------------
fact_dir = os.path.join(SITE_ROOT, "fact")
written_fact_files = sum(
    1 for root, _, fs in os.walk(fact_dir) for name in fs if name == "index.html"
)
sitemap_fact_urls = sum(1 for u in urls if "/fact/" in u)

if not (written_fact_files == len(due) == due_by_formula == sitemap_fact_urls):
    fail(
        f"POST-BUILD COUNT MISMATCH:\n"
        f"  files on disk      : {written_fact_files}\n"
        f"  due list length    : {len(due)}\n"
        f"  calendar formula   : {due_by_formula}\n"
        f"  sitemap fact urls  : {sitemap_fact_urls}\n"
        f"  All four must be equal."
    )

print(f"\n[VERIFIED] {written_fact_files} fact pages == due list == calendar formula (week {due_by_formula}) == sitemap. All four agree.")
print(f"DONE.")
