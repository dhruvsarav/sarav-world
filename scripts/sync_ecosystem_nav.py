#!/usr/bin/env python3
"""
scripts/sync_ecosystem_nav.py
==============================
One-command synchronizer for the two standardized ecosystem menubars:
1. Enterprise Suite Bar: Mode 'enterprise' (8 E-Apps items)
2. Consumer & Arcade Bar: Mode 'consumer' (10 Apps, 11 Games, 4 Projects)
3. Master Gateway Bar: Mode 'gateway' (All 4 categories for /playground/ & /projects/)

Usage:
  python scripts/sync_ecosystem_nav.py
"""

import os
import re

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PUBLIC_DIR = os.path.join(REPO_DIR, 'public')

APPS = [
    ("🎡 Playground Hub", "https://iamsaravofficial.com/apps/"),
    ("GenZ & Alpha Slang", "https://iamsaravofficial.com/apps/genzalphaslang/"),
    ("Salary Planner", "https://iamsaravofficial.com/apps/salary-planner/"),
    ("Home Budget Planner", "https://iamsaravofficial.com/apps/home-budget-planner/"),
    ("Retirement Planner", "https://iamsaravofficial.com/apps/retirement-planner/"),
    ("Gold Price Estimator", "https://iamsaravofficial.com/apps/gold-price-estimator/"),
    ("Gold Loan Calculator", "https://iamsaravofficial.com/apps/gold-loan-calculator/"),
    ("DigiGold Calculator", "https://iamsaravofficial.com/apps/digigold-calculator/"),
    ("FD Calculator", "https://iamsaravofficial.com/apps/fd-calculator/"),
    ("RD Calculator", "https://iamsaravofficial.com/apps/rd-calculator/"),
]

EAPPS = [
    ("🏢 Executive Suite Hub", "https://iamsaravofficial.com/eapps/"),
    ("🧠 Tokenomics (AI Economics)", "https://iamsaravofficial.com/apps/tokenomics/"),
    ("👷 SD Optimizer", "https://iamsaravofficial.com/apps/sdoptimizer/"),
    ("🗺️ Field Services Hub-Spoke", "https://iamsaravofficial.com/apps/fsoptimizer/"),
    ("🖥️ Deskside Support Staffing", "https://iamsaravofficial.com/apps/desksidestaffing/"),
    ("🧭 DEX Advisor", "https://iamsaravofficial.com/apps/dexadvisor/"),
    ("🎫 ITSM Platform Advisor", "https://iamsaravofficial.com/apps/itsmadvisor/"),
    ("⚖️ Vendor RFP Weighted Scorer", "https://iamsaravofficial.com/apps/rfpscorer/"),
]

GAMES = [
    ("🎰 Games Arcade Hub", "https://iamsaravofficial.com/games/"),
    ("🎰 Family Jackpot", "https://iamsaravofficial.com/games/familywinner/"),
    ("💖 Senti-Meter", "https://iamsaravofficial.com/games/sentimeter/"),
    ("🎁 Secret Box", "https://iamsaravofficial.com/games/secretbox/"),
    ("🏓 Ping-Pong Cup Toss", "https://iamsaravofficial.com/games/cuptoss/"),
    ("🍾 Bottle Flip Showdown", "https://iamsaravofficial.com/games/bottleflip/"),
    ("⚡ Samosa Snatch", "https://iamsaravofficial.com/games/samosasnatch/"),
    ("🗣️ Chit-Charades", "https://iamsaravofficial.com/games/chitcharades/"),
    ("🎡 Snack Roulette", "https://iamsaravofficial.com/games/snackroulette/"),
    ("🎙️ Dialogue Detective", "https://iamsaravofficial.com/games/dialoguedetective/"),
    ("🎯 Desi Gulel Strike", "https://iamsaravofficial.com/games/gulelstrike/"),
]

PROJECTS = [
    ("🏛️ Projects Hub", "https://iamsaravofficial.com/projects/"),
    ("Temples of Tamil Gods", "https://iamsaravofficial.com/temples/"),
    ("FactDrop", "https://iamsaravofficial.com/factdrop/"),
    ("Thirukkural Hub", "https://iamsaravofficial.com/thirukkural/"),
]

def is_current(rel_path, target_url):
    rel_clean = rel_path.replace("\\", "/").replace("/index.html", "").replace("index.html", "").strip("/")
    target_clean = target_url.replace("https://iamsaravofficial.com", "").replace("/index.html", "").strip("/")
    return rel_clean == target_clean

def build_dropdown(title, items, rel_path):
    has_active = any(is_current(rel_path, url) for _, url in items)
    btn_style = ' style="color:var(--accent);"' if has_active else ''
    lines = [
        f'      <div class="eco-dropdown">',
        f'        <button class="eco-dropbtn" aria-haspopup="true"{btn_style}>{title} <span class="eco-caret">▾</span></button>',
        f'        <div class="eco-menu">'
    ]
    for name, url in items:
        cur_cls = ' class="current"' if is_current(rel_path, url) else ''
        lines.append(f'          <a href="{url}"{cur_cls}>{name}</a>')
    lines.append('        </div>')
    lines.append('      </div>')
    return '\n'.join(lines)

def build_menubar(mode, rel_path):
    is_tokenomics = 'tokenomics' in rel_path
    is_projects = 'projects' in rel_path

    # Left Links
    links = [
        '      <a href="https://iamsaravofficial.com/" class="eco-brand">← Sarav\'s World</a>',
        '      <span class="eco-divider">│</span>'
    ]

    if mode == 'enterprise':
        links.append(build_dropdown('E-Apps', EAPPS, rel_path))
        if is_tokenomics:
            right = '<div><span class="eco-suite-badge">🧠 Enterprise AI Economics · Version 2026.09</span></div>'
        else:
            right = '<div><span class="eco-suite-badge"><img src="https://iamsaravofficial.com/eapps/eapps-square.png" alt="" style="width:14px; height:14px; border-radius:3px; vertical-align:middle; margin-right:4px;">Digital Workplace Suite · Version 2026.09</span></div>'
    elif mode == 'gateway':
        links.append(build_dropdown('Apps', APPS, rel_path))
        links.append('      <span class="eco-divider">│</span>')
        links.append(build_dropdown('E-Apps', EAPPS, rel_path))
        links.append('      <span class="eco-divider">│</span>')
        links.append(build_dropdown('Games', GAMES, rel_path))
        links.append('      <span class="eco-divider">│</span>')
        links.append(build_dropdown('Projects', PROJECTS, rel_path))
        if is_projects:
            right = (
                '<div style="display:flex; align-items:center; gap:12px;">\n'
                '      <a href="https://iamsaravofficial.com/playground/" style="text-decoration:none; color:var(--text-dim); font-size:12.5px; font-weight:600;">🎪 Playground</a>\n'
                '      <a href="https://iamsaravofficial.com/apps/tokenomics/" class="eco-tokenomics">🧠 Enterprise AI Economics</a>\n'
                '    </div>'
            )
        else:
            right = '<div><a href="https://iamsaravofficial.com/apps/tokenomics/" class="eco-tokenomics">🧠 Enterprise AI Economics</a></div>'
    else:
        # consumer mode
        links.append(build_dropdown('Apps', APPS, rel_path))
        links.append('      <span class="eco-divider">│</span>')
        links.append(build_dropdown('Games', GAMES, rel_path))
        links.append('      <span class="eco-divider">│</span>')
        links.append(build_dropdown('Projects', PROJECTS, rel_path))
        right = (
            '<div style="display:flex; align-items:center; gap:12px;">\n'
            '      <a href="https://iamsaravofficial.com/playground/" style="text-decoration:none; color:var(--text-dim); font-size:12.5px; font-weight:600;">🎪 Playground</a>\n'
            '      <a href="https://iamsaravofficial.com/apps/tokenomics/" class="eco-tokenomics">🧠 Enterprise AI Economics</a>\n'
            '    </div>'
        )

    left_block = '\n'.join(links)
    return (
        '<!-- Sarav\'s World Ecosystem Navigation Bar -->\n'
        '<div class="ecosystem-bar">\n'
        '  <div class="ecosystem-inner">\n'
        '    <div class="ecosystem-links">\n'
        f'{left_block}\n'
        '    </div>\n'
        f'    {right}\n'
        '  </div>\n'
        '</div>'
    )

def get_file_mode(rel_path):
    p = rel_path.replace("\\", "/").lower()
    if p.startswith('playground') or p.startswith('projects'):
        return 'gateway'
    if (
        p.startswith('eapps') or
        'tokenomics' in p or
        'sdoptimizer' in p or
        'fsoptimizer' in p or
        'desksidestaffing' in p or
        'dexadvisor' in p or
        'itsmadvisor' in p or
        'rfpscorer' in p
    ):
        return 'enterprise'
    if 'samosasnatch' in p:
        return None # dedicated 2P duel screen
    return 'consumer'

def sync_file(file_path):
    rel_path = os.path.relpath(file_path, PUBLIC_DIR)
    mode = get_file_mode(rel_path)
    if not mode:
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match ecosystem-bar div block
    pattern = re.compile(
        r'(<!--.*?Ecosystem Navigation Bar.*?-->\s*)?<div class="ecosystem-bar">.*?</div>\s*</div>\s*</div>',
        re.DOTALL
    )

    if not pattern.search(content):
        # Fallback simpler pattern
        pattern = re.compile(r'<div class="ecosystem-bar">.*?</div>\s*</div>', re.DOTALL)
        if not pattern.search(content):
            return False

    new_bar = build_menubar(mode, rel_path)
    new_content, count = pattern.subn(new_bar, content, count=1)
    if count > 0 and new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    updated = 0
    checked = 0
    for root, dirs, files in os.walk(PUBLIC_DIR):
        dirs[:] = [d for d in dirs if d not in ('temples', 'thirukkural', 'swastikastra', 'node_modules', '.git')]
        for f in files:
            if f == 'index.html':
                fp = os.path.join(root, f)
                rel = os.path.relpath(fp, PUBLIC_DIR)
                mode = get_file_mode(rel)
                if mode:
                    checked += 1
                    if sync_file(fp):
                        print(f"[{mode.upper()}] Synced: {rel}")
                        updated += 1
    print(f"\nCompleted! Checked {checked} files, updated {updated} files.")

if __name__ == '__main__':
    main()
