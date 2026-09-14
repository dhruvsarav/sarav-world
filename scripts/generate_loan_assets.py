import os
import math
from PIL import Image, ImageDraw, ImageFont

def generate_loan_assets():
    out_dir = os.path.join("public", "apps", "home-loan-accelerometer")
    os.makedirs(out_dir, exist_ok=True)

    # 1. Favicon SVG
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141922" />
      <stop offset="100%" stop-color="#0C0F14" />
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F9D77E" />
      <stop offset="100%" stop-color="#E3A63E" />
    </linearGradient>
    <linearGradient id="teal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5EEAD4" />
      <stop offset="100%" stop-color="#0D9488" />
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#bg)" stroke="#2A3545" stroke-width="3"/>
  <!-- House silhouette with upward acceleration arrow -->
  <path d="M50 20 L24 42 L30 42 L30 76 L70 76 L70 42 L76 42 Z" fill="#1B222D" stroke="url(#gold)" stroke-width="3" stroke-linejoin="round"/>
  <!-- Doorway -->
  <rect x="43" y="52" width="14" height="24" rx="3" fill="#222B39" stroke="#5C6B80" stroke-width="1.5"/>
  <!-- Ascending Accelerometer Arrow -->
  <path d="M35 62 Q50 35 68 28" fill="none" stroke="url(#teal)" stroke-width="4" stroke-linecap="round"/>
  <polygon points="68,23 75,30 63,33" fill="#5EEAD4"/>
</svg>'''

    with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

    # 2. Master App Icon (1024x1024)
    img = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Base squircle
    margin = 48
    draw.rounded_rectangle(
        [(margin, margin), (1024 - margin, 1024 - margin)],
        radius=220,
        fill=(20, 25, 34, 255),
        outline=(42, 53, 69, 255),
        width=16
    )

    # Inner subtle glow
    draw.rounded_rectangle(
        [(margin + 16, margin + 16), (1024 - margin - 16, 1024 - margin - 16)],
        radius=204,
        fill=None,
        outline=(227, 166, 62, 50),
        width=4
    )

    # House Roof & Body
    roof_pts = [(512, 220), (220, 460), (280, 460), (280, 800), (744, 800), (744, 460), (804, 460)]
    draw.polygon(roof_pts, fill=(27, 34, 45, 255), outline=(227, 166, 62, 255))
    draw.line([(512, 220), (220, 460)], fill=(249, 215, 126, 255), width=24)
    draw.line([(512, 220), (804, 460)], fill=(249, 215, 126, 255), width=24)
    draw.line([(280, 460), (280, 800), (744, 800), (744, 460)], fill=(227, 166, 62, 255), width=18)

    # Doorway
    draw.rounded_rectangle([(436, 560), (588, 800)], radius=20, fill=(34, 43, 57, 255), outline=(92, 107, 128, 255), width=8)

    # Windows
    draw.rounded_rectangle([(330, 520), (410, 600)], radius=14, fill=(249, 215, 126, 80), outline=(227, 166, 62, 255), width=6)
    draw.rounded_rectangle([(614, 520), (694, 600)], radius=14, fill=(249, 215, 126, 80), outline=(227, 166, 62, 255), width=6)

    # Dynamic Accelerometer Gauge / Arc & Swoosh
    arc_box = [(300, 320), (724, 744)]
    draw.arc(arc_box, start=190, end=350, fill=(79, 176, 168, 255), width=22)

    # Upward lightning / arrow
    arrow_pts = [(512, 450), (620, 360), (590, 350), (680, 270), (620, 270), (730, 190), (660, 340), (680, 350)]
    draw.polygon(arrow_pts, fill=(94, 234, 212, 255), outline=(13, 148, 136, 255))

    img.save(os.path.join(out_dir, "loan-full.png"), "PNG")
    print("Generated loan-full.png")

    # Scaled icons
    img.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(out_dir, "favicon-192.png"))
    img.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(out_dir, "apple-touch-icon-180.png"))
    img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(out_dir, "favicon-32.png"))
    print("Generated favicon-192.png, apple-touch-icon-180.png, favicon-32.png")

    # 3. OG Image (1200x630)
    og = Image.new("RGBA", (1200, 630), (12, 15, 20, 255))
    og_draw = ImageDraw.Draw(og)

    # Outer border & subtle glow card
    og_draw.rounded_rectangle([(40, 40), (1160, 590)], radius=32, fill=(20, 25, 34, 255), outline=(42, 53, 69, 255), width=4)
    og_draw.rounded_rectangle([(48, 48), (1152, 582)], radius=28, fill=None, outline=(227, 166, 62, 40), width=2)

    # Left Badge
    og_draw.rounded_rectangle([(80, 76), (360, 116)], radius=12, fill=(34, 43, 57, 255), outline=(79, 176, 168, 255), width=2)

    # Mini Icon on Right
    mini_icon = img.resize((380, 380), Image.Resampling.LANCZOS)
    og.paste(mini_icon, (740, 125), mini_icon)

    # Load system font
    try:
        font_badge = ImageFont.truetype("arial.ttf", 18)
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 22)
        font_pill = ImageFont.truetype("arialbd.ttf", 20)
    except Exception:
        font_badge = font_title = font_sub = font_pill = ImageFont.load_default()

    og_draw.text((95, 86), "⚡ FINANCIAL ACCELERATOR", font=font_badge, fill=(94, 234, 212, 255))
    og_draw.text((80, 150), "Home Loan Prepayment &\nDebt-Free Accelerometer", font=font_title, fill=(255, 255, 255, 255), spacing=12)
    og_draw.text((80, 290), "Simulate reducing-balance prepayments, extra annual EMIs,\n5% step-ups, and shave off 8–12 years & lakhs of bank interest.", font=font_sub, fill=(148, 160, 178, 255), spacing=8)

    # Highlight metrics pills
    pills = [
        ("📉 Tenure Cut: Up to 10+ Yrs", 80, 410),
        ("💰 Interest Saved: ₹15L – ₹45L", 80, 474),
        ("⚖️ Reducing Balance Math", 440, 410),
        ("🛡️ Sec 24(b) Tax Insights", 440, 474)
    ]
    for text, px, py in pills:
        og_draw.rounded_rectangle([(px, py), (px + 330, py + 48)], radius=10, fill=(27, 34, 45, 255), outline=(42, 53, 69, 255), width=2)
        og_draw.text((px + 16, py + 12), text, font=font_pill, fill=(227, 166, 62, 255))

    # Bottom branding
    og_draw.text((80, 546), "iamsaravofficial.com/apps/home-loan-accelerometer/  •  100% Client-Side Privacy  •  Zero Telemetry", font=font_badge, fill=(92, 107, 128, 255))

    og.save(os.path.join(out_dir, "og-image.png"), "PNG")
    print("Generated og-image.png")

if __name__ == "__main__":
    generate_loan_assets()
