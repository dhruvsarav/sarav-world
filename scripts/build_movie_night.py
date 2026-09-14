import os
import json

def generate_movie_night():
    out_path = "public/apps/family-movie-night/index.html"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open('scripts/movie_night_data.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    catalog_json_str = json.dumps(catalog, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Family Movie &amp; Board Game Night Decider — Fair Turn Rotator, 100+ Cinema Gems &amp; Printable Tickets | Sarav's World</title>
<meta name="description" content="Free zero-argument Friday night decider for families. Features fair turn rotation between Dad, Mom, and Kids, 100+ curated wholesome movies, 40 top board games with Amazon links (dhrav-21), snack pairing studio, and printable A4 cinema tickets.">
<link rel="canonical" href="https://iamsaravofficial.com/apps/family-movie-night/">

<!-- Open Graph / Social -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://iamsaravofficial.com/apps/family-movie-night/">
<meta property="og:title" content="Family Movie &amp; Board Game Night Decider | Sarav's World">
<meta property="og:description" content="Zero-argument fair turn rotator, 100+ curated family movies across 6 genres, 40 top board games with Amazon links, and printable souvenir tickets.">
<meta property="og:image" content="https://iamsaravofficial.com/apps/family-movie-night/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Family Movie &amp; Board Game Night Decider | Sarav's World">
<meta name="twitter:description" content="Fair turn rotator, 100+ family films, 40 board games, and printable cinema ticket stubs.">
<meta name="twitter:image" content="https://iamsaravofficial.com/apps/family-movie-night/og-image.png">

<!-- Icons -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="favicon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon-180.png">

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
  :root, [data-theme="dark"] {{
    --bg: #0C0F14;
    --surface: #141922;
    --surface-2: #1B222D;
    --surface-3: #222B39;
    --border: #2A3545;
    --border-soft: #1E2633;
    --text: #EAEFF5;
    --text-dim: #94A0B2;
    --text-faint: #5C6B80;
    --accent: #E3A63E;
    --accent-ink: #141005;
    --accent-soft: rgba(227, 166, 62, 0.15);
    --accent2: #2EC4B6;
    --accent2-soft: rgba(46, 196, 182, 0.15);
    --cinema-red: #E50914;
    --cinema-red-soft: rgba(229, 9, 20, 0.15);
    --gold: #F59E0B;
    --purple: #9B5DE5;
    --success: #20BF6B;
    --shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  }}
  [data-theme="light"] {{
    --bg: #F5F7FA;
    --surface: #FFFFFF;
    --surface-2: #F0F3F7;
    --surface-3: #E4E9F0;
    --border: #D1D8E2;
    --border-soft: #E2E8F0;
    --text: #1A202C;
    --text-dim: #4A5568;
    --text-faint: #718096;
    --accent: #D97706;
    --accent-ink: #FFFFFF;
    --accent-soft: rgba(217, 119, 6, 0.14);
    --accent2: #0D9488;
    --accent2-soft: rgba(13, 148, 136, 0.14);
    --cinema-red: #DC2626;
    --cinema-red-soft: rgba(220, 38, 38, 0.14);
    --gold: #D97706;
    --purple: #7C3AED;
    --success: #16A34A;
    --shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font-family: 'Space Grotesk', system-ui, -apple-system, sans-serif;
    -webkit-font-smoothing: antialiased; line-height: 1.5;
  }}
  .mono {{ font-family: 'IBM Plex Mono', ui-monospace, monospace; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  h1, h2, h3, h4 {{ font-family: 'Space Grotesk', sans-serif; margin: 0; font-weight: 600; }}
  p {{ margin: 0 0 0.6em; }}

  /* Ecosystem Bar */
  .ecosystem-bar {{
    background: var(--surface-2); border-bottom: 1px solid var(--border-soft);
    padding: 7px 20px; font-size: 12.5px; color: var(--text-dim);
    position: relative; z-index: 1000;
  }}
  .ecosystem-inner {{
    max-width: 1240px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;
  }}
  .ecosystem-links {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
  .eco-brand {{ font-weight: 700 !important; color: var(--text) !important; text-decoration: none; transition: color 0.15s ease; }}
  .eco-brand:hover {{ color: var(--accent) !important; text-decoration: none; }}
  .eco-divider {{ color: var(--border); margin: 0 2px; }}
  .eco-dropdown {{ position: relative; display: inline-block; }}
  .eco-dropbtn {{
    background: transparent; border: none; color: var(--text-dim); font-size: 12.5px; font-weight: 500;
    cursor: pointer; padding: 4px 6px; display: inline-flex; align-items: center; gap: 4px;
    font-family: inherit; transition: color 0.15s ease;
  }}
  .eco-dropbtn:hover {{ color: var(--text); }}
  .eco-caret {{ font-size: 10px; transition: transform 0.2s ease; }}
  .eco-dropdown.open .eco-caret {{ transform: rotate(180deg); }}
  .eco-menu {{
    position: absolute; top: calc(100% + 8px); left: 0;
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 8px 6px; min-width: 230px; box-shadow: var(--shadow);
    display: none; flex-direction: column; gap: 2px; z-index: 1001;
  }}
  .eco-menu::before {{ content: ""; position: absolute; top: -10px; left: 0; right: 0; height: 10px; }}
  .eco-dropdown:hover .eco-menu, .eco-dropdown.open .eco-menu {{ display: flex; }}
  .eco-menu a {{
    color: var(--text-dim); font-size: 12.5px; padding: 6px 10px; border-radius: 6px;
    text-decoration: none; display: flex; align-items: center; gap: 8px; transition: all 0.15s ease;
  }}
  .eco-menu a:hover {{ color: var(--text); background: var(--surface-2); text-decoration: none; }}
  .eco-menu a.current {{ color: var(--accent); background: var(--accent-soft); font-weight: 600; }}
  .eco-tokenomics {{
    display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px;
    border-radius: 6px; background: var(--accent2-soft); color: var(--accent2) !important;
    font-size: 12px; font-weight: 600; text-decoration: none; border: 1px solid rgba(46, 196, 182, 0.3);
  }}

  /* App Container */
  .container {{ max-width: 1240px; margin: 0 auto; padding: 24px 20px 60px; }}

  /* Hero Section */
  .hero-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px 28px; margin-bottom: 24px; box-shadow: var(--shadow);
  }}
  .header-main-row {{
    display: flex; justify-content: space-between; align-items: flex-start; gap: 20px;
  }}
  .header-left {{
    display: flex; gap: 20px; align-items: center; flex: 1; min-width: 0;
  }}
  .app-icon-box {{
    width: 68px; height: 68px; border-radius: 16px; background: var(--surface-2);
    border: 1px solid var(--border); padding: 6px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 16px rgba(0,0,0,0.25);
  }}
  .app-icon-box img {{ width: 100%; height: 100%; object-fit: contain; border-radius: 10px; }}
  .header-titles {{ flex: 1; min-width: 0; }}
  .eyebrow {{
    font-size: 11.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--accent); margin-bottom: 4px; display: inline-flex; align-items: center; gap: 6px;
  }}
  .header-titles h1 {{ font-size: 25px; font-weight: 700; color: var(--text); line-height: 1.25; margin-bottom: 4px; }}
  .header-titles .sub {{ font-size: 13.5px; color: var(--text-dim); line-height: 1.5; margin: 0; }}
  .header-right {{ flex-shrink: 0; display: flex; flex-direction: column; align-items: flex-end; gap: 10px; }}

  /* Theme Switcher */
  .theme-selector {{
    display: inline-flex; background: var(--surface-2); border: 1px solid var(--border);
    border-radius: 8px; padding: 2px; gap: 2px;
  }}
  .theme-btn {{
    background: transparent; border: none; color: var(--text-dim); font-size: 11.5px;
    font-weight: 600; padding: 5px 10px; border-radius: 6px; cursor: pointer;
    font-family: inherit; transition: all 0.15s ease;
  }}
  .theme-btn:hover {{ color: var(--text); }}
  .theme-btn.active {{ background: var(--accent); color: var(--accent-ink); }}

  /* Mission Presets */
  .header-presets-wrap {{
    margin-top: 20px; padding-top: 18px; border-top: 1px solid var(--border-soft);
    display: flex; align-items: center; justify-content: space-between; gap: 14px; flex-wrap: wrap;
  }}
  .preset-label {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-faint); }}
  .preset-chips {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  .preset-chip {{
    background: var(--surface-2); border: 1px solid var(--border); color: var(--text);
    padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 600;
    cursor: pointer; font-family: inherit; transition: all 0.15s ease; display: inline-flex; align-items: center; gap: 6px;
  }}
  .preset-chip:hover {{ border-color: var(--accent); color: var(--accent); transform: translateY(-1px); }}
  .preset-chip.active {{ background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }}

  /* Universal 4-Action Suite */
  .action-bar {{
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 24px;
  }}
  @media(max-width: 860px) {{ .action-bar {{ grid-template-columns: repeat(2, 1fr); }} }}
  @media(max-width: 480px) {{ .action-bar {{ grid-template-columns: 1fr; }} }}
  .btn-action {{
    display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 12px 14px; font-size: 13px; font-weight: 600; color: var(--text);
    cursor: pointer; font-family: inherit; transition: all 0.15s ease; box-shadow: var(--shadow);
  }}
  .btn-action:hover {{ border-color: var(--accent); color: var(--accent); transform: translateY(-2px); }}
  .btn-action.btn-whatsapp {{ background: rgba(37, 211, 102, 0.12); border-color: rgba(37, 211, 102, 0.35); color: #25D366; }}
  .btn-action.btn-whatsapp:hover {{ background: #25D366; color: #0C0F14; border-color: #25D366; }}
  .btn-action.btn-print {{ background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }}
  .btn-action.btn-print:hover {{ background: var(--accent); color: var(--accent-ink); }}

  /* FRIDAY HARMONY ROTATOR CARD */
  .rotator-card {{
    background: linear-gradient(135deg, var(--surface) 0%, var(--surface-2) 100%);
    border: 1.5px solid var(--accent); border-radius: 18px; padding: 22px 26px;
    margin-bottom: 26px; box-shadow: var(--shadow);
  }}
  .rotator-header {{
    display: flex; justify-content: space-between; align-items: center; gap: 14px;
    margin-bottom: 16px; flex-wrap: wrap;
  }}
  .rotator-crown-badge {{
    display: inline-flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 700;
    color: var(--accent); background: var(--accent-soft); padding: 5px 12px; border-radius: 20px;
    border: 1px solid var(--accent);
  }}
  .family-members-row {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 14px; margin-bottom: 16px;
  }}
  .member-slot {{
    background: var(--surface); border: 1.5px solid var(--border); border-radius: 14px;
    padding: 14px; display: flex; align-items: center; gap: 12px; transition: all 0.2s ease;
    cursor: pointer; position: relative;
  }}
  .member-slot:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  .member-slot.is-active {{
    border-color: var(--accent); background: linear-gradient(180deg, var(--accent-soft) 0%, var(--surface) 100%);
    box-shadow: 0 6px 18px rgba(227, 166, 62, 0.25);
  }}
  .member-avatar {{
    font-size: 30px; width: 44px; height: 44px; border-radius: 50%;
    background: var(--surface-2); display: flex; align-items: center; justify-content: center;
  }}
  .member-info {{ flex: 1; min-width: 0; }}
  .member-name {{ font-size: 14px; font-weight: 700; color: var(--text); }}
  .member-role {{ font-size: 11px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.04em; }}
  .member-veto-tag {{
    font-size: 10px; font-weight: 700; color: var(--cinema-red); background: var(--cinema-red-soft);
    padding: 1px 6px; border-radius: 6px; margin-top: 2px; display: inline-block;
  }}
  .member-crown-icon {{
    position: absolute; top: -10px; right: 10px; font-size: 18px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
  }}

  .rotator-controls {{
    display: flex; gap: 10px; justify-content: space-between; align-items: center; flex-wrap: wrap;
    padding-top: 14px; border-top: 1px solid var(--border-soft);
  }}

  /* MODE SELECTOR (Movies vs Board Games) */
  .mode-selector-card {{
    display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;
    gap: 12px; flex-wrap: wrap;
  }}
  .mode-tabs {{
    display: inline-flex; background: var(--surface-2); border: 1px solid var(--border);
    border-radius: 12px; padding: 4px; gap: 4px;
  }}
  .mode-tab {{
    background: transparent; border: none; color: var(--text-dim); font-size: 13.5px;
    font-weight: 700; padding: 8px 18px; border-radius: 8px; cursor: pointer;
    font-family: inherit; transition: all 0.15s ease; display: inline-flex; align-items: center; gap: 8px;
  }}
  .mode-tab:hover {{ color: var(--text); }}
  .mode-tab.active {{ background: var(--accent); color: var(--accent-ink); }}

  /* MAIN 2-COLUMN DECIDER & SNACK STUDIO */
  .decider-split {{
    display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px; margin-bottom: 28px;
  }}
  @media(max-width: 980px) {{ .decider-split {{ grid-template-columns: 1fr; }} }}

  .card-box {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px; box-shadow: var(--shadow); display: flex; flex-direction: column;
  }}
  .card-box-header {{
    display: flex; justify-content: space-between; align-items: center; gap: 12px;
    margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border-soft);
  }}
  .card-box-title {{ font-size: 16px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 8px; }}

  /* Spotlight Item Details */
  .spotlight-hero-row {{
    display: flex; gap: 18px; align-items: flex-start; margin-bottom: 16px;
  }}
  .spotlight-art-box {{
    width: 80px; height: 110px; border-radius: 12px; background: var(--surface-2);
    border: 1px solid var(--border); display: flex; flex-direction: column; align-items: center;
    justify-content: center; font-size: 38px; flex-shrink: 0; box-shadow: 0 4px 14px rgba(0,0,0,0.3);
  }}
  .spotlight-title-area {{ flex: 1; min-width: 0; }}
  .spotlight-title {{ font-size: 21px; font-weight: 700; color: var(--text); line-height: 1.25; margin-bottom: 6px; }}
  .badge-row {{ display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 12px; align-items: center; }}
  .pill-badge {{
    font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px;
    background: var(--surface-2); border: 1px solid var(--border); color: var(--text-dim);
  }}
  .pill-badge.genre {{ background: var(--accent-soft); color: var(--accent); border-color: var(--accent); }}
  .pill-badge.imdb {{ background: rgba(245, 158, 11, 0.15); color: #F59E0B; border-color: #F59E0B; font-weight: 700; }}
  .pill-badge.platform {{ background: var(--surface-3); color: var(--text); }}

  .spotlight-synopsis {{
    font-size: 13.5px; color: var(--text); line-height: 1.55; margin-bottom: 14px;
    background: var(--surface-2); border: 1px solid var(--border-soft); border-radius: 10px; padding: 12px 14px;
  }}
  .spotlight-best-for {{
    font-size: 12px; color: var(--accent); font-weight: 600; margin-bottom: 16px;
    display: flex; align-items: center; gap: 6px;
  }}

  /* Amazon Buy Box for Board Games */
  .amazon-boardgame-box {{
    background: linear-gradient(135deg, rgba(227, 166, 62, 0.1) 0%, var(--surface-2) 100%);
    border: 1.5px solid var(--accent); border-radius: 12px; padding: 14px; margin-bottom: 16px;
    display: none; flex-direction: column; gap: 8px;
  }}
  .amazon-boardgame-box.show {{ display: flex; }}
  .amazon-head-row {{ display: flex; justify-content: space-between; align-items: center; }}
  .amazon-title {{ font-size: 12.5px; font-weight: 700; color: var(--accent); display: flex; align-items: center; gap: 6px; }}
  .amazon-tag-pill {{
    font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; font-weight: 700;
    background: var(--accent-soft); color: var(--accent); padding: 2px 7px; border-radius: 6px;
  }}
  .btn-amazon-buy {{
    background: #FF9900; color: #111; font-weight: 700; font-size: 13px;
    padding: 9px 16px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    text-decoration: none; transition: all 0.15s ease; border: none; cursor: pointer;
  }}
  .btn-amazon-buy:hover {{ filter: brightness(1.1); transform: translateY(-1px); text-decoration: none; }}

  /* Spotlight Action Buttons */
  .spotlight-actions {{
    display: flex; gap: 8px; flex-wrap: wrap; margin-top: auto;
  }}
  .btn-spotlight-action {{
    flex: 1; min-width: 120px; background: var(--surface-2); border: 1px solid var(--border);
    color: var(--text); padding: 10px 14px; border-radius: 8px; font-size: 12.5px; font-weight: 700;
    cursor: pointer; font-family: inherit; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
    transition: all 0.15s ease;
  }}
  .btn-spotlight-action:hover {{ border-color: var(--accent); color: var(--accent); transform: translateY(-1px); }}
  .btn-spotlight-action.btn-lock {{ background: var(--accent); color: var(--accent-ink); border-color: var(--accent); }}
  .btn-spotlight-action.btn-lock:hover {{ filter: brightness(1.1); }}
  .btn-spotlight-action.btn-veto {{ background: var(--cinema-red-soft); border-color: var(--cinema-red); color: var(--cinema-red); }}
  .btn-spotlight-action.btn-veto:hover {{ background: var(--cinema-red); color: #fff; }}

  /* SNACK PAIRING STUDIO */
  .snacks-list {{ display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px; }}
  .snack-item {{
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 12px;
    padding: 12px 14px; display: flex; align-items: center; gap: 12px; cursor: pointer;
    transition: all 0.15s ease;
  }}
  .snack-item:hover {{ border-color: var(--accent); }}
  .snack-item.selected {{
    border-color: var(--accent); background: linear-gradient(135deg, var(--accent-soft) 0%, var(--surface-2) 100%);
  }}
  .snack-icon {{ font-size: 26px; }}
  .snack-info {{ flex: 1; min-width: 0; }}
  .snack-title {{ font-size: 13px; font-weight: 700; color: var(--text); margin-bottom: 2px; }}
  .snack-desc {{ font-size: 11px; color: var(--text-dim); line-height: 1.35; }}

  /* SHOWTIME & TICKET CLOCK */
  .showtime-box {{
    background: var(--surface-2); border: 1px solid var(--border); border-radius: 12px;
    padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px;
  }}
  .showtime-label {{ font-size: 12px; font-weight: 700; text-transform: uppercase; color: var(--text-faint); }}
  .showtime-select {{
    background: var(--surface); border: 1px solid var(--border); color: var(--text);
    padding: 6px 12px; border-radius: 6px; font-size: 13px; font-weight: 700; font-family: inherit; outline: none;
  }}

  /* 100+ CATALOG & SEARCH EXPLORER */
  .catalog-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px 28px; margin-bottom: 28px; box-shadow: var(--shadow);
  }}
  .catalog-toolbar {{
    display: flex; gap: 12px; align-items: center; margin-bottom: 16px; flex-wrap: wrap;
  }}
  .search-wrap {{ flex: 1; min-width: 240px; position: relative; }}
  .search-icon {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-faint); font-size: 14px; }}
  .catalog-search-input {{
    width: 100%; background: var(--surface-2); border: 1px solid var(--border);
    border-radius: 8px; padding: 10px 14px 10px 36px; color: var(--text); font-size: 13.5px;
    font-family: inherit; outline: none;
  }}
  .catalog-search-input:focus {{ border-color: var(--accent); }}

  .category-filter-chips {{
    display: flex; gap: 8px; overflow-x: auto; padding-bottom: 6px; margin-bottom: 16px;
  }}
  .cat-chip {{
    background: var(--surface-2); border: 1px solid var(--border); color: var(--text-dim);
    padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;
    cursor: pointer; font-family: inherit; white-space: nowrap; transition: all 0.15s ease;
  }}
  .cat-chip:hover {{ color: var(--text); }}
  .cat-chip.active {{ background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }}

  .catalog-grid {{
    display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px;
    max-height: 620px; overflow-y: auto; padding-right: 4px;
  }}
  .catalog-item-card {{
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 12px;
    padding: 14px; display: flex; flex-direction: column; transition: all 0.15s ease; cursor: pointer;
  }}
  .catalog-item-card:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  .catalog-item-card.is-active {{
    border-color: var(--accent); background: linear-gradient(135deg, var(--accent-soft) 0%, var(--surface-2) 100%);
  }}
  .cat-card-top {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; }}
  .cat-card-title {{ font-size: 14px; font-weight: 700; color: var(--text); line-height: 1.3; margin-bottom: 4px; }}
  .cat-card-sub {{ font-size: 11.5px; color: var(--text-dim); margin-bottom: 8px; }}
  .cat-card-desc {{ font-size: 12px; color: var(--text); line-height: 1.4; margin-bottom: 12px; flex: 1; }}
  .cat-card-footer {{ display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: auto; }}

  /* Modals */
  .modal-overlay {{
    position: fixed; inset: 0; background: rgba(0,0,0,0.75); backdrop-filter: blur(4px);
    display: none; align-items: center; justify-content: center; z-index: 2000; padding: 20px;
  }}
  .modal-overlay.open {{ display: flex; }}
  .modal-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 24px; max-width: 480px; width: 100%; box-shadow: var(--shadow);
  }}
  .modal-head {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
  .modal-head h3 {{ font-size: 18px; font-weight: 700; color: var(--text); }}
  .modal-close {{ background: transparent; border: none; color: var(--text-dim); font-size: 22px; cursor: pointer; }}
  .form-group {{ margin-bottom: 14px; }}
  .form-label {{ display: block; font-size: 12px; font-weight: 600; color: var(--text-dim); margin-bottom: 5px; }}
  .form-input {{
    width: 100%; background: var(--surface-2); border: 1px solid var(--border); border-radius: 8px;
    padding: 9px 12px; color: var(--text); font-size: 13.5px; font-family: inherit; outline: none;
  }}
  .form-input:focus {{ border-color: var(--accent); }}

  /* Non-blocking Toast */
  #toast {{
    position: fixed; bottom: 24px; right: 24px; z-index: 3000;
    background: var(--surface-3); border: 1px solid var(--accent); color: var(--text);
    padding: 12px 20px; border-radius: 10px; font-size: 13px; font-weight: 600;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5); display: flex; align-items: center; gap: 8px;
    opacity: 0; transform: translateY(12px); pointer-events: none;
    transition: opacity 0.25s ease, transform 0.25s ease;
  }}
  #toast.show {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}

  /* Standard Footer */
  footer {{
    padding: 36px 20px 48px; text-align: center; color: var(--text-faint); font-size: 12.5px;
    line-height: 1.6; border-top: 1px solid var(--border-soft); margin-top: 40px;
  }}
  footer a {{ color: var(--text-dim); text-decoration: none; }}
  footer a:hover {{ color: var(--accent); text-decoration: underline; }}
  footer b {{ color: var(--text); }}

  /* PRINTABLE A4 CINEMA TICKETS STUBS */
  @media print {{
    body {{ background: #fff !important; color: #000 !important; font-size: 10pt; }}
    .ecosystem-bar, .theme-selector, .header-presets-wrap, .action-bar,
    .rotator-controls, .mode-selector-card, .decider-split, .catalog-card,
    .modal-overlay, #toast, footer {{ display: none !important; }}
    .container {{ max-width: 100% !important; padding: 0 !important; margin: 0 !important; }}
    .hero-card {{ border: none !important; box-shadow: none !important; padding: 0 0 10pt 0 !important; margin-bottom: 12pt !important; border-bottom: 2pt solid #000 !important; }}
    .app-icon-box {{ display: none !important; }}
    .rotator-card {{ border: 1.5pt solid #000 !important; background: #fff !important; box-shadow: none !important; margin-bottom: 16pt !important; }}
    .member-slot {{ border: 1pt solid #000 !important; background: #fff !important; color: #000 !important; }}

    .print-tickets-section {{ display: block !important; }}
    .print-tickets-grid {{
      display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 14pt !important;
    }}
    .print-ticket-stub {{
      border: 2pt dashed #222 !important; border-radius: 8pt !important; padding: 12pt !important;
      background: #fff !important; color: #000 !important; min-height: 160pt !important;
      display: flex !important; flex-direction: column !important; justify-content: space-between !important;
      position: relative !important;
    }}
    .ticket-head {{ font-size: 14pt !important; font-weight: bold !important; text-align: center; border-bottom: 1pt solid #000; padding-bottom: 4pt; }}
    .ticket-body {{ margin: 8pt 0 !important; font-size: 10pt !important; }}
    .ticket-stars {{ text-align: center; font-size: 16pt !important; letter-spacing: 4pt; margin-top: 6pt; }}
    .ticket-stub-rule {{ border-top: 1pt dashed #444; margin-top: 6pt; padding-top: 4pt; font-size: 8pt; text-align: center; }}
    .print-footer-rule {{ display: block !important; text-align: center; margin-top: 16pt; font-size: 8pt; color: #666; }}
  }}
  .print-tickets-section {{ display: none; }}
  .print-footer-rule {{ display: none; }}
</style>
</head>
<body>

<!-- Sarav's World Standardized Ecosystem Navigation Bar -->
<div class="ecosystem-bar">
  <div class="ecosystem-inner">
    <div class="ecosystem-links">
      <a href="https://iamsaravofficial.com/" class="eco-brand">← Sarav's World</a>
      <span class="eco-divider">│</span>

      <div class="eco-dropdown">
        <button class="eco-dropbtn" aria-haspopup="true">Apps <span class="eco-caret">▾</span></button>
        <div class="eco-menu">
          <a href="https://iamsaravofficial.com/apps/">🎡 Playground Hub</a>
          <a href="https://iamsaravofficial.com/apps/genzalphaslang/">🗣️ GenZ & Alpha Slang</a>
          <a href="https://iamsaravofficial.com/apps/salary-planner/">💰 Salary Planner</a>
          <a href="https://iamsaravofficial.com/apps/home-budget-planner/">🏠 Home Budget Planner</a>
          <a href="https://iamsaravofficial.com/apps/retirement-planner/">🌴 Retirement Planner</a>
          <a href="https://iamsaravofficial.com/apps/gold-price-estimator/">🥇 Gold Price Estimator</a>
          <a href="https://iamsaravofficial.com/apps/gold-loan-calculator/">🏦 Gold Loan Calculator</a>
          <a href="https://iamsaravofficial.com/apps/digigold-calculator/">🪙 DigiGold Calculator</a>
          <a href="https://iamsaravofficial.com/apps/fd-calculator/">🔒 FD Calculator</a>
          <a href="https://iamsaravofficial.com/apps/rd-calculator/">🔁 RD Calculator</a>
          <a href="https://iamsaravofficial.com/apps/glow-up-grid/">🌟 Glow Up Grid</a>
          <a href="https://iamsaravofficial.com/apps/lunchbox-planner/">🍱 Lunchbox & Meal Planner</a>
          <a href="https://iamsaravofficial.com/apps/study-sprint/">🎒 Study Sprint & Exam Matrix</a>
          <a href="https://iamsaravofficial.com/apps/piggy-bank-ledger/">🪙 Piggy Bank & Money Ledger</a>
          <a href="https://iamsaravofficial.com/apps/chore-quest-board/">⚔️ Chore & Quest Board</a>
          <a href="https://iamsaravofficial.com/apps/screen-time-passes/">🎟️ Screen-Time Passes</a>
          <a href="https://iamsaravofficial.com/apps/boredom-buster/">🎡 Boredom Buster Wheel</a>
          <a href="https://iamsaravofficial.com/apps/family-movie-night/" class="current">🎬 Family Movie &amp; Game Night</a>
        </div>
      </div>
      <span class="eco-divider">│</span>

      <div class="eco-dropdown">
        <button class="eco-dropbtn" aria-haspopup="true">Games <span class="eco-caret">▾</span></button>
        <div class="eco-menu">
          <a href="https://iamsaravofficial.com/games/">🎰 Games Arcade Hub</a>
          <a href="https://iamsaravofficial.com/games/familywinner/">🎰 Family Jackpot</a>
          <a href="https://iamsaravofficial.com/games/sentimeter/">💖 Senti-Meter</a>
          <a href="https://iamsaravofficial.com/games/secretbox/">🎁 Secret Box</a>
          <a href="https://iamsaravofficial.com/games/cuptoss/">🏓 Ping-Pong Cup Toss</a>
          <a href="https://iamsaravofficial.com/games/bottleflip/">🍾 Bottle Flip Showdown</a>
          <a href="https://iamsaravofficial.com/games/samosasnatch/">⚡ Samosa Snatch</a>
          <a href="https://iamsaravofficial.com/games/chitcharades/">🗣️ Chit-Charades</a>
          <a href="https://iamsaravofficial.com/games/snackroulette/">🎡 Snack Roulette</a>
          <a href="https://iamsaravofficial.com/games/dialoguedetective/">🎙️ Dialogue Detective</a>
          <a href="https://iamsaravofficial.com/games/gulelstrike/">🎯 Desi Gulel Strike</a>
        </div>
      </div>
      <span class="eco-divider">│</span>

      <div class="eco-dropdown">
        <button class="eco-dropbtn" aria-haspopup="true">Projects <span class="eco-caret">▾</span></button>
        <div class="eco-menu">
          <a href="https://iamsaravofficial.com/projects/">🏛️ Projects Hub</a>
          <a href="https://iamsaravofficial.com/temples/">🛕 Temples of Tamil Gods</a>
          <a href="https://iamsaravofficial.com/factdrop/">💡 FactDrop</a>
          <a href="https://iamsaravofficial.com/thirukkural/">📜 Thirukkural Hub</a>
        </div>
      </div>
    </div>

    <a href="https://iamsaravofficial.com/apps/tokenomics/" class="eco-tokenomics">
      <span>🧠 Tokenomics</span>
    </a>
  </div>
</div>

<div class="container">

  <!-- HERO CARD -->
  <div class="hero-card">
    <div class="header-main-row">
      <div class="header-left">
        <div class="app-icon-box">
          <img src="movie-full.png" alt="Family Movie Night Icon">
        </div>
        <div class="header-titles">
          <div class="eyebrow">🎬 Family Planner Suite #08 • Zero-Argument Weekend Harmony</div>
          <h1>Family Movie &amp; Board Game Night Decider</h1>
          <p class="sub">End 45-minute OTT feed arguments. Rotate weekend turns fairly between Dad, Mom, and Kids, discover 100+ vetted family movies and 40 tabletop board games, pair gourmet snacks, and print souvenir cinema tickets.</p>
        </div>
      </div>
      <div class="header-right">
        <div class="theme-selector" id="themeSelector">
          <button type="button" class="theme-btn" data-theme="auto" onclick="setTheme('auto')">Auto</button>
          <button type="button" class="theme-btn" data-theme="light" onclick="setTheme('light')">☀️ Light</button>
          <button type="button" class="theme-btn" data-theme="dark" onclick="setTheme('dark')">🌙 Dark</button>
        </div>
      </div>
    </div>

    <!-- QUICK PRESETS -->
    <div class="header-presets-wrap">
      <span class="preset-label">Quick Presets:</span>
      <div class="preset-chips">
        <button type="button" class="preset-chip active" onclick="applyPreset('all_movies')">🍿 All Cinema Gems (101)</button>
        <button type="button" class="preset-chip" onclick="applyPreset('board_games')">🎲 Top 40 Board Games</button>
        <button type="button" class="preset-chip" onclick="applyPreset('quick_under100')">⏱️ Under 100 Mins (School Night)</button>
        <button type="button" class="preset-chip" onclick="applyPreset('indian_classics')">🇮🇳 Indian Family Cinema</button>
        <button type="button" class="preset-chip" onclick="applyPreset('animal_quests')">🐾 Animal Quests</button>
        <button type="button" class="preset-chip" onclick="applyPreset('retro_80s')">🕰️ Retro 80s/90s Nostalgia</button>
      </div>
    </div>
  </div>

  <!-- UNIVERSAL 4-ACTION SUITE -->
  <div class="action-bar">
    <button type="button" class="btn-action btn-whatsapp" onclick="shareToWhatsApp()">
      <span>💬</span>
      <span>Broadcast Movie Night on WhatsApp</span>
    </button>
    <button type="button" class="btn-action btn-print" onclick="window.print()">
      <span>🖨️</span>
      <span>Print A4 Souvenir Tickets</span>
    </button>
    <button type="button" class="btn-action" onclick="copyMovieSummary()">
      <span>📋</span>
      <span>Copy Selection &amp; Showtime</span>
    </button>
    <button type="button" class="btn-action" onclick="saveAllToStorage()">
      <span>💾</span>
      <span>Save Roster &amp; History</span>
    </button>
  </div>

  <!-- FRIDAY HARMONY ROTATOR -->
  <div class="rotator-card">
    <div class="rotator-header">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 20px;">⚖️</span>
        <h2 style="font-size: 16px; font-weight: 700; color: var(--text);">Friday Harmony Turn Rotator</h2>
      </div>
      <div class="rotator-crown-badge" id="activePickerBadge">
        <span>👑 Active Picker:</span> <span id="activePickerNameDisplay">Kid 1 (Elder Child)</span>
      </div>
    </div>

    <!-- Family Member Slots -->
    <div class="family-members-row" id="familySlotsRow">
      <!-- Generated via JS -->
    </div>

    <div class="rotator-controls">
      <div style="display: flex; gap: 8px; align-items: center;">
        <button type="button" class="preset-chip" onclick="openFamilyModal()" style="margin:0;">
          <span>⚙️ Edit Family Members</span>
        </button>
        <button type="button" class="preset-chip" onclick="resetVetos()" style="margin:0;">
          <span>🔄 Refresh Monthly Vetos</span>
        </button>
      </div>

      <div style="font-size: 12px; color: var(--text-dim);">
        Rule: Each member gets 1 Veto per month. Locking a pick advances turn to the next person.
      </div>
    </div>
  </div>

  <!-- MODE SELECTOR: MOVIES VS BOARD GAMES -->
  <div class="mode-selector-card">
    <div class="mode-tabs">
      <button type="button" class="mode-tab active" id="tabMovies" onclick="switchMode('movies')">
        <span>🍿</span> <span>Family Cinema Gems (101)</span>
      </button>
      <button type="button" class="mode-tab" id="tabGames" onclick="switchMode('board_games')">
        <span>🎲</span> <span>Top Family Board Games (40)</span>
      </button>
    </div>

    <div style="display: flex; align-items: center; gap: 10px;">
      <button type="button" class="preset-chip" onclick="pickRandomSurprise()" style="margin: 0; background: var(--accent-soft); color: var(--accent); border-color: var(--accent);">
        <span>🎲 Surprise Us!</span>
      </button>
    </div>
  </div>

  <!-- MAIN 2-COLUMN: SPOTLIGHT DECIDER + SNACK PAIRING STUDIO -->
  <div class="decider-split">

    <!-- LEFT: ACTIVE SPOTLIGHT CARD -->
    <div class="card-box" id="spotlightCard">
      <div class="card-box-header">
        <div class="card-box-title">
          <span>✨ Tonight's Contender Spotlight</span>
        </div>
        <div style="font-size: 12px; color: var(--text-dim);" id="spotlightChosenBy">
          Chosen by: <b>Dad</b>
        </div>
      </div>

      <div class="spotlight-hero-row">
        <div class="spotlight-art-box" id="spotlightIcon">🎬</div>
        <div class="spotlight-title-area">
          <div class="badge-row" id="spotlightBadgeRow">
            <span class="pill-badge genre" id="spotlightGenre">Animation Classics</span>
            <span class="pill-badge" id="spotlightRating">U / PG</span>
            <span class="pill-badge" id="spotlightRuntime">1h 45m</span>
            <span class="pill-badge imdb" id="spotlightImdb">⭐ 8.4 IMDb</span>
          </div>
          <div class="spotlight-title" id="spotlightTitle">Coco (2017)</div>
          <div style="font-size: 12px; color: var(--text-dim);" id="spotlightVibe">Heartfelt • Music • Tears of Joy</div>
        </div>
      </div>

      <div class="spotlight-synopsis" id="spotlightSynopsis">
        Aspiring musician Miguel enters the Land of the Dead to unlock the real story behind his family's generational music ban.
      </div>

      <div class="spotlight-best-for" id="spotlightBestFor">
        <span>🎯 Best For:</span> <span id="spotlightBestForText">Everyone • Musical families</span>
      </div>

      <!-- Streaming Platforms Row -->
      <div style="margin-bottom: 16px;" id="platformBox">
        <div style="font-size: 11px; font-weight: 700; color: var(--text-faint); text-transform: uppercase; margin-bottom: 6px;">Available on:</div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap;" id="spotlightPlatforms">
          <span class="pill-badge platform">Disney+ Hotstar</span>
        </div>
      </div>

      <!-- AMAZON ASSOCIATES BUY BOX (For Board Games) -->
      <div class="amazon-boardgame-box" id="amazonBoardGameBox">
        <div class="amazon-head-row">
          <div class="amazon-title">
            <span>🛒 Order Board Game on Amazon</span>
          </div>
          <span class="amazon-tag-pill">Tag: dhrav-21</span>
        </div>
        <a href="https://www.amazon.in/s?k=catan+board+game&tag=dhrav-21" target="_blank" rel="noopener noreferrer" class="btn-amazon-buy" id="amazonBuyLink">
          <span>🛍️ Find &amp; Buy on Amazon India</span>
          <span>↗</span>
        </a>
        <div style="font-size: 11px; color: var(--text-faint);">
          Amazon Affiliate Tag: <code>dhrav-21</code>. Small commissions support Sarav's World offline family apps.
        </div>
      </div>

      <!-- CONTROLS & ACTIONS -->
      <div class="spotlight-actions">
        <button type="button" class="btn-spotlight-action btn-lock" onclick="lockInChoice()">
          <span>🔒 Lock In &amp; Advance Turn</span>
        </button>
        <button type="button" class="btn-spotlight-action btn-veto" onclick="callVeto()">
          <span>✋ Call Veto (1 Left)</span>
        </button>
        <button type="button" class="btn-spotlight-action" onclick="pickRandomSurprise()">
          <span>🎲 Spin Next</span>
        </button>
      </div>
    </div>

    <!-- RIGHT: SNACK & SHOWTIME STUDIO -->
    <div class="card-box">
      <div class="card-box-header">
        <div class="card-box-title">
          <span>🍿 Gourmet Snack &amp; Showtime Studio</span>
        </div>
      </div>

      <!-- Showtime Select -->
      <div class="showtime-box" style="margin-bottom: 16px;">
        <span class="showtime-label">Showtime:</span>
        <select class="showtime-select" id="showtimeSelect" onchange="onShowtimeChange(this.value)">
          <option value="7:00 PM">7:00 PM (Early Bird)</option>
          <option value="7:30 PM">7:30 PM</option>
          <option value="8:00 PM" selected>8:00 PM (Prime Time)</option>
          <option value="8:30 PM">8:30 PM</option>
          <option value="9:00 PM">9:00 PM (Weekend Late)</option>
        </select>
      </div>

      <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; color: var(--text-faint); margin-bottom: 8px;">
        Select Tonight's Snack Pairing:
      </div>

      <div class="snacks-list" id="snacksList">
        <!-- Rendered by JS -->
      </div>
    </div>

  </div>

  <!-- 100+ CATALOG & SEARCH EXPLORER -->
  <div class="catalog-card">
    <div class="card-box-header">
      <div class="card-box-title">
        <span id="catalogSectionTitle">📚 Explore 101 Curated Family Movies</span>
      </div>
    </div>

    <div class="catalog-toolbar">
      <div class="search-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" class="catalog-search-input" id="catalogSearchInput" placeholder="Search by title, vibe, actors, or keywords..." oninput="onSearchInput(this.value)">
      </div>
    </div>

    <div class="category-filter-chips" id="catFilterChips">
      <!-- Injected by JS -->
    </div>

    <div class="catalog-grid" id="catalogGrid">
      <!-- Injected by JS -->
    </div>
  </div>

</div>

<!-- PRINTABLE A4 CINEMA TICKETS SECTION -->
<div class="print-tickets-section">
  <div style="text-align: center; margin-bottom: 16pt;">
    <h2 style="font-size: 18pt; margin: 0 0 4pt;">🎟️ SARAV FAMILY CINEMA &amp; TABLETOP NIGHT</h2>
    <p style="font-size: 9.5pt; color: #444; margin: 0;">Official Souvenir Family Passes • Cut along dashed lines • Fill stars after the show!</p>
  </div>

  <div class="print-tickets-grid" id="printTicketsGrid">
    <!-- Populated by JS -->
  </div>

  <div class="print-footer-rule">
    Sarav's World Family Movie &amp; Board Game Decider • https://iamsaravofficial.com/apps/family-movie-night/ • Zero Arguments, 100% Family Harmony
  </div>
</div>

<!-- MANAGE FAMILY MEMBERS MODAL -->
<div class="modal-overlay" id="familyModal" onclick="if(event.target===this)closeFamilyModal()">
  <div class="modal-card">
    <div class="modal-head">
      <h3>👨‍👩‍👧‍👦 Manage Family Roster</h3>
      <button type="button" class="modal-close" onclick="closeFamilyModal()">&times;</button>
    </div>
    <div id="modalMembersList" style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px;">
      <!-- Populated by JS -->
    </div>
    <button type="button" class="preset-chip" onclick="addNewFamilyMember()" style="width: 100%; justify-content: center; margin-bottom: 16px;">
      <span>➕ Add Another Member</span>
    </button>
    <div style="display: flex; justify-content: flex-end; gap: 10px;">
      <button type="button" class="btn-spotlight-action" onclick="closeFamilyModal()">Done</button>
    </div>
  </div>
</div>

<!-- NON-BLOCKING TOAST NOTIFICATION -->
<div id="toast"></div>

<footer>
  <div style="max-width: 800px; margin: 0 auto;">
    <p><b>Sarav's World — Family Movie &amp; Board Game Night Decider</b></p>
    <p>100% Client-Side Privacy • Zero Telemetry • LocalStorage Persistence</p>
    <p style="font-size: 11.5px; color: var(--text-faint);">
      Amazon Associates Disclosure: As an Amazon Associate, Sarav's World earns from qualifying purchases made via links featuring tracking ID <code>dhrav-21</code>.
    </p>
    <p><a href="https://iamsaravofficial.com/apps/">Back to Playground Hub</a> │ <a href="https://iamsaravofficial.com/">Sarav's World Home</a></p>
  </div>
</footer>

<script>
// RAW DATA INJECTION
const DATA = {catalog_json_str};

// STATE
let state = {{
  mode: 'movies', // 'movies' or 'board_games'
  currentCategory: 'all',
  searchQuery: '',
  selectedItem: DATA.movies[0],
  selectedSnack: DATA.snacks[0],
  showtime: '8:00 PM',
  activeMemberIndex: 0,
  familyMembers: [
    {{ name: 'Dad', role: 'Parent', emoji: '👨', vetos: 1 }},
    {{ name: 'Mom', role: 'Parent', emoji: '👩', vetos: 1 }},
    {{ name: 'Kid 1', role: 'Elder Child', emoji: '👦', vetos: 1 }},
    {{ name: 'Kid 2', role: 'Younger Child', emoji: '👧', vetos: 1 }}
  ],
  watchHistory: []
}};

// Web Audio API
let audioCtx = null;
function getAudioCtx() {{
  if (!audioCtx) {{
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) audioCtx = new AudioContext();
  }}
  if (audioCtx && audioCtx.state === 'suspended') {{
    audioCtx.resume();
  }}
  return audioCtx;
}}

function playChime(success = true) {{
  try {{
    const ctx = getAudioCtx();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = success ? 'triangle' : 'sawtooth';
    osc.frequency.setValueAtTime(success ? 600 : 250, ctx.currentTime);
    if (success) {{
      osc.frequency.exponentialRampToValueAtTime(1200, ctx.currentTime + 0.15);
    }} else {{
      osc.frequency.exponentialRampToValueAtTime(150, ctx.currentTime + 0.2);
    }}
    gain.gain.setValueAtTime(0.1, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.25);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.26);
  }} catch (e) {{}}
}}

// TOAST
let toastTimer = null;
function showToast(msg) {{
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.innerHTML = msg;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {{
    toast.classList.remove('show');
  }}, 2800);
}}

// THEME
function setTheme(mode) {{
  document.querySelectorAll('#themeSelector .theme-btn').forEach(b => {{
    b.classList.toggle('active', b.dataset.theme === mode);
  }});
  if (mode === 'auto') {{
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
    localStorage.removeItem('fmn_theme');
  }} else {{
    document.documentElement.setAttribute('data-theme', mode);
    localStorage.setItem('fmn_theme', mode);
  }}
}}

// LOAD / SAVE STORAGE
function loadFromStorage() {{
  try {{
    const saved = localStorage.getItem('family_movie_night_v1');
    if (saved) {{
      const parsed = JSON.parse(saved);
      if (parsed.familyMembers) state.familyMembers = parsed.familyMembers;
      if (parsed.activeMemberIndex !== undefined) state.activeMemberIndex = parsed.activeMemberIndex;
      if (parsed.watchHistory) state.watchHistory = parsed.watchHistory;
      if (parsed.showtime) state.showtime = parsed.showtime;
    }}
    const savedTheme = localStorage.getItem('fmn_theme');
    if (savedTheme) setTheme(savedTheme);
  }} catch (e) {{}}
}}

function saveAllToStorage() {{
  try {{
    const toSave = {{
      familyMembers: state.familyMembers,
      activeMemberIndex: state.activeMemberIndex,
      watchHistory: state.watchHistory,
      showtime: state.showtime
    }};
    localStorage.setItem('family_movie_night_v1', JSON.stringify(toSave));
    showToast('💾 Family roster, turn rotation &amp; history saved!');
  }} catch (e) {{
    showToast('⚠️ Storage error');
  }}
}}

// ROTATOR LOGIC
function renderFamilySlots() {{
  const container = document.getElementById('familySlotsRow');
  if (!container) return;
  container.innerHTML = '';

  const activeMember = state.familyMembers[state.activeMemberIndex] || state.familyMembers[0];
  document.getElementById('activePickerNameDisplay').textContent = activeMember.name + ' (' + activeMember.role + ')';

  state.familyMembers.forEach((mem, idx) => {{
    const isCurrent = idx === state.activeMemberIndex;
    const slot = document.createElement('div');
    slot.className = 'member-slot' + (isCurrent ? ' is-active' : '');
    slot.onclick = function() {{
      state.activeMemberIndex = idx;
      renderFamilySlots();
      updateSpotlightChosenBy();
      saveAllToStorage();
      playChime(true);
      showToast('👑 Passed turn to: <b>' + mem.name + '</b>');
    }};

    slot.innerHTML = `
      ${{isCurrent ? '<div class="member-crown-icon">👑</div>' : ''}}
      <div class="member-avatar">${{mem.emoji || '👤'}}</div>
      <div class="member-info">
        <div class="member-name">${{mem.name}}</div>
        <div class="member-role">${{mem.role}}</div>
        <div class="member-veto-tag">Vetos: ${{mem.vetos || 0}} left</div>
      </div>
    `;
    container.appendChild(slot);
  }});
}}

function lockInChoice() {{
  const curMember = state.familyMembers[state.activeMemberIndex];
  const item = state.selectedItem;

  state.watchHistory.unshift({{
    title: item.title,
    type: state.mode,
    pickedBy: curMember.name,
    date: new Date().toLocaleDateString()
  }});

  // Advance turn to next member
  state.activeMemberIndex = (state.activeMemberIndex + 1) % state.familyMembers.length;
  const nextMember = state.familyMembers[state.activeMemberIndex];

  renderFamilySlots();
  updateSpotlightChosenBy();
  saveAllToStorage();
  playChime(true);
  showToast('🔒 <b>' + item.title + '</b> locked in! Crown passed to <b>' + nextMember.name + '</b> for next week!');
}}

function callVeto() {{
  const curMember = state.familyMembers[state.activeMemberIndex];
  if (!curMember.vetos || curMember.vetos <= 0) {{
    playChime(false);
    showToast('❌ ' + curMember.name + ' has 0 vetos remaining this month!');
    return;
  }}

  curMember.vetos -= 1;
  playChime(false);
  showToast('✋ <b>VETO CALLED!</b> ' + curMember.name + ' used a veto. Rolling new candidate...');
  pickRandomSurprise();
  renderFamilySlots();
  saveAllToStorage();
}}

function resetVetos() {{
  state.familyMembers.forEach(m => m.vetos = 1);
  renderFamilySlots();
  saveAllToStorage();
  showToast('🔄 Monthly vetos reset to 1 per member!');
}}

function updateSpotlightChosenBy() {{
  const curMember = state.familyMembers[state.activeMemberIndex];
  document.getElementById('spotlightChosenBy').innerHTML = 'Chosen by: <b>' + curMember.name + ' (' + curMember.role + ')</b>';
}}

// MODE SWITCHER (Movies vs Board Games)
function switchMode(newMode) {{
  state.mode = newMode;
  document.getElementById('tabMovies').classList.toggle('active', newMode === 'movies');
  document.getElementById('tabGames').classList.toggle('active', newMode === 'board_games');

  const titleElem = document.getElementById('catalogSectionTitle');
  if (newMode === 'movies') {{
    titleElem.textContent = '🍿 Explore 101 Curated Family Movies';
    state.selectedItem = DATA.movies[0];
  }} else {{
    titleElem.textContent = '🎲 Explore 40 Top Family Board Games';
    state.selectedItem = DATA.board_games[0];
  }}

  state.currentCategory = 'all';
  renderCatFilterChips();
  renderCatalog();
  renderSpotlight();
  populatePrintTickets();
}}

// SPOTLIGHT RENDERING
function renderSpotlight() {{
  const item = state.selectedItem;
  if (!item) return;

  const isMovie = state.mode === 'movies';

  document.getElementById('spotlightTitle').textContent = item.title + (item.year ? ' (' + item.year + ')' : '');
  document.getElementById('spotlightIcon').textContent = isMovie ? '🎬' : '🎲';
  document.getElementById('spotlightGenre').textContent = item.genre || item.category;

  const ratingPill = document.getElementById('spotlightRating');
  ratingPill.textContent = isMovie ? item.rating : (item.age + ' Age');

  const runtimePill = document.getElementById('spotlightRuntime');
  runtimePill.textContent = isMovie ? item.runtime : (item.time + ' Playtime');

  const imdbPill = document.getElementById('spotlightImdb');
  if (isMovie && item.imdb) {{
    imdbPill.textContent = '⭐ ' + item.imdb + ' IMDb';
    imdbPill.style.display = 'inline-block';
  }} else if (!isMovie && item.players) {{
    imdbPill.textContent = '👥 ' + item.players;
    imdbPill.style.display = 'inline-block';
  }} else {{
    imdbPill.style.display = 'none';
  }}

  document.getElementById('spotlightVibe').textContent = isMovie ? (item.vibe || '') : (item.players + ' • ' + item.category);
  document.getElementById('spotlightSynopsis').textContent = isMovie ? item.synopsis : item.desc;

  const bestForBox = document.getElementById('spotlightBestFor');
  if (isMovie && item.bestFor) {{
    bestForBox.style.display = 'flex';
    document.getElementById('spotlightBestForText').textContent = item.bestFor;
  }} else {{
    bestForBox.style.display = 'none';
  }}

  // Platforms row
  const platformBox = document.getElementById('platformBox');
  const platformContainer = document.getElementById('spotlightPlatforms');
  if (isMovie && Array.isArray(item.platforms) && item.platforms.length > 0) {{
    platformBox.style.display = 'block';
    platformContainer.innerHTML = item.platforms.map(p => `<span class="pill-badge platform">${{p}}</span>`).join('');
  }} else {{
    platformBox.style.display = 'none';
  }}

  // Amazon Buy Box (for board games)
  const amazonBox = document.getElementById('amazonBoardGameBox');
  if (!isMovie) {{
    amazonBox.classList.add('show');
    const q = encodeURIComponent(item.amazon || item.title);
    const aLink = 'https://www.amazon.in/s?k=' + q + '&tag=dhrav-21';
    const buyBtn = document.getElementById('amazonBuyLink');
    buyBtn.href = aLink;
  }} else {{
    amazonBox.classList.remove('show');
  }}

  updateSpotlightChosenBy();
}}

function pickRandomSurprise() {{
  const pool = state.mode === 'movies' ? DATA.movies : DATA.board_games;
  const filtered = pool.filter(i => {{
    if (state.currentCategory !== 'all') {{
      const cat = i.genre || i.category;
      if (cat !== state.currentCategory) return false;
    }}
    return true;
  }});

  if (filtered.length === 0) return;
  const rand = filtered[Math.floor(Math.random() * filtered.length)];
  state.selectedItem = rand;
  renderSpotlight();
  renderCatalog();
  populatePrintTickets();
  playChime(true);
  showToast('🎲 Selected: <b>' + rand.title + '</b>');
}}

// SNACKS STUDIO
function renderSnacks() {{
  const list = document.getElementById('snacksList');
  if (!list) return;
  list.innerHTML = '';

  DATA.snacks.forEach(snk => {{
    const isSel = state.selectedSnack && state.selectedSnack.id === snk.id;
    const item = document.createElement('div');
    item.className = 'snack-item' + (isSel ? ' selected' : '');
    item.onclick = function() {{
      state.selectedSnack = snk;
      renderSnacks();
      populatePrintTickets();
      showToast('🍿 Paired with: <b>' + snk.title + '</b>');
    }};

    item.innerHTML = `
      <div class="snack-icon">${{snk.icon}}</div>
      <div class="snack-info">
        <div class="snack-title">${{snk.title}} (${{snk.prep}})</div>
        <div class="snack-desc">${{snk.desc}}</div>
      </div>
    `;
    list.appendChild(item);
  }});
}}

function onShowtimeChange(val) {{
  state.showtime = val;
  populatePrintTickets();
  showToast('⏰ Showtime set to: ' + val);
}}

// CATALOG & CATEGORY FILTERS
function renderCatFilterChips() {{
  const container = document.getElementById('catFilterChips');
  if (!container) return;
  container.innerHTML = '';

  const isMovie = state.mode === 'movies';
  const categories = isMovie
    ? ['all', 'Animation Classics', 'Adventure & Wonder', 'Animal Quests', 'Retro 80s/90s Classics', 'Wholesome Sci-Fi', 'Indian Family Cinema']
    : ['all', 'Strategy & Gateway', 'Party & Word Laughter', 'Party & Fast Cards', 'Sibling Co-op', 'Classic Tabletop', 'Family Strategy'];

  categories.forEach(cat => {{
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'cat-chip' + (state.currentCategory === cat ? ' active' : '');
    btn.textContent = cat === 'all' ? (isMovie ? 'All Movies (101)' : 'All Games (40)') : cat;
    btn.onclick = function() {{
      state.currentCategory = cat;
      renderCatFilterChips();
      renderCatalog();
    }};
    container.appendChild(btn);
  }});
}}

function renderCatalog() {{
  const grid = document.getElementById('catalogGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const pool = state.mode === 'movies' ? DATA.movies : DATA.board_games;
  const q = state.searchQuery.toLowerCase().trim();

  const filtered = pool.filter(item => {{
    const cat = item.genre || item.category;
    if (state.currentCategory !== 'all' && cat !== state.currentCategory) return false;
    if (q) {{
      const haystack = (item.title + ' ' + cat + ' ' + (item.vibe || '') + ' ' + (item.synopsis || item.desc || '')).toLowerCase();
      if (!haystack.includes(q)) return false;
    }}
    return true;
  }});

  if (filtered.length === 0) {{
    grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-faint);">No titles matched your query.</div>';
    return;
  }}

  filtered.forEach(item => {{
    const isMovie = state.mode === 'movies';
    const isSelected = state.selectedItem && state.selectedItem.id === item.id;
    const card = document.createElement('div');
    card.className = 'catalog-item-card' + (isSelected ? ' is-active' : '');
    card.onclick = function() {{
      state.selectedItem = item;
      renderSpotlight();
      renderCatalog();
      populatePrintTickets();
      window.scrollTo({{ top: 380, behavior: 'smooth' }});
      showToast('🎯 Spotlight loaded: <b>' + item.title + '</b>');
    }};

    const catName = item.genre || item.category;
    const subLine = isMovie ? (item.runtime + ' • ' + (item.rating || 'U') + (item.imdb ? ' • ⭐ ' + item.imdb : '')) : (item.players + ' • ' + item.time);
    const desc = isMovie ? item.synopsis : item.desc;

    card.innerHTML = `
      <div class="cat-card-top">
        <span style="font-size: 20px;">${{isMovie ? '🎬' : '🎲'}}</span>
        <span class="pill-badge genre" style="font-size: 10.5px;">${{catName}}</span>
      </div>
      <div class="cat-card-title">${{item.title}}${{item.year ? ' (' + item.year + ')' : ''}}</div>
      <div class="cat-card-sub">${{subLine}}</div>
      <div class="cat-card-desc">${{desc.length > 90 ? desc.slice(0, 87) + '…' : desc}}</div>
      <div class="cat-card-footer">
        <span style="font-size: 11px; font-weight: 700; color: var(--accent);">${{isSelected ? '✓ Selected' : 'Tap to Select'}}</span>
        ${{!isMovie ? `<a href="https://www.amazon.in/s?k=${{encodeURIComponent(item.amazon || item.title)}}&tag=dhrav-21" target="_blank" rel="noopener noreferrer" class="pill-badge" style="color: var(--accent); text-decoration: none;" onclick="event.stopPropagation()">🛒 Buy</a>` : ''}}
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function onSearchInput(val) {{
  state.searchQuery = val;
  renderCatalog();
}}

// PRESETS
function applyPreset(preset) {{
  document.querySelectorAll('.header-presets-wrap .preset-chip').forEach(p => p.classList.remove('active'));
  if (event && event.target) event.target.classList.add('active');

  if (preset === 'all_movies') {{
    switchMode('movies');
  }} else if (preset === 'board_games') {{
    switchMode('board_games');
  }} else if (preset === 'quick_under100') {{
    switchMode('movies');
    state.searchQuery = '';
    const quickOnes = DATA.movies.filter(m => {{
      const match = m.runtime.match(/(\\d+)h\\s*(\\d+)m/);
      if (match) {{
        const mins = parseInt(match[1]) * 60 + parseInt(match[2]);
        return mins <= 100;
      }}
      return false;
    }});
    if (quickOnes.length > 0) state.selectedItem = quickOnes[0];
    renderSpotlight();
    showToast('⏱️ Showing films under 100 minutes!');
  }} else if (preset === 'indian_classics') {{
    switchMode('movies');
    state.currentCategory = 'Indian Family Cinema';
    renderCatFilterChips();
    renderCatalog();
    const ind = DATA.movies.find(m => m.genre === 'Indian Family Cinema');
    if (ind) state.selectedItem = ind;
    renderSpotlight();
  }} else if (preset === 'animal_quests') {{
    switchMode('movies');
    state.currentCategory = 'Animal Quests';
    renderCatFilterChips();
    renderCatalog();
    const anim = DATA.movies.find(m => m.genre === 'Animal Quests');
    if (anim) state.selectedItem = anim;
    renderSpotlight();
  }} else if (preset === 'retro_80s') {{
    switchMode('movies');
    state.currentCategory = 'Retro 80s/90s Classics';
    renderCatFilterChips();
    renderCatalog();
    const ret = DATA.movies.find(m => m.genre === 'Retro 80s/90s Classics');
    if (ret) state.selectedItem = ret;
    renderSpotlight();
  }}
}}

// 4-ACTION SUITE HANDLERS
function shareToWhatsApp() {{
  const curMember = state.familyMembers[state.activeMemberIndex];
  const item = state.selectedItem;
  const snack = state.selectedSnack;
  const isMovie = state.mode === 'movies';

  const text = `🎬 *FAMILY WEEKEND GATHERING ANNOUNCEMENT!*
━━━━━━━━━━━━━━━━━━━━━━
👑 *Tonight's Picker:* ${{curMember.name}} (${{curMember.role}})
${{isMovie ? '🍿 *Featured Movie:*' : '🎲 *Featured Board Game:*'}} *${{item.title}}*${{item.year ? ' (' + item.year + ')' : ''}}
📂 *Category:* ${{item.genre || item.category}}
⏱️ *Runtime / Duration:* ${{item.runtime || item.time}}
${{item.platforms ? '📺 *Platform:* ' + item.platforms.join(', ') : ''}}

⏰ *Showtime:* ${{state.showtime}} sharp!
🍽️ *Snack Pairing:* ${{snack ? snack.title + ' (' + snack.icon + ')' : 'Stovetop Popcorn'}}

${{!isMovie ? '🛒 Amazon Link: https://www.amazon.in/s?k=' + encodeURIComponent(item.amazon || item.title) + '&tag=dhrav-21\\n' : ''}}
🛋️ *Gather in living room on time!*
Generated with Sarav's World Family Movie Decider:
https://iamsaravofficial.com/apps/family-movie-night/`;

  const url = 'https://api.whatsapp.com/send?text=' + encodeURIComponent(text);
  window.open(url, '_blank');
}}

function copyMovieSummary() {{
  const curMember = state.familyMembers[state.activeMemberIndex];
  const item = state.selectedItem;
  const snack = state.selectedSnack;

  const text = `🎬 Tonight: ${{item.title}}${{item.year ? ' (' + item.year + ')' : ''}}
👑 Chosen by: ${{curMember.name}}
⏰ Showtime: ${{state.showtime}}
🍿 Snack: ${{snack.title}}
https://iamsaravofficial.com/apps/family-movie-night/`;

  navigator.clipboard.writeText(text).then(() => {{
    showToast('📋 Summary copied to clipboard!');
  }}).catch(() => {{
    showToast('⚠️ Could not copy to clipboard');
  }});
}}

// POPULATE PRINT SOUVENIR TICKETS
function populatePrintTickets() {{
  const container = document.getElementById('printTicketsGrid');
  if (!container) return;
  container.innerHTML = '';

  const item = state.selectedItem || DATA.movies[0];
  const snack = state.selectedSnack || DATA.snacks[0];
  const showtime = state.showtime;

  state.familyMembers.forEach((mem, idx) => {{
    const div = document.createElement('div');
    div.className = 'print-ticket-stub';
    div.innerHTML = `
      <div class="ticket-head">★ ADMIT ONE ★</div>
      <div class="ticket-body">
        <div><b>ATTENDEE:</b> ${{mem.name}} (${{mem.role}})</div>
        <div><b>EVENT:</b> ${{item.title}}</div>
        <div><b>SHOWTIME:</b> ${{showtime}} • SEAT #${{idx + 1}}</div>
        <div><b>TREAT:</b> ${{snack.title}}</div>
      </div>
      <div>
        <div style="font-size: 8.5pt; text-align: center; color: #444;">Rate after watching:</div>
        <div class="ticket-stars">☆ ☆ ☆ ☆ ☆</div>
      </div>
      <div class="ticket-stub-rule">
        ✂️ Sarav Family Cinema • Admit 1 • No Screen Arguments Allowed!
      </div>
    `;
    container.appendChild(div);
  }});
}}

// FAMILY MANAGEMENT MODAL
function openFamilyModal() {{
  renderModalMembers();
  document.getElementById('familyModal').classList.add('open');
}}

function closeFamilyModal() {{
  document.getElementById('familyModal').classList.remove('open');
  renderFamilySlots();
  saveAllToStorage();
}}

function renderModalMembers() {{
  const list = document.getElementById('modalMembersList');
  if (!list) return;
  list.innerHTML = '';

  state.familyMembers.forEach((mem, idx) => {{
    const row = document.createElement('div');
    row.style.display = 'flex';
    row.style.gap = '8px';
    row.style.alignItems = 'center';

    row.innerHTML = `
      <input type="text" class="form-input" style="width: 50px; text-align: center;" value="${{mem.emoji}}" onchange="state.familyMembers[${{idx}}].emoji=this.value">
      <input type="text" class="form-input" style="flex: 1;" value="${{mem.name}}" onchange="state.familyMembers[${{idx}}].name=this.value">
      <input type="text" class="form-input" style="width: 90px;" value="${{mem.role}}" onchange="state.familyMembers[${{idx}}].role=this.value">
      ${{state.familyMembers.length > 2 ? `<button type="button" class="preset-chip" style="color: var(--cinema-red); margin:0;" onclick="removeFamilyMember(${{idx}})">✕</button>` : ''}}
    `;
    list.appendChild(row);
  }});
}}

function addNewFamilyMember() {{
  state.familyMembers.push({{
    name: 'Family Member ' + (state.familyMembers.length + 1),
    role: 'Guest',
    emoji: '👤',
    vetos: 1
  }});
  renderModalMembers();
}}

function removeFamilyMember(idx) {{
  state.familyMembers.splice(idx, 1);
  if (state.activeMemberIndex >= state.familyMembers.length) {{
    state.activeMemberIndex = 0;
  }}
  renderModalMembers();
}}

// INITIALIZATION
window.addEventListener('DOMContentLoaded', () => {{
  loadFromStorage();
  renderFamilySlots();
  renderCatFilterChips();
  renderCatalog();
  renderSpotlight();
  renderSnacks();
  populatePrintTickets();
}});
</script>

</body>
</html>"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Built {out_path} successfully ({len(html_content)} bytes).")

if __name__ == "__main__":
    generate_movie_night()
