import json

with open('scripts/birthday_matrix_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

gifts = data['gift_ideas']

extra_gifts = [
    {
        "id": "gft_speedcube",
        "title": "MoYu Magnetic 3x3 Speed Cube",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹549",
        "category": "Puzzles & Brain",
        "age": "Ages 7+",
        "desc": "Smooth, corner-cutting stickerless magnetic 3x3 speedcube for developing spatial problem-solving, finger dexterity, and algorithmic memory.",
        "amazon": "moyu magnetic 3x3 speed cube"
    },
    {
        "id": "gft_scratch_art",
        "title": "Rainbow Scratch Art Scratchboard Notes (50 Sheets)",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹599",
        "category": "Creative Arts",
        "age": "Ages 4+",
        "desc": "Wooden stylus pens scrape off matte black coating to reveal dazzling rainbow patterns underneath. Zero-mess creative fun.",
        "amazon": "rainbow scratch art paper for kids"
    },
    {
        "id": "gft_tangram",
        "title": "Wooden Geometric Tangram Puzzle with Challenge Cards",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹649",
        "category": "Puzzles & Brain",
        "age": "Ages 4–9",
        "desc": "7 colorful wooden geometric polygons with 60 double-sided pattern cards to form animals, boats, and human figures.",
        "amazon": "wooden tangram puzzle challenge cards"
    },
    {
        "id": "gft_glow_stars",
        "title": "3D Glow-in-the-Dark Solar System Planets & Stars",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹699",
        "category": "STEM & Discovery",
        "age": "Ages 4+",
        "desc": "Luminous glow-in-the-dark wall stickers featuring the 8 planets, moon, and 200 twinkling stars for ceiling bedtime wonder.",
        "amazon": "glow in the dark planets and stars for ceiling"
    },
    {
        "id": "gft_lego_classic",
        "title": "LEGO Classic Medium Creative Brick Box (484 Pieces)",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹2,399",
        "category": "Building & Construction",
        "age": "Ages 4+",
        "desc": "35 different colored bricks, windows, eyes, wheels, and green baseplate housed in a sturdy yellow plastic storage box.",
        "amazon": "lego classic medium creative brick box"
    },
    {
        "id": "gft_crystal_growing",
        "title": "National Geographic Mega Crystal Growing Lab",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,899",
        "category": "STEM & Discovery",
        "age": "Ages 8+",
        "desc": "Grow 8 vibrant crystals in 3-4 days with a light-up night display base that illuminates your homegrown geology specimens.",
        "amazon": "national geographic crystal growing lab"
    },
    {
        "id": "gft_karaoke_mic",
        "title": "Wireless Bluetooth Karaoke Microphone with LED Lights",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,299",
        "category": "Music & Performance",
        "age": "Ages 5+",
        "desc": "Built-in stereo speaker, voice-changer effects (chipmunk, robot, monster), and dancing LED lights for birthday party sing-alongs.",
        "amazon": "wireless bluetooth karaoke microphone for kids"
    },
    {
        "id": "gft_rc_stunt_car",
        "title": "360° Rotating 4WD Remote Control Stunt Car",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,499",
        "category": "Remote Control & Action",
        "age": "Ages 6+",
        "desc": "Double-sided flipping and tumbling RC car with headlights that drives on carpet, tile, grass, and ramps without flipping over.",
        "amazon": "remote control stunt car 360 rotating"
    },
    {
        "id": "gft_easel_set",
        "title": "Wooden Tabletop Art Easel & Acrylic Painting Studio",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,799",
        "category": "Creative Arts",
        "age": "Ages 7+",
        "desc": "Adjustable beechwood desk easel, stretched canvases, 24 acrylic paint tubes, palette knife, and 10 artist brushes.",
        "amazon": "tabletop art easel acrylic painting kit"
    },
    {
        "id": "gft_marble_run_wooden",
        "title": "ROKR 3D Mechanical Wooden Marble Run Park Kit",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹2,999",
        "category": "STEM & Engineering",
        "age": "Ages 10+",
        "desc": "Laser-cut plywood gear mechanics with hand crank, spiral elevator, and multi-track marble ramps. Assembles without glue!",
        "amazon": "rokr 3d wooden puzzle marble run"
    },
    {
        "id": "gft_guitar",
        "title": "Yamaha / Juarez 38-Inch Acoustic Guitar Starter Pack",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹2,799",
        "category": "Music & Instruments",
        "age": "Ages 9+",
        "desc": "Cutaway acoustic guitar with carrying gig bag, spare strings, strap, and picks. Ideal first guitar for children and teens.",
        "amazon": "juarez acoustic guitar 38 inch"
    },
    {
        "id": "gft_smart_band",
        "title": "Smart Fitness Band with AMOLED Screen & Heart Rate",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹2,999",
        "category": "Sports & Active",
        "age": "Ages 10+",
        "desc": "Tracks daily steps, cycling, badminton, swimming, and sleep with vibrant AMOLED display and 14-day battery life.",
        "amazon": "smart fitness band amoled display"
    },
    {
        "id": "gft_binoculars",
        "title": "Celestron Outland 8x42 Waterproof Binoculars",
        "tier": "Tier 4: ₹5,000+",
        "priceRange": "₹6,499",
        "category": "Outdoors & Nature",
        "age": "Ages 9+",
        "desc": "Multi-coated optics with BaK-4 prisms for bird-watching, wildlife safaris, stargazing, and sports stadium events.",
        "amazon": "celestron outland x 8x42 binoculars"
    },
    {
        "id": "gft_action_camera",
        "title": "4K Ultra-HD Waterproof Sports Action Camera",
        "tier": "Tier 4: ₹5,000+",
        "priceRange": "₹5,499",
        "category": "Electronics & Photography",
        "age": "Ages 9+",
        "desc": "Mounts to bicycle handlebars, helmets, or skateboards. Waterproof up to 30 meters with dual screens and accessories kit.",
        "amazon": "4k waterproof action camera for kids"
    }
]

gifts.extend(extra_gifts)
data['gift_ideas'] = gifts

with open('scripts/birthday_matrix_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Total Gift Ideas now: {len(gifts)}")
