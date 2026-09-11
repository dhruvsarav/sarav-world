import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
WIDTH, HEIGHT = 1200, 630

# Font paths
FONT_BOLD = 'C:/Windows/Fonts/segoeuib.ttf'
FONT_REGULAR = 'C:/Windows/Fonts/segoeui.ttf'
FONT_SEMI = 'C:/Windows/Fonts/segoeuisl.ttf'
FONT_MONO = 'C:/Windows/Fonts/consola.ttf'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def draw_app_icon(draw, x, y, icon_type, theme_family):
    """Draws a clean geometric brand icon on the top-left."""
    size = 48
    if theme_family == 'gold_light':
        # Physical gold light container
        draw.rounded_rectangle([x, y, x + size, y + size], radius=12, fill='#FFF8E7', outline='#D8B979', width=2)
        accent = '#C1810A'
        accent2 = '#8B5E00'
    elif theme_family == 'gold':
        # Obsidian container with gold border
        draw.rounded_rectangle([x, y, x + size, y + size], radius=12, fill='#1D1913', outline='#52411E', width=2)
        accent = '#FFC04D'
        accent2 = '#E5A93C'
    else:
        # Deep navy container with border
        draw.rounded_rectangle([x, y, x + size, y + size], radius=12, fill='#1B222D', outline='#2A3545', width=2)
        accent = '#E3A63E'
        accent2 = '#4FB0A8'

    # Inner geometric shapes based on icon_type
    if icon_type == 'coins':
        # Stacked coin bars
        draw.rounded_rectangle([x+10, y+12, x+38, y+18], radius=3, fill=accent)
        draw.rounded_rectangle([x+14, y+21, x+38, y+27], radius=3, fill=accent2)
        draw.rounded_rectangle([x+18, y+30, x+38, y+36], radius=3, fill='#1B8A3D' if theme_family=='gold_light' else ('#5FBF77' if theme_family!='gold' else '#FFD580'))
    elif icon_type == 'house':
        # House shape with budget lines
        draw.polygon([(x+24, y+10), (x+10, y+22), (x+38, y+22)], fill=accent)
        draw.rectangle([x+13, y+22, x+35, y+37], fill=accent2)
        draw.rectangle([x+18, y+26, x+30, y+34], fill='#FFF8E7' if theme_family=='gold_light' else ('#0C0F14' if theme_family!='gold' else '#12100C'))
    elif icon_type == 'chart':
        # Bar chart
        draw.rounded_rectangle([x+11, y+24, x+17, y+36], radius=2, fill=accent)
        draw.rounded_rectangle([x+21, y+16, x+27, y+36], radius=2, fill=accent2)
        draw.rounded_rectangle([x+31, y+10, x+37, y+36], radius=2, fill='#1B8A3D' if theme_family=='gold_light' else ('#5FBF77' if theme_family!='gold' else '#FFD580'))
    elif icon_type == 'bank':
        # Pillar bank shape
        draw.polygon([(x+24, y+10), (x+10, y+18), (x+38, y+18)], fill=accent)
        draw.rectangle([x+13, y+20, x+17, y+33], fill=accent2)
        draw.rectangle([x+22, y+20, x+26, y+33], fill=accent2)
        draw.rectangle([x+31, y+20, x+35, y+33], fill=accent2)
        draw.rectangle([x+10, y+33, x+38, y+37], fill=accent)
    elif icon_type == 'slang':
        # Chat bubbles / speech icon
        draw.rounded_rectangle([x+10, y+12, x+32, y+28], radius=6, fill=accent)
        draw.rounded_rectangle([x+18, y+22, x+38, y+36], radius=6, fill=accent2)
    elif icon_type == 'gold':
        # Gold bar ingot
        draw.polygon([(x+14, y+14), (x+34, y+14), (x+38, y+28), (x+10, y+28)], fill='#D4AF37' if theme_family=='gold_light' else '#FFC04D')
        draw.polygon([(x+10, y+28), (x+38, y+28), (x+34, y+36), (x+14, y+36)], fill='#8B5E00' if theme_family=='gold_light' else '#B8860B')
    elif icon_type == 'loan':
        # Scales of loan & pledge
        draw.line([(x+24, y+12), (x+24, y+36)], fill=accent, width=2)
        draw.line([(x+12, y+18), (x+36, y+18)], fill=accent, width=2)
        draw.polygon([(x+10, y+26), (x+18, y+26), (x+14, y+20)], fill=accent2)
        draw.polygon([(x+30, y+26), (x+38, y+26), (x+34, y+20)], fill=accent2)
    else:
        # Default layered cards
        draw.rounded_rectangle([x+10, y+12, x+38, y+36], radius=6, fill=accent2)
        draw.rounded_rectangle([x+14, y+16, x+34, y+32], radius=4, fill=accent)

def generate_og_card(app_config):
    family = app_config['family']
    
    # Palette definition
    if family == 'gold_light':
        bg_color = '#F7F3EB'
        card_bg = '#FFFFFF'
        border_color = '#E2D5BE'
        accent_border = '#C1810A'
        eyebrow_color = '#A76906'
        title_color = '#2E1E05'
        sub_color = '#6E5D46'
        bullet_text_color = '#2E1E05'
        url_color = '#8A7554'
        tag_bg = '#F6E3B0'
        tag_text = '#8B5E00'
    elif family == 'gold':
        bg_color = '#12100C'
        card_bg = '#1D1913'
        border_color = '#38290E'
        accent_border = '#E5A93C'
        eyebrow_color = '#E5A93C'
        title_color = '#FFC04D'
        sub_color = '#B0A28E'
        bullet_text_color = '#F7F2E8'
        url_color = '#8A7554'
        tag_bg = '#2E2412'
        tag_text = '#FFC04D'
    else: # family == 'navy'
        bg_color = '#0C0F14'
        card_bg = '#141922'
        border_color = '#2A3545'
        accent_border = '#4FB0A8'
        eyebrow_color = '#4FB0A8'
        title_color = '#FFFFFF'
        sub_color = '#94A0B2'
        bullet_text_color = '#EAEFF5'
        url_color = '#5C6B80'
        tag_bg = '#1B222D'
        tag_text = '#E3A63E'

    im = Image.new('RGB', (WIDTH, HEIGHT), bg_color)
    draw = ImageDraw.Draw(im)

    # 1. Subtle decorative background grid / corner glow
    # Draw soft outer frame
    draw.rectangle([20, 20, WIDTH-20, HEIGHT-20], outline=border_color, width=1)
    # Accent top border strip
    draw.line([(20, 20), (WIDTH-20, 20)], fill=accent_border, width=4)

    # 2. Geometric App Icon on top-left
    draw_app_icon(draw, 72, 60, app_config['icon'], family)

    # 3. Eyebrow Tag & App Category
    font_eyebrow = get_font(FONT_BOLD, 15)
    eyebrow_text = app_config['eyebrow'].upper()
    draw.text((134, 66), eyebrow_text, font=font_eyebrow, fill=eyebrow_color)

    font_sub_tag = get_font(FONT_REGULAR, 14)
    draw.text((134, 88), "SARAV'S WORLD · CLIENT-SIDE SUITE", font=font_sub_tag, fill=url_color)

    # 4. Badge on top-right
    if app_config.get('badge'):
        font_badge = get_font(FONT_BOLD, 13)
        badge_w = draw.textlength(app_config['badge'], font=font_badge)
        bx = WIDTH - 72 - badge_w - 24
        draw.rounded_rectangle([bx, 60, WIDTH-72, 92], radius=16, fill=tag_bg, outline=border_color, width=1)
        draw.text((bx + 12, 67), app_config['badge'], font=font_badge, fill=tag_text)

    # 5. Main Title (Big & Bold)
    font_title = get_font(FONT_BOLD, 54)
    title_lines = app_config['title'].split('\n')
    ty = 150
    for line in title_lines:
        draw.text((72, ty), line, font=font_title, fill=title_color)
        ty += 64

    # 6. Subtitle / Value Proposition
    font_sub = get_font(FONT_REGULAR, 24)
    draw.text((72, ty + 8), app_config['subtitle'], font=font_sub, fill=sub_color)

    # 7. Divider rule
    dy = ty + 52
    draw.line([(72, dy), (WIDTH-72, dy)], fill=border_color, width=1)

    # 8. Feature Bullets with colored dots
    font_bullet = get_font(FONT_REGULAR, 20)
    font_bullet_bold = get_font(FONT_BOLD, 20)
    
    by = dy + 28
    for dot_color, b_prefix, b_text in app_config['bullets']:
        # Draw colored dot
        draw.ellipse([72, by + 6, 86, by + 20], fill=dot_color)
        # Prefix in bold, text in regular
        draw.text((98, by), b_prefix + " ", font=font_bullet_bold, fill=bullet_text_color)
        pw = draw.textlength(b_prefix + " ", font=font_bullet_bold)
        draw.text((98 + pw, by), b_text, font=font_bullet, fill=sub_color)
        by += 40

    # 9. Bottom URL & Telemetry Note
    font_url = get_font(FONT_MONO, 16)
    draw.text((72, HEIGHT - 56), app_config['url'], font=font_url, fill=url_color)
    
    font_badge_btm = get_font(FONT_REGULAR, 14)
    btm_note = "Zero Telemetry · 100% Client-Side Computation"
    bw = draw.textlength(btm_note, font=font_badge_btm)
    draw.text((WIDTH - 72 - bw, HEIGHT - 54), btm_note, font=font_badge_btm, fill=url_color)

    # Save
    out_path = Path(app_config['dest'])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(str(out_path), 'PNG', optimize=True)
    print(f"Generated: {out_path} ({os.path.getsize(out_path)} bytes)")

APPS_CONFIG = [
    # -------------------------------------------------------------
    # FAMILY A: PRECIOUS METALS SUITE (Physical Gold Light Mode)
    # -------------------------------------------------------------
    {
        "id": "gold-price-estimator",
        "family": "gold_light",
        "icon": "gold",
        "eyebrow": "Precious Metals · Retail Valuation",
        "badge": "INDIAN JEWELLERY ENGINE",
        "title": "Metal Price Estimator",
        "subtitle": "Real-world Indian jewellery billing, wastage deduction & portfolio gain",
        "bullets": [
            ("#C1810A", "Precise Indian Billing:", "Gross weight, stone deductions, wastage (VA in g & %), and 3% GST"),
            ("#1B8A3D", "Live Portfolio Valuation:", "Tracks Gold & Silver appreciation in Pavans (8g) and Tolas (11.66g)")
        ],
        "url": "iamsaravofficial.com/apps/gold-price-estimator",
        "dest": "D:/Websites/SaravsWorld/public/apps/gold-price-estimator/og-image.png"
    },
    {
        "id": "gold-loan-calculator",
        "family": "gold_light",
        "icon": "loan",
        "eyebrow": "Precious Metals · RBI Compliance",
        "badge": "MAX 75% LTV CAP",
        "title": "Gold Loan Calculator",
        "subtitle": "RBI Master Directions compliance, loan-per-gram & risk simulator",
        "bullets": [
            ("#C1810A", "Statutory Lending Math:", "Strict 75% LTV ceiling evaluated against 30-day conservative 24K rate"),
            ("#1B8A3D", "3 Repayment Schemes:", "Monthly Interest Only, Bullet Repayment (12-mo), and Standard EMI")
        ],
        "url": "iamsaravofficial.com/apps/gold-loan-calculator",
        "dest": "D:/Websites/SaravsWorld/public/apps/gold-loan-calculator/og-image.png"
    },
    {
        "id": "digigold-calculator",
        "family": "gold_light",
        "icon": "coins",
        "eyebrow": "Precious Metals · Digital Gold",
        "badge": "FRICTION & TAX CLOCK",
        "title": "DigiGold SIP Calculator",
        "subtitle": "True in-hand redemption wealth after 3% GST, bid-ask spreads & taxes",
        "bullets": [
            ("#C1810A", "Sunk Friction Modeled:", "3% non-refundable GST on every lot plus platform buy-sell spreads"),
            ("#1B8A3D", "Per-Lot Tax Clock:", "LTCG 12.5% (≥ 24 months) vs STCG slab rate under Budget 2024 rules")
        ],
        "url": "iamsaravofficial.com/apps/digigold-calculator",
        "dest": "D:/Websites/SaravsWorld/public/apps/digigold-calculator/og-image.png"
    },

    # -------------------------------------------------------------
    # FAMILY B & C: FINANCIAL WEALTH & MODERN SUITE (Deep Space Navy)
    # -------------------------------------------------------------
    {
        "id": "salary-planner",
        "family": "navy",
        "icon": "chart",
        "eyebrow": "Financial Planning · Advisory Sequenced",
        "badge": "SAFETY NET FIRST",
        "title": "Where Your Salary Should Go",
        "subtitle": "Sequenced safety net first, debt-aware HLV cover, then surplus investing",
        "bullets": [
            ("#E3A63E", "Projected FHS Scorecard:", "Family Intelligence scoring across Savings, Budget, Recurring & Solvency"),
            ("#4FB0A8", "Debt-Aware Protection:", "HLV life cover sizing including outstanding liabilities & 3-way surplus routing")
        ],
        "url": "iamsaravofficial.com/apps/salary-planner",
        "dest": "D:/Websites/SaravsWorld/public/apps/salary-planner/og-image.png"
    },
    {
        "id": "home-budget-planner",
        "family": "navy",
        "icon": "house",
        "eyebrow": "Household Finance · Living Cashflow",
        "badge": "BILL DUE TRACKER",
        "title": "Your Whole Month, One Page",
        "subtitle": "Fixed obligations, daily running ledger, 50/30/20 diagnosis & real FHS",
        "bullets": [
            ("#E3A63E", "Bill Due Date Checklist:", "Home Loan, Car Loan, Rent, Utilities with 1-tap 'Mark as Paid' flow"),
            ("#4FB0A8", "Household Diagnostics:", "50/30/20 rule, FOIR debt health, emergency runway & real FHS trend")
        ],
        "url": "iamsaravofficial.com/apps/home-budget-planner",
        "dest": "D:/Websites/SaravsWorld/public/apps/home-budget-planner/og-image.png"
    },
    {
        "id": "retirement-planner",
        "family": "navy",
        "icon": "chart",
        "eyebrow": "Retirement Wealth · NPS + EPF",
        "badge": "AGE 60 WEALTH SPLIT",
        "title": "Liquid vs Locked Wealth at 60",
        "subtitle": "Spendable cash vs locked annuity with annual salary step-up compounding",
        "bullets": [
            ("#E3A63E", "True Liquidity Split:", "100% EPF + 60% NPS lump-sum tax-exempt vs 40% NPS taxable annuity"),
            ("#4FB0A8", "Inflation & Real Math:", "Statutory EPS monthly pension, salary step-up, and Rule 9D advisory")
        ],
        "url": "iamsaravofficial.com/apps/retirement-planner",
        "dest": "D:/Websites/SaravsWorld/public/apps/retirement-planner/og-image.png"
    },
    {
        "id": "fd-calculator",
        "family": "navy",
        "icon": "bank",
        "eyebrow": "Banking · Fixed Deposits",
        "badge": "SEC 194A TDS MATH",
        "title": "Cumulative vs Payout FD Engine",
        "subtitle": "Quarterly IBA compounding with Budget 2025 TDS & slab reconciliation",
        "bullets": [
            ("#E3A63E", "Budget 2025 Bank TDS:", "Evaluates ₹50,000 general and ₹1,00,000 senior citizen TDS limits"),
            ("#4FB0A8", "ITR Slab Reconciliation:", "Marginal tax slab (0%–30%) true liability and inflation-adjusted yield")
        ],
        "url": "iamsaravofficial.com/apps/fd-calculator",
        "dest": "D:/Websites/SaravsWorld/public/apps/fd-calculator/og-image.png"
    },
    {
        "id": "rd-calculator",
        "family": "navy",
        "icon": "bank",
        "eyebrow": "Banking · Systematic Deposits",
        "badge": "OFFICIAL IBA MATH",
        "title": "The Real RD Maturity Value",
        "subtitle": "Exact IBA quarterly formula with annual 12-month block TDS evaluation",
        "bullets": [
            ("#E3A63E", "Official Banking Math:", "Quarterly-compounded formula verified to the exact Indian rupee"),
            ("#4FB0A8", "12-Month Block TDS:", "Section 194A TDS checked per accrual cycle with premature closure penalty")
        ],
        "url": "iamsaravofficial.com/apps/rd-calculator",
        "dest": "D:/Websites/SaravsWorld/public/apps/rd-calculator/og-image.png"
    },
    {
        "id": "genzalphaslang",
        "family": "navy",
        "icon": "slang",
        "eyebrow": "Sociolinguistics · Dialect Decoder",
        "badge": "156 NEURAL AUDIOS",
        "title": "Then & Now: GenZ & Alpha Slang",
        "subtitle": "How the next generation communicates with millennial translations & audio",
        "bullets": [
            ("#A78BFA", "156 Verified Entries:", "Viral modern lingo, internet catchphrases, and rapid texting shorthands"),
            ("#38BDF8", "Dual-Engine Audio:", "Authentic neural voice pronunciation with automatic offline speech fallback")
        ],
        "url": "iamsaravofficial.com/apps/genzalphaslang",
        "dest": "D:/Websites/SaravsWorld/public/apps/genzalphaslang/og-image.png"
    }
]

def main():
    print(f"Regenerating {len(APPS_CONFIG)} OpenGraph preview cards...")
    for cfg in APPS_CONFIG:
        generate_og_card(cfg)
    
    # Also save a copy of home-budget-planner to D:/sdrv/metalprice/newapps/home-budget-planner/og-image.png
    src_hbp = Path("D:/Websites/SaravsWorld/public/apps/home-budget-planner/og-image.png")
    dst_hbp = Path("D:/sdrv/metalprice/newapps/home-budget-planner/og-image.png")
    if src_hbp.exists():
        import shutil
        shutil.copy2(src_hbp, dst_hbp)
        print(f"Synced copy to: {dst_hbp}")

if __name__ == '__main__':
    main()
