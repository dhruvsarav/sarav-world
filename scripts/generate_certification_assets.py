import os, sys
from PIL import Image, ImageDraw, ImageFont

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def generate_certification_assets():
    out_dir = os.path.join("D:\\Websites\\SaravsWorld", "public", "apps", "ai-certification-hub")
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
    <linearGradient id="purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC" />
      <stop offset="100%" stop-color="#7C3AED" />
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#bg)" stroke="#2A3545" stroke-width="3"/>
  <!-- Graduation Cap / Scholar AI Emblem -->
  <!-- Cap Rhombus -->
  <polygon points="50,22 84,36 50,50 16,36" fill="#1B222D" stroke="url(#gold)" stroke-width="3.5" stroke-linejoin="round"/>
  <!-- Skull Cap base -->
  <path d="M30 43 L30 64 C30 74 70 74 70 64 L70 43" fill="#141922" stroke="url(#teal)" stroke-width="3" stroke-linejoin="round"/>
  <!-- Tassel ribbon & medal drop -->
  <path d="M80 37 L80 58 L76 66" fill="none" stroke="url(#gold)" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="76" cy="67" r="3" fill="#F9D77E"/>
  <!-- Central AI Neural Spark / Diamond -->
  <polygon points="50,31 56,36 50,41 44,36" fill="url(#teal)"/>
  <circle cx="50" cy="36" r="1.5" fill="#FFFFFF"/>
</svg>'''

    svg_path = os.path.join(out_dir, "favicon.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("✅ Wrote", svg_path)

    # 2. Master App Icon (1024x1024)
    img = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    margin = 48
    draw.rounded_rectangle(
        [(margin, margin), (1024 - margin, 1024 - margin)],
        radius=220,
        fill=(20, 25, 34, 255),
        outline=(42, 53, 69, 255),
        width=16
    )

    draw.rounded_rectangle(
        [(margin + 16, margin + 16), (1024 - margin - 16, 1024 - margin - 16)],
        radius=204,
        fill=None,
        outline=(227, 166, 62, 60),
        width=4
    )

    # Draw Scholar Cap
    cap_points = [(512, 230), (870, 375), (512, 520), (154, 375)]
    draw.polygon(cap_points, fill=(27, 34, 45, 255), outline=(227, 166, 62, 255))
    draw.line(cap_points + [cap_points[0]], fill=(249, 215, 126, 255), width=18)

    # Skullcap body
    draw.chord([(290, 440), (734, 760)], start=0, end=180, fill=(20, 25, 34, 255), outline=(79, 176, 168, 255), width=14)

    # Center Neural Spark
    spark = [(512, 320), (570, 375), (512, 430), (454, 375)]
    draw.polygon(spark, fill=(94, 234, 212, 255), outline=(227, 166, 62, 255))
    draw.ellipse([(494, 357), (530, 393)], fill=(255, 255, 255, 255))

    # Tassel
    draw.line([(830, 385), (830, 610), (790, 690)], fill=(227, 166, 62, 255), width=14)
    draw.ellipse([(765, 680), (815, 730)], fill=(249, 215, 126, 255))

    # Save 512x512
    full_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    full_512.save(os.path.join(out_dir, "ai-certification-hub-full.png"))
    print("✅ Wrote ai-certification-hub-full.png")

    # Apple touch icon 180x180
    icon_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
    icon_180.save(os.path.join(out_dir, "apple-touch-icon.png"))
    print("✅ Wrote apple-touch-icon.png")

    # Favicon 32x32
    icon_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    icon_32.save(os.path.join(out_dir, "favicon-32x32.png"))

    # Favicon 16x16
    icon_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    icon_16.save(os.path.join(out_dir, "favicon-16x16.png"))
    print("✅ Wrote favicons")

    # 3. OpenGraph Card (1200x630)
    og = Image.new("RGB", (1200, 630), (12, 15, 20))
    og_draw = ImageDraw.Draw(og)

    # Gradient border
    og_draw.rectangle([(24, 24), (1176, 606)], outline=(42, 53, 69), width=2)
    og_draw.rectangle([(32, 32), (1168, 598)], outline=(227, 166, 62, 60), width=1)

    # Accent decorative top strip
    og_draw.rectangle([(24, 24), (1176, 32)], fill=(227, 166, 62))

    # Paste emblem thumbnail
    thumb = img.resize((260, 260), Image.Resampling.LANCZOS)
    og.paste(thumb, (70, 180), thumb)

    # Text elements
    try:
        font_eyebrow = ImageFont.truetype("arial.ttf", 22)
        font_title = ImageFont.truetype("arialbd.ttf", 52)
        font_sub = ImageFont.truetype("arial.ttf", 26)
        font_meta = ImageFont.truetype("arialbd.ttf", 20)
    except Exception:
        font_eyebrow = font_title = font_sub = font_meta = ImageFont.load_default()

    og_draw.text((380, 170), "SARAV'S WORLD · AI LEARNING & ARCHITECTURE", fill=(227, 166, 62), font=font_eyebrow)
    og_draw.text((380, 210), "AI Certification Hub", fill=(255, 255, 255), font=font_title)
    og_draw.text((380, 280), "Master Hyperscaler & Frontier AI Credentials", fill=(94, 234, 212), font=font_sub)
    og_draw.text((380, 325), "Anthropic Claude · Microsoft Azure · Google Cloud · AWS · NVIDIA", fill=(148, 160, 178), font=font_sub)

    # Pill tags
    pills = [
        "26 Verified Certifications",
        "Official Learn Portals",
        "Coursera & Udemy Prep",
        "Practice Exams Bank",
        "Pearson VUE & Webassessor",
        "100% Free & Zero Telemetry"
    ]
    x_pos = 380
    y_pos = 410
    for p in pills:
        bbox = og_draw.textbbox((x_pos, y_pos), p, font=font_meta)
        w = bbox[2] - bbox[0] + 24
        if x_pos + w > 1140:
            x_pos = 380
            y_pos += 44
        og_draw.rounded_rectangle([(x_pos, y_pos), (x_pos + w, y_pos + 34)], radius=8, fill=(27, 34, 45), outline=(42, 53, 69))
        og_draw.text((x_pos + 12, y_pos + 6), p, fill=(234, 239, 245), font=font_meta)
        x_pos += w + 12

    # Bottom watermark
    og_draw.text((70, 560), "iamsaravofficial.com/apps/ai-certification-hub/", fill=(92, 107, 128), font=font_meta)
    og_draw.text((950, 560), "Curated by Sarav", fill=(227, 166, 62), font=font_meta)

    og.save(os.path.join(out_dir, "og-image.png"))
    print("✅ Wrote og-image.png")

if __name__ == "__main__":
    generate_certification_assets()
