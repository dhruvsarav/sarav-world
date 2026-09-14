import os
from PIL import Image, ImageDraw, ImageFont

def render_movie_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 128.0

    # Squircle background
    r = int(28 * scale)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(18, 22, 30, 255), outline=(227, 166, 62, 120), width=max(1, int(2 * scale)))

    cx, cy = size / 2, size / 2

    # Draw film clapperboard / popcorn bucket
    # Clapperboard body
    cw, ch = int(72 * scale), int(52 * scale)
    x0, y0 = int(cx - cw / 2), int(cy - ch / 2 + 10 * scale)
    draw.rounded_rectangle([x0, y0, x0 + cw, y0 + ch], radius=int(8 * scale), fill=(28, 35, 48, 255), outline=(255, 255, 255, 200), width=max(1, int(2 * scale)))

    # Clapper top angled stick
    stick_h = int(18 * scale)
    stick_y0 = y0 - stick_h - int(4 * scale)
    draw.rounded_rectangle([x0, stick_y0, x0 + cw, stick_y0 + stick_h], radius=int(4 * scale), fill=(227, 166, 62, 255))

    # Clapper diagonal stripes
    for sx in range(int(x0 + 8 * scale), int(x0 + cw - 8 * scale), int(16 * scale)):
        draw.polygon([(sx, stick_y0), (sx + int(8 * scale), stick_y0), (sx + int(2 * scale), stick_y0 + stick_h), (sx - int(6 * scale), stick_y0 + stick_h)], fill=(18, 22, 30, 255))

    # Star in center of clapperboard
    star_r = int(14 * scale)
    star_cy = int(y0 + ch / 2)
    draw.ellipse([cx - star_r, star_cy - star_r, cx + star_r, star_cy + star_r], fill=(227, 166, 62, 240))

    # Play triangle inside star
    tri_s = int(6 * scale)
    draw.polygon([(cx - int(2 * scale), star_cy - tri_s), (cx - int(2 * scale), star_cy + tri_s), (cx + int(6 * scale), star_cy)], fill=(18, 22, 30, 255))

    return img

def create_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141922"/>
      <stop offset="100%" stop-color="#0C0F14"/>
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
  </defs>
  <rect width="128" height="128" rx="28" fill="url(#bg)" stroke="#F59E0B" stroke-width="2.5" stroke-opacity="0.4"/>
  <rect x="26" y="52" width="76" height="50" rx="8" fill="#1E2633" stroke="#FFF" stroke-width="2" stroke-opacity="0.8"/>
  <rect x="26" y="30" width="76" height="16" rx="4" fill="url(#gold)"/>
  <!-- Clapper stripes -->
  <polygon points="36,30 44,30 38,46 30,46" fill="#141922"/>
  <polygon points="56,30 64,30 58,46 50,46" fill="#141922"/>
  <polygon points="76,30 84,30 78,46 70,46" fill="#141922"/>
  <polygon points="96,30 102,30 98,46 90,46" fill="#141922"/>
  <circle cx="64" cy="77" r="15" fill="url(#gold)"/>
  <polygon points="61,70 61,84 71,77" fill="#141922"/>
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
    draw.rectangle([0, 0, width, 12], fill=(227, 166, 62))

    # Badge
    draw.rounded_rectangle([40, 50, 360, 92], radius=8, fill=(35, 28, 15), outline=(227, 166, 62))
    draw.text((60, 62), "🎬 ZERO-ARGUMENT ROTATOR", font=font_badge, fill=(254, 243, 199))

    # Title
    draw.text((40, 126), "Family Movie & Board Game Night Decider", font=font_title, fill=(255, 255, 255))
    draw.text((40, 196), "Friday Harmony Turnkey Rotator, 100+ Family Cinema Gems & Printable Tickets", font=font_subtitle, fill=(148, 163, 184))

    # Feature Pills
    features = [
        ("🎡 Fair-Turn Family Rotator (Dad, Mom & Kids)", 40, 268),
        ("🍿 100+ Filterable Cinema Titles Across 6 Genres", 450, 268),
        ("🎲 Top 40 Family Board Games with Amazon Links", 40, 338),
        ("🛡️ 'One Veto Per Month' Harmony Rule Engine", 450, 338),
        ("🎟️ Printable Souvenir A4 Cinema Ticket Stubs", 40, 408),
        ("🥤 Gourmet Snack & Desi Popcorn Pairing Studio", 450, 408),
        ("🛍️ Amazon Board Game & Gear Buying Links (dhrav-21)", 40, 478),
        ("🔒 100% Client-Side Privacy • Zero Telemetry", 450, 478)
    ]
    for text, x, y in features:
        draw.rounded_rectangle([x, y, x + 380, y + 48], radius=10, fill=(20, 25, 34), outline=(42, 53, 69))
        draw.text((x + 16, y + 14), text, font=font_tag, fill=(226, 232, 240))

    # Watermark
    draw.text((40, 570), "iamsaravofficial.com/apps/family-movie-night/", font=font_tag, fill=(100, 116, 139))
    draw.text((950, 570), "Sarav's Playground", font=font_tag, fill=(227, 166, 62))

    return img

def main():
    out_dir = "public/apps/family-movie-night"
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(create_svg())

    icon_32 = render_movie_icon(32)
    icon_32.save(os.path.join(out_dir, "favicon-32.png"))

    icon_192 = render_movie_icon(192)
    icon_192.save(os.path.join(out_dir, "favicon-192.png"))

    icon_180 = render_movie_icon(180)
    icon_180.save(os.path.join(out_dir, "apple-touch-icon-180.png"))

    movie_full = render_movie_icon(512)
    movie_full.save(os.path.join(out_dir, "movie-full.png"))

    og_img = create_og_image()
    og_img.save(os.path.join(out_dir, "og-image.png"))

    print(f"Movie Night assets created successfully in {out_dir}")

if __name__ == "__main__":
    main()
