import json

GIFT_IDEAS = [
    # -------------------------------------------------------------------------
    # Tier 1: ₹500 – ₹1,000 (Thoughtful Essentials & Spark Gifts)
    # -------------------------------------------------------------------------
    {
        "id": "gft_origami_kit",
        "title": "Japanese Origami Paper Art & 3D Animals Kit",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹599",
        "category": "Creative Arts",
        "age": "Ages 6+",
        "desc": "100 sheets of dual-color folding paper with step-by-step instruction booklet for folding cranes, frogs, and dragons.",
        "amazon": "origami paper kit for kids"
    },
    {
        "id": "gft_science_kaleidoscope",
        "title": "DIY Optical Kaleidoscope Science Toy",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹649",
        "category": "STEM & Discovery",
        "age": "Ages 5+",
        "desc": "Assemble rotating mirrors and colored beads to discover reflection optics, geometric symmetry, and mesmerizing patterns.",
        "amazon": "diy kaleidoscope kit kids"
    },
    {
        "id": "gft_monopoly_deal",
        "title": "Monopoly Deal & Uno Flip Card Game Bundle",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹699",
        "category": "Tabletop Games",
        "age": "Ages 7+",
        "desc": "Two world-favorite fast card games in a travel pouch. 15-minute high-energy sessions perfect for family trips and train rides.",
        "amazon": "monopoly deal card game"
    },
    {
        "id": "gft_sketch_markers",
        "title": "Dual-Tip Alcohol Art Brush Markers (24 Colors)",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹799",
        "category": "Creative Arts",
        "age": "Ages 8+",
        "desc": "Professional fine-tip and broad chisel markers for manga, cartoon sketching, architectural drawing, and calligraphy.",
        "amazon": "dual tip art markers 24 set"
    },
    {
        "id": "gft_magic_clay",
        "title": "Ultra-Light Air Dry Clay 24-Color Modeling Set",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹749",
        "category": "Creative Arts",
        "age": "Ages 4+",
        "desc": "Non-sticky, mess-free modeling clay that air-dries into permanent lightweight figurines without baking.",
        "amazon": "air dry clay 24 colors modeling"
    },
    {
        "id": "gft_sudha_murty_bundle",
        "title": "Sudha Murty Children's 3-Book Storybook Box",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹850",
        "category": "Books & Reading",
        "age": "Ages 6–12",
        "desc": "Grandma's Bag of Stories, The Magic Drum, and The Bird with the Golden Wings. Heartfelt Indian moral tales.",
        "amazon": "grandmas bag of stories sudha murty"
    },
    {
        "id": "gft_fountain_pen",
        "title": "Pilot Kakuno Ergonomic Fountain Pen with Ink Cartridges",
        "tier": "Tier 1: ₹500 – ₹1,000",
        "priceRange": "₹899",
        "category": "Keepsakes & Writing",
        "age": "Ages 9+",
        "desc": "Japanese student fountain pen with smiling nib face to teach correct grip angle, smooth flow, and neat penmanship.",
        "amazon": "pilot kakuno fountain pen fine"
    },

    # -------------------------------------------------------------------------
    # Tier 2: ₹1,000 – ₹2,500 (Skill Builders, Classic Games & Active Play)
    # -------------------------------------------------------------------------
    {
        "id": "gft_magnetic_tiles",
        "title": "Magnetic 3D Building Tiles (60 Pieces)",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,499",
        "category": "STEM & Discovery",
        "age": "Ages 4–10",
        "desc": "Translucent colorful magnetic geometric shapes for building towers, castles, rocket ships, and marble mazes.",
        "amazon": "magnetic tiles building blocks for kids"
    },
    {
        "id": "gft_microscope",
        "title": "Junior Biological Monocular Microscope (1200x)",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,699",
        "category": "STEM & Discovery",
        "age": "Ages 7+",
        "desc": "LED-illuminated optical microscope with prepared glass slides of onion cells, butterfly wings, and pond droplets.",
        "amazon": "kids microscope science kit"
    },
    {
        "id": "gft_catan",
        "title": "Catan / Ticket to Ride Gateway Board Game",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹2,199",
        "category": "Tabletop Games",
        "age": "Ages 8+",
        "desc": "The ultimate family board game milestone. Learn trading, negotiation, route building, and strategic patience.",
        "amazon": "catan board game original"
    },
    {
        "id": "gft_badminton_set",
        "title": "Yonex Carbon Graphite Badminton Racket Duo Set",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹1,899",
        "category": "Sports & Active",
        "age": "Ages 7+",
        "desc": "Two lightweight isometric graphite rackets, full carrying cover, and 3 durable nylon shuttlecocks for weekend matches.",
        "amazon": "yonex badminton racket set of 2"
    },
    {
        "id": "gft_carrom_board",
        "title": "Champion Wooden Carrom Board with Coins & Striker",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹2,299",
        "category": "Tabletop Games",
        "age": "Ages 6+",
        "desc": "Thick Assam plywood carrom playing surface with smooth rebound borders, wooden coins, tournament striker, and boric powder.",
        "amazon": "carrom board with coins full size"
    },
    {
        "id": "gft_roald_dahl_box",
        "title": "Roald Dahl: Phizz-Whizzing 16-Book Collection",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹2,399",
        "category": "Books & Reading",
        "age": "Ages 7–12",
        "desc": "16 timeless paperback chapter books including Matilda, Charlie and the Chocolate Factory, The BFG, and Danny the Champion.",
        "amazon": "roald dahl 16 books box set"
    },
    {
        "id": "gft_roller_skates",
        "title": "Adjustable Inline Roller Skates with Light-Up Wheels",
        "tier": "Tier 2: ₹1,000 – ₹2,500",
        "priceRange": "₹2,199",
        "category": "Sports & Active",
        "age": "Ages 5–12",
        "desc": "4-size adjustable inline boots with illuminating PU wheels that glow when rolling without batteries, plus knee guard pads.",
        "amazon": "inline skates adjustable light wheels kids"
    },

    # -------------------------------------------------------------------------
    # Tier 3: ₹2,500 – ₹5,000 (Creative Mastery, Instruments & Optics)
    # -------------------------------------------------------------------------
    {
        "id": "gft_telescope",
        "title": "Astronomical Refractor Telescope (70mm Aperture)",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹3,999",
        "category": "STEM & Discovery",
        "age": "Ages 8+",
        "desc": "Explore lunar craters, Saturn's rings, and Jupiter's moons with 70mm multi-coated optics, smartphone adapter, and tripod.",
        "amazon": "astronomical telescope 70mm aperture for kids"
    },
    {
        "id": "gft_keyboard",
        "title": "Casio Mini Electronic Keyboard (44 Keys)",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹3,495",
        "category": "Music & Instruments",
        "age": "Ages 5+",
        "desc": "100 built-in tones, 50 rhythms, 10 practice songs, and LCD screen. Portable piano introduction for musical ear training.",
        "amazon": "casio sa 77 electronic keyboard"
    },
    {
        "id": "gft_robotics_kit",
        "title": "Smart Programmable STEM Robotics & Sensor Kit",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹3,799",
        "category": "STEM & Discovery",
        "age": "Ages 9+",
        "desc": "Build an obstacle-avoiding, Bluetooth-controlled robot vehicle. Learn block-based coding, ultrasonic sensors, and microcontrollers.",
        "amazon": "programmable robot kit stem for kids"
    },
    {
        "id": "gft_harry_potter_box",
        "title": "Harry Potter: Complete 7-Book Boxed Set (Bloomsbury)",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹2,899",
        "category": "Books & Reading",
        "age": "Ages 9–14+",
        "desc": "The complete 7-book magical series in a collectible display slipcase featuring original Jonny Duddle cover art.",
        "amazon": "harry potter complete box set bloomsbury"
    },
    {
        "id": "gft_instant_camera",
        "title": "Fujifilm Instax Mini 12 Instant Film Camera",
        "tier": "Tier 3: ₹2,500 – ₹5,000",
        "priceRange": "₹4,999",
        "category": "Keepsakes & Art",
        "age": "Ages 8+",
        "desc": "Credit-card size instant photo prints! Perfect for family trips, scrapbooking, and capturing candid childhood memories.",
        "amazon": "fujifilm instax mini 12 camera"
    },

    # -------------------------------------------------------------------------
    # Tier 4: ₹5,000+ (Milestone Electronics, Wheels & Family Keepsakes)
    # -------------------------------------------------------------------------
    {
        "id": "gft_kindle_paperwhite",
        "title": "Kindle Paperwhite (6.8\" Glare-Free E-Reader)",
        "tier": "Tier 4: ₹5,000+",
        "priceRange": "₹12,999",
        "category": "Books & Reading",
        "age": "Ages 9+",
        "desc": "300 ppi glare-free display that reads like real paper, adjustable warm light, weeks of battery life, and zero video/app distractions.",
        "amazon": "kindle paperwhite 16gb"
    },
    {
        "id": "gft_cycle",
        "title": "Hero / Firefox Multi-Speed Geared Mountain Bicycle",
        "tier": "Tier 4: ₹5,000+",
        "priceRange": "₹8,500 – ₹11,000",
        "category": "Sports & Active",
        "age": "Ages 8–14",
        "desc": "Front suspension, disc brakes, Shimano 21-speed gears, and lightweight alloy frame for neighborhood adventures and fitness.",
        "amazon": "kids geared bicycle 24 inch"
    },
    {
        "id": "gft_noise_cancelling_headphones",
        "title": "Sony Over-Ear Noise Cancelling Headphones",
        "tier": "Tier 4: ₹5,000+",
        "priceRange": "₹6,990",
        "category": "Electronics & Audio",
        "age": "Ages 12+",
        "desc": "Crystal-clear audio for study sessions, online courses, and music listening with active noise cancellation and 35-hour battery.",
        "amazon": "sony active noise cancelling headphones"
    }
]

DEFAULT_OCCASIONS = [
    {
        "id": "occ_child1_bday",
        "person": "Elder Child",
        "relationship": "Child 1 / Son",
        "type": "Birthday",
        "date": "10-24", # MM-DD
        "displayDate": "October 24",
        "milestone": "Double Digits 10th Birthday! 🎂",
        "emoji": "👦"
    },
    {
        "id": "occ_child2_bday",
        "person": "Younger Child",
        "relationship": "Child 2 / Daughter",
        "type": "Birthday",
        "date": "06-15",
        "displayDate": "June 15",
        "milestone": "7th Birthday Sparkle 🎈",
        "emoji": "👧"
    },
    {
        "id": "occ_mom_bday",
        "person": "Mom",
        "relationship": "Mother",
        "type": "Birthday",
        "date": "03-12",
        "displayDate": "March 12",
        "milestone": "Queen of the House Birthday 👑",
        "emoji": "👩"
    },
    {
        "id": "occ_dad_bday",
        "person": "Dad",
        "relationship": "Father",
        "type": "Birthday",
        "date": "08-04",
        "displayDate": "August 4",
        "milestone": "Chief Fun Officer Birthday 🌟",
        "emoji": "👨"
    },
    {
        "id": "occ_anniversary",
        "person": "Parents",
        "relationship": "Mom & Dad",
        "type": "Wedding Anniversary",
        "date": "11-18",
        "displayDate": "November 18",
        "milestone": "Crystal Anniversary (15 Years) 💍",
        "emoji": "💑"
    },
    {
        "id": "occ_grandpa_bday",
        "person": "Grandpa",
        "relationship": "Grandfather",
        "type": "Birthday",
        "date": "01-14",
        "displayDate": "January 14",
        "milestone": "Grandpa's Milestone Year 👴",
        "emoji": "👴"
    },
    {
        "id": "occ_grandma_bday",
        "person": "Grandma",
        "relationship": "Grandmother",
        "type": "Birthday",
        "date": "05-20",
        "displayDate": "May 20",
        "milestone": "Grandma's Golden Year 👵",
        "emoji": "👵"
    },
    {
        "id": "occ_diwali",
        "person": "Whole Family",
        "relationship": "Household",
        "type": "Festival Milestone",
        "date": "11-01",
        "displayDate": "November 1",
        "milestone": "Diwali Festival of Lights 🪔",
        "emoji": "🪔"
    }
]

data = {
    "gift_ideas": GIFT_IDEAS,
    "default_occasions": DEFAULT_OCCASIONS
}

with open('scripts/birthday_matrix_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Compiled {len(GIFT_IDEAS)} gift ideas across 4 tiers and {len(DEFAULT_OCCASIONS)} family occasions.")
