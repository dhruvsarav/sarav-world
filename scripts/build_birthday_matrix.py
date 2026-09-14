import os
import json

def generate_birthday_matrix():
    out_path = "public/apps/birthday-gift-matrix/index.html"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open('scripts/birthday_matrix_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    data_json_str = json.dumps(data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Family Birthday &amp; Milestone Gift Wishlist Matrix — 12-Month Occasion Wall &amp; Relative Share | Sarav's World</title>
<meta name="description" content="Free family birthday and milestone gift matrix. Track 12 months of birthdays and anniversaries with live countdowns, manage tiered budget gift wishlists with Amazon links (tag: dhrav-21), enable anti-duplicate reservation for relatives, and print fridge calendars.">
<link rel="canonical" href="https://iamsaravofficial.com/apps/birthday-gift-matrix/">

<!-- Open Graph / Social -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://iamsaravofficial.com/apps/birthday-gift-matrix/">
<meta property="og:title" content="Family Birthday &amp; Milestone Gift Matrix | Sarav's World">
<meta property="og:description" content="12-month occasion countdown wall, 4 tiered budget envelopes, anti-duplicate gift reservations for relatives, and printable fridge calendars.">
<meta property="og:image" content="https://iamsaravofficial.com/apps/birthday-gift-matrix/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Family Birthday &amp; Milestone Gift Matrix | Sarav's World">
<meta name="twitter:description" content="12-month family birthday wall, anti-duplicate gift reservations, and printable calendars.">
<meta name="twitter:image" content="https://iamsaravofficial.com/apps/birthday-gift-matrix/og-image.png">

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
    --accent: #FF5E7E;
    --accent-ink: #1F070E;
    --accent-soft: rgba(255, 94, 126, 0.15);
    --gold: #FF9F1C;
    --gold-soft: rgba(255, 159, 28, 0.15);
    --teal: #2EC4B6;
    --teal-soft: rgba(46, 196, 182, 0.15);
    --purple: #9B5DE5;
    --purple-soft: rgba(155, 93, 229, 0.15);
    --success: #20BF6B;
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
    --accent: #E11D48;
    --accent-ink: #FFFFFF;
    --accent-soft: rgba(225, 29, 72, 0.14);
    --gold: #D97706;
    --gold-soft: rgba(217, 119, 6, 0.14);
    --teal: #0D9488;
    --teal-soft: rgba(13, 148, 136, 0.14);
    --purple: #7C3AED;
    --purple-soft: rgba(124, 58, 237, 0.14);
    --success: #16A34A;
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
    border-radius: 6px; background: var(--accent-soft); color: var(--accent) !important;
    font-size: 12px; font-weight: 600; text-decoration: none; border: 1px solid rgba(255, 94, 126, 0.3);
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

  /* COUNTDOWN HIGHLIGHT BANNER */
  .countdown-banner {{
    background: linear-gradient(135deg, rgba(255, 94, 126, 0.14) 0%, var(--surface-2) 100%);
    border: 1.5px solid var(--accent); border-radius: 14px; padding: 16px 20px;
    margin-top: 18px; display: flex; align-items: center; justify-content: space-between; gap: 14px; flex-wrap: wrap;
  }}
  .countdown-left {{ display: flex; align-items: center; gap: 14px; }}
  .countdown-badge {{
    font-size: 28px; width: 50px; height: 50px; border-radius: 12px;
    background: var(--surface); display: flex; align-items: center; justify-content: center;
    border: 1px solid var(--border); flex-shrink: 0;
  }}
  .countdown-title {{ font-size: 16px; font-weight: 700; color: var(--text); margin-bottom: 2px; }}
  .countdown-sub {{ font-size: 12px; color: var(--text-dim); }}
  .countdown-timer-box {{
    font-family: 'IBM Plex Mono', monospace; font-size: 18px; font-weight: 700;
    color: var(--accent); background: var(--surface); padding: 8px 16px; border-radius: 8px;
    border: 1px solid var(--border); white-space: nowrap;
  }}

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

  /* 12-MONTH OCCASION WALL */
  .wall-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px 28px; margin-bottom: 28px; box-shadow: var(--shadow);
  }}
  .wall-header {{
    display: flex; justify-content: space-between; align-items: center; gap: 14px;
    margin-bottom: 18px; flex-wrap: wrap;
  }}
  .wall-title {{ font-size: 17px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 8px; }}

  .month-grid {{
    display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px;
  }}
  @media(max-width: 980px) {{ .month-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
  @media(max-width: 580px) {{ .month-grid {{ grid-template-columns: repeat(2, 1fr); }} }}

  .month-box {{
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 12px;
    padding: 12px; display: flex; flex-direction: column; min-height: 120px; transition: all 0.15s ease;
  }}
  .month-box:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  .month-box.has-events {{ border-color: var(--accent); background: linear-gradient(180deg, rgba(255, 94, 126, 0.08) 0%, var(--surface-2) 100%); }}
  .month-name {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-faint); margin-bottom: 8px; border-bottom: 1px solid var(--border-soft); padding-bottom: 4px; }}
  .month-events {{ display: flex; flex-direction: column; gap: 6px; flex: 1; }}
  .event-pill {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 6px;
    padding: 5px 8px; font-size: 11.5px; font-weight: 600; color: var(--text);
    cursor: pointer; transition: all 0.15s ease; display: flex; align-items: center; gap: 6px;
  }}
  .event-pill:hover {{ border-color: var(--accent); color: var(--accent); }}
  .event-pill.is-active {{ border-color: var(--accent); background: var(--accent-soft); color: var(--accent); }}

  /* ACTIVE PERSON WISHLIST STUDIO (2-COLUMN) */
  .wishlist-split {{
    display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 24px; margin-bottom: 28px;
  }}
  @media(max-width: 980px) {{ .wishlist-split {{ grid-template-columns: 1fr; }} }}

  .card-box {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 18px;
    padding: 24px; box-shadow: var(--shadow); display: flex; flex-direction: column;
  }}
  .card-box-header {{
    display: flex; justify-content: space-between; align-items: center; gap: 12px;
    margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border-soft);
  }}
  .card-box-title {{ font-size: 16px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 8px; }}

  /* Budget Tier Filters */
  .tier-chips {{ display: flex; gap: 6px; overflow-x: auto; padding-bottom: 6px; margin-bottom: 14px; }}
  .tier-chip {{
    background: var(--surface-2); border: 1px solid var(--border); color: var(--text-dim);
    padding: 5px 12px; border-radius: 16px; font-size: 11.5px; font-weight: 600;
    cursor: pointer; font-family: inherit; white-space: nowrap; transition: all 0.15s ease;
  }}
  .tier-chip:hover {{ color: var(--text); }}
  .tier-chip.active {{ background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }}

  .wish-list {{ display: flex; flex-direction: column; gap: 12px; max-height: 480px; overflow-y: auto; padding-right: 4px; }}
  .wish-item-card {{
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 12px;
    padding: 14px; display: flex; flex-direction: column; transition: all 0.15s ease;
  }}
  .wish-item-card:hover {{ border-color: var(--accent); }}
  .wish-item-card.claimed {{
    background: linear-gradient(135deg, rgba(32, 191, 107, 0.1) 0%, var(--surface-2) 100%);
    border-color: var(--success);
  }}
  .wish-top-row {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; }}
  .wish-title {{ font-size: 14px; font-weight: 700; color: var(--text); }}
  .wish-price {{ font-family: 'IBM Plex Mono', monospace; font-size: 13.5px; font-weight: 700; color: var(--gold); }}
  .wish-desc {{ font-size: 12px; color: var(--text-dim); line-height: 1.4; margin-bottom: 10px; }}
  .wish-actions-row {{
    display: flex; justify-content: space-between; align-items: center; gap: 8px; flex-wrap: wrap; margin-top: auto;
  }}

  .btn-claim {{
    background: var(--surface-3); border: 1px solid var(--border); color: var(--text);
    padding: 6px 12px; border-radius: 6px; font-size: 11.5px; font-weight: 600; cursor: pointer;
    font-family: inherit; transition: all 0.15s ease; display: inline-flex; align-items: center; gap: 5px;
  }}
  .btn-claim:hover {{ border-color: var(--success); color: var(--success); }}
  .btn-claim.claimed {{ background: rgba(32, 191, 107, 0.2); border-color: var(--success); color: var(--success); }}

  .btn-amazon-wish {{
    background: #FF9900; color: #111; font-weight: 700; font-size: 11.5px;
    padding: 6px 12px; border-radius: 6px; text-decoration: none; display: inline-flex;
    align-items: center; gap: 4px; transition: all 0.15s ease;
  }}
  .btn-amazon-wish:hover {{ filter: brightness(1.1); text-decoration: none; }}

  /* CURATED IDEAS BANK (RIGHT COLUMN) */
  .ideas-grid {{
    display: flex; flex-direction: column; gap: 10px; max-height: 520px; overflow-y: auto; padding-right: 4px;
  }}
  .idea-card {{
    background: var(--surface-2); border: 1px solid var(--border); border-radius: 10px;
    padding: 12px; display: flex; flex-direction: column; gap: 4px; transition: all 0.15s ease;
  }}
  .idea-card:hover {{ border-color: var(--teal); }}
  .idea-title {{ font-size: 13px; font-weight: 700; color: var(--text); }}
  .idea-meta {{ font-size: 11px; color: var(--text-dim); display: flex; justify-content: space-between; }}
  .idea-actions {{ display: flex; gap: 6px; margin-top: 6px; }}

  /* MODALS */
  .modal-overlay {{
    position: fixed; inset: 0; background: rgba(0,0,0,0.75); backdrop-filter: blur(4px);
    display: none; align-items: center; justify-content: center; z-index: 2000; padding: 20px;
  }}
  .modal-overlay.open {{ display: flex; }}
  .modal-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 24px; max-width: 480px; width: 100%; box-shadow: var(--shadow);
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

  /* PRINTABLE A4 FAMILY CALENDAR */
  @media print {{
    body {{ background: #fff !important; color: #000 !important; font-size: 9pt; }}
    .ecosystem-bar, .theme-selector, .countdown-banner, .action-bar,
    .wishlist-split, .modal-overlay, #toast, footer {{ display: none !important; }}
    .container {{ max-width: 100% !important; padding: 0 !important; margin: 0 !important; }}
    .hero-card {{ border: none !important; box-shadow: none !important; padding: 0 0 8pt 0 !important; margin-bottom: 10pt !important; border-bottom: 2pt solid #000 !important; }}
    .app-icon-box {{ display: none !important; }}

    .wall-card {{ border: 1.5pt solid #000 !important; box-shadow: none !important; padding: 10pt !important; }}
    .month-grid {{ grid-template-columns: repeat(4, 1fr) !important; gap: 8pt !important; }}
    .month-box {{ border: 1pt solid #000 !important; background: #fff !important; color: #000 !important; }}
    .month-name {{ color: #000 !important; border-bottom: 1pt solid #000 !important; }}
    .event-pill {{ border: 1pt solid #444 !important; background: #fff !important; color: #000 !important; }}
    .print-footer-rule {{ display: block !important; text-align: center; margin-top: 14pt; font-size: 8pt; color: #444; }}
  }}
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
          <a href="https://iamsaravofficial.com/apps/family-movie-night/">🎬 Family Movie &amp; Game Night</a>
          <a href="https://iamsaravofficial.com/apps/book-nook/">📚 Kids' Book Nook &amp; Quest</a>
          <a href="https://iamsaravofficial.com/apps/birthday-gift-matrix/" class="current">🎁 Birthday &amp; Milestone Matrix</a>
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
          <img src="gift-full.png" alt="Birthday Matrix Icon">
        </div>
        <div class="header-titles">
          <div class="eyebrow">🎁 Family Planner Suite #10 • Occasion &amp; Wishlist Matrix</div>
          <h1>Family Birthday &amp; Milestone Gift Matrix</h1>
          <p class="sub">Never scramble for last-minute gifts again. Track 12 months of family birthdays and anniversaries, manage tiered budget wishlists with Amazon buy links, protect against duplicate presents with relative reservation, and print a fridge calendar.</p>
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

    <!-- NEXT OCCASION COUNTDOWN BANNER -->
    <div class="countdown-banner" id="countdownBanner">
      <div class="countdown-left">
        <div class="countdown-badge" id="cdIcon">🎂</div>
        <div>
          <div class="countdown-title" id="cdTitle">Elder Child's 10th Birthday!</div>
          <div class="countdown-sub" id="cdSub">Double Digits Milestone • October 24</div>
        </div>
      </div>
      <div class="countdown-timer-box" id="cdTimer">
        ⏳ 18 Days Away
      </div>
    </div>

  </div>

  <!-- UNIVERSAL 4-ACTION SUITE -->
  <div class="action-bar">
    <button type="button" class="btn-action btn-whatsapp" onclick="shareWishlistWhatsApp()">
      <span>💬</span>
      <span>Share Wishlist with Relatives</span>
    </button>
    <button type="button" class="btn-action btn-print" onclick="window.print()">
      <span>🖨️</span>
      <span>Print 12-Month Fridge Calendar</span>
    </button>
    <button type="button" class="btn-action" onclick="copyWishlistSummary()">
      <span>📋</span>
      <span>Copy Wishlist Summary</span>
    </button>
    <button type="button" class="btn-action" onclick="saveAllToStorage()">
      <span>💾</span>
      <span>Save Occasions to Storage</span>
    </button>
  </div>

  <!-- 12-MONTH OCCASION WALL -->
  <div class="wall-card">
    <div class="wall-header">
      <div class="wall-title">
        <span>📅 12-Month Family Occasion &amp; Milestone Wall</span>
      </div>
      <button type="button" class="preset-chip" onclick="openOccasionModal()" style="margin:0; background: var(--accent-soft); color: var(--accent); border-color: var(--accent);">
        <span>➕ Add Birthday / Milestone</span>
      </button>
    </div>

    <div class="month-grid" id="monthGrid">
      <!-- 12 Month Boxes generated by JS -->
    </div>
  </div>

  <!-- ACTIVE PERSON WISHLIST STUDIO (2-COLUMN) -->
  <div class="wishlist-split">

    <!-- LEFT: ACTIVE PERSON'S TIERED WISHLIST -->
    <div class="card-box">
      <div class="card-box-header">
        <div class="card-box-title">
          <span>🎁 <span id="activeWishlistPersonName">Elder Child</span>'s Gift Wishlist</span>
        </div>
        <button type="button" class="preset-chip" onclick="openCustomWishModal()" style="margin:0;">
          <span>➕ Add Custom Gift</span>
        </button>
      </div>

      <!-- Budget Tier Chips -->
      <div class="tier-chips">
        <button type="button" class="tier-chip active" onclick="filterTier('all')">All Tiers</button>
        <button type="button" class="tier-chip" onclick="filterTier('Tier 1: ₹500 – ₹1,000')">₹500 – ₹1,000</button>
        <button type="button" class="tier-chip" onclick="filterTier('Tier 2: ₹1,000 – ₹2,500')">₹1,000 – ₹2,500</button>
        <button type="button" class="tier-chip" onclick="filterTier('Tier 3: ₹2,500 – ₹5,000')">₹2,500 – ₹5,000</button>
        <button type="button" class="tier-chip" onclick="filterTier('Tier 4: ₹5,000+')">₹5,000+</button>
      </div>

      <!-- Wishlist Items -->
      <div class="wish-list" id="wishList">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- RIGHT: CURATED GIFT IDEAS INSPIRATION VAULT -->
    <div class="card-box">
      <div class="card-box-header">
        <div class="card-box-title">
          <span>💡 Curated Gift Inspiration Vault</span>
        </div>
      </div>
      <div style="font-size: 12px; color: var(--text-dim); margin-bottom: 12px;">
        Kid-tested favorites with direct Amazon buying links (Tag: <code>dhrav-21</code>). Tap <b>+ Wishlist</b> to add to <span id="activePersonLabel">Elder Child</span>'s list!
      </div>

      <div class="ideas-grid" id="ideasGrid">
        <!-- 36 Ideas rendered by JS -->
      </div>
    </div>

  </div>

</div>

<!-- ADD OCCASION MODAL -->
<div class="modal-overlay" id="occasionModal" onclick="if(event.target===this)closeOccasionModal()">
  <div class="modal-card">
    <div class="modal-head">
      <h3>➕ Add Family Occasion</h3>
      <button type="button" class="modal-close" onclick="closeOccasionModal()">&times;</button>
    </div>
    <form id="occasionForm" onsubmit="handleOccasionSubmit(event)">
      <div class="form-group">
        <label class="form-label">Person / Couple Name *</label>
        <input type="text" class="form-input" id="occPerson" placeholder="e.g. Younger Child or Uncle &amp; Aunt" required>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label class="form-label">Occasion Type</label>
          <select class="form-input" id="occType">
            <option value="Birthday">🎂 Birthday</option>
            <option value="Wedding Anniversary">💍 Wedding Anniversary</option>
            <option value="Festival Milestone">🪔 Festival Milestone</option>
            <option value="Graduation / Exam">🎓 Graduation / Exam</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Emoji Icon</label>
          <input type="text" class="form-input" id="occEmoji" value="🎂" maxlength="3">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label class="form-label">Month</label>
          <select class="form-input" id="occMonth">
            <option value="01">January</option>
            <option value="02">February</option>
            <option value="03">March</option>
            <option value="04">April</option>
            <option value="05">May</option>
            <option value="06">June</option>
            <option value="07">July</option>
            <option value="08">August</option>
            <option value="09">September</option>
            <option value="10">October</option>
            <option value="11">November</option>
            <option value="12">December</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Day of Month</label>
          <input type="number" class="form-input" id="occDay" min="1" max="31" value="15" required>
        </div>
      </div>
      <div class="form-group">
        <label class="form-label">Milestone Subtitle</label>
        <input type="text" class="form-input" id="occMilestone" placeholder="e.g. 10th Birthday (Double Digits!)">
      </div>
      <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 18px;">
        <button type="button" class="preset-chip" onclick="closeOccasionModal()">Cancel</button>
        <button type="submit" class="btn-action" style="background: var(--accent); color: var(--accent-ink); font-weight: 700;">Save Occasion</button>
      </div>
    </form>
  </div>
</div>

<!-- ADD CUSTOM WISH MODAL -->
<div class="modal-overlay" id="wishModal" onclick="if(event.target===this)closeWishModal()">
  <div class="modal-card">
    <div class="modal-head">
      <h3>🎁 Add Custom Gift Wish</h3>
      <button type="button" class="modal-close" onclick="closeWishModal()">&times;</button>
    </div>
    <form id="wishForm" onsubmit="handleWishSubmit(event)">
      <div class="form-group">
        <label class="form-label">Gift Title *</label>
        <input type="text" class="form-input" id="wTitle" placeholder="e.g. Harry Potter Illustrated Edition" required>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label class="form-label">Budget Tier</label>
          <select class="form-input" id="wTier">
            <option value="Tier 1: ₹500 – ₹1,000">Tier 1: ₹500 – ₹1,000</option>
            <option value="Tier 2: ₹1,000 – ₹2,500">Tier 2: ₹1,000 – ₹2,500</option>
            <option value="Tier 3: ₹2,500 – ₹5,000">Tier 3: ₹2,500 – ₹5,000</option>
            <option value="Tier 4: ₹5,000+">Tier 4: ₹5,000+</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Price / Estimate</label>
          <input type="text" class="form-input" id="wPrice" placeholder="₹1,299">
        </div>
      </div>
      <div class="form-group">
        <label class="form-label">Notes / Why They Want It</label>
        <textarea class="form-input" id="wNotes" rows="2" placeholder="e.g. For reading before bed"></textarea>
      </div>
      <div class="form-group">
        <label class="form-label">Amazon Search Query</label>
        <input type="text" class="form-input" id="wAmazon" placeholder="e.g. harry potter illustrated edition bloomsbury">
      </div>
      <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 18px;">
        <button type="button" class="preset-chip" onclick="closeWishModal()">Cancel</button>
        <button type="submit" class="btn-action" style="background: var(--accent); color: var(--accent-ink); font-weight: 700;">Add to Wishlist</button>
      </div>
    </form>
  </div>
</div>

<!-- CLAIM GIFT PROMPT MODAL -->
<div class="modal-overlay" id="claimModal" onclick="if(event.target===this)closeClaimModal()">
  <div class="modal-card">
    <div class="modal-head">
      <h3>🛡️ Reserve / Claim Gift</h3>
      <button type="button" class="modal-close" onclick="closeClaimModal()">&times;</button>
    </div>
    <div style="font-size: 13px; color: var(--text-dim); margin-bottom: 14px;">
      Mark this gift as reserved so other relatives know you're buying it. Prevents duplicate gifts!
    </div>
    <input type="hidden" id="claimItemIndex" value="0">
    <div class="form-group">
      <label class="form-label">Your Name / Relationship</label>
      <input type="text" class="form-input" id="claimBuyerName" placeholder="e.g. Priya Masi, Uncle Rahul, Grandpa" required>
    </div>
    <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 18px;">
      <button type="button" class="preset-chip" onclick="unclaimActiveItem()" style="color: var(--danger);">Unclaim (Free Up)</button>
      <button type="button" class="btn-action" style="background: var(--success); color: #fff; font-weight: 700;" onclick="confirmClaim()">Confirm Reservation</button>
    </div>
  </div>
</div>

<!-- NON-BLOCKING TOAST NOTIFICATION -->
<div id="toast"></div>

<!-- PRINT VIEW FOOTER -->
<div class="print-footer-rule">
  Sarav's World Family Occasions • 12-Month Calendar • https://iamsaravofficial.com/apps/birthday-gift-matrix/ • Zero Duplicate Gifts
</div>

<footer>
  <div style="max-width: 800px; margin: 0 auto;">
    <p><b>Sarav's World — Family Birthday &amp; Milestone Gift Wishlist Matrix</b></p>
    <p>100% Client-Side Privacy • Zero Telemetry • LocalStorage Persistence</p>
    <p style="font-size: 11.5px; color: var(--text-faint);">
      Amazon Associates Disclosure: As an Amazon Associate, Sarav's World earns from qualifying purchases made via links featuring tracking ID <code>dhrav-21</code>.
    </p>
    <p><a href="https://iamsaravofficial.com/apps/">Back to Playground Hub</a> │ <a href="https://iamsaravofficial.com/">Sarav's World Home</a></p>
  </div>
</footer>

<script>
// RAW DATA INJECTION
const DATA = {data_json_str};

// STATE
let state = {{
  occasions: [...DATA.default_occasions],
  activeOccasionId: DATA.default_occasions[0].id,
  selectedTier: 'all',
  wishlists: {{
    // Person ID -> array of wish items
    'occ_child1_bday': [
      {{ id: 'w1', title: 'LEGO Classic Medium Brick Box', tier: 'Tier 2: ₹1,000 – ₹2,500', price: '₹2,399', amazon: 'lego classic medium creative brick box', claimedBy: null, notes: 'For building houses and starships' }},
      {{ id: 'w2', title: 'Harry Potter 7-Book Boxed Set', tier: 'Tier 3: ₹2,500 – ₹5,000', price: '₹2,899', amazon: 'harry potter complete box set bloomsbury', claimedBy: 'Family Member', notes: 'Loved book 1, wants the full series' }},
      {{ id: 'w3', title: 'Astronomical 70mm Refractor Telescope', tier: 'Tier 3: ₹2,500 – ₹5,000', price: '₹3,999', amazon: 'astronomical telescope 70mm aperture for kids', claimedBy: null, notes: 'For moon crater watching from balcony' }}
    ]
  }}
}};

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
    localStorage.removeItem('bgm_theme');
  }} else {{
    document.documentElement.setAttribute('data-theme', mode);
    localStorage.setItem('bgm_theme', mode);
  }}
}}

// LOAD / SAVE STORAGE
function loadFromStorage() {{
  try {{
    const saved = localStorage.getItem('birthday_gift_matrix_v1');
    if (saved) {{
      const parsed = JSON.parse(saved);
      if (Array.isArray(parsed.occasions)) state.occasions = parsed.occasions;
      if (parsed.wishlists) state.wishlists = parsed.wishlists;
      if (parsed.activeOccasionId) state.activeOccasionId = parsed.activeOccasionId;
    }}
    const savedTheme = localStorage.getItem('bgm_theme');
    if (savedTheme) setTheme(savedTheme);
  }} catch (e) {{}}
}}

function saveAllToStorage() {{
  try {{
    const toSave = {{
      occasions: state.occasions,
      wishlists: state.wishlists,
      activeOccasionId: state.activeOccasionId
    }};
    localStorage.setItem('birthday_gift_matrix_v1', JSON.stringify(toSave));
    showToast('💾 Occasions, wishlists &amp; reservations saved!');
  }} catch (e) {{
    showToast('⚠️ Storage error');
  }}
}}

// 12-MONTH WALL & COUNTDOWN
const MONTH_NAMES = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

function updateCountdown() {{
  // Find closest upcoming occasion
  const now = new Date();
  const currentMonth = now.getMonth() + 1; // 1-12
  const currentDay = now.getDate();

  let closest = null;
  let minDiffDays = 9999;

  state.occasions.forEach(occ => {{
    const parts = occ.date.split('-');
    const m = parseInt(parts[0]);
    const d = parseInt(parts[1]);

    let targetYear = now.getFullYear();
    let targetDate = new Date(targetYear, m - 1, d);
    if (targetDate < now) {{
      targetDate = new Date(targetYear + 1, m - 1, d);
    }}

    const diffDays = Math.ceil((targetDate - now) / (1000 * 60 * 60 * 24));
    if (diffDays < minDiffDays) {{
      minDiffDays = diffDays;
      closest = {{ occ, diffDays }};
    }}
  }});

  if (closest) {{
    document.getElementById('cdIcon').textContent = closest.occ.emoji || '🎂';
    document.getElementById('cdTitle').textContent = closest.occ.person + ' (' + closest.occ.type + ')';
    document.getElementById('cdSub').textContent = closest.occ.milestone || closest.occ.displayDate;
    document.getElementById('cdTimer').textContent = closest.diffDays === 0 ? '🎉 TODAY!' : '⏳ ' + closest.diffDays + ' Days Away';
  }}
}}

function renderMonthGrid() {{
  const grid = document.getElementById('monthGrid');
  if (!grid) return;
  grid.innerHTML = '';

  for (let m = 1; m <= 12; m++) {{
    const mStr = m < 10 ? '0' + m : '' + m;
    const mEvents = state.occasions.filter(o => o.date.startsWith(mStr));

    const box = document.createElement('div');
    box.className = 'month-box' + (mEvents.length > 0 ? ' has-events' : '');

    let eventsHtml = '';
    mEvents.forEach(ev => {{
      const isAct = ev.id === state.activeOccasionId;
      eventsHtml += `
        <div class="event-pill${{isAct ? ' is-active' : ''}}" onclick="selectOccasion('${{ev.id}}')">
          <span>${{ev.emoji || '🎂'}}</span>
          <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${{ev.person}}</span>
        </div>
      `;
    }});

    box.innerHTML = `
      <div class="month-name">${{MONTH_NAMES[m - 1]}} (${{mEvents.length}})</div>
      <div class="month-events">${{eventsHtml || '<div style="font-size: 11px; color: var(--text-faint); margin-top: 4px;">No events</div>'}}</div>
    `;
    grid.appendChild(box);
  }}
}}

function selectOccasion(id) {{
  state.activeOccasionId = id;
  renderMonthGrid();
  renderWishlist();
  const occ = state.occasions.find(o => o.id === id);
  if (occ) {{
    document.getElementById('activeWishlistPersonName').textContent = occ.person;
    document.getElementById('activePersonLabel').textContent = occ.person;
    showToast('Loaded wishlist for: <b>' + occ.person + '</b>');
  }}
}}

// TIERED WISHLIST RENDERING
function filterTier(tier) {{
  state.selectedTier = tier;
  document.querySelectorAll('.tier-chips .tier-chip').forEach(c => {{
    c.classList.toggle('active', c.textContent.includes(tier) || (tier === 'all' && c.textContent === 'All Tiers'));
  }});
  renderWishlist();
}}

function renderWishlist() {{
  const container = document.getElementById('wishList');
  if (!container) return;
  container.innerHTML = '';

  const list = state.wishlists[state.activeOccasionId] || [];
  const filtered = list.filter(item => {{
    if (state.selectedTier !== 'all' && item.tier !== state.selectedTier) return false;
    return true;
  }});

  if (filtered.length === 0) {{
    container.innerHTML = '<div style="text-align: center; padding: 30px; color: var(--text-faint); font-size: 13px;">No wish items in this tier yet. Add from the right or click "Add Custom Gift"!</div>';
    return;
  }}

  filtered.forEach((item, idx) => {{
    const card = document.createElement('div');
    const isClaimed = !!item.claimedBy;
    card.className = 'wish-item-card' + (isClaimed ? ' claimed' : '');

    const amazonLink = 'https://www.amazon.in/s?k=' + encodeURIComponent(item.amazon || item.title) + '&tag=dhrav-21';

    card.innerHTML = `
      <div class="wish-top-row">
        <div class="wish-title">${{item.title}}</div>
        <div class="wish-price">${{item.price || '₹1,000'}}</div>
      </div>
      <div class="wish-desc">${{item.notes || item.tier}}</div>
      <div class="wish-actions-row">
        <button type="button" class="btn-claim${{isClaimed ? ' claimed' : ''}}" onclick="openClaimModal('${{item.id}}')">
          <span>${{isClaimed ? '✅ Claimed by ' + item.claimedBy : '🛡️ Reserve / Claim'}}</span>
        </button>
        <div style="display: flex; gap: 6px; align-items: center;">
          <a href="${{amazonLink}}" target="_blank" rel="noopener noreferrer" class="btn-amazon-wish">
            <span>🛒 Buy (Tag: dhrav-21)</span>
          </a>
          <button type="button" class="preset-chip" style="color: var(--danger); margin:0; padding: 4px 8px;" onclick="removeWishItem('${{item.id}}')">✕</button>
        </div>
      </div>
    `;
    container.appendChild(card);
  }});
}}

function removeWishItem(itemId) {{
  let list = state.wishlists[state.activeOccasionId] || [];
  state.wishlists[state.activeOccasionId] = list.filter(i => i.id !== itemId);
  renderWishlist();
  saveAllToStorage();
  showToast('Item removed from wishlist.');
}}

// CURATED IDEAS BANK RENDERING
function renderIdeas() {{
  const grid = document.getElementById('ideasGrid');
  if (!grid) return;
  grid.innerHTML = '';

  DATA.gift_ideas.forEach(idea => {{
    const card = document.createElement('div');
    card.className = 'idea-card';
    const aLink = 'https://www.amazon.in/s?k=' + encodeURIComponent(idea.amazon || idea.title) + '&tag=dhrav-21';

    card.innerHTML = `
      <div class="idea-title">${{idea.title}}</div>
      <div class="idea-meta">
        <span>${{idea.tier}}</span>
        <span style="font-weight: 700; color: var(--gold);">${{idea.priceRange}}</span>
      </div>
      <div style="font-size: 11.5px; color: var(--text-dim); margin-top: 2px;">${{idea.desc}}</div>
      <div class="idea-actions">
        <button type="button" class="btn-claim" style="flex:1;" onclick="addIdeaToWishlist('${{idea.id}}')">
          <span>➕ Add to Wishlist</span>
        </button>
        <a href="${{aLink}}" target="_blank" rel="noopener noreferrer" class="btn-amazon-wish">
          <span>🛒 Buy</span>
        </a>
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function addIdeaToWishlist(ideaId) {{
  const idea = DATA.gift_ideas.find(i => i.id === ideaId);
  if (!idea) return;

  if (!state.wishlists[state.activeOccasionId]) {{
    state.wishlists[state.activeOccasionId] = [];
  }}

  state.wishlists[state.activeOccasionId].push({{
    id: 'w_' + Date.now() + Math.random().toString(36).substr(2, 4),
    title: idea.title,
    tier: idea.tier,
    price: idea.priceRange,
    amazon: idea.amazon,
    claimedBy: null,
    notes: idea.desc
  }});

  renderWishlist();
  saveAllToStorage();
  showToast(`🎁 Added <b>${{idea.title}}</b> to wishlist!`);
}}

// CLAIM / RESERVE MODAL
let activeClaimingItemId = null;
function openClaimModal(itemId) {{
  activeClaimingItemId = itemId;
  const list = state.wishlists[state.activeOccasionId] || [];
  const item = list.find(i => i.id === itemId);
  document.getElementById('claimBuyerName').value = item && item.claimedBy ? item.claimedBy : '';
  document.getElementById('claimModal').classList.add('open');
}}

function closeClaimModal() {{
  document.getElementById('claimModal').classList.remove('open');
}}

function confirmClaim() {{
  const name = document.getElementById('claimBuyerName').value.trim() || 'Reserved Relative';
  const list = state.wishlists[state.activeOccasionId] || [];
  const item = list.find(i => i.id === activeClaimingItemId);
  if (item) {{
    item.claimedBy = name;
  }}
  closeClaimModal();
  renderWishlist();
  saveAllToStorage();
  showToast(`🛡️ Marked as claimed by <b>${{name}}</b>! Duplicate prevented.`);
}}

function unclaimActiveItem() {{
  const list = state.wishlists[state.activeOccasionId] || [];
  const item = list.find(i => i.id === activeClaimingItemId);
  if (item) {{
    item.claimedBy = null;
  }}
  closeClaimModal();
  renderWishlist();
  saveAllToStorage();
  showToast('Reservation cleared. Item available to others.');
}}

// ADD OCCASION MODAL
function openOccasionModal() {{
  document.getElementById('occasionModal').classList.add('open');
}}

function closeOccasionModal() {{
  document.getElementById('occasionModal').classList.remove('open');
}}

function handleOccasionSubmit(e) {{
  e.preventDefault();
  const person = document.getElementById('occPerson').value.trim();
  const type = document.getElementById('occType').value;
  const emoji = document.getElementById('occEmoji').value.trim() || '🎂';
  const month = document.getElementById('occMonth').value;
  const day = parseInt(document.getElementById('occDay').value);
  const dayStr = day < 10 ? '0' + day : '' + day;
  const milestone = document.getElementById('occMilestone').value.trim() || type;

  const newOcc = {{
    id: 'occ_' + Date.now(),
    person,
    relationship: 'Family Member',
    type,
    date: `${{month}}-${{dayStr}}`,
    displayDate: `${{MONTH_NAMES[parseInt(month) - 1]}} ${{day}}`,
    milestone,
    emoji
  }};

  state.occasions.push(newOcc);
  state.activeOccasionId = newOcc.id;
  closeOccasionModal();
  updateCountdown();
  renderMonthGrid();
  selectOccasion(newOcc.id);
  saveAllToStorage();
  showToast(`🎉 Occasion for <b>${{person}}</b> added to your 12-month calendar!`);
}}

// ADD CUSTOM WISH MODAL
function openCustomWishModal() {{
  document.getElementById('wishModal').classList.add('open');
}}

function closeWishModal() {{
  document.getElementById('wishModal').classList.remove('open');
}}

function handleWishSubmit(e) {{
  e.preventDefault();
  const title = document.getElementById('wTitle').value.trim();
  const tier = document.getElementById('wTier').value;
  const price = document.getElementById('wPrice').value.trim() || '₹1,000';
  const notes = document.getElementById('wNotes').value.trim();
  const amazon = document.getElementById('wAmazon').value.trim() || title;

  if (!state.wishlists[state.activeOccasionId]) {{
    state.wishlists[state.activeOccasionId] = [];
  }}

  state.wishlists[state.activeOccasionId].push({{
    id: 'w_' + Date.now(),
    title,
    tier,
    price,
    amazon,
    claimedBy: null,
    notes
  }});

  closeWishModal();
  renderWishlist();
  saveAllToStorage();
  showToast(`🎁 Added custom gift: <b>${{title}}</b>`);
}}

// 4-ACTION SUITE HANDLERS
function shareWishlistWhatsApp() {{
  const occ = state.occasions.find(o => o.id === state.activeOccasionId) || state.occasions[0];
  const list = state.wishlists[state.activeOccasionId] || [];

  let itemsText = '';
  list.forEach(it => {{
    const claimStatus = it.claimedBy ? ` (Reserved by ${{it.claimedBy}})` : ' (Available to gift)';
    itemsText += `• ${{it.title}} [${{it.price}}]${{claimStatus}}\\n`;
  }});

  const text = `🎁 *${{occ.person.toUpperCase()}}'S GIFT WISHLIST* (${{occ.milestone || occ.type}})
━━━━━━━━━━━━━━━━━━━━━━
Date: ${{occ.displayDate}}

To make gifting easy and avoid duplicate presents, here are thoughtful ideas ${{occ.person}} would truly cherish:

${{itemsText || '• Contact parents for favorite ideas!\\n'}}
🛒 Search gifts with tracking tag dhrav-21 on Amazon India.
View & reserve live on Sarav's World:
https://iamsaravofficial.com/apps/birthday-gift-matrix/`;

  const url = 'https://api.whatsapp.com/send?text=' + encodeURIComponent(text);
  window.open(url, '_blank');
}}

function copyWishlistSummary() {{
  const occ = state.occasions.find(o => o.id === state.activeOccasionId) || state.occasions[0];
  const list = state.wishlists[state.activeOccasionId] || [];

  let text = `🎁 ${{occ.person}}'s Wishlist (${{occ.displayDate}})\\n`;
  list.forEach(i => {{
    text += `- ${{i.title}} (${{i.price}})${{i.claimedBy ? ' [Claimed by ' + i.claimedBy + ']' : ''}}\\n`;
  }});
  text += 'https://iamsaravofficial.com/apps/birthday-gift-matrix/';

  navigator.clipboard.writeText(text).then(() => {{
    showToast('📋 Wishlist copied to clipboard!');
  }}).catch(() => {{
    showToast('⚠️ Could not copy');
  }});
}}

// INITIALIZATION
window.addEventListener('DOMContentLoaded', () => {{
  loadFromStorage();
  updateCountdown();
  renderMonthGrid();
  renderIdeas();
  selectOccasion(state.activeOccasionId);
}});
</script>

</body>
</html>"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Built {out_path} successfully ({len(html_content)} bytes).")

if __name__ == "__main__":
    generate_birthday_matrix()
