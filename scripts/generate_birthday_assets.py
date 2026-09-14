import os
from PIL import Image, ImageDraw, ImageFont

def render_gift_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 128.0

    # Squircle background
    r = int(28 * scale)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(20, 24, 34, 255), outline=(255, 159, 28, 120), width=max(1, int(2 * scale)))

    cx, cy = size / 2, size / 2

    # Draw festive gift box with ribbon and bow
    gw = int(68 * scale)
    gh = int(58 * scale)
    gx = int(cx - gw / 2)
    gy = int(cy - gh / 2 + 10 * scale)

    # Gift box base
    draw.rounded_rectangle([gx, gy, gx + gw, gy + gh], radius=int(6 * scale), fill=(235, 75, 105, 255), outline=(255, 255, 255, 220), width=max(1, int(2 * scale)))

    # Box lid
    lid_h = int(14 * scale)
    lid_w = gw + int(8 * scale)
    lx = int(cx - lid_w / 2)
    ly = gy - lid_h + int(2 * scale)
    draw.rounded_rectangle([lx, ly, lx + lid_w, ly + lid_h], radius=int(4 * scale), fill=(245, 95, 125, 255), outline=(255, 255, 255, 220), width=max(1, int(1.5 * scale)))

    # Golden vertical ribbon
    rw = int(14 * scale)
    rx = int(cx - rw / 2)
    draw.rectangle([rx, ly, rx + rw, gy + gh], fill=(255, 185, 45, 255))

    # Golden horizontal ribbon on box
    rh_w = int(10 * scale)
    ry = int(gy + gh / 2 - rh_w / 2)
    draw.rectangle([gx, ry, gx + gw, ry + rh_w], fill=(255, 185, 45, 255))

    # Ribbon bow at top
    bow_r = int(12 * scale)
    bow_y = ly - int(4 * scale)
    draw.ellipse([cx - int(18 * scale), bow_y - bow_r, cx - int(2 * scale), bow_y + int(2 * scale)], fill=(255, 200, 60, 255), outline=(230, 160, 20, 255), width=max(1, int(1.5 * scale)))
    draw.ellipse([cx + int(2 * scale), bow_y - bow_r, cx + int(18 * scale), bow_y + int(2 * scale)], fill=(255, 200, 60, 255), outline=(230, 160, 20, 255), width=max(1, int(1.5 * scale)))
    # Bow center knot
    draw.ellipse([cx - int(6 * scale), bow_y - int(8 * scale), cx + int(6 * scale), bow_y + int(4 * scale)], fill=(255, 180, 30, 255))

    return img

def create_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141922"/>
      <stop offset="100%" stop-color="#0C0F14"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF5E7E"/>
      <stop offset="100%" stop-color="#E11D48"/>
    </linearGradient>
    <linearGradient id="goldRibbon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
  </defs>
  <rect width="128" height="128" rx="28" fill="url(#bg)" stroke="#FF5E7E" stroke-width="2.5" stroke-opacity="0.4"/>
  <!-- Gift box body -->
  <rect x="30" y="58" width="68" height="54" rx="6" fill="url(#boxGrad)" stroke="#FFF" stroke-width="2" stroke-opacity="0.8"/>
  <!-- Box lid -->
  <rect x="25" y="44" width="78" height="16" rx="4" fill="#FF7597" stroke="#FFF" stroke-width="1.5" stroke-opacity="0.9"/>
  <!-- Gold vertical ribbon -->
  <rect x="57" y="44" width="14" height="68" fill="url(#goldRibbon)"/>
  <!-- Gold horizontal ribbon -->
  <rect x="30" y="80" width="68" height="10" fill="url(#goldRibbon)"/>
  <!-- Bow loops -->
  <path d="M64,44 C50,28 38,36 50,46 Z" fill="url(#goldRibbon)"/>
  <path d="M64,44 C78,28 90,36 78,46 Z" fill="url(#goldRibbon)"/>
  <circle cx="64" cy="42" r="6" fill="#D97706"/>
</svg>'''
    return svg

def create_og_image():
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), (12, 15, 20))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_subtitle = ImageFont.truetype("arial.ttf", 23)
        font_badge = ImageFont.truetype("arialbd.ttf", 18)
        font_tag = ImageFont.truetype("arial.ttf", 18)
    except:
        font_title = font_subtitle = font_badge = font_tag = ImageFont.load_default()

    # Top ambient line
    draw.rectangle([0, 0, width, 12], fill=(255, 94, 126))

    # Badge
    draw.rounded_rectangle([40, 50, 420, 92], radius=8, fill=(35, 18, 25), outline=(255, 94, 126))
    draw.text((60, 62), "🎁 12-MONTH OCCASIONS & WISHLISTS", font=font_badge, fill=(255, 228, 235))

    # Title
    draw.text((40, 126), "Family Birthday & Milestone Gift Matrix", font=font_title, fill=(255, 255, 255))
    draw.text((40, 196), "12-Month Occasion Wall, Budget Envelopes, Anti-Duplicate Wishlists & Amazon Buying", font=font_subtitle, fill=(148, 163, 184))

    # Feature Pills
    features = [
        ("📅 12-Month Interactive Occasion & Milestone Wall", 40, 268),
        ("💰 4 Tiered Budget Envelopes (₹500 to ₹5,000+)", 450, 268),
        ("🛡️ Anti-Duplicate Reservation Engine for Relatives", 40, 338),
        ("⏳ Real-Time Birthday & Anniversary Countdown", 450, 338),
        ("🖨️ Printable A4 12-Month Family Calendar Poster", 40, 408),
        ("💬 1-Tap Polite WhatsApp Wishlist Broadcast", 450, 408),
        ("🛍️ Amazon Wishlist Buying Links (tag: dhrav-21)", 40, 478),
        ("🔒 100% Client-Side Privacy • Zero Telemetry", 450, 478)
    ]
    for text, x, y in features:
        draw.rounded_rectangle([x, y, x + 380, y + 48], radius=10, fill=(20, 25, 34), outline=(42, 53, 69))
        draw.text((x + 16, y + 14), text, font=font_tag, fill=(226, 232, 240))

    # Watermark
    draw.text((40, 570), "iamsaravofficial.com/apps/birthday-gift-matrix/", font=font_tag, fill=(100, 116, 139))
    draw.text((950, 570), "Sarav's Playground", font=font_tag, fill=(255, 94, 126))

    return img

def main():
    out_dir = "public/apps/birthday-gift-matrix"
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(create_svg())

    icon_32 = render_gift_icon(32)
    icon_32.save(os.path.join(out_dir, "favicon-32.png"))

    icon_192 = render_gift_icon(192)
    icon_192.save(os.path.join(out_dir, "favicon-192.png"))

    icon_180 = render_gift_icon(180)
    icon_180.save(os.path.join(out_dir, "apple-touch-icon-180.png"))

    gift_full = render_gift_icon(512)
    gift_full.save(os.path.join(out_dir, "gift-full.png"))

    og_img = create_og_image()
    og_img.save(os.path.join(out_dir, "og-image.png"))

    print(f"Birthday Gift Matrix assets created successfully in {out_dir}")

if __name__ == "__main__":
    main()
