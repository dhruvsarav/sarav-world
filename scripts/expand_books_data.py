import json

with open('scripts/book_nook_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

box_sets = data['box_sets']
books = data['curated_books']

extra_boxes = [
    {
        "id": "box_bad_guys",
        "title": "The Bad Guys: Episodes 1–10 Box Set",
        "author": "Aaron Blabey",
        "age": "Ages 6–10",
        "booksCount": "10 Graphic Novels",
        "desc": "Mr. Wolf, Mr. Snake, Mr. Piranha, and Mr. Shark want to be heroes! High-velocity graphic novel comedy that gets kids reading instantly.",
        "amazon": "the bad guys box set aaron blabey",
        "coverEmoji": "🐺"
    },
    {
        "id": "box_dog_man",
        "title": "Dog Man: The Supa Epic 10-Book Collection",
        "author": "Dav Pilkey",
        "age": "Ages 6–10",
        "booksCount": "10 Graphic Novels",
        "desc": "Part dog, part policeman, and all hero! Dav Pilkey's blockbuster graphic novel series exploring kindness, empathy, and hilarious heroics.",
        "amazon": "dog man box set dav pilkey",
        "coverEmoji": "🐶"
    },
    {
        "id": "box_goosebumps",
        "title": "Classic Goosebumps 20-Book Retro Tin Set",
        "author": "R.L. Stine",
        "age": "Ages 8–12",
        "booksCount": "20 Spooky Paperbacks",
        "desc": "Reader beware, you're in for a scare! Night of the Living Dummy, Monster Blood, The Haunted Mask, and Stay Out of the Basement.",
        "amazon": "goosebumps retro tin box set rl stine",
        "coverEmoji": "👻"
    },
    {
        "id": "box_dork_diaries",
        "title": "Dork Diaries 12-Book Boxed Set",
        "author": "Rachel Renée Russell",
        "age": "Ages 8–12",
        "booksCount": "12 Illustrated Books",
        "desc": "Nikki Maxwell's comic diary chronicles middle-school drama, best friends Chloe and Zoey, and awkward crushes with doodle illustrations.",
        "amazon": "dork diaries box set rachel renee russell",
        "coverEmoji": "🎀"
    },
    {
        "id": "box_secret_seven",
        "title": "Enid Blyton: The Secret Seven 15-Book Box Set",
        "author": "Enid Blyton",
        "age": "Ages 6–9",
        "booksCount": "15 Books",
        "desc": "Peter, Janet, Jack, Barbara, George, Pam, and Scamper the dog meet in their shed with a secret password to crack local neighborhood mysteries.",
        "amazon": "secret seven complete box set enid blyton",
        "coverEmoji": "🔍"
    },
    {
        "id": "box_heroes_of_olympus",
        "title": "Heroes of Olympus 5-Book Hardcover Box Set",
        "author": "Rick Riordan",
        "age": "Ages 10–14",
        "booksCount": "5 Books",
        "desc": "The continuation of Percy Jackson: Greek and Roman demigods join forces aboard the flying warship Argo II to battle Gaea and the giants.",
        "amazon": "heroes of olympus box set rick riordan",
        "coverEmoji": "⚔️"
    },
    {
        "id": "box_fudge_collection",
        "title": "Judy Blume: The Fudge 5-Book Collection",
        "author": "Judy Blume",
        "age": "Ages 7–11",
        "booksCount": "5 Books",
        "desc": "Tales of a Fourth Grade Nothing, Superfudge, Fudge-a-Mania, and Double Fudge. Peter Hatcher's hilarious travails with toddler brother Fudge.",
        "amazon": "judy blume fudge series box set",
        "coverEmoji": "🐢"
    },
    {
        "id": "box_horrid_henry",
        "title": "Horrid Henry 25-Book Mega Box Collection",
        "author": "Francesca Simon",
        "age": "Ages 6–9",
        "booksCount": "25 Books",
        "desc": "Horrid Henry and his squeaky-clean brother Perfect Peter. Hilarious, snappy chapter stories that turn early readers into book lovers.",
        "amazon": "horrid henry box set francesca simon",
        "coverEmoji": "😈"
    }
]

extra_books = [
    {
        "id": "bk_bfg",
        "title": "The BFG (Big Friendly Giant)",
        "author": "Roald Dahl",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Fantasy & Magic",
        "pages": 208,
        "desc": "Orphan Sophie is whisked away by the BFG, a gentle 24-foot giant who catches dreams in jars and blows happy dreams into children's bedrooms.",
        "amazon": "the bfg roald dahl",
        "rating": 5
    },
    {
        "id": "bk_wonder",
        "title": "Wonder",
        "author": "R.J. Palacio",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Empathy & Kindness",
        "pages": 315,
        "desc": "August Pullman, a boy born with facial differences, enters fifth grade at a mainstream prep school, teaching an entire community courage and kindness.",
        "amazon": "wonder rj palacio",
        "rating": 5
    },
    {
        "id": "bk_ivan",
        "title": "The One and Only Ivan",
        "author": "Katherine Applegate",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Heartfelt Animal Tale",
        "pages": 300,
        "desc": "Ivan the silverback gorilla lives in a glass cage at the Exit 8 Big Top Mall. Inspired by baby elephant Ruby, he paints a way to freedom.",
        "amazon": "the one and only ivan katherine applegate",
        "rating": 5
    },
    {
        "id": "bk_secret_garden",
        "title": "The Secret Garden",
        "author": "Frances Hodgson Burnett",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Classic Mystery & Healing",
        "pages": 280,
        "desc": "Orphan Mary Lennox discovers a locked, overgrown walled garden at Misselthwaite Manor, nursing it back to life alongside invalid cousin Colin.",
        "amazon": "the secret garden frances hodgson burnett",
        "rating": 5
    },
    {
        "id": "bk_wrinkle_in_time",
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Sci-Fi Fantasy Classic",
        "pages": 228,
        "desc": "Meg Murry, her brother Charles Wallace, and friend Calvin travel through time and space via a tesseract to rescue their scientist father from IT.",
        "amazon": "a wrinkle in time madeleine lengle",
        "rating": 5
    },
    {
        "id": "bk_tenali_raman",
        "title": "The Wit and Wisdom of Tenali Raman",
        "author": "Traditional Indian Heritage",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Indian Wit & Humor",
        "pages": 140,
        "desc": "The witty court poet of Emperor Krishnadevaraya solves tricky royal dilemmas with unmatched humor, presence of mind, and sharp intelligence.",
        "amazon": "tenali raman stories for kids",
        "rating": 5
    },
    {
        "id": "bk_akbar_birbal",
        "title": "Classic Tales of Akbar and Birbal",
        "author": "Traditional Indian Heritage",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Indian Wit & Justice",
        "pages": 150,
        "desc": "Mughal Emperor Akbar tests his wisest court minister Birbal with impossible riddles, showing how fairness and wisdom always triumph.",
        "amazon": "akbar and birbal illustrated stories",
        "rating": 5
    },
    {
        "id": "bk_room_on_roof",
        "title": "The Room on the Roof",
        "author": "Ruskin Bond",
        "band": "Young Adventurers (Ages 10–13)",
        "genre": "Dehradun Coming-of-Age",
        "pages": 160,
        "desc": "Written by Ruskin Bond at age seventeen! 16-year-old Anglo-Indian boy Rusty runs away from his strict guardian to live in the vibrant bazaars of Dehra.",
        "amazon": "the room on the roof ruskin bond",
        "rating": 5
    },
    {
        "id": "bk_lost_temple",
        "title": "The Magic of the Lost Temple",
        "author": "Sudha Murty",
        "band": "Middle Grade (Ages 7–10)",
        "genre": "Archaeological Quest",
        "pages": 160,
        "desc": "City girl Nooni spends her summer vacation in her grandparents' Karnataka village, stumbling upon an ancient stepped well hidden inside the forest.",
        "amazon": "the magic of the lost temple sudha murty",
        "rating": 5
    },
    {
        "id": "bk_serpent_revenge",
        "title": "The Serpent's Revenge: Unusual Tales from the Mahabharata",
        "author": "Sudha Murty",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Epic Retelling",
        "pages": 190,
        "desc": "Lesser-known, fascinating legends from the Mahabharata: Babruvahana's battle with Arjuna, the mystery of the golden mongoose, and lessons of dharma.",
        "amazon": "the serpents revenge sudha murty",
        "rating": 5
    },
    {
        "id": "bk_wind_in_willows",
        "title": "The Wind in the Willows",
        "author": "Kenneth Grahame",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Riverside Animal Fable",
        "pages": 240,
        "desc": "Mole, Ratty, Badger, and the reckless, motor-car loving Mr. Toad of Toad Hall on the English countryside riverbank.",
        "amazon": "the wind in the willows kenneth grahame",
        "rating": 5
    },
    {
        "id": "bk_black_beauty",
        "title": "Black Beauty",
        "author": "Anna Sewell",
        "band": "Timeless Classics (Ages 8–14)",
        "genre": "Animal Compassion Classic",
        "pages": 220,
        "desc": "Narrated from the viewpoint of a handsome, gentle black horse living in Victorian England, pioneering kindness and empathy toward animals.",
        "amazon": "black beauty anna sewell",
        "rating": 5
    }
]

box_sets.extend(extra_boxes)
books.extend(extra_books)

data['box_sets'] = box_sets
data['curated_books'] = books

with open('scripts/book_nook_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Total Box Sets now: {len(box_sets)}")
print(f"Total Curated Books now: {len(books)}")
