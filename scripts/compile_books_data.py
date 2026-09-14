import json

BOX_SETS = [
    {
        "id": "box_roald_dahl",
        "title": "Roald Dahl: Phizz-Whizzing 16-Book Collection",
        "author": "Roald Dahl",
        "age": "Ages 7–12",
        "booksCount": "16 Paperbacks",
        "desc": "The complete beloved collection including Matilda, Charlie and the Chocolate Factory, The BFG, James and the Giant Peach, Danny the Champion of the World, and Fantastic Mr. Fox.",
        "amazon": "roald dahl 16 books box set",
        "coverEmoji": "🍫"
    },
    {
        "id": "box_harry_potter",
        "title": "Harry Potter Complete 7-Book Boxed Set",
        "author": "J.K. Rowling",
        "age": "Ages 9–14+",
        "booksCount": "7 Books (The Complete Saga)",
        "desc": "From the Philosopher's Stone to the Deathly Hallows. The defining magical fantasy series of our generation housed in a collectible display slipcase.",
        "amazon": "harry potter complete boxed set bloomsbury",
        "coverEmoji": "⚡"
    },
    {
        "id": "box_percy_jackson",
        "title": "Percy Jackson & the Olympians: 5-Book Box Set",
        "author": "Rick Riordan",
        "age": "Ages 9–13",
        "booksCount": "5 Books",
        "desc": "Modern teenage demigods battle ancient Greek monsters, titans, and prophecies across America. Fast-paced, witty, and mythological.",
        "amazon": "percy jackson box set rick riordan",
        "coverEmoji": "🔱"
    },
    {
        "id": "box_narnia",
        "title": "The Complete Chronicles of Narnia (7-Book Box Set)",
        "author": "C.S. Lewis",
        "age": "Ages 8–13",
        "booksCount": "7 Books",
        "desc": "Step beyond the wardrobe into Pauline Baynes' timeless world of Aslan, talking beasts, and the battle between good and evil in Narnia.",
        "amazon": "chronicles of narnia complete box set cs lewis",
        "coverEmoji": "🦁"
    },
    {
        "id": "box_sudha_murty",
        "title": "Sudha Murty Children's Collection Box Set",
        "author": "Sudha Murty",
        "age": "Ages 6–12",
        "booksCount": "6 Books",
        "desc": "Heartwarming Indian moral stories celebrating kindness, humility, and family values: Grandma's Bag of Stories, The Magic Drum, The Bird with the Golden Wings, and How I Taught My Grandmother to Read.",
        "amazon": "sudha murty children books box set penguin",
        "coverEmoji": "🪷"
    },
    {
        "id": "box_ruskin_bond",
        "title": "The Best of Ruskin Bond Children's Box Set",
        "author": "Ruskin Bond",
        "age": "Ages 8–14",
        "booksCount": "5 Books",
        "desc": "Enchanting nature tales from the Himalayan foothills of Mussoorie: The Blue Umbrella, Rusty the Boy from the Hills, Great Stories for Children, and The Cherry Tree.",
        "amazon": "ruskin bond children box set rupa",
        "coverEmoji": "🌲"
    },
    {
        "id": "box_amar_chitra_katha",
        "title": "Amar Chitra Katha: Epics & Mythology Box Set",
        "author": "Anant Pai (ACK Heritage)",
        "age": "Ages 7–14+",
        "booksCount": "20 Comic Volumes",
        "desc": "The gold standard of Indian cultural graphic storytelling: Mahabharata, Ramayana, Tales of Shiva, Krishna, Ganesha, Birbal, and Tenali Raman in vivid full color.",
        "amazon": "amar chitra katha box set mythology",
        "coverEmoji": "📜"
    },
    {
        "id": "box_famous_five",
        "title": "Enid Blyton: The Famous Five 21-Book Box Set",
        "author": "Enid Blyton",
        "age": "Ages 7–11",
        "booksCount": "21 Books",
        "desc": "Julian, Dick, Anne, George, and Timmy the dog on Kirrin Island. Ginger beer, ruined castles, secret underground passages, and unforgettable adventure.",
        "amazon": "famous five complete 21 books box set enid blyton",
        "coverEmoji": "🏝️"
    },
    {
        "id": "box_wimpy_kid",
        "title": "Diary of a Wimpy Kid Box Set (Books 1–12)",
        "author": "Jeff Kinney",
        "age": "Ages 8–12",
        "booksCount": "12 Hardcovers / Paperbacks",
        "desc": "Greg Heffley's hilarious middle-school survival diary illustrated with iconic stick drawings. Reluctant readers finish these in a single sitting!",
        "amazon": "diary of a wimpy kid box set jeff kinney",
        "coverEmoji": "📓"
    },
    {
        "id": "box_magic_treehouse",
        "title": "Magic Tree House Boxed Set (Books 1–28)",
        "author": "Mary Pope Osborne",
        "age": "Ages 6–9",
        "booksCount": "28 Early Chapters",
        "desc": "Jack and Annie travel through time in their backyard treehouse to prehistoric dinosaur valleys, ancient Egypt pyramids, and medieval castles.",
        "amazon": "magic tree house box set books",
        "coverEmoji": "🌳"
    },
    {
        "id": "box_geronimo_stilton",
        "title": "Geronimo Stilton Fabumouse 10-Book Collection",
        "author": "Elisabetta Dami",
        "age": "Ages 6–10",
        "booksCount": "10 Books",
        "desc": "Editor of The Rodent's Gazette travels on cheesy adventures across New Mouse City with full-color dynamic typography and hilarious maps.",
        "amazon": "geronimo stilton collection box set",
        "coverEmoji": "🧀"
    },
    {
        "id": "box_dr_seuss",
        "title": "Dr. Seuss Classic Rhyming Collection",
        "author": "Dr. Seuss",
        "age": "Ages 3–7",
        "booksCount": "10 Hardcovers",
        "desc": "The Cat in the Hat, Green Eggs and Ham, One Fish Two Fish, Horton Hears a Who, and Oh the Places You'll Go! Timeless phonics rhymes.",
        "amazon": "dr seuss classic collection box set",
        "coverEmoji": "🎩"
    }
]

CURATED_BOOKS = [
    # -------------------------------------------------------------------------
    # 1. 🐣 Early Readers (Ages 3–6)
    # -------------------------------------------------------------------------
    {
        "id": "bk_gruffalo",
        "title": "The Gruffalo",
        "author": "Julia Donaldson",
        "band": "Early Readers (Ages 3–6)",
        "genre": "Rhyming Animals",
        "pages": 32,
        "desc": "A clever little mouse takes a stroll through the deep dark wood, inventing a terrifying monster to scare off predators—only to meet the real beast!",
        "amazon": "the gruffalo julia donaldson",
        "rating": 5
    },
    {
        "id": "bk_hungry_caterpillar",
        "title": "The Very Hungry Caterpillar",
        "author": "Eric Carle",
        "band": "Early Readers (Ages 3–6)",
        "genre": "Picture Book",
        "pages": 32,
        "desc": "The iconic collage journey of an insatiable caterpillar eating his way through apples, plums, pickles, and cake before emerging as a radiant butterfly.",
        "amazon": "the very hungry caterpillar eric carle",
        "rating": 5
    },
    {
        "id": "bk_room_on_broom",
        "title": "Room on the Broom",
        "author": "Julia Donaldson",
        "band": "Early Readers (Ages 3–6)",
        "genre": "Rhyming Animals",
        "pages": 32,
        "desc": "A kindly witch and her cat invite a dog, a bird, and a frog onto their flying broomstick, teaming up to defeat a hungry dragon.",
        "amazon": "room on the broom julia donaldson",
        "rating": 5
    },
    {
        "id": "bk_where_wild_things",
        "title": "Where the Wild Things Are",
        "author": "Maurice Sendak",
        "band": "Early Readers (Ages 3–6)",
        "genre": "Imagination",
        "pages": 48,
        "desc": "Max wears his wolf suit, sails across the ocean to the land of the Wild Things, becomes their king, and returns home to find his supper still hot.",
        "amazon": "where the wild things are maurice sendak",
        "rating": 5
    },
    {
        "id": "bk_green_eggs_ham",
        "title": "Green Eggs and Ham",
        "author": "Dr. Seuss",
        "band": "Early Readers (Ages 3–6)",
        "genre": "Phonics & Rhyme",
        "pages": 62,
        "desc": "Sam-I-Am persistently asks a stubborn character to try green eggs and ham in a house, with a mouse, on a boat, or with a goat.",
        "amazon": "green eggs and ham dr seuss",
        "rating": 5
    },
    {
        "id": "bk_gajapati_kulapati",
        "title": "Gajapati Kulapati",
        "author": "Ashok Rajagopalan",
        "band": "Early Readers (Ages 3–6)",
        "genre": "Indian Picture Book",
        "pages": 28,
        "desc": "A funny, affectionate village elephant catches a giant cold after bathing in the rain. 'Aaaaaa-CHHOOOOO!' shakes the entire village!",
        "amazon": "gajapati kulapati tulika books",
        "rating": 5
    },

    # -------------------------------------------------------------------------
    # 2. 🦊 Middle Grade Chapter Books (Ages 7–10)
    # -------------------------------------------------------------------------
    {
        "id": "bk_matilda",
        "title": "Matilda",
        "author": "Roald Dahl",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Humor & Magic",
        "pages": 240,
        "desc": "Genius young bookworm Matilda uses her brilliant mind and telekinetic gifts to outwit the tyrannical school headmistress Miss Trunchbull.",
        "amazon": "matilda roald dahl",
        "rating": 5
    },
    {
        "id": "bk_charlie_chocolate",
        "title": "Charlie and the Chocolate Factory",
        "author": "Roald Dahl",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Fantasy & Humor",
        "pages": 190,
        "desc": "Humble Charlie Bucket finds a coveted Golden Ticket and tours Willy Wonka's mysterious candy wonderland alongside four spoiled children.",
        "amazon": "charlie and the chocolate factory roald dahl",
        "rating": 5
    },
    {
        "id": "bk_grandmas_bag_stories",
        "title": "Grandma's Bag of Stories",
        "author": "Sudha Murty",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Indian Folk Tales",
        "pages": 176,
        "desc": "Anand, Krishna, Raghu, and Meena visit their grandparents in Shiggaon during summer vacation, gathering around Ajji as she opens her magical bag of tales.",
        "amazon": "grandmas bag of stories sudha murty",
        "rating": 5
    },
    {
        "id": "bk_blue_umbrella",
        "title": "The Blue Umbrella",
        "author": "Ruskin Bond",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Himalayan Real-Life",
        "pages": 64,
        "desc": "In a Garhwal mountain village, young Binya trades her lucky leopard-claw pendant for a dazzling blue umbrella, learning about jealousy and generosity.",
        "amazon": "the blue umbrella ruskin bond",
        "rating": 5
    },
    {
        "id": "bk_magic_drum",
        "title": "The Magic Drum and Other Favorite Stories",
        "author": "Sudha Murty",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Folk Wisdom",
        "pages": 160,
        "desc": "Clever princesses, greedy moneylenders, wise ministers, and foolish kings populate these timeless traditional folk tales passed down through generations.",
        "amazon": "the magic drum sudha murty",
        "rating": 5
    },
    {
        "id": "bk_charlottes_web",
        "title": "Charlotte's Web",
        "author": "E.B. White",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Friendship & Heart",
        "pages": 192,
        "desc": "The miraculous bond between Wilbur the little spring pig and Charlotte the wise grey barn spider who writes tribute words in her web.",
        "amazon": "charlottes web eb white",
        "rating": 5
    },
    {
        "id": "bk_malgudi_days",
        "title": "Swami and Friends",
        "author": "R.K. Narayan",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Indian School Days",
        "pages": 190,
        "desc": "10-year-old Swaminathan navigates British-era school life, homework dread, cricket matches, and friendship in the fictional town of Malgudi.",
        "amazon": "swami and friends rk narayan",
        "rating": 5
    },
    {
        "id": "bk_five_treasure_island",
        "title": "Five on a Treasure Island",
        "author": "Enid Blyton",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Adventure & Mystery",
        "pages": 192,
        "desc": "The very first Famous Five adventure! Julian, Dick, Anne, and cousin George explore Kirrin Island and discover gold bullion in an old shipwreck.",
        "amazon": "five on a treasure island enid blyton",
        "rating": 5
    },

    # -------------------------------------------------------------------------
    # 3. ⚡ Young Adventurers & Fantasy (Ages 10–13)
    # -------------------------------------------------------------------------
    {
        "id": "bk_hp1",
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Magic & School",
        "pages": 352,
        "desc": "An orphaned boy learns on his eleventh birthday that he is a wizard and attends Hogwarts School of Witchcraft and Wizardry.",
        "amazon": "harry potter and the philosophers stone",
        "rating": 5
    },
    {
        "id": "bk_lightning_thief",
        "title": "The Lightning Thief (Percy Jackson #1)",
        "author": "Rick Riordan",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Mythology & Action",
        "pages": 377,
        "desc": "Percy Jackson discovers his real father is Poseidon, god of the sea, and embarks on a cross-country quest to prevent an Olympian war.",
        "amazon": "the lightning thief percy jackson",
        "rating": 5
    },
    {
        "id": "bk_lion_witch_wardrobe",
        "title": "The Lion, the Witch and the Wardrobe",
        "author": "C.S. Lewis",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Fantasy Epic",
        "pages": 208,
        "desc": "Four children step through a spare room wardrobe into the snow-covered kingdom of Narnia, fulfilling an ancient prophecy under Aslan's guidance.",
        "amazon": "the lion the witch and the wardrobe cs lewis",
        "rating": 5
    },
    {
        "id": "bk_hobbit",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Epic Fantasy",
        "pages": 310,
        "desc": "Reluctant hobbit Bilbo Baggins is swept away from his comfortable hobbit-hole by Gandalf and thirteen dwarves to reclaim the Lonely Mountain from Smaug.",
        "amazon": "the hobbit jrr tolkien",
        "rating": 5
    },
    {
        "id": "bk_aru_shah",
        "title": "Aru Shah and the End of Time",
        "author": "Roshani Chokshi",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Indian Hindu Mythology Fantasy",
        "pages": 368,
        "desc": "12-year-old Aru lights a cursed lamp in the Museum of Ancient Indian Art, awakening an ancient demon and discovering she is the reincarnation of a Pandava.",
        "amazon": "aru shah and the end of time roshani chokshi",
        "rating": 5
    },
    {
        "id": "bk_wings_of_fire",
        "title": "Wings of Fire: The Dragonet Prophecy",
        "author": "Tui T. Sutherland",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Dragon Fantasy",
        "pages": 336,
        "desc": "Five young dragonets raised in a hidden cave must fulfill an ancient prophecy to end a bloody war tearing the dragon kingdom of Pyrrhia apart.",
        "amazon": "wings of fire dragonet prophecy tui sutherland",
        "rating": 5
    },

    # -------------------------------------------------------------------------
    # 4. 🌟 Timeless Classics & Non-Fiction (Ages 8–14)
    # -------------------------------------------------------------------------
    {
        "id": "bk_little_prince",
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Philosophical Wonder",
        "pages": 96,
        "desc": "A stranded aviator in the Sahara desert meets an enigmatic little prince from asteroid B-612 who tends his unique rose and questions adult absurdity.",
        "amazon": "the little prince antoine de saint exupery",
        "rating": 5
    },
    {
        "id": "bk_panchatantra",
        "title": "Panchatantra: Illustrated Moral Tales",
        "author": "Pandit Vishnu Sharma",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Ancient Animal Fables",
        "pages": 220,
        "desc": "Centuries-old Indian animal fables demonstrating political wisdom, real-world pragmatism, true friendship, and ethical problem solving.",
        "amazon": "panchatantra complete illustrated stories",
        "rating": 5
    },
    {
        "id": "bk_boy_harnessed_wind",
        "title": "The Boy Who Harnessed the Wind",
        "author": "William Kamkwamba",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Inspirational STEM Biography",
        "pages": 304,
        "desc": "The true story of a 14-year-old boy in Malawi who built a working electricity-generating windmill from scrap bicycle parts to save his village from famine.",
        "amazon": "the boy who harnessed the wind young readers",
        "rating": 5
    },
    {
        "id": "bk_apg_wings_fire",
        "title": "Wings of Fire: An Autobiography",
        "author": "Dr. A.P.J. Abdul Kalam",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Inspirational Indian Biography",
        "pages": 196,
        "desc": "The inspiring life journey of India's 'Missile Man' and beloved 11th President from a humble Rameshwaram boat-owner's family to space pioneer.",
        "amazon": "wings of fire apj abdul kalam",
        "rating": 5
    }
]

BINGO_PROMPTS = [
    "Read a book with an animal hero 🐾",
    "Read under a blanket fort with a flashlight 🔦",
    "Read an illustrated comic or graphic novel 💬",
    "Read a book written by an Indian author 🇮🇳",
    "Read a book with over 200 pages 📖",
    "Read aloud a chapter to a parent or sibling 🗣️",
    "Read a mystery where you solve the culprit 🕵️",
    "Read a fantasy book featuring magic or spells 🪄",
    "Read a book set in another country or era 🗺️",
    "Read a science or nature non-fiction book 🔬",
    "Read while listening to rain or cozy music 🌧️",
    "Read a timeless classic written before you were born 📜",
    "Re-read your all-time favorite childhood book 🌟",
    "Read a book recommended by a friend or librarian 🤝",
    "Read a poetry or rhyming book 🪶",
    "Read a book that was made into a movie 🎬"
]

data = {
    "box_sets": BOX_SETS,
    "curated_books": CURATED_BOOKS,
    "bingo_prompts": BINGO_PROMPTS
}

with open('scripts/book_nook_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Compiled {len(BOX_SETS)} box sets, {len(CURATED_BOOKS)} curated books, and {len(BINGO_PROMPTS)} bingo prompts.")
