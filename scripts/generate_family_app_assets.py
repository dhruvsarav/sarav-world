import os
from PIL import Image, ImageDraw, ImageFont

def create_chore_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312E81"/>
      <stop offset="50%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="bladeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0E7FF"/>
      <stop offset="100%" stop-color="#818CF8"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Background squircle -->
  <rect width="128" height="128" rx="28" fill="url(#bgGrad)"/>
  <rect x="2" y="2" width="124" height="124" rx="26" fill="none" stroke="#6366F1" stroke-width="2" stroke-opacity="0.4"/>
  
  <!-- Crossed Swords -->
  <path d="M36 28 L92 84 M92 28 L36 84" stroke="url(#bladeGrad)" stroke-width="6" stroke-linecap="round"/>
  <!-- Sword Guards -->
  <path d="M44 24 L28 40 M84 24 L100 40" stroke="#CBD5E1" stroke-width="4" stroke-linecap="round"/>
  
  <!-- Central Shield -->
  <path d="M64 42 C78 42, 88 48, 88 62 C88 82, 74 96, 64 102 C54 96, 40 82, 40 62 C40 48, 50 42, 64 42 Z" 
        fill="url(#shieldGrad)" filter="url(#glow)"/>
  <path d="M64 46 C75 46, 84 51, 84 62 C84 78, 72 90, 64 96 C56 90, 44 78, 44 62 C44 51, 53 46, 64 46 Z" 
        fill="#1E1B4B" opacity="0.4"/>
  
  <!-- Star in Shield -->
  <polygon points="64,54 67,63 76,63 69,69 72,78 64,72 56,78 59,69 52,63 61,63" fill="#FDE047"/>
  
  <!-- Sparkles -->
  <circle cx="28" cy="64" r="3" fill="#67E8F9"/>
  <circle cx="100" cy="64" r="3" fill="#67E8F9"/>
  <circle cx="64" cy="24" r="4" fill="#FDE047"/>
</svg>'''
    return svg

def create_ticket_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="ticketGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBBF24"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Background squircle -->
  <rect width="128" height="128" rx="28" fill="url(#bgGrad)"/>
  <rect x="2" y="2" width="124" height="124" rx="26" fill="none" stroke="#F59E0B" stroke-width="2" stroke-opacity="0.3"/>
  
  <!-- Ticket Body with Cutouts -->
  <g transform="rotate(-10 64 64)">
    <!-- Main Ticket -->
    <path d="M 24 38 
             L 104 38 
             A 6 6 0 0 0 104 50 
             L 104 78 
             A 6 6 0 0 0 104 90 
             L 24 90 
             A 6 6 0 0 0 24 78 
             L 24 50 
             A 6 6 0 0 0 24 38 Z" 
          fill="url(#ticketGrad)" filter="url(#glow)"/>
    
    <!-- Perforated Line -->
    <line x1="48" y1="38" x2="48" y2="90" stroke="#78350F" stroke-width="2" stroke-dasharray="3,3"/>
    
    <!-- Clock / Star Icon -->
    <circle cx="36" cy="64" r="8" fill="#78350F" opacity="0.3"/>
    <polygon points="36,58 38,62 42,62 39,65 40,69 36,66 32,69 33,65 30,62 34,62" fill="#FFFBEB"/>
    
    <!-- PASS text -->
    <rect x="56" y="48" width="38" height="12" rx="3" fill="#78350F" opacity="0.8"/>
    <text x="75" y="58" font-family="system-ui, sans-serif" font-weight="900" font-size="9" fill="#FEF3C7" text-anchor="middle" letter-spacing="1">PASS</text>
    
    <!-- Star ratings / dots -->
    <circle cx="62" cy="74" r="2.5" fill="#78350F"/>
    <circle cx="75" cy="74" r="2.5" fill="#78350F"/>
    <circle cx="88" cy="74" r="2.5" fill="#78350F"/>
  </g>
</svg>'''
    return svg

def render_png(app_type, size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 128.0
    
    if app_type == 'chore':
        # Background
        r = int(28 * scale)
        draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(30, 27, 75, 255), outline=(99, 102, 241, 120), width=max(1, int(2*scale)))
        
        # Crossed sword paths (simplified geometric)
        w = max(2, int(6 * scale))
        draw.line([(int(36*scale), int(28*scale)), (int(92*scale), int(84*scale))], fill=(199, 210, 254, 255), width=w)
        draw.line([(int(92*scale), int(28*scale)), (int(36*scale), int(84*scale))], fill=(199, 210, 254, 255), width=w)
        
        # Shield
        shield_pts = [
            (int(64*scale), int(42*scale)),
            (int(86*scale), int(48*scale)),
            (int(84*scale), int(68*scale)),
            (int(64*scale), int(100*scale)),
            (int(44*scale), int(68*scale)),
            (int(42*scale), int(48*scale))
        ]
        draw.polygon(shield_pts, fill=(245, 158, 11, 255), outline=(252, 211, 77, 255))
        
        # Star in shield
        cx, cy, s_r = int(64*scale), int(66*scale), int(14*scale)
        draw.ellipse([cx - s_r, cy - s_r, cx + s_r, cy + s_r], fill=(254, 240, 138, 255))
        
    elif app_type == 'ticket':
        # Background
        r = int(28 * scale)
        draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(15, 23, 42, 255), outline=(245, 158, 11, 100), width=max(1, int(2*scale)))
        
        # Ticket rectangle
        t_box = [int(22*scale), int(42*scale), int(106*scale), int(86*scale)]
        draw.rounded_rectangle(t_box, radius=int(6*scale), fill=(245, 158, 11, 255), outline=(251, 191, 36, 255), width=max(1, int(2*scale)))
        
        # Ticket stub line
        draw.line([(int(48*scale), int(42*scale)), (int(48*scale), int(86*scale))], fill=(120, 53, 15, 255), width=max(1, int(2*scale)))
        
        # Perforation notches (cutouts)
        cut_r = int(6*scale)
        draw.ellipse([int(48*scale)-cut_r, int(42*scale)-cut_r, int(48*scale)+cut_r, int(42*scale)+cut_r], fill=(15, 23, 42, 255))
        draw.ellipse([int(48*scale)-cut_r, int(86*scale)-cut_r, int(48*scale)+cut_r, int(86*scale)+cut_r], fill=(15, 23, 42, 255))
        
        # Star on stub
        draw.ellipse([int(35*scale - 6*scale), int(64*scale - 6*scale), int(35*scale + 6*scale), int(64*scale + 6*scale)], fill=(254, 243, 199, 255))
        
        # Pass block
        draw.rounded_rectangle([int(58*scale), int(52*scale), int(96*scale), int(76*scale)], radius=int(3*scale), fill=(120, 53, 15, 220))
        
    return img

def create_og_image(app_type):
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    
    # Try to load Arial or default font
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 52)
        font_subtitle = ImageFont.truetype("arial.ttf", 26)
        font_badge = ImageFont.truetype("arialbd.ttf", 20)
        font_tag = ImageFont.truetype("arial.ttf", 18)
    except:
        font_title = font_subtitle = font_badge = font_tag = ImageFont.load_default()
        
    if app_type == 'chore':
        # Ambient gradient / colored bars
        draw.rectangle([0, 0, width, 12], fill=(99, 102, 241))
        draw.rectangle([40, 50, 240, 90], fill=(49, 46, 129), outline=(99, 102, 241))
        draw.text((60, 60), "⚔️ RPG ADVENTURE", font=font_badge, fill=(224, 231, 255))
        
        # Title
        draw.text((40, 130), "Kids' Chore & Quest Board", font=font_title, fill=(255, 255, 255))
        draw.text((40, 205), "Gamified Daily Chores, Habit XP, Shields & Hero Levels", font=font_subtitle, fill=(203, 213, 225))
        
        # Feature Pills
        features = [
            ("🛡️ 5-Tier Hero Progression", 40, 280),
            ("✨ XP Points & Difficulty Shields", 360, 280),
            ("🖨️ Printable A4 Fridge Quest Poster", 40, 350),
            ("🔥 Streak Bonuses & Multipliers", 420, 350),
            ("🔊 Web Audio Fanfares & Sound Effects", 40, 420),
            ("🔒 100% Client-Side • Zero Telemetry", 440, 420)
        ]
        for text, x, y in features:
            draw.rounded_rectangle([x, y, x + 340, y + 48], radius=10, fill=(30, 27, 75), outline=(99, 102, 241))
            draw.text((x + 18, y + 14), text, font=font_tag, fill=(224, 231, 255))
            
        # Watermark
        draw.text((40, 550), "iamsaravofficial.com/apps/chore-quest-board/", font=font_tag, fill=(148, 163, 184))
        draw.text((950, 550), "Sarav's Playground", font=font_tag, fill=(245, 158, 11))
        
        # Embedded large icon
        icon = render_png('chore', 280)
        img.paste(icon, (850, 150), icon)
        
    elif app_type == 'ticket':
        # Ambient gradient / colored bars
        draw.rectangle([0, 0, width, 12], fill=(245, 158, 11))
        draw.rectangle([40, 50, 260, 90], fill=(120, 53, 15), outline=(245, 158, 11))
        draw.text((60, 60), "🎟️ FAMILY CURRENCY", font=font_badge, fill=(254, 243, 199))
        
        # Title
        draw.text((40, 130), "Screen-Time Swap Tickets", font=font_title, fill=(255, 255, 255))
        draw.text((40, 205), "Printable Family Reward Passes & Delayed Gratification Currency", font=font_subtitle, fill=(203, 213, 225))
        
        # Feature Pills
        features = [
            ("🎟️ Perforated Cut-Out Ticket Sheet", 40, 280),
            ("📱 Golden 15/30/45 Min Screen Passes", 390, 280),
            ("👑 Privilege & Treat Rule-Breaker Passes", 40, 350),
            ("⏱️ Delayed Gratification Swap Matrix", 440, 350),
            ("✍️ Parent Signature & Stamp Pacts", 40, 420),
            ("🔒 100% Client-Side • Zero Telemetry", 400, 420)
        ]
        for text, x, y in features:
            draw.rounded_rectangle([x, y, x + 340, y + 48], radius=10, fill=(45, 30, 15), outline=(217, 119, 6))
            draw.text((x + 18, y + 14), text, font=font_tag, fill=(254, 243, 199))
            
        # Watermark
        draw.text((40, 550), "iamsaravofficial.com/apps/screen-time-passes/", font=font_tag, fill=(148, 163, 184))
        draw.text((950, 550), "Sarav's Playground", font=font_tag, fill=(245, 158, 11))
        
        # Embedded large icon
        icon = render_png('ticket', 280)
        img.paste(icon, (850, 150), icon)
        
    return img

def main():
    # 1. chore-quest-board
    chore_dir = "public/apps/chore-quest-board"
    with open(f"{chore_dir}/favicon.svg", "w", encoding="utf-8") as f:
        f.write(create_chore_svg())
    render_png('chore', 32).save(f"{chore_dir}/favicon-32.png")
    render_png('chore', 192).save(f"{chore_dir}/favicon-192.png")
    render_png('chore', 180).save(f"{chore_dir}/apple-touch-icon-180.png")
    render_png('chore', 512).save(f"{chore_dir}/quest-full.png")
    create_og_image('chore').save(f"{chore_dir}/og-image.png")
    print("Chore Quest Board assets generated.")
    
    # 2. screen-time-passes
    ticket_dir = "public/apps/screen-time-passes"
    with open(f"{ticket_dir}/favicon.svg", "w", encoding="utf-8") as f:
        f.write(create_ticket_svg())
    render_png('ticket', 32).save(f"{ticket_dir}/favicon-32.png")
    render_png('ticket', 192).save(f"{ticket_dir}/favicon-192.png")
    render_png('ticket', 180).save(f"{ticket_dir}/apple-touch-icon-180.png")
    render_png('ticket', 512).save(f"{ticket_dir}/ticket-full.png")
    create_og_image('ticket').save(f"{ticket_dir}/og-image.png")
    print("Screen Time Passes assets generated.")

if __name__ == "__main__":
    main()
