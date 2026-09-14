import os
from PIL import Image, ImageDraw, ImageFont

def render_book_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 128.0

    # Squircle background
    r = int(28 * scale)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(18, 22, 30, 255), outline=(79, 176, 168, 120), width=max(1, int(2 * scale)))

    cx, cy = size / 2, size / 2

    # Draw open book with golden pages and ribbon bookmark
    # Left page
    lw = int(36 * scale)
    lh = int(50 * scale)
    x0_left = int(cx - lw - 2 * scale)
    y0 = int(cy - lh / 2)

    # Left page polygon
    draw.polygon([
        (cx - int(2 * scale), y0 + int(6 * scale)),
        (x0_left, y0),
        (x0_left, y0 + lh),
        (cx - int(2 * scale), y0 + lh + int(6 * scale))
    ], fill=(235, 240, 245, 255), outline=(200, 210, 220, 255))

    # Right page polygon
    x0_right = int(cx + 2 * scale)
    draw.polygon([
        (x0_right, y0 + int(6 * scale)),
        (x0_right + lw, y0),
        (x0_right + lw, y0 + lh),
        (x0_right, y0 + lh + int(6 * scale))
    ], fill=(255, 255, 255, 255), outline=(200, 210, 220, 255))

    # Spine binding behind
    draw.line([(cx, y0 + int(5 * scale)), (cx, y0 + lh + int(8 * scale))], fill=(46, 196, 182, 255), width=max(1, int(4 * scale)))

    # Red silk ribbon bookmark hanging from top
    ribbon_w = max(1, int(4 * scale))
    draw.line([(cx + int(6 * scale), y0 + int(4 * scale)), (cx + int(6 * scale), y0 + lh + int(14 * scale))], fill=(229, 9, 20, 255), width=ribbon_w)

    # Mini text lines on left page
    for i in range(4):
        ly = y0 + int((14 + i * 8) * scale)
        draw.line([(x0_left + int(6 * scale), ly), (cx - int(8 * scale), ly + int(2 * scale))], fill=(180, 190, 205, 200), width=max(1, int(1.5 * scale)))

    # Mini star on right page
    star_x = cx + int(18 * scale)
    star_y = y0 + int(24 * scale)
    star_r = int(7 * scale)
    draw.ellipse([star_x - star_r, star_y - star_r, star_x + star_r, star_y + star_r], fill=(245, 158, 11, 240))

    return img

def create_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141922"/>
      <stop offset="100%" stop-color="#0C0F14"/>
    </linearGradient>
    <linearGradient id="teal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2EC4B6"/>
      <stop offset="100%" stop-color="#0D9488"/>
    </linearGradient>
  </defs>
  <rect width="128" height="128" rx="28" fill="url(#bg)" stroke="#2EC4B6" stroke-width="2.5" stroke-opacity="0.4"/>
  <!-- Open Book Left Page -->
  <polygon points="62,40 24,34 24,90 62,96" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="2"/>
  <!-- Open Book Right Page -->
  <polygon points="66,40 104,34 104,90 66,96" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <!-- Spine -->
  <line x1="64" y1="38" x2="64" y2="98" stroke="url(#teal)" stroke-width="4" stroke-linecap="round"/>
  <!-- Bookmark Ribbon -->
  <polyline points="72,36 72,106 75,102 78,106 78,36" fill="#E11D48"/>
  <!-- Gold Star -->
  <circle cx="85" cy="62" r="8" fill="#F59E0B"/>
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
    draw.rectangle([0, 0, width, 12], fill=(46, 196, 182))

    # Badge
    draw.rounded_rectangle([40, 50, 380, 92], radius=8, fill=(15, 35, 32), outline=(46, 196, 182))
    draw.text((60, 62), "📚 100-BOOK QUEST & BOX SETS", font=font_badge, fill=(204, 251, 241))

    # Title
    draw.text((40, 126), "Kids' Book Nook & 100-Book Quest", font=font_title, fill=(255, 255, 255))
    draw.text((40, 196), "Visual Bookshelf Wall, Curated Books & Box Set Recommendations with Amazon Buying", font=font_subtitle, fill=(148, 163, 184))

    # Feature Pills
    features = [
        ("🪵 Interactive 100-Book Wooden Bookshelf Wall", 40, 268),
        ("📦 Curated Children's Box Sets & Series Recommendations", 450, 268),
        ("🎯 4x4 Screen-Free Reading Genre Bingo", 40, 338),
        ("🛡️ Bronze to Diamond Reading Milestone Ranks", 450, 338),
        ("🖨️ Printable A4 Blank Fridge Coloring Bookshelf", 40, 408),
        ("⭐ Book Review Logger, Quotes & Star Ratings", 450, 408),
        ("🛍️ Amazon Book & Box Set Buying Links (dhrav-21)", 40, 478),
        ("🔒 100% Client-Side Privacy • Zero Telemetry", 450, 478)
    ]
    for text, x, y in features:
        draw.rounded_rectangle([x, y, x + 380, y + 48], radius=10, fill=(20, 25, 34), outline=(42, 53, 69))
        draw.text((x + 16, y + 14), text, font=font_tag, fill=(226, 232, 240))

    # Watermark
    draw.text((40, 570), "iamsaravofficial.com/apps/book-nook/", font=font_tag, fill=(100, 116, 139))
    draw.text((950, 570), "Sarav's Playground", font=font_tag, fill=(46, 196, 182))

    return img

def main():
    out_dir = "public/apps/book-nook"
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(create_svg())

    icon_32 = render_book_icon(32)
    icon_32.save(os.path.join(out_dir, "favicon-32.png"))

    icon_192 = render_book_icon(192)
    icon_192.save(os.path.join(out_dir, "favicon-192.png"))

    icon_180 = render_book_icon(180)
    icon_180.save(os.path.join(out_dir, "apple-touch-icon-180.png"))

    book_full = render_book_icon(512)
    book_full.save(os.path.join(out_dir, "book-full.png"))

    og_img = create_og_image()
    og_img.save(os.path.join(out_dir, "og-image.png"))

    print(f"Book Nook assets created successfully in {out_dir}")

if __name__ == "__main__":
    main()
