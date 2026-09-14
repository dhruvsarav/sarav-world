import os
import json

def generate_boredom_buster():
    out_path = "public/apps/boredom-buster/index.html"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Load 122 activities
    with open('scripts/activities_data.json', 'r', encoding='utf-8') as f:
        activities_data = json.load(f)
    
    activities_json_str = json.dumps(activities_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Kids' Screen-Free "I'm Bored" Adventure Wheel — 120+ Offline Missions, Weekend Bingo &amp; Printable Jar Slips | Sarav's World</title>
<meta name="description" content="Free screen-free adventure generator for kids ages 4–14. Spin the tactile mission wheel across 120+ zero-mess crafts, STEM experiments, active obstacle quests, and 4x4 weekend bingo. Includes printable A4 cut-out jar tokens.">
<link rel="canonical" href="https://iamsaravofficial.com/apps/boredom-buster/">

<!-- Open Graph / Social -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://iamsaravofficial.com/apps/boredom-buster/">
<meta property="og:title" content="Kids' Screen-Free 'I'm Bored' Adventure Wheel | Sarav's World">
<meta property="og:description" content="120+ screen-free missions, tactile spin wheel, 4x4 weekend bingo, Web Audio sound effects, and printable fridge jar cut-outs.">
<meta property="og:image" content="https://iamsaravofficial.com/apps/boredom-buster/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Kids' Screen-Free 'I'm Bored' Adventure Wheel | Sarav's World">
<meta name="twitter:description" content="Tactile screen-free spin wheel, 120+ offline missions, weekend bingo, and printable fridge jar tokens.">
<meta name="twitter:image" content="https://iamsaravofficial.com/apps/boredom-buster/og-image.png">

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
    --accent: #FF9F1C;
    --accent-ink: #140E04;
    --accent-soft: rgba(255, 159, 28, 0.15);
    --accent2: #2EC4B6;
    --accent2-soft: rgba(46, 196, 182, 0.15);
    --purple: #9B5DE5;
    --purple-soft: rgba(155, 93, 229, 0.15);
    --coral: #FF5E7E;
    --coral-soft: rgba(255, 94, 126, 0.15);
    --green: #20BF6B;
    --green-soft: rgba(32, 191, 107, 0.15);
    --blue: #3A86FF;
    --blue-soft: rgba(58, 134, 255, 0.15);
    --danger: #E2665A;
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
    --accent: #E07A00;
    --accent-ink: #FFFFFF;
    --accent-soft: rgba(224, 122, 0, 0.14);
    --accent2: #0D9488;
    --accent2-soft: rgba(13, 148, 136, 0.14);
    --purple: #7C3AED;
    --purple-soft: rgba(124, 58, 237, 0.14);
    --coral: #E11D48;
    --coral-soft: rgba(225, 29, 72, 0.14);
    --green: #16A34A;
    --green-soft: rgba(22, 163, 74, 0.14);
    --blue: #2563EB;
    --blue-soft: rgba(37, 99, 235, 0.14);
    --danger: #DC2626;
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

  /* 2-COLUMN MAIN LAYOUT: Wheel Spinner & Active Spotlight */
  .spinner-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 28px;
  }}
  @media(max-width: 960px) {{ .spinner-grid {{ grid-template-columns: 1fr; }} }}

  .card-box {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px; box-shadow: var(--shadow); display: flex; flex-direction: column;
  }}
  .card-box-header {{
    display: flex; justify-content: space-between; align-items: center; gap: 12px;
    margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border-soft);
  }}
  .card-box-title {{ font-size: 16px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 8px; }}

  /* Wheel Container */
  .wheel-wrapper {{
    position: relative; width: 100%; max-width: 420px; aspect-ratio: 1; margin: 0 auto;
    display: flex; align-items: center; justify-content: center;
  }}
  #wheelCanvas {{
    width: 100%; height: 100%; border-radius: 50%;
    filter: drop-shadow(0 10px 24px rgba(0,0,0,0.4));
    transition: filter 0.3s ease;
  }}
  .wheel-pointer {{
    position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
    width: 0; height: 0;
    border-left: 16px solid transparent; border-right: 16px solid transparent;
    border-top: 32px solid var(--accent);
    filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));
    z-index: 20; pointer-events: none;
  }}
  .wheel-center-btn {{
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 90px; height: 90px; border-radius: 50%;
    background: var(--surface-2); border: 4px solid var(--accent);
    color: var(--text); font-weight: 700; font-size: 13px; text-transform: uppercase;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    cursor: pointer; z-index: 25; box-shadow: 0 4px 18px rgba(0,0,0,0.6);
    transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }}
  .wheel-center-btn:hover {{
    transform: translate(-50%, -50%) scale(1.08); background: var(--accent); color: var(--accent-ink);
  }}
  .wheel-center-btn:active {{
    transform: translate(-50%, -50%) scale(0.95);
  }}
  .wheel-center-btn .spin-icon {{ font-size: 22px; line-height: 1; margin-bottom: 2px; }}

  .wheel-controls-row {{
    display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-top: 18px; flex-wrap: wrap;
  }}
  .select-custom {{
    background: var(--surface-2); border: 1px solid var(--border); color: var(--text);
    padding: 7px 12px; border-radius: 8px; font-size: 12.5px; font-family: inherit; outline: none;
  }}
  .select-custom:focus {{ border-color: var(--accent); }}

  /* Active Mission Spotlight Card */
  .spotlight-mission {{
    display: flex; flex-direction: column; height: 100%;
  }}
  .mission-hero-top {{
    display: flex; gap: 16px; align-items: flex-start; margin-bottom: 16px;
  }}
  .mission-big-icon {{
    width: 64px; height: 64px; border-radius: 16px; background: var(--surface-2);
    border: 1.5px solid var(--border); display: flex; align-items: center; justify-content: center;
    font-size: 34px; flex-shrink: 0; box-shadow: 0 4px 14px rgba(0,0,0,0.25);
  }}
  .mission-heading-wrap {{ flex: 1; min-width: 0; }}
  .mission-title {{ font-size: 19px; font-weight: 700; color: var(--text); line-height: 1.3; margin-bottom: 6px; }}
  .cat-badge {{
    display: inline-flex; align-items: center; gap: 5px; font-size: 11px; font-weight: 700;
    padding: 3px 9px; border-radius: 12px; text-transform: uppercase; letter-spacing: 0.04em;
  }}
  .cat-energy {{ background: var(--coral-soft); color: var(--coral); border: 1px solid var(--coral); }}
  .cat-craft {{ background: var(--purple-soft); color: var(--purple); border: 1px solid var(--purple); }}
  .cat-stem {{ background: var(--accent2-soft); color: var(--accent2); border: 1px solid var(--accent2); }}
  .cat-quiet {{ background: var(--blue-soft); color: var(--blue); border: 1px solid var(--blue); }}
  .cat-nature {{ background: var(--green-soft); color: var(--green); border: 1px solid var(--green); }}
  .cat-family {{ background: var(--accent-soft); color: var(--accent); border: 1px solid var(--accent); }}

  .meta-chips-row {{
    display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;
  }}
  .meta-chip {{
    font-size: 11.5px; font-weight: 600; padding: 4px 10px; border-radius: 6px;
    background: var(--surface-2); border: 1px solid var(--border); color: var(--text-dim);
    display: inline-flex; align-items: center; gap: 5px;
  }}

  .section-block {{
    background: var(--surface-2); border: 1px solid var(--border-soft); border-radius: 12px;
    padding: 14px 16px; margin-bottom: 12px;
  }}
  .section-block-title {{
    font-size: 11.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;
    color: var(--text-faint); margin-bottom: 6px; display: flex; align-items: center; gap: 6px;
  }}
  .section-block-content {{ font-size: 13.5px; color: var(--text); line-height: 1.55; }}

  /* Amazon Affiliate Box */
  .amazon-box {{
    background: linear-gradient(135deg, rgba(255, 159, 28, 0.08) 0%, var(--surface-2) 100%);
    border: 1.5px solid var(--accent); border-radius: 12px; padding: 14px 16px; margin-top: auto;
    display: flex; flex-direction: column; gap: 8px;
  }}
  .amazon-box-header {{
    display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap;
  }}
  .amazon-title {{ font-size: 12px; font-weight: 700; color: var(--accent); display: flex; align-items: center; gap: 6px; }}
  .amazon-tag-badge {{
    font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; font-weight: 700;
    background: var(--accent-soft); color: var(--accent); padding: 2px 7px; border-radius: 6px;
  }}
  .btn-amazon-primary {{
    background: #FF9900; color: #111; font-weight: 700; font-size: 12.5px;
    padding: 9px 16px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    text-decoration: none; transition: all 0.15s ease; border: none; cursor: pointer;
  }}
  .btn-amazon-primary:hover {{ filter: brightness(1.1); transform: translateY(-1px); text-decoration: none; }}
  .amazon-subtext {{ font-size: 11px; color: var(--text-faint); line-height: 1.35; }}

  /* Mission Toolbar */
  .mission-actions-row {{
    display: flex; gap: 8px; margin-top: 14px; flex-wrap: wrap;
  }}
  .btn-mission-sub {{
    flex: 1; min-width: 110px; background: var(--surface-2); border: 1px solid var(--border);
    color: var(--text); padding: 8px 12px; border-radius: 8px; font-size: 12px; font-weight: 600;
    cursor: pointer; font-family: inherit; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
    transition: all 0.15s ease;
  }}
  .btn-mission-sub:hover {{ border-color: var(--accent); color: var(--accent); }}
  .btn-mission-sub.btn-completed.active {{ background: var(--green-soft); border-color: var(--green); color: var(--green); }}

  /* 4x4 WEEKEND BINGO CARD */
  .bingo-card-container {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px 28px; margin-bottom: 28px; box-shadow: var(--shadow);
  }}
  .bingo-header {{
    display: flex; justify-content: space-between; align-items: center; gap: 14px;
    margin-bottom: 18px; flex-wrap: wrap;
  }}
  .bingo-stats {{
    display: flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 600;
  }}
  .bingo-progress-bar {{
    width: 140px; height: 8px; background: var(--surface-2); border-radius: 4px; overflow: hidden;
    border: 1px solid var(--border-soft);
  }}
  .bingo-progress-fill {{ height: 100%; background: linear-gradient(90deg, var(--accent2), var(--accent)); transition: width 0.3s ease; }}

  .bingo-grid {{
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
  }}
  @media(max-width: 720px) {{ .bingo-grid {{ grid-template-columns: repeat(2, 1fr); }} }}

  .bingo-tile {{
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 12px;
    padding: 14px 12px; display: flex; flex-direction: column; align-items: center; text-align: center;
    cursor: pointer; transition: all 0.18s ease; position: relative; min-height: 120px;
    justify-content: center; user-select: none;
  }}
  .bingo-tile:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  .bingo-tile.completed {{
    background: linear-gradient(135deg, rgba(32, 191, 107, 0.15) 0%, var(--surface-2) 100%);
    border-color: var(--green); color: var(--text-dim);
  }}
  .bingo-tile.completed .tile-title {{ text-decoration: line-through; opacity: 0.8; }}
  .tile-icon {{ font-size: 26px; margin-bottom: 6px; }}
  .tile-title {{ font-size: 12px; font-weight: 600; color: var(--text); line-height: 1.35; }}
  .tile-check-icon {{
    position: absolute; top: 6px; right: 6px; font-size: 14px; color: var(--green); display: none;
  }}
  .bingo-tile.completed .tile-check-icon {{ display: block; }}

  /* 122-ACTIVITY CATALOG & SEARCH EXPLORER */
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
    max-height: 600px; overflow-y: auto; padding-right: 4px;
  }}
  .catalog-item-card {{
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 12px;
    padding: 14px; display: flex; flex-direction: column; transition: all 0.15s ease;
  }}
  .catalog-item-card:hover {{ border-color: var(--accent2); transform: translateY(-2px); }}
  .cat-item-top {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }}
  .cat-item-title {{ font-size: 13.5px; font-weight: 700; color: var(--text); line-height: 1.35; margin-bottom: 4px; }}
  .cat-item-desc {{ font-size: 12px; color: var(--text-dim); line-height: 1.45; margin-bottom: 10px; flex: 1; }}
  .cat-item-footer {{ display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-top: auto; }}
  .btn-cat-mini {{
    background: var(--surface-3); border: 1px solid var(--border); color: var(--text);
    padding: 5px 10px; border-radius: 6px; font-size: 11px; font-weight: 600;
    cursor: pointer; font-family: inherit; text-decoration: none; display: inline-flex; align-items: center; gap: 4px;
  }}
  .btn-cat-mini:hover {{ border-color: var(--accent); color: var(--accent); text-decoration: none; }}

  /* Modal Overlay */
  .modal-overlay {{
    position: fixed; inset: 0; background: rgba(0,0,0,0.75); backdrop-filter: blur(4px);
    display: none; align-items: center; justify-content: center; z-index: 2000; padding: 20px;
  }}
  .modal-overlay.open {{ display: flex; }}
  .modal-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 24px; max-width: 520px; width: 100%; box-shadow: var(--shadow);
    max-height: 90vh; overflow-y: auto;
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
  .form-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}

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

  /* PRINT VIEW: HIGH CONTRAST BLACK & WHITE FRIDGE POSTER */
  @media print {{
    body {{ background: #fff !important; color: #000 !important; font-size: 10pt; }}
    .ecosystem-bar, .theme-selector, .header-presets-wrap, .action-bar,
    .spinner-grid, .catalog-card, .modal-overlay, #toast, footer {{ display: none !important; }}
    .container {{ max-width: 100% !important; padding: 0 !important; margin: 0 !important; }}
    .hero-card {{ border: none !important; box-shadow: none !important; padding: 0 0 10pt 0 !important; margin-bottom: 12pt !important; border-bottom: 2pt solid #000 !important; }}
    .app-icon-box {{ display: none !important; }}

    /* Bingo Print Sheet */
    .bingo-card-container {{
      border: 1.5pt solid #000 !important; box-shadow: none !important;
      padding: 10pt !important; margin-bottom: 16pt !important; background: #fff !important;
      page-break-after: always;
    }}
    .bingo-grid {{
      grid-template-columns: repeat(4, 1fr) !important; gap: 6pt !important;
    }}
    .bingo-tile {{
      border: 1pt solid #000 !important; background: #fff !important; color: #000 !important;
      min-height: 80pt !important; padding: 6pt !important;
    }}
    .bingo-tile.completed {{ background: #eee !important; }}
    .bingo-tile .tile-title {{ color: #000 !important; font-size: 9pt !important; }}

    .print-jar-slips-section {{ display: block !important; }}
    .print-slips-grid {{
      display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 8pt !important;
    }}
    .print-slip-box {{
      border: 1.5pt dashed #444 !important; padding: 8pt !important; border-radius: 4pt !important;
      background: #fff !important; color: #000 !important; min-height: 90pt !important;
      display: flex !important; flex-direction: column !important; justify-content: space-between !important;
    }}
    .print-slip-title {{ font-weight: bold !important; font-size: 9pt !important; margin-bottom: 4pt !important; }}
    .print-slip-desc {{ font-size: 8pt !important; line-height: 1.3 !important; color: #222 !important; }}
    .print-slip-meta {{ font-size: 7.5pt !important; color: #666 !important; margin-top: 4pt !important; }}
    .print-footer-rule {{ display: block !important; text-align: center; margin-top: 14pt; font-size: 8pt; color: #666; }}
  }}
  .print-jar-slips-section {{ display: none; }}
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
          <a href="https://iamsaravofficial.com/apps/boredom-buster/" class="current">🎡 Boredom Buster Wheel</a>
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
          <img src="wheel-full.png" alt="Boredom Buster Wheel Icon">
        </div>
        <div class="header-titles">
          <div class="eyebrow">🎡 Family Planner Suite #07 • Screen-Free Adventure Engine</div>
          <h1>Kids' Screen-Free "I'm Bored" Adventure Wheel</h1>
          <p class="sub">Turn complaints into instant real-world quests. Spin the tactile mission wheel across 122 zero-prep adventures, conquer the 4x4 Screen-Free Weekend Bingo, and print DIY cut-out jar slips for your fridge.</p>
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

    <!-- MISSION PRESET FILTERS -->
    <div class="header-presets-wrap">
      <span class="preset-label">Quick Presets:</span>
      <div class="preset-chips">
        <button type="button" class="preset-chip active" onclick="applyPreset('all')">🌟 All Adventures (122)</button>
        <button type="button" class="preset-chip" onclick="applyPreset('quick')">⚡ 0–2 Min Zero Prep</button>
        <button type="button" class="preset-chip" onclick="applyPreset('action')">🌋 Living Room Action</button>
        <button type="button" class="preset-chip" onclick="applyPreset('craft')">🎨 Mess-Free Studio</button>
        <button type="button" class="preset-chip" onclick="applyPreset('stem')">🔬 Kitchen STEM Lab</button>
        <button type="button" class="preset-chip" onclick="applyPreset('sibling')">🤝 Sibling Co-op</button>
        <button type="button" class="preset-chip" onclick="applyPreset('nature')">🌿 Balcony &amp; Nature</button>
      </div>
    </div>
  </div>

  <!-- UNIVERSAL 4-ACTION SUITE -->
  <div class="action-bar">
    <button type="button" class="btn-action btn-whatsapp" onclick="shareMissionWhatsApp()">
      <span>💬</span>
      <span>Share Mission on WhatsApp</span>
    </button>
    <button type="button" class="btn-action btn-print" onclick="window.print()">
      <span>🖨️</span>
      <span>Print Fridge Jar Slips &amp; Bingo</span>
    </button>
    <button type="button" class="btn-action" onclick="copyActiveMission()">
      <span>📋</span>
      <span>Copy Mission Summary</span>
    </button>
    <button type="button" class="btn-action" onclick="saveAllToStorage()">
      <span>💾</span>
      <span>Save Progress to Storage</span>
    </button>
  </div>

  <!-- MAIN SPINNER & SPOTLIGHT GRID -->
  <div class="spinner-grid">

    <!-- LEFT: ADVENTURE WHEEL SPINNER -->
    <div class="card-box">
      <div class="card-box-header">
        <div class="card-box-title">
          <span>🎯 Spin the Adventure Wheel</span>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;">
          <button type="button" id="soundToggleBtn" class="theme-btn" onclick="toggleSound()" title="Toggle Web Audio Ticks">🔊 Sound ON</button>
        </div>
      </div>

      <div class="wheel-wrapper">
        <div class="wheel-pointer"></div>
        <canvas id="wheelCanvas" width="800" height="800"></canvas>
        <button type="button" class="wheel-center-btn" id="spinCenterBtn" onclick="spinWheel()">
          <span class="spin-icon">🎲</span>
          <span>SPIN!</span>
        </button>
      </div>

      <div class="wheel-controls-row">
        <select class="select-custom" id="wheelCategorySelect" onchange="onCategoryFilterChange(this.value)">
          <option value="all">Category: All 6 Categories</option>
          <option value="High Energy & Action">🚀 High Energy & Action</option>
          <option value="Creative & Craft Studio">🎨 Creative & Craft</option>
          <option value="STEM & Kitchen">🔬 STEM & Kitchen</option>
          <option value="Quiet Focus & Brain Quests">🧩 Quiet Focus</option>
          <option value="Nature & Balcony Safari">🌿 Nature & Balcony</option>
          <option value="Family & Sibling Challenges">🤝 Sibling & Family</option>
        </select>

        <button type="button" class="preset-chip" onclick="instantSurprise()" style="margin: 0;">
          <span>⚡ Instant Surprise</span>
        </button>
      </div>
    </div>

    <!-- RIGHT: ACTIVE MISSION SPOTLIGHT -->
    <div class="card-box spotlight-mission" id="missionSpotlightBox">
      <div class="card-box-header">
        <div class="card-box-title">
          <span>✨ Current Screen-Free Mission</span>
        </div>
        <button type="button" class="btn-mission-sub" id="btnFavActive" onclick="toggleFavoriteCurrent()" style="flex: none; min-width: auto; padding: 4px 10px;">
          <span>⭐</span> <span id="favText">Favorite</span>
        </button>
      </div>

      <div class="mission-hero-top">
        <div class="mission-big-icon" id="spotlightIcon">🌋</div>
        <div class="mission-heading-wrap">
          <div id="spotlightCatBadge" class="cat-badge cat-energy">🚀 High Energy</div>
          <div class="mission-title" id="spotlightTitle">Living Room 'Floor is Lava' Obstacle Island</div>
        </div>
      </div>

      <div class="meta-chips-row" id="spotlightMetaRow">
        <div class="meta-chip"><span>⏱️</span> <span id="spotlightPrep">0 min prep</span></div>
        <div class="meta-chip"><span>✨</span> <span id="spotlightMess">Zero Mess</span></div>
        <div class="meta-chip"><span>⚡</span> <span id="spotlightEnergy">High Energy</span></div>
        <div class="meta-chip"><span>👥</span> <span id="spotlightMode">Solo or Sibling</span></div>
      </div>

      <div class="section-block">
        <div class="section-block-title"><span>🎒</span> What You Need</div>
        <div class="section-block-content" id="spotlightNeeds">Cushions, pillows, small towels, or cardboard squares.</div>
      </div>

      <div class="section-block">
        <div class="section-block-title"><span>🎮</span> How to Play</div>
        <div class="section-block-content" id="spotlightPlay">Scatter cushions across the living room carpet. Move from the sofa to the kitchen doorway without your feet touching the bare floor!</div>
      </div>

      <div class="section-block" style="border-left: 3px solid var(--accent);">
        <div class="section-block-title"><span>🏆</span> Sibling / Bonus Level-Up</div>
        <div class="section-block-content" id="spotlightBonus">Time yourself with a stopwatch or carry an 'ancient treasure' (stuffed toy) without dropping it.</div>
      </div>

      <!-- AMAZON ASSOCIATES RECOMMENDATION -->
      <div class="amazon-box">
        <div class="amazon-box-header">
          <div class="amazon-title">
            <span>🛒 Activity Gear &amp; Craft Kits on Amazon</span>
          </div>
          <span class="amazon-tag-badge">Tag: dhrav-21</span>
        </div>
        <a href="https://www.amazon.in/s?k=indoor+obstacle+course+kids&tag=dhrav-21" target="_blank" rel="noopener noreferrer" class="btn-amazon-primary" id="spotlightAmazonLink">
          <span>🔎 Search Kit &amp; Materials on Amazon</span>
          <span>↗</span>
        </a>
        <div class="amazon-subtext">As an Amazon Associate, Sarav's World earns from qualifying purchases via affiliate tracking ID <code>dhrav-21</code>.</div>
      </div>

      <div class="mission-actions-row">
        <button type="button" class="btn-mission-sub btn-completed" id="btnMarkCompleted" onclick="toggleCompletedCurrent()">
          <span>✅</span> <span id="completedBtnText">Mark Conquered</span>
        </button>
        <button type="button" class="btn-mission-sub" onclick="addCurrentToBingo()">
          <span>➕</span> <span>Pin to Weekend Bingo</span>
        </button>
        <button type="button" class="btn-mission-sub" onclick="spinWheel()">
          <span>🎲</span> <span>Spin Again</span>
        </button>
      </div>

    </div>

  </div>

  <!-- 4x4 SCREEN-FREE WEEKEND BINGO CARD -->
  <div class="bingo-card-container">
    <div class="bingo-header">
      <div>
        <h2 style="font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 4px;">
          🎟️ 4x4 Screen-Free Weekend Bingo
        </h2>
        <p style="font-size: 13px; color: var(--text-dim); margin: 0;">
          Tap any mission tile as your family conquers it this weekend. Complete 4-in-a-row for the grand family reward!
        </p>
      </div>
      <div class="bingo-stats">
        <div style="text-align: right;">
          <div style="font-size: 11px; color: var(--text-faint); text-transform: uppercase;">Conquered</div>
          <div style="font-size: 14px; font-weight: 700; color: var(--accent);" id="bingoStatScore">0 / 16 Conquered</div>
        </div>
        <div class="bingo-progress-bar">
          <div class="bingo-progress-fill" id="bingoProgressFill" style="width: 0%;"></div>
        </div>
        <button type="button" class="preset-chip" onclick="reshuffleBingo()" style="margin: 0;">
          <span>🎲 Reshuffle</span>
        </button>
      </div>
    </div>

    <div class="bingo-grid" id="bingoGrid">
      <!-- Generated via JS -->
    </div>
  </div>

  <!-- 122-ACTIVITY CATALOG EXPLORER -->
  <div class="catalog-card">
    <div class="card-box-header">
      <div class="card-box-title">
        <span>📚 122 Screen-Free Adventures Catalog</span>
      </div>
      <button type="button" class="preset-chip" onclick="openCustomModal()" style="margin: 0; background: var(--accent2-soft); color: var(--accent2); border-color: var(--accent2);">
        <span>➕ Add Custom Family Game</span>
      </button>
    </div>

    <div class="catalog-toolbar">
      <div class="search-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" class="catalog-search-input" id="catalogSearchInput" placeholder="Search 122 missions by keyword, materials, or rules..." oninput="onCatalogSearch(this.value)">
      </div>
      <button type="button" class="preset-chip" id="favFilterBtn" onclick="toggleFavFilterOnly()">
        <span>⭐ Favorites Only</span>
      </button>
    </div>

    <div class="category-filter-chips">
      <button type="button" class="cat-chip active" onclick="filterCatalogByCat('all')">All (122)</button>
      <button type="button" class="cat-chip" onclick="filterCatalogByCat('High Energy & Action')">🚀 High Energy (22)</button>
      <button type="button" class="cat-chip" onclick="filterCatalogByCat('Creative & Craft Studio')">🎨 Creative (22)</button>
      <button type="button" class="cat-chip" onclick="filterCatalogByCat('STEM & Kitchen')">🔬 STEM Lab (20)</button>
      <button type="button" class="cat-chip" onclick="filterCatalogByCat('Quiet Focus & Brain Quests')">🧩 Quiet Focus (20)</button>
      <button type="button" class="cat-chip" onclick="filterCatalogByCat('Nature & Balcony Safari')">🌿 Nature Safari (18)</button>
      <button type="button" class="cat-chip" onclick="filterCatalogByCat('Family & Sibling Challenges')">🤝 Sibling Co-op (20)</button>
    </div>

    <div class="catalog-grid" id="catalogGrid">
      <!-- 122 Cards rendered by JS -->
    </div>
  </div>

</div>

<!-- PRINTABLE HIGH CONTRAST FRIDGE JAR SLIPS SECTION -->
<div class="print-jar-slips-section">
  <div style="text-align: center; margin-bottom: 12pt;">
    <h2 style="font-size: 16pt; margin: 0 0 4pt;">✂️ Boredom Buster Jar — DIY Cut-Out Activity Slips</h2>
    <p style="font-size: 9pt; color: #444; margin: 0;">Cut along the dashed lines, fold, and place inside a glass jar or mason jar at home. Pull one out whenever kids say "I'm bored!"</p>
  </div>

  <div class="print-slips-grid" id="printSlipsGrid">
    <!-- Populated by JS for printable jar slips -->
  </div>

  <div class="print-footer-rule">
    Sarav's World Boredom Buster • https://iamsaravofficial.com/apps/boredom-buster/ • Screen-Free Family Adventures
  </div>
</div>

<!-- ADD CUSTOM ACTIVITY MODAL -->
<div class="modal-overlay" id="customModal" onclick="if(event.target===this)closeCustomModal()">
  <div class="modal-card">
    <div class="modal-head">
      <h3>➕ Add Custom Family Adventure</h3>
      <button type="button" class="modal-close" onclick="closeCustomModal()">&times;</button>
    </div>
    <form id="customForm" onsubmit="handleCustomSubmit(event)">
      <div class="form-group">
        <label class="form-label">Mission Title *</label>
        <input type="text" class="form-input" id="custTitle" placeholder="e.g. Grandma's Secret Recipe Bake-Off" required>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label class="form-label">Category</label>
          <select class="form-input" id="custCat">
            <option value="High Energy & Action">🚀 High Energy & Action</option>
            <option value="Creative & Craft Studio">🎨 Creative & Craft Studio</option>
            <option value="STEM & Kitchen">🔬 STEM & Kitchen</option>
            <option value="Quiet Focus & Brain Quests">🧩 Quiet Focus</option>
            <option value="Nature & Balcony Safari">🌿 Nature Safari</option>
            <option value="Family & Sibling Challenges">🤝 Sibling & Family</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Emoji Icon</label>
          <input type="text" class="form-input" id="custIcon" value="🎯" maxlength="3">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label class="form-label">Prep Time</label>
          <input type="text" class="form-input" id="custPrep" value="0 min" placeholder="0 min / 5 min">
        </div>
        <div class="form-group">
          <label class="form-label">Mess Level</label>
          <input type="text" class="form-input" id="custMess" value="Zero Mess" placeholder="Zero Mess / Low Mess">
        </div>
      </div>
      <div class="form-group">
        <label class="form-label">What You Need</label>
        <input type="text" class="form-input" id="custNeeds" placeholder="e.g. Blank paper, pencil, timer">
      </div>
      <div class="form-group">
        <label class="form-label">How to Play</label>
        <textarea class="form-input" id="custPlay" rows="3" placeholder="Describe the mission rules..." required></textarea>
      </div>
      <div class="form-group">
        <label class="form-label">Bonus Challenge</label>
        <input type="text" class="form-input" id="custBonus" placeholder="e.g. Sibling double-point challenge">
      </div>
      <div class="form-group">
        <label class="form-label">Amazon Search Keyword</label>
        <input type="text" class="form-input" id="custAmazon" placeholder="e.g. kids baking kit" value="screen free family games">
      </div>
      <div style="display: flex; gap: 10px; justify-content: flex-end; margin-top: 18px;">
        <button type="button" class="preset-chip" onclick="closeCustomModal()">Cancel</button>
        <button type="submit" class="btn-mission-sub" style="background: var(--accent); color: var(--accent-ink); border-color: var(--accent); font-weight: 700;">Save Mission</button>
      </div>
    </form>
  </div>
</div>

<!-- NON-BLOCKING TOAST NOTIFICATION -->
<div id="toast"></div>

<footer>
  <div style="max-width: 800px; margin: 0 auto;">
    <p><b>Sarav's World — Kids' Screen-Free "I'm Bored" Adventure Wheel</b></p>
    <p>100% Client-Side Privacy • Zero Telemetry • LocalStorage Persistence</p>
    <p style="font-size: 11.5px; color: var(--text-faint);">
      Amazon Associates Disclosure: As an Amazon Associate, Sarav's World earns from qualifying purchases made via links featuring tracking ID <code>dhrav-21</code>.
    </p>
    <p><a href="https://iamsaravofficial.com/apps/">Back to Playground Hub</a> │ <a href="https://iamsaravofficial.com/">Sarav's World Home</a></p>
  </div>
</footer>

<script>
// RAW 122 CURATED ACTIVITIES INJECTED DIRECTLY
const RAW_ACTIVITIES = {activities_json_str};

// STATE
let state = {{
  allActivities: [...RAW_ACTIVITIES],
  wheelPool: [...RAW_ACTIVITIES],
  activeActivity: RAW_ACTIVITIES[0],
  favorites: [],
  completedIds: [],
  bingoIds: [],
  bingoMarks: {{}},
  selectedCat: 'all',
  catalogCat: 'all',
  searchQuery: '',
  favsOnly: false,
  sound: true,
  isSpinning: false,
  wheelAngle: 0
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

function playTickSound() {{
  if (!state.sound) return;
  try {{
    const ctx = getAudioCtx();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(650 + Math.random() * 200, ctx.currentTime);
    gain.gain.setValueAtTime(0.08, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.035);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.04);
  }} catch (e) {{}}
}}

function playVictoryFanfare() {{
  if (!state.sound) return;
  try {{
    const ctx = getAudioCtx();
    if (!ctx) return;
    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    notes.forEach((freq, idx) => {{
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.08);
      gain.gain.setValueAtTime(0, ctx.currentTime + idx * 0.08);
      gain.gain.linearRampToValueAtTime(0.12, ctx.currentTime + idx * 0.08 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.08 + 0.28);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(ctx.currentTime + idx * 0.08);
      osc.stop(ctx.currentTime + idx * 0.08 + 0.3);
    }});
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
    localStorage.removeItem('bb_theme');
  }} else {{
    document.documentElement.setAttribute('data-theme', mode);
    localStorage.setItem('bb_theme', mode);
  }}
}}

function toggleSound() {{
  state.sound = !state.sound;
  const btn = document.getElementById('soundToggleBtn');
  if (btn) {{
    btn.textContent = state.sound ? '🔊 Sound ON' : '🔇 Sound OFF';
  }}
  showToast(state.sound ? '🔊 Web Audio Ticks enabled' : '🔇 Audio muted');
}}

// LOAD / SAVE STORAGE
function loadFromStorage() {{
  try {{
    const custom = JSON.parse(localStorage.getItem('boredom_buster_custom_v1') || '[]');
    if (Array.isArray(custom) && custom.length > 0) {{
      state.allActivities = [...custom, ...RAW_ACTIVITIES];
    }}
    state.favorites = JSON.parse(localStorage.getItem('boredom_buster_favs_v1') || '[]');
    state.completedIds = JSON.parse(localStorage.getItem('boredom_buster_completed_v1') || '[]');
    state.bingoIds = JSON.parse(localStorage.getItem('boredom_buster_bingo_v1') || '[]');
    state.bingoMarks = JSON.parse(localStorage.getItem('boredom_buster_bingo_marks_v1') || '{{}}');
    
    const savedTheme = localStorage.getItem('bb_theme');
    if (savedTheme) setTheme(savedTheme);
  }} catch (e) {{}}

  // Fallback bingo initialization
  if (!Array.isArray(state.bingoIds) || state.bingoIds.length < 16) {{
    initRandomBingo();
  }}
}}

function saveAllToStorage() {{
  try {{
    const customOnly = state.allActivities.filter(a => a.isCustom);
    localStorage.setItem('boredom_buster_custom_v1', JSON.stringify(customOnly));
    localStorage.setItem('boredom_buster_favs_v1', JSON.stringify(state.favorites));
    localStorage.setItem('boredom_buster_completed_v1', JSON.stringify(state.completedIds));
    localStorage.setItem('boredom_buster_bingo_v1', JSON.stringify(state.bingoIds));
    localStorage.setItem('boredom_buster_bingo_marks_v1', JSON.stringify(state.bingoMarks));
    showToast('💾 Progress &amp; custom adventures saved to browser storage!');
  }} catch (e) {{
    showToast('⚠️ Storage error');
  }}
}}

// CATEGORY BADGE COLOR MAP
function getCatClass(cat) {{
  if (cat.includes('High Energy')) return 'cat-energy';
  if (cat.includes('Creative')) return 'cat-craft';
  if (cat.includes('STEM')) return 'cat-stem';
  if (cat.includes('Quiet')) return 'cat-quiet';
  if (cat.includes('Nature')) return 'cat-nature';
  return 'cat-family';
}}

// WEDGE COLORS
const WEDGE_COLORS = [
  '#FF9F1C', '#2EC4B6', '#9B5DE5', '#FF5E7E', '#20BF6B', '#3A86FF',
  '#F15BB5', '#00BBF9', '#00F5D4', '#FEE440', '#FB5607', '#8338EC'
];

// CANVAS WHEEL DRAWING
const canvas = document.getElementById('wheelCanvas');
const ctx = canvas.getContext('2d');

function updateWheelPool() {{
  if (state.selectedCat === 'all') {{
    state.wheelPool = [...state.allActivities];
  }} else {{
    state.wheelPool = state.allActivities.filter(a => a.category === state.selectedCat);
  }}
  drawWheel();
}}

function drawWheel() {{
  if (!canvas || !ctx) return;
  const width = canvas.width;
  const height = canvas.height;
  const centerX = width / 2;
  const centerY = height / 2;
  const radius = width / 2 - 20;

  ctx.clearRect(0, 0, width, height);

  // Pick up to 12 items for clean wedge readability
  const pool = state.wheelPool.slice(0, 12);
  const numWedges = pool.length;
  if (numWedges === 0) return;

  const arc = (2 * Math.PI) / numWedges;

  ctx.save();
  ctx.translate(centerX, centerY);
  ctx.rotate(state.wheelAngle);

  for (let i = 0; i < numWedges; i++) {{
    const angle = i * arc;
    ctx.beginPath();
    ctx.fillStyle = WEDGE_COLORS[i % WEDGE_COLORS.length];
    ctx.moveTo(0, 0);
    ctx.arc(0, 0, radius, angle, angle + arc);
    ctx.lineTo(0, 0);
    ctx.fill();

    // Border line
    ctx.lineWidth = 3;
    ctx.strokeStyle = '#0C0F14';
    ctx.stroke();

    // Draw text and icon
    ctx.save();
    ctx.rotate(angle + arc / 2);
    ctx.textAlign = 'right';
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 24px "Space Grotesk", sans-serif';
    ctx.shadowColor = 'rgba(0,0,0,0.6)';
    ctx.shadowBlur = 4;

    const item = pool[i];
    let label = item.icon + ' ' + item.title;
    if (label.length > 20) label = label.slice(0, 19) + '…';
    ctx.fillText(label, radius - 36, 8);
    ctx.restore();
  }}

  // Outer border rim
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, 2 * Math.PI);
  ctx.lineWidth = 10;
  ctx.strokeStyle = '#2A3545';
  ctx.stroke();

  ctx.restore();
}}

// SPIN PHYSICS WITH SOUND
let lastTickWedge = -1;

function spinWheel() {{
  if (state.isSpinning) return;
  state.isSpinning = true;

  const pool = state.wheelPool.slice(0, 12);
  const numWedges = pool.length;
  if (numWedges === 0) return;

  const arc = (2 * Math.PI) / numWedges;
  const spins = 5 + Math.random() * 4; // 5 to 9 full spins
  const randomStop = Math.random() * 2 * Math.PI;
  const targetTotal = spins * 2 * Math.PI + randomStop;

  const startAngle = state.wheelAngle;
  const startTime = performance.now();
  const duration = 4000; // 4 seconds

  function easeOutCubic(t) {{
    return 1 - Math.pow(1 - t, 3);
  }}

  function animate(now) {{
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const eased = easeOutCubic(progress);

    state.wheelAngle = startAngle + targetTotal * eased;

    // Tick sound check
    const normalizedAngle = (state.wheelAngle % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI);
    // Pointer is at 12 o'clock (-PI/2)
    const pointerAngle = ( (3 * Math.PI / 2) - normalizedAngle + 2 * Math.PI ) % (2 * Math.PI);
    const currentWedge = Math.floor(pointerAngle / arc);

    if (currentWedge !== lastTickWedge) {{
      playTickSound();
      lastTickWedge = currentWedge;
    }}

    drawWheel();

    if (progress < 1) {{
      requestAnimationFrame(animate);
    }} else {{
      state.isSpinning = false;
      const winningItem = pool[currentWedge % numWedges];
      selectActivity(winningItem);
      playVictoryFanfare();
      showToast('🎉 Wheel landed on: <b>' + winningItem.title + '</b>');
    }}
  }}

  requestAnimationFrame(animate);
}}

function instantSurprise() {{
  if (state.wheelPool.length === 0) return;
  const rand = state.wheelPool[Math.floor(Math.random() * state.wheelPool.length)];
  selectActivity(rand);
  playVictoryFanfare();
  showToast('⚡ Instant Adventure selected!');
}}

// SELECT AND DISPLAY ACTIVITY
function selectActivity(item) {{
  state.activeActivity = item;

  document.getElementById('spotlightTitle').textContent = item.title;
  document.getElementById('spotlightIcon').textContent = item.icon || '🎯';
  
  const badge = document.getElementById('spotlightCatBadge');
  badge.textContent = item.category;
  badge.className = 'cat-badge ' + getCatClass(item.category);

  document.getElementById('spotlightPrep').textContent = item.prep + ' prep';
  document.getElementById('spotlightMess').textContent = item.mess;
  document.getElementById('spotlightEnergy').textContent = item.energy;
  document.getElementById('spotlightMode').textContent = item.mode;

  document.getElementById('spotlightNeeds').textContent = item.needs;
  document.getElementById('spotlightPlay').textContent = item.play;
  document.getElementById('spotlightBonus').textContent = item.bonus || 'Try repeating it twice as fast!';

  // Amazon Affiliate link with tag=dhrav-21
  const amazonQuery = encodeURIComponent(item.amazon || item.title);
  const amazonLink = 'https://www.amazon.in/s?k=' + amazonQuery + '&tag=dhrav-21';
  const aElem = document.getElementById('spotlightAmazonLink');
  aElem.href = amazonLink;
  aElem.setAttribute('title', 'Search ' + (item.amazon || item.title) + ' on Amazon (Tag: dhrav-21)');

  // Update button states
  updateSpotlightButtons();

  // Pulse animation
  const card = document.getElementById('missionSpotlightBox');
  card.style.transform = 'scale(1.02)';
  setTimeout(() => card.style.transform = 'none', 200);
}}

function updateSpotlightButtons() {{
  const id = state.activeActivity.id;
  const isFav = state.favorites.includes(id);
  const isComp = state.completedIds.includes(id);

  const favBtn = document.getElementById('btnFavActive');
  const favText = document.getElementById('favText');
  favText.textContent = isFav ? 'Favorited' : 'Favorite';
  favBtn.style.color = isFav ? 'var(--accent)' : 'inherit';

  const compBtn = document.getElementById('btnMarkCompleted');
  const compText = document.getElementById('completedBtnText');
  compBtn.classList.toggle('active', isComp);
  compText.textContent = isComp ? 'Conquered! 🌟' : 'Mark Conquered';
}}

function toggleFavoriteCurrent() {{
  const id = state.activeActivity.id;
  const idx = state.favorites.indexOf(id);
  if (idx === -1) {{
    state.favorites.push(id);
    showToast('⭐ Added to Favorites');
  }} else {{
    state.favorites.splice(idx, 1);
    showToast('Removed from Favorites');
  }}
  updateSpotlightButtons();
  renderCatalog();
  saveAllToStorage();
}}

function toggleCompletedCurrent() {{
  const id = state.activeActivity.id;
  const idx = state.completedIds.indexOf(id);
  if (idx === -1) {{
    state.completedIds.push(id);
    playVictoryFanfare();
    showToast('🌟 Awesome! Mission conquered!');
  }} else {{
    state.completedIds.splice(idx, 1);
    showToast('Mission marked not done');
  }}
  updateSpotlightButtons();
  saveAllToStorage();
}}

// 4x4 WEEKEND BINGO LOGIC
function initRandomBingo() {{
  // Shuffle all activities and pick 16 diverse ones
  const shuffled = [...state.allActivities].sort(() => 0.5 - Math.random());
  state.bingoIds = shuffled.slice(0, 16).map(a => a.id);
  state.bingoMarks = {{}};
  renderBingo();
}}

function reshuffleBingo() {{
  initRandomBingo();
  saveAllToStorage();
  showToast('🎲 New 4x4 Weekend Bingo generated!');
}}

function renderBingo() {{
  const grid = document.getElementById('bingoGrid');
  if (!grid) return;
  grid.innerHTML = '';

  let markedCount = 0;

  state.bingoIds.forEach((id, idx) => {{
    const act = state.allActivities.find(a => a.id === id) || RAW_ACTIVITIES[idx % RAW_ACTIVITIES.length];
    const isDone = !!state.bingoMarks[id];
    if (isDone) markedCount++;

    const tile = document.createElement('div');
    tile.className = 'bingo-tile' + (isDone ? ' completed' : '');
    tile.dataset.id = id;
    tile.onclick = function() {{ toggleBingoTile(id); }};

    tile.innerHTML = `
      <span class="tile-check-icon">✓</span>
      <div class="tile-icon">${{act.icon || '🎯'}}</div>
      <div class="tile-title">${{act.title}}</div>
    `;
    grid.appendChild(tile);
  }});

  // Update progress bar & score
  document.getElementById('bingoStatScore').textContent = `${{markedCount}} / 16 Conquered`;
  const pct = Math.round((markedCount / 16) * 100);
  document.getElementById('bingoProgressFill').style.width = pct + '%';
}}

function toggleBingoTile(id) {{
  state.bingoMarks[id] = !state.bingoMarks[id];
  if (state.bingoMarks[id]) {{
    playVictoryFanfare();
    showToast('⭐ Bingo tile marked!');
  }}
  checkBingoWinningLines();
  renderBingo();
  saveAllToStorage();
}}

function checkBingoWinningLines() {{
  // 4x4 winning lines
  const lines = [
    // Rows
    [0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15],
    // Cols
    [0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15],
    // Diagonals
    [0,5,10,15], [3,6,9,12]
  ];

  let winningLines = 0;
  lines.forEach(line => {{
    const complete = line.every(idx => !!state.bingoMarks[state.bingoIds[idx]]);
    if (complete) winningLines++;
  }});

  if (winningLines > 0) {{
    showToast(`🎉 <b>BINGO!</b> You achieved ${{winningLines}} line(s)! Claim your weekend family reward!`);
  }}
}}

function addCurrentToBingo() {{
  const id = state.activeActivity.id;
  if (state.bingoIds.includes(id)) {{
    showToast("ℹ️ Already on this weekend's Bingo board");
    return;
  }}
  // Replace first uncompleted tile
  const replaceIdx = state.bingoIds.findIndex(tid => !state.bingoMarks[tid]);
  if (replaceIdx !== -1) {{
    state.bingoIds[replaceIdx] = id;
  }} else {{
    state.bingoIds[0] = id;
  }}
  renderBingo();
  saveAllToStorage();
  showToast('➕ Pinned to Weekend Bingo grid!');
}}

// 122-ACTIVITY CATALOG & SEARCH
function renderCatalog() {{
  const grid = document.getElementById('catalogGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const q = state.searchQuery.toLowerCase().trim();
  const filtered = state.allActivities.filter(item => {{
    if (state.catalogCat !== 'all' && item.category !== state.catalogCat) return false;
    if (state.favsOnly && !state.favorites.includes(item.id)) return false;
    if (q) {{
      const haystack = (item.title + ' ' + item.category + ' ' + item.needs + ' ' + item.play).toLowerCase();
      if (!haystack.includes(q)) return false;
    }}
    return true;
  }});

  if (filtered.length === 0) {{
    grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-faint);">No adventures matched your search. Try adjusting filters!</div>';
    return;
  }}

  filtered.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'catalog-item-card';
    const isFav = state.favorites.includes(item.id);
    const catClass = getCatClass(item.category);
    const amazonLink = 'https://www.amazon.in/s?k=' + encodeURIComponent(item.amazon || item.title) + '&tag=dhrav-21';

    card.innerHTML = `
      <div class="cat-item-top">
        <span style="font-size: 26px;">${{item.icon || '🎯'}}</span>
        <span class="cat-badge ${{catClass}}">${{item.prep}} prep</span>
      </div>
      <div class="cat-item-title">${{item.title}}</div>
      <div class="cat-item-desc">${{item.play.length > 95 ? item.play.slice(0, 92) + '…' : item.play}}</div>
      <div class="cat-item-footer">
        <button type="button" class="btn-cat-mini" data-id="${{item.id}}" onclick="onCatalogSpinClick(this.dataset.id)">🎯 Spin</button>
        <button type="button" class="btn-cat-mini" data-id="${{item.id}}" onclick="onCatalogFavClick(this.dataset.id)" style="color: ${{isFav ? 'var(--accent)' : 'inherit'}}">${{isFav ? '⭐' : '☆'}}</button>
        <a href="${{amazonLink}}" target="_blank" rel="noopener noreferrer" class="btn-cat-mini" style="color: var(--accent);">🛒 Kit</a>
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function onCatalogSpinClick(id) {{
  const item = state.allActivities.find(a => a.id === id);
  if (item) {{
    selectActivity(item);
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
    showToast('🎯 Loaded "' + item.title + '" into spotlight!');
  }}
}}

function onCatalogFavClick(id) {{
  const idx = state.favorites.indexOf(id);
  if (idx === -1) {{
    state.favorites.push(id);
  }} else {{
    state.favorites.splice(idx, 1);
  }}
  renderCatalog();
  updateSpotlightButtons();
  saveAllToStorage();
}}

function onCatalogSearch(val) {{
  state.searchQuery = val;
  renderCatalog();
}}

function filterCatalogByCat(cat) {{
  state.catalogCat = cat;
  document.querySelectorAll('.category-filter-chips .cat-chip').forEach(c => {{
    c.classList.toggle('active', c.textContent.includes(cat) || (cat === 'all' && c.textContent.startsWith('All')));
  }});
  renderCatalog();
}}

function toggleFavFilterOnly() {{
  state.favsOnly = !state.favsOnly;
  const btn = document.getElementById('favFilterBtn');
  btn.classList.toggle('active', state.favsOnly);
  renderCatalog();
}}

// PRESETS
function applyPreset(preset) {{
  document.querySelectorAll('.header-presets-wrap .preset-chip').forEach(p => p.classList.remove('active'));
  if (event && event.target) event.target.classList.add('active');

  if (preset === 'all') {{
    state.selectedCat = 'all';
    state.wheelPool = [...state.allActivities];
  }} else if (preset === 'quick') {{
    state.selectedCat = 'all';
    state.wheelPool = state.allActivities.filter(a => a.prep === '0 min' || a.prep === '1 min' || a.prep === '2 min');
  }} else if (preset === 'action') {{
    state.selectedCat = 'High Energy & Action';
    state.wheelPool = state.allActivities.filter(a => a.category === state.selectedCat);
  }} else if (preset === 'craft') {{
    state.selectedCat = 'Creative & Craft Studio';
    state.wheelPool = state.allActivities.filter(a => a.category === state.selectedCat);
  }} else if (preset === 'stem') {{
    state.selectedCat = 'STEM & Kitchen';
    state.wheelPool = state.allActivities.filter(a => a.category === state.selectedCat);
  }} else if (preset === 'sibling') {{
    state.selectedCat = 'Family & Sibling Challenges';
    state.wheelPool = state.allActivities.filter(a => a.category === state.selectedCat);
  }} else if (preset === 'nature') {{
    state.selectedCat = 'Nature & Balcony Safari';
    state.wheelPool = state.allActivities.filter(a => a.category === state.selectedCat);
  }}

  const select = document.getElementById('wheelCategorySelect');
  if (select) select.value = state.selectedCat;

  drawWheel();
  showToast('🎯 Applied preset: ' + state.wheelPool.length + ' adventures loaded on wheel');
}}

function onCategoryFilterChange(val) {{
  state.selectedCat = val;
  updateWheelPool();
}}

// CUSTOM ACTIVITY MODAL
function openCustomModal() {{
  document.getElementById('customModal').classList.add('open');
}}

function closeCustomModal() {{
  document.getElementById('customModal').classList.remove('open');
}}

function handleCustomSubmit(e) {{
  e.preventDefault();
  const title = document.getElementById('custTitle').value.trim();
  const cat = document.getElementById('custCat').value;
  const icon = document.getElementById('custIcon').value.trim() || '🎯';
  const prep = document.getElementById('custPrep').value.trim() || '0 min';
  const mess = document.getElementById('custMess').value.trim() || 'Zero Mess';
  const needs = document.getElementById('custNeeds').value.trim() || 'Household items';
  const play = document.getElementById('custPlay').value.trim();
  const bonus = document.getElementById('custBonus').value.trim();
  const amazon = document.getElementById('custAmazon').value.trim() || 'screen free family games';

  const newActivity = {{
    id: 'custom_' + Date.now(),
    title,
    category: cat,
    icon,
    prep,
    mess,
    energy: 'Custom',
    mode: 'Family Choice',
    needs,
    play,
    bonus,
    amazon,
    isCustom: true
  }};

  state.allActivities.unshift(newActivity);
  state.wheelPool.unshift(newActivity);
  selectActivity(newActivity);
  closeCustomModal();
  drawWheel();
  renderCatalog();
  saveAllToStorage();
  showToast('🎉 Custom mission added to your family wheel!');
}}

// 4-ACTION SUITE HANDLERS
function shareMissionWhatsApp() {{
  const act = state.activeActivity;
  const text = `🎡 *Kids' Screen-Free Mission of the Day!*
🏆 *${{act.title}}* (${{act.icon}})
📂 Category: ${{act.category}}
⏱️ Prep: ${{act.prep}} • ${{act.mess}} • ${{act.mode}}

🎒 *What You Need:*
${{act.needs}}

🎮 *How to Play:*
${{act.play}}

✨ *Bonus Challenge:*
${{act.bonus}}

🛒 Craft kit search on Amazon:
https://www.amazon.in/s?k=${{encodeURIComponent(act.amazon || act.title)}}&tag=dhrav-21

Generated from Sarav's World Boredom Buster:
https://iamsaravofficial.com/apps/boredom-buster/`;

  const url = 'https://api.whatsapp.com/send?text=' + encodeURIComponent(text);
  window.open(url, '_blank');
}}

function copyActiveMission() {{
  const act = state.activeActivity;
  const text = `🎡 Screen-Free Mission: ${{act.title}} (${{act.icon}})
Category: ${{act.category}} | Prep: ${{act.prep}} | Mess: ${{act.mess}}
Needs: ${{act.needs}}
Rules: ${{act.play}}
Bonus: ${{act.bonus}}
Amazon Kit: https://www.amazon.in/s?k=${{encodeURIComponent(act.amazon || act.title)}}&tag=dhrav-21
https://iamsaravofficial.com/apps/boredom-buster/`;

  navigator.clipboard.writeText(text).then(() => {{
    showToast('📋 Mission summary copied to clipboard!');
  }}).catch(() => {{
    showToast('⚠️ Could not copy to clipboard');
  }});
}}

// POPULATE PRINT JAR SLIPS
function populatePrintSlips() {{
  const container = document.getElementById('printSlipsGrid');
  if (!container) return;
  container.innerHTML = '';

  // Take 24 distinct adventures for 2 pages of cut-out jar slips
  const sample = state.allActivities.slice(0, 24);
  sample.forEach(item => {{
    const div = document.createElement('div');
    div.className = 'print-slip-box';
    div.innerHTML = `
      <div>
        <div class="print-slip-title">✂️ ${{item.icon}} ${{item.title}}</div>
        <div class="print-slip-desc">${{item.play}}</div>
      </div>
      <div class="print-slip-meta">
        Needs: ${{item.needs}}<br>
        ⏱️ ${{item.prep}} • ${{item.mess}} • ${{item.category}}
      </div>
    `;
    container.appendChild(div);
  }});
}}

// INITIALIZATION
window.addEventListener('DOMContentLoaded', () => {{
  loadFromStorage();
  updateWheelPool();
  selectActivity(state.allActivities[0]);
  renderBingo();
  renderCatalog();
  populatePrintSlips();
}});
</script>

</body>
</html>"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Built {out_path} successfully ({len(html_content)} bytes).")

if __name__ == "__main__":
    generate_boredom_buster()
