import json

MOVIES = [
    # -------------------------------------------------------------------------
    # 1. 🍿 Animation Classics & Modern Masterpieces
    # -------------------------------------------------------------------------
    {
        "id": "mov_coco",
        "title": "Coco",
        "year": 2017,
        "genre": "Animation Classics",
        "rating": "U / PG",
        "runtime": "1h 45m",
        "vibe": "Heartfelt • Music • Tears of Joy",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.4",
        "synopsis": "Aspiring musician Miguel enters the Land of the Dead to unlock the real story behind his family's generational music ban.",
        "bestFor": "Everyone • Musical families"
    },
    {
        "id": "mov_spirited_away",
        "title": "Spirited Away",
        "year": 2001,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "2h 05m",
        "vibe": "Magical • Wonder • Studio Ghibli",
        "platforms": ["Netflix"],
        "imdb": "8.6",
        "synopsis": "10-year-old Chihiro wanders into a secret bathhouse world of spirits, gods, and witches, discovering inner courage to rescue her parents.",
        "bestFor": "Ages 8+ • Imagination lovers"
    },
    {
        "id": "mov_finding_nemo",
        "title": "Finding Nemo",
        "year": 2003,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 40m",
        "vibe": "Adventure • Father-Son Love • Ocean Quest",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.2",
        "synopsis": "After his son is captured in the Great Barrier Reef, timid clownfish Marlin embarks on an epic journey across the Pacific Ocean with forgetful Dory.",
        "bestFor": "All ages • Sibling night"
    },
    {
        "id": "mov_ratatouille",
        "title": "Ratatouille",
        "year": 2007,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 51m",
        "vibe": "Culinary Passion • Paris • Pure Joy",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.1",
        "synopsis": "Remy, a rat with gourmet taste and an uncanny culinary gift, forms an alliance with a bumbling restaurant garbage boy in the heart of Paris.",
        "bestFor": "Foodie families • All ages"
    },
    {
        "id": "mov_encanto",
        "title": "Encanto",
        "year": 2021,
        "genre": "Animation Classics",
        "rating": "U / PG",
        "runtime": "1h 42m",
        "vibe": "Vibrant • Family Empathy • Catchy Songs",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.2",
        "synopsis": "In a magical realm in Colombia, every Madrigal child receives a miracle gift—except Mirabel. When their magic falters, Mirabel becomes their only hope.",
        "bestFor": "Sing-alongs • Sibling bonding"
    },
    {
        "id": "mov_klaus",
        "title": "Klaus",
        "year": 2019,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 36m",
        "vibe": "Winter Warmth • Generosity • Holiday Magic",
        "platforms": ["Netflix"],
        "imdb": "8.2",
        "synopsis": "A selfish postman stationed in a frozen, feuding island town befriends an elusive reclusive toymaker, birthing a legendary tradition of kindness.",
        "bestFor": "Holiday vibes • Cozy blankets"
    },
    {
        "id": "mov_up",
        "title": "Up",
        "year": 2009,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 36m",
        "vibe": "Tearjerker • Wild Adventure • Unlikely Friendship",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.3",
        "synopsis": "78-year-old Carl Fredricksen ties thousands of balloons to his house to fly to South America, inadvertently bringing along overeager scout Russell.",
        "bestFor": "Grandparents & grandkids • All ages"
    },
    {
        "id": "mov_incredibles",
        "title": "The Incredibles",
        "year": 2004,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 55m",
        "vibe": "Superhero Action • Family Teamwork",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.0",
        "synopsis": "A family of undercover superheroes forced into suburban domesticity are pulled into a world-saving battle against an vengeful villain.",
        "bestFor": "Action night • Sibling co-op"
    },
    {
        "id": "mov_spiderverse",
        "title": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 57m",
        "vibe": "Visual Masterpiece • Hip-Hop Energy • Heart",
        "platforms": ["SonyLIV", "Prime Video", "Netflix"],
        "imdb": "8.4",
        "synopsis": "Teenager Miles Morales becomes the new Spider-Man and teams up with five alternate-dimension spider-heroes to stop a reality-destroying portal.",
        "bestFor": "Tweens & teens • Visual feast"
    },
    {
        "id": "mov_how_to_train_dragon",
        "title": "How to Train Your Dragon",
        "year": 2010,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 38m",
        "vibe": "Epic Flying • Loyalty • Empathy Over Force",
        "platforms": ["Prime Video", "JioCinema"],
        "imdb": "8.1",
        "synopsis": "Misfit Viking teen Hiccup cannot bring himself to kill dragons, instead befriending the injured Night Fury 'Toothless' and altering his tribe's destiny.",
        "bestFor": "Ages 6+ • Inspiring adventure"
    },
    {
        "id": "mov_zootopia",
        "title": "Zootopia",
        "year": 2016,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 48m",
        "vibe": "Detective Mystery • Laugh-Out-Loud • Inclusion",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.0",
        "synopsis": "Rookie bunny cop Judy Hopps partners with cynical con-artist fox Nick Wilde to unravel a city-wide conspiracy in a gleaming mammalian metropolis.",
        "bestFor": "Detective minds • Pure comedy"
    },
    {
        "id": "mov_puss_in_boots_last_wish",
        "title": "Puss in Boots: The Last Wish",
        "year": 2022,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 42m",
        "vibe": "Thrilling Art • Life Gratitude • Fairytale Quest",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "7.9",
        "synopsis": "Puss in Boots discovers he has burned through eight of his nine lives and embarks on an epic journey to find the mythical Wishing Star.",
        "bestFor": "Ages 7+ • Stunning animation"
    },
    {
        "id": "mov_song_of_the_sea",
        "title": "Song of the Sea",
        "year": 2014,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 33m",
        "vibe": "Folklore Poetry • Hand-Drawn • Calming Wonder",
        "platforms": ["Apple TV", "YouTube"],
        "imdb": "8.0",
        "synopsis": "Irish boy Ben discovers his mute sister Saoirse is a Selkie who must free faerie creatures trapped by the Owl Witch.",
        "bestFor": "Bedtime calm • Artistic families"
    },
    {
        "id": "mov_totoro",
        "title": "My Neighbor Totoro",
        "year": 1988,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 26m",
        "vibe": "Gentle Nature • Zero Conflict • Pure Innocence",
        "platforms": ["Netflix"],
        "imdb": "8.1",
        "synopsis": "Two young sisters move to the countryside to be near their ailing mother and discover friendly woodland spirits including giant cuddly Totoro.",
        "bestFor": "Toddlers & up • Peaceful night"
    },
    {
        "id": "mov_kung_fu_panda",
        "title": "Kung Fu Panda",
        "year": 2008,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 32m",
        "vibe": "Martial Arts • Belly Laughs • Inner Belief",
        "platforms": ["Prime Video", "Netflix"],
        "imdb": "7.6",
        "synopsis": "Po the noodle-slurping clumsy panda is unexpectedly chosen as the legendary Dragon Warrior and must master kung fu to defend the Valley of Peace.",
        "bestFor": "High energy • Popcorn night"
    },
    {
        "id": "mov_moana",
        "title": "Moana",
        "year": 2016,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 47m",
        "vibe": "Ocean Voyaging • Polynesian Myth • Anthem Songs",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.6",
        "synopsis": "Adventurous teenager Moana sails out on a daring mission across the open ocean to enlist the demigod Maui and restore the glowing heart of Te Fiti.",
        "bestFor": "Sing-along • Ocean dreamers"
    },
    {
        "id": "mov_wall_e",
        "title": "WALL-E",
        "year": 2008,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 38m",
        "vibe": "Cinematic Poetry • Romance • Earth Conservation",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.4",
        "synopsis": "A small waste-collecting robot left alone on a deserted Earth discovers a new purpose when he falls in love with sleek search droid EVE.",
        "bestFor": "Visual thinkers • Sci-fi lovers"
    },

    # -------------------------------------------------------------------------
    # 2. 🧭 Real-World Adventure & Wonder
    # -------------------------------------------------------------------------
    {
        "id": "mov_paddington2",
        "title": "Paddington 2",
        "year": 2017,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 43m",
        "vibe": "Kindness • Visual Wit • British Charm",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "7.8",
        "synopsis": "Paddington takes on odd jobs to buy a rare pop-up book for Aunt Lucy, only to be framed for its theft by a washed-up theatrical actor.",
        "bestFor": "100% Family Harmony • Pure Perfection"
    },
    {
        "id": "mov_night_museum",
        "title": "Night at the Museum",
        "year": 2006,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 48m",
        "vibe": "History Comes Alive • Robin Williams • Fun Thrills",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.5",
        "synopsis": "A newly recruited night watchman at New York's Museum of Natural History discovers that an ancient Egyptian artifact brings the exhibits to life every night.",
        "bestFor": "History curiosity • Laughs"
    },
    {
        "id": "mov_jumanji_welcome",
        "title": "Jumanji: Welcome to the Jungle",
        "year": 2017,
        "genre": "Adventure & Wonder",
        "rating": "12+",
        "runtime": "1h 59m",
        "vibe": "Gaming Tropes • The Rock & Kevin Hart • High Energy",
        "platforms": ["Netflix", "Prime Video"],
        "imdb": "7.0",
        "synopsis": "Four high school kids in detention get sucked into a vintage video game console, trapped inside avatar bodies in a perilous jungle world.",
        "bestFor": "Tweens & teens • Video gamers"
    },
    {
        "id": "mov_goonies",
        "title": "The Goonies",
        "year": 1985,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 54m",
        "vibe": "Treasure Hunt • 80s Nostalgia • Sibling Loyalty",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "7.7",
        "synopsis": "A band of Oregon kids discover a Spanish pirate map in an attic and follow underground booby-trapped caves to save their homes from foreclosure.",
        "bestFor": "Kids ages 8+ • Retro adventure"
    },
    {
        "id": "mov_hugo",
        "title": "Hugo",
        "year": 2011,
        "genre": "Adventure & Wonder",
        "rating": "U / PG",
        "runtime": "2h 06m",
        "vibe": "Cinema History • Parisian Clockwork • Mystery",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "7.5",
        "synopsis": "An orphan boy living in the walls of a 1930s Paris train station uncovers a mystery involving his late father's mechanical automaton.",
        "bestFor": "Ages 9+ • Visual thinkers"
    },
    {
        "id": "mov_narnia_wardrobe",
        "title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
        "year": 2005,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "2h 23m",
        "vibe": "Snowy Fantasy • Epic Quest • Bravery",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.9",
        "synopsis": "Four siblings step through a wardrobe into the mythical land of Narnia, trapped in perpetual winter by the White Witch, and join forces with the noble lion Aslan.",
        "bestFor": "Ages 7+ • Cozy winter night"
    },
    {
        "id": "mov_school_of_rock",
        "title": "School of Rock",
        "year": 2003,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 49m",
        "vibe": "Rock n Roll • Jack Black Energy • Kids Finding Their Voice",
        "platforms": ["Netflix", "Prime Video"],
        "imdb": "7.2",
        "synopsis": "Down-on-his-luck rock guitarist Dewey Finn imposts as a prep school substitute teacher and turns his classically trained pupils into a mind-blowing rock band.",
        "bestFor": "Music fans • Ages 8+"
    },
    {
        "id": "mov_enola_holmes",
        "title": "Enola Holmes",
        "year": 2020,
        "genre": "Adventure & Wonder",
        "rating": "12+",
        "runtime": "2h 03m",
        "vibe": "Ciphers • 4th-Wall Breaking • Victorian London",
        "platforms": ["Netflix"],
        "imdb": "6.6",
        "synopsis": "Sherlock Holmes' fiercely intelligent teen sister Enola journeys across Victorian London to solve the mystery of her missing mother.",
        "bestFor": "Tweens & teens • Mystery lovers"
    },
    {
        "id": "mov_national_treasure",
        "title": "National Treasure",
        "year": 2004,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "2h 11m",
        "vibe": "Declaration of Independence • Clues • Action",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.9",
        "synopsis": "Historian Benjamin Franklin Gates races rival treasure hunters to steal the Declaration of Independence and uncover an ancient Templar treasure.",
        "bestFor": "Ages 8+ • Puzzle lovers"
    },

    # -------------------------------------------------------------------------
    # 3. 🐾 Heartwarming Animal Quests
    # -------------------------------------------------------------------------
    {
        "id": "mov_lion_king",
        "title": "The Lion King",
        "year": 1994,
        "genre": "Animal Quests",
        "rating": "U",
        "runtime": "1h 28m",
        "vibe": "Majestic African Savannah • Hakuna Matata • Timeless",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.5",
        "synopsis": "Lion prince Simba is exiled after the tragic death of his father, growing up in the jungle until duty calls him to reclaim Pride Rock.",
        "bestFor": "All generations • Absolute classic"
    },
    {
        "id": "mov_babe",
        "title": "Babe",
        "year": 1995,
        "genre": "Animal Quests",
        "rating": "U",
        "runtime": "1h 31m",
        "vibe": "Heart of Gold • Farmyard Charm • Politeness",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "6.9",
        "synopsis": "Babe, a polite pig raised by sheepdogs on an Australian farm, learns to herd sheep with kindness instead of barking and fear.",
        "bestFor": "Young kids & grandparents"
    },
    {
        "id": "mov_bolt",
        "title": "Bolt",
        "year": 2008,
        "genre": "Animal Quests",
        "rating": "PG",
        "runtime": "1h 36m",
        "vibe": "Cross-Country Road Trip • Loyal Pup • Humor",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.8",
        "synopsis": "A TV star dog who believes his onscreen superpowers are real gets shipped across the country and must journey home alongside an alley cat and a hamster.",
        "bestFor": "Dog lovers • Sibling laughs"
    },
    {
        "id": "mov_march_penguins",
        "title": "March of the Penguins",
        "year": 2005,
        "genre": "Animal Quests",
        "rating": "U",
        "runtime": "1h 20m",
        "vibe": "Morgan Freeman Voice • Antarctic Majesty • Real Nature",
        "platforms": ["Prime Video", "YouTube"],
        "imdb": "7.5",
        "synopsis": "An extraordinary documentary capturing emperor penguins walking hundreds of miles across the frozen Antarctic wilderness to bring new life into the world.",
        "bestFor": "Nature lovers • Calm Sunday night"
    },
    {
        "id": "mov_finding_dory",
        "title": "Finding Dory",
        "year": 2016,
        "genre": "Animal Quests",
        "rating": "PG",
        "runtime": "1h 37m",
        "vibe": "Family Memory • Ocean Life • Hank the Octopus",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.3",
        "synopsis": "Dory suddenly recalls childhood memories of her parents and sets off across the California coast to the Marine Life Institute to find them.",
        "bestFor": "All ages • Feel-good"
    },

    # -------------------------------------------------------------------------
    # 4. 🕰️ Timeless Retro 80s & 90s Family
    # -------------------------------------------------------------------------
    {
        "id": "mov_back_to_future",
        "title": "Back to the Future",
        "year": 1985,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 56m",
        "vibe": "Time Machine DeLorean • Rock n Roll • Masterpiece",
        "platforms": ["Netflix", "Prime Video", "JioCinema"],
        "imdb": "8.5",
        "synopsis": "Marty McFly is accidentally sent 30 years into the past in a plutonium-powered DeLorean by eccentric scientist Doc Brown.",
        "bestFor": "Ages 8+ • Ultimate popcorn flick"
    },
    {
        "id": "mov_home_alone",
        "title": "Home Alone",
        "year": 1990,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 43m",
        "vibe": "Slapstick Traps • Christmas Cheer • Sibling Fantasy",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.7",
        "synopsis": "8-year-old Kevin McCallister is accidentally left behind when his family flies to Paris, and he must defend his suburban home against two bumbling burglars.",
        "bestFor": "Hysterical laughs • Holiday tradition"
    },
    {
        "id": "mov_mrs_doubtfire",
        "title": "Mrs. Doubtfire",
        "year": 1993,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "2h 05m",
        "vibe": "Robin Williams Genius • Family Healing • Hysterical",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.1",
        "synopsis": "After a bitter separation, a loving father disguises himself as an eccentric Scottish female housekeeper to spend precious time with his children.",
        "bestFor": "Ages 8+ • Emotional warmth"
    },
    {
        "id": "mov_honey_shrunk_kids",
        "title": "Honey, I Shrunk the Kids",
        "year": 1989,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 33m",
        "vibe": "Giant Backyard Insects • Science Blunder • Teamwork",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.4",
        "synopsis": "An eccentric inventor father's shrink ray machine accidentally reduces his children and the next-door neighbors to quarter-inch size in their backyard.",
        "bestFor": "Fun nostalgic thrills"
    },
    {
        "id": "mov_parent_trap",
        "title": "The Parent Trap",
        "year": 1998,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "2h 08m",
        "vibe": "Twin Swap • Summer Camp • Heartwarming",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.6",
        "synopsis": "Identical twins Hallie and Annie, separated at birth and raised on opposite sides of the Atlantic, meet at summer camp and plot to reunite their parents.",
        "bestFor": "Tween girls & whole family"
    },
    {
        "id": "mov_matilda",
        "title": "Matilda",
        "year": 1996,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 38m",
        "vibe": "Book Lover • Telekinesis • Roald Dahl Whimsy",
        "platforms": ["Netflix", "Prime Video"],
        "imdb": "7.0",
        "synopsis": "A genius young girl with neglected, dishonest parents and a terrifying school headmistress develops telekinetic powers to right everyday wrongs.",
        "bestFor": "Bookworms • Ages 6+"
    },
    {
        "id": "mov_space_jam",
        "title": "Space Jam",
        "year": 1996,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 28m",
        "vibe": "Michael Jordan • Looney Tunes • 90s Soundtrack",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "6.5",
        "synopsis": "Bugs Bunny and the Looney Tunes recruit retired basketball legend Michael Jordan to help them win an intergalactic basketball match against alien invaders.",
        "bestFor": "Sports fans • Casual Friday"
    },

    # -------------------------------------------------------------------------
    # 5. 🚀 Wholesome Sci-Fi & Space Fantasies
    # -------------------------------------------------------------------------
    {
        "id": "mov_et",
        "title": "E.T. the Extra-Terrestrial",
        "year": 1982,
        "genre": "Wholesome Sci-Fi",
        "rating": "U / PG",
        "runtime": "1h 55m",
        "vibe": "Flying Bicycles • Friendship • Spielberg Magic",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "7.9",
        "synopsis": "A troubled boy gathers courage to help a friendly stranded alien escape Earth and return to his home planet.",
        "bestFor": "Cinema milestone • All ages"
    },
    {
        "id": "mov_iron_giant",
        "title": "The Iron Giant",
        "year": 1999,
        "genre": "Wholesome Sci-Fi",
        "rating": "PG",
        "runtime": "1h 26m",
        "vibe": "'You Are Who You Choose to Be' • Soulful • 50s Sci-Fi",
        "platforms": ["Apple TV", "Prime Video"],
        "imdb": "8.1",
        "synopsis": "In 1957 Maine, a young boy befriends an enormous metal robot from outer space whom a paranoid government agent wants destroyed.",
        "bestFor": "Heartfelt tears • Ages 6+"
    },
    {
        "id": "mov_star_wars_new_hope",
        "title": "Star Wars: Episode IV - A New Hope",
        "year": 1977,
        "genre": "Wholesome Sci-Fi",
        "rating": "U / PG",
        "runtime": "2h 01m",
        "vibe": "Lightsabers • Millennium Falcon • Galactic Heroism",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.6",
        "synopsis": "Farm boy Luke Skywalker joins forces with Jedi Master Obi-Wan Kenobi, cocky pilot Han Solo, and two droids to rescue Princess Leia and save the galaxy.",
        "bestFor": "First Star Wars introduction"
    },
    {
        "id": "mov_zathura",
        "title": "Zathura: A Space Adventure",
        "year": 2005,
        "genre": "Wholesome Sci-Fi",
        "rating": "PG",
        "runtime": "1h 41m",
        "vibe": "Space Board Game • Sibling Reconciliation • Thrills",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "6.2",
        "synopsis": "Two bickering brothers find an old mechanical space board game in their basement that hurls their entire suburban house into deep outer space.",
        "bestFor": "Siblings who squabble • Ages 7+"
    },

    # -------------------------------------------------------------------------
    # 6. 🇮🇳 Indian Family & Regional Cinema Gems
    # -------------------------------------------------------------------------
    {
        "id": "mov_taare_zameen_par",
        "title": "Taare Zameen Par (Like Stars on Earth)",
        "year": 2007,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 45m",
        "vibe": "Empathy • Beautiful Art • Parent Awakening",
        "platforms": ["Netflix"],
        "imdb": "8.3",
        "synopsis": "An 8-year-old boy labeled lazy and rebellious struggles with dyslexia until an unconventional art teacher sees his true brilliance.",
        "bestFor": "Parents & kids • Unforgettable emotion"
    },
    {
        "id": "mov_stanley_dabba",
        "title": "Stanley Ka Dabba",
        "year": 2011,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "1h 36m",
        "vibe": "School Friendship • Food Sharing • Sincere",
        "platforms": ["Prime Video", "Disney+ Hotstar"],
        "imdb": "7.8",
        "synopsis": "Stanley is a beloved, creative fourth-grader who never brings a lunchbox to school, triggering conflict with a greedy Hindi teacher who snatches students' dabbas.",
        "bestFor": "School-age kids • Foodie kindness"
    },
    {
        "id": "mov_chillar_party",
        "title": "Chillar Party",
        "year": 2011,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 14m",
        "vibe": "Childhood Guts • Street Dog Loyalty • Pure Laughs",
        "platforms": ["Netflix", "Prime Video"],
        "imdb": "7.4",
        "synopsis": "A mischievous society gang of Mumbai kids band together to take on a powerful politician who wants to ban stray dogs from the city.",
        "bestFor": "Neighborhood kids • Sibling fun"
    },
    {
        "id": "mov_dhanak",
        "title": "Dhanak (Rainbow)",
        "year": 2015,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "1h 46m",
        "vibe": "Rajasthan Colors • Sibling Devotion • Shah Rukh Khan",
        "platforms": ["Netflix"],
        "imdb": "7.9",
        "synopsis": "10-year-old Pari leads her blind 8-year-old brother Chotu on a 300-km desert trek across Rajasthan to ask Bollywood superstar Shah Rukh Khan for eye surgery.",
        "bestFor": "Brother-sister bond • Uplifting"
    },
    {
        "id": "mov_munna_bhai",
        "title": "Munna Bhai M.B.B.S.",
        "year": 2003,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 36m",
        "vibe": "Jaadu Ki Jhappi • Pure Comedy • Respecting Parents",
        "platforms": ["Prime Video", "SonyLIV"],
        "imdb": "8.1",
        "synopsis": "A lovable Mumbai gangster enrolls in medical college to fulfill his father's dream of seeing him become a doctor, curing patients through human empathy.",
        "bestFor": "Whole family laughs • Timeless"
    },
    {
        "id": "mov_iqbal",
        "title": "Iqbal",
        "year": 2005,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 12m",
        "vibe": "Cricket Dream • Overcoming Odds • Sister Support",
        "platforms": ["Prime Video", "Zee5"],
        "imdb": "8.1",
        "synopsis": "A deaf and mute village boy passionately practices bowling with buffaloes, coached by an alcoholic former cricketer to reach the Indian national team.",
        "bestFor": "Cricket lovers • Inspiration"
    },
    {
        "id": "mov_3_idiots",
        "title": "3 Idiots",
        "year": 2009,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 50m",
        "vibe": "Follow Your Passion • Friendship • All Is Well",
        "platforms": ["Prime Video"],
        "imdb": "8.4",
        "synopsis": "Two friends search for their long-lost college roommate Rancho, recalling how his unconventional thinking inspired them to follow their true passions.",
        "bestFor": "Teens & parents • Universal masterpiece"
    },
    {
        "id": "mov_i_am_kalam",
        "title": "I Am Kalam",
        "year": 2011,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "1h 28m",
        "vibe": "Curiosity • Education • Cross-Class Friendship",
        "platforms": ["Prime Video", "YouTube"],
        "imdb": "7.9",
        "synopsis": "An impoverished Rajasthani roadside dhaba boy is inspired by President APJ Abdul Kalam, adopting his name and pursuing learning against all odds.",
        "bestFor": "Inspirational Sunday • Ages 6+"
    },
    {
        "id": "mov_english_vinglish",
        "title": "English Vinglish",
        "year": 2012,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 14m",
        "vibe": "Mother's Dignity • Sridevi • Ladoos • Warmth",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "7.8",
        "synopsis": "A quiet, sweet-tempered homemaker and caterer who is mocked by her husband and daughter for her poor English secretly enrolls in an English speaking course in Manhattan.",
        "bestFor": "Appreciating Mom • Whole family"
    },
    {
        "id": "mov_nil_battey_sannata",
        "title": "Nil Battey Sannata",
        "year": 2015,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "1h 40m",
        "vibe": "Math Dreams • Mother-Daughter Grit • Heart",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "8.2",
        "synopsis": "A hardworking maid enrolls in the same 10th-grade class as her unmotivated daughter to challenge her to study mathematics and aim high in life.",
        "bestFor": "Exam inspiration • Mother & daughter"
    }
]

BOARD_GAMES = [
    {
        "id": "bg_catan",
        "title": "Catan (Settlers of Catan)",
        "category": "Strategy & Gateway",
        "players": "3–4 Players",
        "age": "10+",
        "time": "60–90 min",
        "desc": "Collect wood, brick, wheat, sheep, and ore to build roads, settlements, and cities on the island of Catan. Master trading and negotiation with family.",
        "amazon": "catan board game"
    },
    {
        "id": "bg_ticket_to_ride",
        "title": "Ticket to Ride (Europe or Classic)",
        "category": "Strategy & Gateway",
        "players": "2–5 Players",
        "age": "8+",
        "time": "30–60 min",
        "desc": "Claim railway routes connecting iconic cities across Europe or North America. Easy to learn in 5 minutes, endlessly replayable.",
        "amazon": "ticket to ride board game"
    },
    {
        "id": "bg_carcassonne",
        "title": "Carcassonne",
        "category": "Strategy & Gateway",
        "players": "2–5 Players",
        "age": "7+",
        "time": "35–45 min",
        "desc": "Tile-placement masterpiece where players draw and place countryside tiles to construct medieval cities, roads, monasteries, and meadows.",
        "amazon": "carcassonne board game"
    },
    {
        "id": "bg_azul",
        "title": "Azul",
        "category": "Strategy & Gateway",
        "players": "2–4 Players",
        "age": "8+",
        "time": "30–45 min",
        "desc": "Tactile ceramic-like tiles drafting game where players compete to embellish the walls of the Royal Palace of Evora with Moorish art.",
        "amazon": "azul board game"
    },
    {
        "id": "bg_splendor",
        "title": "Splendor",
        "category": "Strategy & Gateway",
        "players": "2–4 Players",
        "age": "10+",
        "time": "30 min",
        "desc": "Fast engine-building chip-collecting game where Renaissance merchants acquire gem mines, trade routes, and noble patronage.",
        "amazon": "splendor board game"
    },
    {
        "id": "bg_codenames",
        "title": "Codenames (Classic or Pictures)",
        "category": "Party & Word Laughter",
        "players": "4–8+ Players",
        "age": "10+",
        "time": "15–20 min",
        "desc": "Two spymasters give one-word clues pointing to secret agent words on a 5x5 grid without tipping off the dreaded Assassin word!",
        "amazon": "codenames board game"
    },
    {
        "id": "bg_dixit",
        "title": "Dixit (Dreamy Art Cards)",
        "category": "Party & Word Laughter",
        "players": "3–6 Players",
        "age": "6+",
        "time": "30 min",
        "desc": "Imaginative storytelling game with 84 whimsical dreamlike illustrated cards. Give a subtle riddle or clue that only some players guess!",
        "amazon": "dixit board game"
    },
    {
        "id": "bg_exploding_kittens",
        "title": "Exploding Kittens",
        "category": "Party & Fast Cards",
        "players": "2–5 Players",
        "age": "7+",
        "time": "15 min",
        "desc": "Russian roulette card game powered by kittens, laser beams, and goat cheese. Defuse bombs, steal cards, and avoid blowing up!",
        "amazon": "exploding kittens card game"
    },
    {
        "id": "bg_monopoly_deal",
        "title": "Monopoly Deal Card Game",
        "category": "Party & Fast Cards",
        "players": "2–5 Players",
        "age": "8+",
        "time": "15 min",
        "desc": "All the fun of Monopoly in 15 snappy minutes! Collect 3 full property sets, charge rent, and play sneaky 'Deal Breaker' cards.",
        "amazon": "monopoly deal card game"
    },
    {
        "id": "bg_taco_cat",
        "title": "Taco Cat Goat Cheese Pizza",
        "category": "Party & Fast Cards",
        "players": "2–8 Players",
        "age": "6+",
        "time": "10–15 min",
        "desc": "High-octane slap card game! As players recite the words in sequence, slap the central pile whenever card matches spoken word. Pure family hysteria!",
        "amazon": "taco cat goat cheese pizza"
    },
    {
        "id": "bg_dobble",
        "title": "Spot It! / Dobble",
        "category": "Party & Fast Cards",
        "players": "2–8 Players",
        "age": "5+",
        "time": "10 min",
        "desc": "Round cards where any two cards always share exactly one matching symbol. Race to spot and shout out the match before anyone else.",
        "amazon": "spot it dobble game"
    },
    {
        "id": "bg_forbidden_island",
        "title": "Forbidden Island (Cooperative Quest)",
        "category": "Sibling Co-op",
        "players": "2–4 Players",
        "age": "8+",
        "time": "30 min",
        "desc": "Cooperative family board game where all players win or lose together! Work as adventurers to capture 4 sacred treasures before the island sinks.",
        "amazon": "forbidden island board game"
    },
    {
        "id": "bg_carrom",
        "title": "Classic Indian Carrom Board & Coins",
        "category": "Classic Tabletop",
        "players": "2–4 Players",
        "age": "6+",
        "time": "20–40 min",
        "desc": "The quintessential Indian family tabletop pastime. Pocket white and black carrom men, flick the striker with precision, and capture the red Queen with cover.",
        "amazon": "carrom board full size wooden"
    },
    {
        "id": "bg_jenga",
        "title": "Jenga Wooden Block Tower",
        "category": "Classic Tabletop",
        "players": "1–8 Players",
        "age": "5+",
        "time": "10–20 min",
        "desc": "Carefully pull wooden blocks from the 54-block tower and stack them on top without causing the wobbling tower to crash to the floor!",
        "amazon": "jenga classic game"
    },
    {
        "id": "bg_scrabble",
        "title": "Scrabble Deluxe / Junior",
        "category": "Classic Tabletop",
        "players": "2–4 Players",
        "age": "8+",
        "time": "45–60 min",
        "desc": "The world's favorite word crossword challenge. Place letter tiles on double and triple word score tiles to build vocabulary together.",
        "amazon": "scrabble original board game"
    },
    {
        "id": "bg_chess",
        "title": "Handcrafted Wooden Chess Set",
        "category": "Classic Tabletop",
        "players": "2 Players",
        "age": "6+",
        "time": "20–60 min",
        "desc": "Timeless game of kings, rooks, knights, and pawns. Fosters concentration, forward planning, sportsmanship, and tactical patience.",
        "amazon": "wooden chess board set magnetic"
    },
    {
        "id": "bg_sequence",
        "title": "Sequence Board Game",
        "category": "Family Strategy",
        "players": "2–12 Players",
        "age": "7+",
        "time": "20–30 min",
        "desc": "Play playing cards from your hand to place chips on corresponding spaces on the board. Complete two 5-in-a-row sequences to win.",
        "amazon": "sequence board game original"
    },
    {
        "id": "bg_blokus",
        "title": "Blokus Strategy Game",
        "category": "Family Strategy",
        "players": "2–4 Players",
        "age": "7+",
        "time": "20–30 min",
        "desc": "Tetris-like geometric tile placement where each new piece must touch at least one other piece of the same color, but only at the corners!",
        "amazon": "blokus board game"
    },
    {
        "id": "bg_uno_flip",
        "title": "UNO Flip! Double-Sided Card Game",
        "category": "Party & Fast Cards",
        "players": "2–10 Players",
        "age": "7+",
        "time": "15 min",
        "desc": "The classic UNO with an unexpected twist: a special FLIP card turns the entire deck over to the 'Dark Side' with vicious Draw 5 penalties!",
        "amazon": "uno flip card game"
    },
    {
        "id": "bg_clue",
        "title": "Cluedo / Clue Detective Game",
        "category": "Family Strategy",
        "players": "2–6 Players",
        "age": "8+",
        "time": "45 min",
        "desc": "Who did it? Where? And with what weapon? Move between rooms of the mansion, eliminate suspects with deductive logic, and make the final accusation.",
        "amazon": "cluedo board game hasbro"
    }
]

SNACKS = [
    {
        "id": "snk_popcorn",
        "title": "Stovetop Golden Cinema Butter Popcorn",
        "prep": "5 min",
        "icon": "🍿",
        "desc": "Pop yellow corn kernels in coconut or groundnut oil with turmeric and fine salt. Toss with melted butter and nutritional yeast for authentic cinema gold."
    },
    {
        "id": "snk_makhana",
        "title": "Desi Chaat Masala Roasted Makhana",
        "prep": "5 min",
        "icon": "🪷",
        "desc": "Slow-roast lotus seed foxnuts in pure A2 ghee until ultra crunchy. Dust generously with amchur, black salt, cumin, and kashmiri chili powder."
    },
    {
        "id": "snk_nachos",
        "title": "Loaded Oven Nachos with Warm Cheese Dip",
        "prep": "8 min",
        "icon": "🧀",
        "desc": "Spread crisp corn tortilla chips on a baking tray, top with diced tomatoes, sweet corn, jalapeños, and shredded mozzarella. Broil until bubbly."
    },
    {
        "id": "snk_fruit_skewers",
        "title": "Rainbow Fruit Skewers with Honey-Yogurt Dip",
        "prep": "7 min",
        "icon": "🍓",
        "desc": "Thread strawberries, green grapes, pineapple chunks, and blueberries onto wooden skewers. Serve chilled with vanilla Greek yogurt."
    },
    {
        "id": "snk_cocoa",
        "title": "Cozy Spiced Cinnamon Hot Chocolate",
        "prep": "6 min",
        "icon": "☕",
        "desc": "Warm whole milk with 70% dark chocolate chips, a pinch of Ceylon cinnamon, and brown sugar. Top with fluffy mini marshmallows."
    },
    {
        "id": "snk_garlic_bread",
        "title": "Pull-Apart Cheesy Herb Garlic Toast",
        "prep": "10 min",
        "icon": "🥖",
        "desc": "Slather crusty baguette slices with garlic herb butter, pack with shredded cheese, and toast until golden and crunchy."
    }
]

data = {
    "movies": MOVIES,
    "board_games": BOARD_GAMES,
    "snacks": SNACKS
}

with open('scripts/movie_night_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Compiled {len(MOVIES)} movies, {len(BOARD_GAMES)} board games, and {len(SNACKS)} snacks into scripts/movie_night_data.json.")
