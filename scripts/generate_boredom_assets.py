import os
import math
from PIL import Image, ImageDraw, ImageFont

def render_wheel_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 128.0

    # Squircle background
    r = int(28 * scale)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(20, 25, 34, 255), outline=(245, 158, 11, 100), width=max(1, int(2 * scale)))

    cx, cy = size / 2, size / 2
    outer_r = 44 * scale
    inner_r = 14 * scale

    # Draw 8 colored wedges
    colors = [
        (245, 158, 11, 230),  # Amber
        (56, 189, 248, 230),  # Sky blue
        (16, 185, 129, 230),  # Emerald
        (236, 72, 153, 230),  # Pink
        (139, 92, 246, 230),  # Purple
        (249, 115, 22, 230),  # Orange
        (6, 182, 212, 230),   # Cyan
        (234, 179, 8, 230)    # Yellow
    ]

    for i in range(8):
        start_angle = i * 45
        end_angle = (i + 1) * 45
        draw.pieslice([cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r],
                      start=start_angle, end=end_angle, fill=colors[i])

    # Outer border ring
    draw.ellipse([cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r],
                 outline=(255, 255, 255, 200), width=max(1, int(2.5 * scale)))

    # Center hub
    draw.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
                 fill=(15, 23, 42, 255), outline=(255, 255, 255, 255), width=max(1, int(2 * scale)))

    # Center dot
    center_dot = 5 * scale
    draw.ellipse([cx - center_dot, cy - center_dot, cx + center_dot, cy + center_dot],
                 fill=(245, 158, 11, 255))

    # Pointer arrow at top
    arrow_top = cy - outer_r - (6 * scale)
    arrow_bottom = cy - outer_r + (8 * scale)
    arrow_w = 6 * scale
    draw.polygon([(cx, arrow_top), (cx - arrow_w, arrow_bottom), (cx + arrow_w, arrow_bottom)],
                 fill=(255, 255, 255, 255), outline=(245, 158, 11, 255))

    return img

def create_og_image():
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), (12, 15, 20))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 48)
        font_subtitle = ImageFont.truetype("arial.ttf", 24)
        font_badge = ImageFont.truetype("arialbd.ttf", 18)
        font_tag = ImageFont.truetype("arial.ttf", 18)
    except:
        font_title = font_subtitle = font_badge = font_tag = ImageFont.load_default()

    # Top ambient line
    draw.rectangle([0, 0, width, 12], fill=(245, 158, 11))

    # Badge
    draw.rounded_rectangle([40, 50, 320, 92], radius=8, fill=(35, 28, 15), outline=(245, 158, 11))
    draw.text((60, 62), "🎲 120+ SCREEN-FREE IDEAS", font=font_badge, fill=(254, 243, 199))

    # Title
    draw.text((40, 128), "Kids' Screen-Free Adventure Wheel", font=font_title, fill=(255, 255, 255))
    draw.text((40, 198), "The Boredom Buster: Interactive Wheel, Zero-Mess Play & Fridge Jar Tokens", font=font_subtitle, fill=(148, 163, 184))

    # Feature Pills
    features = [
        ("🎡 Interactive Animated Adventure Spinner", 40, 270),
        ("🧽 Zero-Cleanup & Low-Mess Filter Modes", 450, 270),
        ("⏱️ Instant 0-Min Household Item Activities", 40, 340),
        ("⚡ High-Energy Physical Burners vs Quiet Focus", 450, 340),
        ("🖨️ Printable Boredom Buster Jar Token Slips", 40, 410),
        ("🎯 Screen-Free Weekend Bingo Challenge", 450, 410),
        ("🛍️ Amazon Craft & Science Kit Links (dhrav-21)", 40, 480),
        ("🔒 100% Client-Side • Zero Telemetry", 450, 480)
    ]
    for text, x, y in features:
        draw.rounded_rectangle([x, y, x + 380, y + 48], radius=10, fill=(22, 28, 38), outline=(42, 53, 69))
        draw.text((x + 18, y + 14), text, font=font_tag, fill=(226, 232, 240))

    # Watermark
    draw.text((40, 570), "iamsaravofficial.com/apps/boredom-buster/", font=font_tag, fill=(100, 116, 139))
    draw.text((950, 570), "Sarav's Playground", font=font_tag, fill=(245, 158, 11))

    # Paste Wheel icon on right
    icon = render_wheel_icon(280)
    img.paste(icon, (860, 170), icon)

    return img

def main():
    target_dir = "public/apps/boredom-buster"
    os.makedirs(target_dir, exist_ok=True)

    render_wheel_icon(32).save(f"{target_dir}/favicon-32.png")
    render_wheel_icon(192).save(f"{target_dir}/favicon-192.png")
    render_wheel_icon(180).save(f"{target_dir}/apple-touch-icon-180.png")
    render_wheel_icon(512).save(f"{target_dir}/wheel-full.png")
    create_og_image().save(f"{target_dir}/og-image.png")
    print("Boredom Buster PNG and OG assets successfully generated!")

if __name__ == "__main__":
    main()
