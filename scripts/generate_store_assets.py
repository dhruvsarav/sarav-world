import os
from PIL import Image, ImageDraw, ImageFont

def render_store_icon(target_size):
    # 4x supersampling for crisp anti-aliased rendering
    render_scale = 4
    size = target_size * render_scale
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 128.0

    # Squircle background
    r = int(28 * scale)
    draw.rounded_rectangle(
        [0, 0, size - 1, size - 1],
        radius=r,
        fill=(18, 22, 30, 255),
        outline=(227, 166, 62, 180),
        width=max(1, int(2.5 * scale))
    )

    cx = size / 2.0
    cy = size / 2.0

    # Shopping bag body
    # Dimensions
    bag_w = int(60 * scale)
    bag_h = int(52 * scale)
    bag_x0 = int(cx - bag_w / 2.0)
    bag_x1 = int(cx + bag_w / 2.0)
    bag_y0 = int(cy - bag_h / 2.0 + 8 * scale)
    bag_y1 = int(cy + bag_h / 2.0 + 8 * scale)
    bag_r = int(8 * scale)

    # Bag body filled with warm gold/amber gradient tones
    draw.rounded_rectangle(
        [bag_x0, bag_y0, bag_x1, bag_y1],
        radius=bag_r,
        fill=(227, 150, 40, 255),
        outline=(255, 185, 80, 255),
        width=max(1, int(2 * scale))
    )

    # Bag fold/depth top flap
    flap_h = int(10 * scale)
    draw.rounded_rectangle(
        [bag_x0, bag_y0, bag_x1, bag_y0 + flap_h],
        radius=int(4 * scale),
        fill=(245, 175, 60, 255),
        outline=(255, 205, 110, 255),
        width=max(1, int(1.5 * scale))
    )

    # Handles (two arches)
    handle_w = int(26 * scale)
    handle_h = int(32 * scale)
    hx0 = int(cx - handle_w / 2.0)
    hx1 = int(cx + handle_w / 2.0)
    hy0 = int(bag_y0 - handle_h / 2.0 - 4 * scale)
    hy1 = int(bag_y0 + handle_h / 2.0)

    handle_thickness = max(2, int(4 * scale))
    draw.arc([hx0, hy0, hx1, hy1], start=180, end=360, fill=(255, 220, 150, 255), width=handle_thickness)

    # Sparkle / 4-point star badge in the center of the bag
    star_cx = int(cx)
    star_cy = int(bag_y0 + bag_h / 2.0 + 3 * scale)
    star_r = int(12 * scale)
    star_inner = int(3.5 * scale)

    # Draw 4-point star polygon
    star_points = [
        (star_cx, star_cy - star_r),
        (star_cx + star_inner, star_cy - star_inner),
        (star_cx + star_r, star_cy),
        (star_cx + star_inner, star_cy + star_inner),
        (star_cx, star_cy + star_r),
        (star_cx - star_inner, star_cy + star_inner),
        (star_cx - star_r, star_cy),
        (star_cx - star_inner, star_cy - star_inner),
    ]
    draw.polygon(star_points, fill=(255, 255, 255, 255))

    # Mini accent dots / sparkles
    draw.ellipse([star_cx - star_r - int(8 * scale), star_cy - int(8 * scale), star_cx - star_r - int(5 * scale), star_cy - int(5 * scale)], fill=(255, 255, 255, 220))
    draw.ellipse([star_cx + star_r + int(5 * scale), star_cy + int(6 * scale), star_cx + star_r + int(8 * scale), star_cy + int(9 * scale)], fill=(255, 255, 255, 220))

    # Resize down with Lanczos resampling
    return img.resize((target_size, target_size), Image.Resampling.LANCZOS)

def create_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#181D26"/>
      <stop offset="100%" stop-color="#0E1218"/>
    </linearGradient>
    <linearGradient id="bagGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="flapGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FBBF24"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
  </defs>

  <!-- Background Squircle -->
  <rect width="128" height="128" rx="28" fill="url(#bg)" stroke="#E3A63E" stroke-width="2.5" stroke-opacity="0.6"/>

  <!-- Handle Loop -->
  <path d="M 48 50 C 48 26, 80 26, 80 50" fill="none" stroke="#FDE68A" stroke-width="4.5" stroke-linecap="round"/>

  <!-- Shopping Bag Body -->
  <rect x="32" y="46" width="64" height="56" rx="9" fill="url(#bagGrad)" stroke="#FBBF24" stroke-width="2"/>

  <!-- Bag Flap Lip -->
  <rect x="32" y="46" width="64" height="12" rx="4" fill="url(#flapGrad)"/>

  <!-- 4-point Diamond Star Center -->
  <path d="M 64 61 Q 64 72 75 72 Q 64 72 64 83 Q 64 72 53 72 Q 64 72 64 61 Z" fill="#FFFFFF"/>

  <!-- Mini Sparkles -->
  <circle cx="48" cy="65" r="2" fill="#FFFFFF" opacity="0.9"/>
  <circle cx="80" cy="79" r="2.2" fill="#FFFFFF" opacity="0.9"/>
</svg>'''

def create_og_image():
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), (12, 15, 20))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_subtitle = ImageFont.truetype("arial.ttf", 22)
        font_badge = ImageFont.truetype("arialbd.ttf", 18)
        font_tag = ImageFont.truetype("arial.ttf", 17)
        font_mono = ImageFont.truetype("courbd.ttf", 19)
    except:
        font_title = font_subtitle = font_badge = font_tag = font_mono = ImageFont.load_default()

    # Top ambient line in amber
    draw.rectangle([0, 0, width, 12], fill=(227, 166, 62))

    # Badge: Curated Store
    draw.rounded_rectangle([40, 48, 480, 92], radius=8, fill=(35, 28, 14), outline=(227, 166, 62))
    draw.text((58, 60), "🛍️ CURATED FINDS • VIDHYA & SARAV", font=font_badge, fill=(254, 240, 138))

    # Title
    draw.text((40, 122), "Curated Store & Home Recommendations", font=font_title, fill=(255, 255, 255))
    draw.text((40, 192), "A handpicked collection of tested kitchen essentials, smart tech, children's books & bedding.", font=font_subtitle, fill=(148, 163, 184))

    # Feature Pills Grid
    features = [
        ("⚡ Tech & Desk Productivity Gear", 40, 260),
        ("🏠 Home, Kitchen & Comfort Bedding", 450, 260),
        ("🌿 Lifestyle & Everyday Wellness Finds", 40, 328),
        ("🍱 Primary School Lunchbox & Stationery", 450, 328),
        ("📚 Kids' Booksets & Story Adventures", 40, 396),
        ("🧩 Engaging STEM Puzzles & Family Games", 450, 396),
        ("🏷️ Amazon Verified Associates Tag: dhrav-21", 40, 464),
        ("🤖 Instant Telegram Curation Bot Workflow", 450, 464)
    ]
    for text, x, y in features:
        draw.rounded_rectangle([x, y, x + 380, y + 48], radius=10, fill=(20, 25, 34), outline=(42, 53, 69))
        draw.text((x + 16, y + 14), text, font=font_tag, fill=(226, 232, 240))

    # Decorative mini shopping bag icon preview on right side
    icon_preview = render_store_icon(220)
    img.paste(icon_preview, (910, 260), icon_preview)

    # Watermark Footer
    draw.text((40, 566), "iamsaravofficial.com/store/", font=font_tag, fill=(100, 116, 139))
    draw.text((910, 566), "Curated with ❤️ by Vidhya & Sarav", font=font_tag, fill=(227, 166, 62))

    return img

def main():
    out_dir = "public/store"
    os.makedirs(out_dir, exist_ok=True)

    # 1. Favicon SVG
    with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(create_svg())

    # 2. Favicon 32x32 PNG
    icon_32 = render_store_icon(32)
    icon_32.save(os.path.join(out_dir, "favicon-32.png"))

    # 3. Favicon 192x192 PNG
    icon_192 = render_store_icon(192)
    icon_192.save(os.path.join(out_dir, "favicon-192.png"))

    # 4. Apple Touch Icon 180x180 PNG
    icon_180 = render_store_icon(180)
    icon_180.save(os.path.join(out_dir, "apple-touch-icon-180.png"))

    # 5. Favicon ICO (16, 32, 48)
    icon_16 = render_store_icon(16)
    icon_48 = render_store_icon(48)
    icon_32.save(
        os.path.join(out_dir, "favicon.ico"),
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)]
    )

    # 6. Store Full Badge 512x512 PNG
    store_full = render_store_icon(512)
    store_full.save(os.path.join(out_dir, "store-full.png"))

    # 7. OG Social Image 1200x630
    og_img = create_og_image()
    og_img.save(os.path.join(out_dir, "og-image.png"))

    print(f"Store assets generated successfully in {out_dir}")

if __name__ == "__main__":
    main()
