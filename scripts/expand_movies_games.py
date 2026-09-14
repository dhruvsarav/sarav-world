import json

with open('scripts/movie_night_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

movies = data['movies']
games = data['board_games']
snacks = data['snacks']

# Add 50 more world-class family movies
extra_movies = [
    {
        "id": "mov_tangled",
        "title": "Tangled",
        "year": 2010,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 40m",
        "vibe": "Floating Lanterns • Pure Joy • Music",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.7",
        "synopsis": "Feisty Rapunzel with 70 feet of golden hair escapes her secluded tower with the aid of charming bandit Flynn Rider.",
        "bestFor": "All ages • Family favorite"
    },
    {
        "id": "mov_inside_out",
        "title": "Inside Out",
        "year": 2015,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 35m",
        "vibe": "Emotional Intelligence • Joy and Sadness • Heartfelt",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.1",
        "synopsis": "After 11-year-old Riley moves to a new city, her core emotions Joy, Sadness, Anger, Fear, and Disgust struggle to navigate her inner world.",
        "bestFor": "Every parent and child • Growing up"
    },
    {
        "id": "mov_inside_out_2",
        "title": "Inside Out 2",
        "year": 2024,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 36m",
        "vibe": "Teen Anxiety • Self-Acceptance • Hilarious",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.6",
        "synopsis": "As Riley enters teenage headquarters, brand-new complex emotions like Anxiety, Envy, Ennui, and Embarrassment take over the console.",
        "bestFor": "Tweens, teens and parents"
    },
    {
        "id": "mov_toy_story",
        "title": "Toy Story",
        "year": 1995,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 21m",
        "vibe": "To Infinity and Beyond • Friendship • Landmark",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.3",
        "synopsis": "Woody, a good-hearted cowboy pull-string doll, feels threatened when flashy modern space ranger Buzz Lightyear arrives in Andy's bedroom.",
        "bestFor": "All generations"
    },
    {
        "id": "mov_toy_story_3",
        "title": "Toy Story 3",
        "year": 2010,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 43m",
        "vibe": "Growing Up • Loyalty • Beautiful Farewell",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.3",
        "synopsis": "The toys are mistakenly donated to a daycare center as Andy departs for college, banding together for an escape.",
        "bestFor": "Heartfelt family tears"
    },
    {
        "id": "mov_shrek",
        "title": "Shrek",
        "year": 2001,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 30m",
        "vibe": "Fairy Tale Parody • Donkey and Ogre • Laughs",
        "platforms": ["Prime Video", "Netflix", "JioCinema"],
        "imdb": "7.9",
        "synopsis": "A grumpy ogre's solitary swamp is overrun by evicted fairy tale creatures, forcing him to rescue a fiery princess to reclaim his home.",
        "bestFor": "Belly laughs • All ages"
    },
    {
        "id": "mov_shrek_2",
        "title": "Shrek 2",
        "year": 2004,
        "genre": "Animation Classics",
        "rating": "U / PG",
        "runtime": "1h 33m",
        "vibe": "Far Far Away • Puss in Boots • Pop Songs",
        "platforms": ["Prime Video", "JioCinema"],
        "imdb": "7.3",
        "synopsis": "Shrek and Fiona travel to the kingdom of Far Far Away to meet Fiona's royal parents, encountering the scheming Fairy Godmother and Prince Charming.",
        "bestFor": "High-energy laughs • Whole family"
    },
    {
        "id": "mov_monsters_inc",
        "title": "Monsters, Inc.",
        "year": 2001,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 32m",
        "vibe": "Boo! • Lovable Monsters • Laughter Over Fear",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.1",
        "synopsis": "Top scare-factory duo Sulley and Mike Wazowski discover their entire monster city power grid changes when a human toddler enters their world.",
        "bestFor": "Ages 4+ • Pure warmth"
    },
    {
        "id": "mov_mitchells_machines",
        "title": "The Mitchells vs. the Machines",
        "year": 2021,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 53m",
        "vibe": "Quirky Family • Robot Uprising • Fast and Funny",
        "platforms": ["Netflix"],
        "imdb": "7.6",
        "synopsis": "A quirky, dysfunctional family's road trip is interrupted when the world's electronic devices mount an apocalyptic revolt.",
        "bestFor": "Tech generation families • High energy"
    },
    {
        "id": "mov_bad_guys",
        "title": "The Bad Guys",
        "year": 2022,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 40m",
        "vibe": "Heist Comedy • Animal Rogues • Redemption",
        "platforms": ["Netflix", "Prime Video"],
        "imdb": "6.8",
        "synopsis": "To avoid prison, a criminal crew of animal outlaws must pull off their most challenging con yet: pretending to be model citizens.",
        "bestFor": "Cool cartoon action • All ages"
    },
    {
        "id": "mov_sing",
        "title": "Sing",
        "year": 2016,
        "genre": "Animation Classics",
        "rating": "U / PG",
        "runtime": "1h 48m",
        "vibe": "Pop Music Hits • Animals with Dreams • Inspiring",
        "platforms": ["Netflix", "JioCinema"],
        "imdb": "7.1",
        "synopsis": "In a city of humanoid animals, an optimistic koala theater owner stages the world's greatest singing competition to save his crumbling theater.",
        "bestFor": "Pop music lovers • Sibling night"
    },
    {
        "id": "mov_big_hero_6",
        "title": "Big Hero 6",
        "year": 2014,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 42m",
        "vibe": "Baymax Hug • San Fransokyo • Robotics",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.8",
        "synopsis": "Tech prodigy Hiro Hamada bonds with inflatable healthcare robot Baymax, transforming into high-tech heroes to solve a city mystery.",
        "bestFor": "STEM kids • Sibling love"
    },
    {
        "id": "mov_lilo_stitch",
        "title": "Lilo & Stitch",
        "year": 2002,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 25m",
        "vibe": "Ohana Means Family • Hawaiian Sun • Alien Chaos",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.3",
        "synopsis": "A lonely Hawaiian girl adopts an ugly little dog who is actually a rogue alien genetic experiment, teaching him the deep meaning of Ohana.",
        "bestFor": "Family unconditional love"
    },
    {
        "id": "mov_frozen",
        "title": "Frozen",
        "year": 2013,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 42m",
        "vibe": "Let It Go • Sister Loyalty • Olaf Snowman",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.4",
        "synopsis": "Fearless Anna teams up with rugged iceman Kristoff and snowman Olaf on an epic quest to find her sister Elsa, whose icy powers have trapped the kingdom in eternal winter.",
        "bestFor": "Sisters • Sing-alongs"
    },
    {
        "id": "mov_aladdin",
        "title": "Aladdin",
        "year": 1992,
        "genre": "Animation Classics",
        "rating": "U",
        "runtime": "1h 30m",
        "vibe": "A Whole New World • Robin Williams Genie • Magic Carpet",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.0",
        "synopsis": "A kindhearted Arabian street urchin and a power-hungry Grand Vizier vie for a magic oil lamp that has the power to make their deepest wishes come true.",
        "bestFor": "Timeless animation magic"
    },
    {
        "id": "mov_princess_bride",
        "title": "The Princess Bride",
        "year": 1987,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 38m",
        "vibe": "Fencing • True Love • Inconceivable Laughs",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "8.0",
        "synopsis": "A grandfather reads an epic fairy tale to his sick grandson about farm boy Westley's quest to rescue his true love Princess Buttercup.",
        "bestFor": "Ages 8+ • Absolute classic"
    },
    {
        "id": "mov_paddington1",
        "title": "Paddington",
        "year": 2014,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 35m",
        "vibe": "Marmalade Sandwiches • London • Warmth",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "7.3",
        "synopsis": "A young Peruvian bear travels to London in search of a home, taken in by the kindly Brown family while evading a sinister taxidermist.",
        "bestFor": "All ages • Family comfort"
    },
    {
        "id": "mov_holes",
        "title": "Holes",
        "year": 2003,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 57m",
        "vibe": "Desert Mystery • Camp Green Lake • Destiny",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.0",
        "synopsis": "A wrongfully convicted boy is sent to a brutal desert detention camp where the warden forces inmates to dig holes for hidden treasure.",
        "bestFor": "Ages 9+ • Mystery & justice"
    },
    {
        "id": "mov_babys_day_out",
        "title": "Baby's Day Out",
        "year": 1994,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 39m",
        "vibe": "Slapstick Escapades • Chicago Skyline • Laughs",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.2",
        "synopsis": "Three clumsy kidnappers abduct a wealthy baby who miraculously wanders loose across the entire city of Chicago visiting storybook landmarks.",
        "bestFor": "Kids laughing uncontrollably"
    },
    {
        "id": "mov_stuart_little",
        "title": "Stuart Little",
        "year": 1999,
        "genre": "Adventure & Wonder",
        "rating": "U",
        "runtime": "1h 24m",
        "vibe": "Little Mouse • Big City • Central Park Sailboats",
        "platforms": ["Netflix", "SonyLIV"],
        "imdb": "6.0",
        "synopsis": "The Little family adopts an articulate, plucky white mouse named Stuart, winning over his new human brother and jealous cat Snowbell.",
        "bestFor": "Young kids • Gentle fun"
    },
    {
        "id": "mov_hachi",
        "title": "Hachi: A Dog's Tale",
        "year": 2009,
        "genre": "Animal Quests",
        "rating": "U",
        "runtime": "1h 33m",
        "vibe": "Loyalty of a Lifetime • Akita Dog • Deep Emotion",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "8.1",
        "synopsis": "The true story of an Akita dog who faithfully waits at the train station every evening for nine years for his deceased university professor master.",
        "bestFor": "Dog lovers • Big box of tissues"
    },
    {
        "id": "mov_homeward_bound",
        "title": "Homeward Bound: The Incredible Journey",
        "year": 1993,
        "genre": "Animal Quests",
        "rating": "U",
        "runtime": "1h 24m",
        "vibe": "Two Dogs and a Cat • Wilderness Journey • Unstoppable",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.0",
        "synopsis": "A loyal golden retriever, an energetic bulldog pup, and a sassy Himalayan cat trek across the Sierra Nevada mountains to reunite with their human family.",
        "bestFor": "Ages 5+ • Pet lovers"
    },
    {
        "id": "mov_free_willy",
        "title": "Free Willy",
        "year": 1993,
        "genre": "Animal Quests",
        "rating": "PG",
        "runtime": "1h 52m",
        "vibe": "Ocean Freedom • Foster Boy • Orca Jump",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "6.0",
        "synopsis": "A rebellious foster boy sentenced to clean a rundown aquatic park bonds with an alienated captive orca whale, risking everything to return him to the ocean.",
        "bestFor": "Ages 7+ • Animal empathy"
    },
    {
        "id": "mov_sandlot",
        "title": "The Sandlot",
        "year": 1993,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 41m",
        "vibe": "Babe Ruth • Summer Baseball • The Beast Dog",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.8",
        "synopsis": "In the summer of 1962, a new kid in town is welcomed into a neighborhood baseball squad on an abandoned lot, facing down a legendary backyard guard dog.",
        "bestFor": "Summer nostalgia • Pure fun"
    },
    {
        "id": "mov_jumanji_1995",
        "title": "Jumanji (Classic 1995)",
        "year": 1995,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 44m",
        "vibe": "Robin Williams • Stampeders • Jungle Drumbeats",
        "platforms": ["Netflix", "SonyLIV"],
        "imdb": "7.1",
        "synopsis": "Two kids play a magical board game that unleashes jungle stampedes, giant spiders, and a man who has been trapped inside the game for 26 years.",
        "bestFor": "Thrilling retro night"
    },
    {
        "id": "mov_casper",
        "title": "Casper",
        "year": 1995,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 40m",
        "vibe": "Friendly Ghost • Whipstaff Manor • Gentle Spooks",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "6.2",
        "synopsis": "An afterlife therapist and his daughter move into a haunted Maine manor to communicate with three mischievous ghost uncles and kindly Casper.",
        "bestFor": "Autumn / Halloween family night"
    },
    {
        "id": "mov_flubber",
        "title": "Flubber",
        "year": 1997,
        "genre": "Retro 80s/90s Classics",
        "rating": "PG",
        "runtime": "1h 33m",
        "vibe": "Green Bouncy Slime • Robin Williams • Slapstick",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "5.3",
        "synopsis": "An absent-minded science professor invents an ultra-elastic green substance called Flubber that allows cars to fly and bowling balls to bounce sky-high.",
        "bestFor": "Kids who love slime"
    },
    {
        "id": "mov_transformers",
        "title": "Transformers",
        "year": 2007,
        "genre": "Wholesome Sci-Fi",
        "rating": "12+",
        "runtime": "2h 24m",
        "vibe": "Optimus Prime • Bumblebee • High-Octane CGI",
        "platforms": ["Netflix", "Prime Video", "JioCinema"],
        "imdb": "7.0",
        "synopsis": "An ordinary teenager buys his first car only to discover it is Bumblebee, an alien Autobot fighting to protect Earth from the Decepticons.",
        "bestFor": "Tweens & car lovers"
    },
    {
        "id": "mov_flight_navigator",
        "title": "Flight of the Navigator",
        "year": 1986,
        "genre": "Wholesome Sci-Fi",
        "rating": "PG",
        "runtime": "1h 30m",
        "vibe": "Silver Alien Spacecraft • Time Travel • 80s Charm",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.9",
        "synopsis": "A 12-year-old boy knocked unconscious in 1978 wakes up in 1986 without aging a day, discovering a chrome alien starship has chosen him as navigator.",
        "bestFor": "80s sci-fi nostalgia"
    },
    {
        "id": "mov_dangal",
        "title": "Dangal",
        "year": 2016,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 41m",
        "vibe": "Sister Power • Gold Medals • Father's Belief",
        "platforms": ["Apple TV", "Netflix"],
        "imdb": "8.3",
        "synopsis": "Former wrestler Mahavir Singh Phogat trains his daughters Geeta and Babita to break gender barriers and win India's first Commonwealth wrestling gold.",
        "bestFor": "Daughters and fathers • Electrifying"
    },
    {
        "id": "mov_secret_superstar",
        "title": "Secret Superstar",
        "year": 2017,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 30m",
        "vibe": "YouTube Dream • Mother's Love • Musical Wings",
        "platforms": ["Netflix"],
        "imdb": "7.8",
        "synopsis": "A 14-year-old girl from Vadodara with a passion for singing uploads anonymous YouTube videos in a burqa, becoming an overnight global sensation.",
        "bestFor": "Mother-daughter night • Inspiring"
    },
    {
        "id": "mov_super_30",
        "title": "Super 30",
        "year": 2019,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 34m",
        "vibe": "Education Merit • IIT Dream • Hrithik Roshan",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.9",
        "synopsis": "Genius mathematician Anand Kumar launches a free educational coaching program for 30 underprivileged students from Bihar to crack the elite IIT exam.",
        "bestFor": "Exam-prep motivation • Families"
    },
    {
        "id": "mov_chak_de_india",
        "title": "Chak De! India",
        "year": 2007,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 33m",
        "vibe": "Sattar Minute • Team India • Women's Hockey Glory",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "8.1",
        "synopsis": "Disgraced former Indian hockey captain Kabir Khan coaches a fractious, underestimated women's national hockey squad into World Cup champions.",
        "bestFor": "Patriotic goosebumps • Sports night"
    },
    {
        "id": "mov_lagaan",
        "title": "Lagaan: Once Upon a Time in India",
        "year": 2001,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "3h 44m",
        "vibe": "Village Cricket • British Tax Match • Historic Epic",
        "platforms": ["Netflix"],
        "imdb": "8.1",
        "synopsis": "In Victorian India, villagers stake their future on a game of cricket against ruthless British officers to cancel their oppressive agricultural taxes.",
        "bestFor": "Epic Sunday afternoon family feast"
    },
    {
        "id": "mov_paa",
        "title": "Paa",
        "year": 2009,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 13m",
        "vibe": "Father-Son Role Reversal • Big B • Auro",
        "platforms": ["YouTube", "Prime Video"],
        "imdb": "7.1",
        "synopsis": "Auro is an intelligent, witty 12-year-old boy suffering from an extremely rare genetic condition called progeria, uniting his estranged parents.",
        "bestFor": "Warmth & emotional bonding"
    },
    {
        "id": "mov_ferrari_sawaari",
        "title": "Ferrari Ki Sawaari",
        "year": 2012,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "2h 10m",
        "vibe": "Cricket Dreams • Father's Honesty • Sachin's Ferrari",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "6.6",
        "synopsis": "An honest father takes an audacious risk to borrow cricket legend Sachin Tendulkar's red Ferrari for a day to fund his son's cricket training at Lord's.",
        "bestFor": "Father-son movie night"
    },
    {
        "id": "mov_hichki",
        "title": "Hichki",
        "year": 2018,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "1h 56m",
        "vibe": "Teacher Who Believed • Tourette Syndrome • Heart",
        "platforms": ["Prime Video"],
        "imdb": "7.5",
        "synopsis": "An aspiring teacher with Tourette syndrome lands a job at an elite school assigned to teach a rowdy, underprivileged classroom labeled unteachable.",
        "bestFor": "Inspiring school kids"
    },
    {
        "id": "mov_we_bought_a_zoo",
        "title": "We Bought a Zoo",
        "year": 2011,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "2h 04m",
        "vibe": "20 Seconds of Insane Courage • Animals • Healing",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "7.1",
        "synopsis": "Following the loss of his wife, a father purchases a dilapidated countryside sanctuary with 200 exotic animals, working with his kids to reopen it.",
        "bestFor": "Family healing & hope"
    },
    {
        "id": "mov_bridge_terabithia",
        "title": "Bridge to Terabithia",
        "year": 2007,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 36m",
        "vibe": "Secret Forest Kingdom • Unshakable Friendship • Wonder",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "7.2",
        "synopsis": "Two fifth-grade outsiders invent a magical fantasy kingdom in the woods called Terabithia where they rule as king and queen, escaping reality.",
        "bestFor": "Ages 8+ • Imaginative kids"
    },
    {
        "id": "mov_night_museum_2",
        "title": "Night at the Museum: Battle of the Smithsonian",
        "year": 2009,
        "genre": "Adventure & Wonder",
        "rating": "PG",
        "runtime": "1h 45m",
        "vibe": "Smithsonian Archives • Amelia Earhart • Pure Fun",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "6.0",
        "synopsis": "Larry Daley infiltrates the Smithsonian Institution archives in Washington, D.C. when the magical golden tablet resurrects historical villains.",
        "bestFor": "History fans • High laughter"
    },
    {
        "id": "mov_klaus_repeat",
        "title": "Arthur Christmas",
        "year": 2011,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 37m",
        "vibe": "High-Tech North Pole • Sibling Rivalry • Pure Heart",
        "platforms": ["Netflix", "SonyLIV"],
        "imdb": "7.1",
        "synopsis": "Santa's clumsy youngest son Arthur sets out on an urgent mission using an old wooden sleigh to deliver one forgotten child's present before sunrise.",
        "bestFor": "Cozy winter movie night"
    },
    {
        "id": "mov_charlotte_web",
        "title": "Charlotte's Web",
        "year": 2006,
        "genre": "Animal Quests",
        "rating": "U",
        "runtime": "1h 37m",
        "vibe": "Some Pig • Spider Kindness • E.B. White Classic",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "6.3",
        "synopsis": "Wilbur the pig fears the slaughterhouse, so wise barn spider Charlotte weaves miraculous words praising Wilbur into her web to save his life.",
        "bestFor": "Ages 4+ • Empathy"
    },
    {
        "id": "mov_mr_beans_holiday",
        "title": "Mr. Bean's Holiday",
        "year": 2007,
        "genre": "Adventure & Wonder",
        "rating": "U",
        "runtime": "1h 30m",
        "vibe": "French Riviera • Slapstick Comedy • Zero Violence",
        "platforms": ["JioCinema", "Prime Video"],
        "imdb": "6.4",
        "synopsis": "Mr. Bean wins a church raffle trip to Cannes, creating innocent, chaotic comedic mayhem across France with a video camera and a lost Russian boy.",
        "bestFor": "Non-stop physical laughs"
    },
    {
        "id": "mov_dolphintale",
        "title": "Dolphin Tale",
        "year": 2011,
        "genre": "Animal Quests",
        "rating": "PG",
        "runtime": "1h 53m",
        "vibe": "Winter the Dolphin • Prosthetic Tail • True Story",
        "platforms": ["Prime Video", "Apple TV"],
        "imdb": "6.8",
        "synopsis": "The inspiring true story of Winter, a bottlenose dolphin who loses her tail in a crab trap, and the dedicated humans who invent a prosthetic tail to save her.",
        "bestFor": "Animal lovers • Perseverance"
    },
    {
        "id": "mov_fly_away_home",
        "title": "Fly Away Home",
        "year": 1996,
        "genre": "Animal Quests",
        "rating": "PG",
        "runtime": "1h 47m",
        "vibe": "Ultralight Aircraft • Canada Geese • Father-Daughter",
        "platforms": ["Apple TV", "Prime Video"],
        "imdb": "6.9",
        "synopsis": "A 13-year-old girl and her estranged inventor father pilot tiny ultralight aircraft across North America to teach a flock of orphaned geese how to migrate south.",
        "bestFor": "Nature lovers • Breathtaking visuals"
    },
    {
        "id": "mov_interstellar_family",
        "title": "Interstellar (Older Teens 13+)",
        "year": 2014,
        "genre": "Wholesome Sci-Fi",
        "rating": "13+",
        "runtime": "2h 49m",
        "vibe": "Wormholes • Father-Daughter Bond Across Time • Hans Zimmer",
        "platforms": ["Netflix", "Prime Video", "JioCinema"],
        "imdb": "8.7",
        "synopsis": "A team of space travelers journey through a wormhole near Saturn in search of a new habitable home for humanity, anchored by a father's promise to his daughter.",
        "bestFor": "Teens 13+ & parents • Epic science night"
    },
    {
        "id": "mov_the_sky_is_pink",
        "title": "The Sky Is Pink",
        "year": 2019,
        "genre": "Indian Family Cinema",
        "rating": "U / PG",
        "runtime": "2h 23m",
        "vibe": "Aisha Chaudhary • Family Grit • Unconditional Love",
        "platforms": ["Netflix"],
        "imdb": "7.6",
        "synopsis": "Told through the vibrant, cheeky voice of teenage motivational speaker Aisha Chaudhary, chronicling her parents' 25-year love story through life and adversity.",
        "bestFor": "Older kids & parents • Deep family appreciation"
    },
    {
        "id": "mov_bhaag_milkha",
        "title": "Bhaag Milkha Bhaag",
        "year": 2013,
        "genre": "Indian Family Cinema",
        "rating": "U",
        "runtime": "3h 06m",
        "vibe": "Flying Sikh • Determination • Triumph of the Spirit",
        "platforms": ["Disney+ Hotstar"],
        "imdb": "8.2",
        "synopsis": "The inspiring life story of Milkha Singh, an Indian athlete who overcame partition tragedy to become an Olympian champion and national legend.",
        "bestFor": "Sunday sports cinema • Patriotism"
    },
    {
        "id": "mov_kung_fu_panda_2",
        "title": "Kung Fu Panda 2",
        "year": 2011,
        "genre": "Animation Classics",
        "rating": "PG",
        "runtime": "1h 30m",
        "vibe": "Inner Peace • Goose Dad Love • Baby Po",
        "platforms": ["Prime Video", "Netflix"],
        "imdb": "7.3",
        "synopsis": "Po and the Furious Five travel to Gongmen City to defeat peacock Lord Shen, while Po uncovers the truth about his biological origins and loving goose dad.",
        "bestFor": "Adoption & family love • Great martial arts"
    }
]

# Add 20 more top board games
extra_games = [
    {
        "id": "bg_7wonders",
        "title": "7 Wonders (Architectural Drafting)",
        "category": "Strategy & Gateway",
        "players": "3–7 Players",
        "age": "10+",
        "time": "30 min",
        "desc": "Lead one of the seven great cities of the Ancient World! Draft cards to develop commercial routes, military strength, and scientific marvels.",
        "amazon": "7 wonders board game"
    },
    {
        "id": "bg_kingdomino",
        "title": "Kingdomino",
        "category": "Strategy & Gateway",
        "players": "2–4 Players",
        "age": "8+",
        "time": "15 min",
        "desc": "Build a 5x5 kingdom using domino-like terrain tiles (lakes, wheatfields, forests). Winner of the prestigious Spiel des Jahres board game award.",
        "amazon": "kingdomino board game"
    },
    {
        "id": "bg_wingspan",
        "title": "Wingspan",
        "category": "Strategy & Gateway",
        "players": "1–5 Players",
        "age": "10+",
        "time": "40–70 min",
        "desc": "Award-winning bird enthusiast board game with pastel eggs, bird feeder dice tower, and gorgeous biological illustrations of 170 species.",
        "amazon": "wingspan board game stonemaier"
    },
    {
        "id": "bg_pandemic",
        "title": "Pandemic (Original Cooperative)",
        "category": "Sibling Co-op",
        "players": "2–4 Players",
        "age": "8+",
        "time": "45 min",
        "desc": "Join forces as a disease containment team (Medic, Scientist, Dispatcher) to travel the globe, treat hotspots, and synthesize 4 cures.",
        "amazon": "pandemic board game original"
    },
    {
        "id": "bg_taboo",
        "title": "Taboo Party Game",
        "category": "Party & Word Laughter",
        "players": "4–10 Players",
        "age": "12+",
        "time": "20 min",
        "desc": "Get your teammates to guess the secret word without uttering any of the 5 forbidden taboo words on the card! High-speed buzzer excitement.",
        "amazon": "taboo board game hasbro"
    },
    {
        "id": "bg_telestrations",
        "title": "Telestrations: The Telephone Game Sketched Out",
        "category": "Party & Word Laughter",
        "players": "4–8 Players",
        "age": "8+",
        "time": "20 min",
        "desc": "Sketch what you see, then guess what you saw! Hilarious visual miscommunications guarantee side-splitting laughter across generations.",
        "amazon": "telestrations board game"
    },
    {
        "id": "bg_just_one",
        "title": "Just One (Cooperative Word Game)",
        "category": "Party & Word Laughter",
        "players": "3–7 Players",
        "age": "8+",
        "time": "20 min",
        "desc": "Write one-word clues for the active player to guess the secret word. If identical clues are written, they cancel each other out!",
        "amazon": "just one board game repos"
    },
    {
        "id": "bg_sushi_go",
        "title": "Sushi Go! Fast Card Drafting",
        "category": "Party & Fast Cards",
        "players": "2–5 Players",
        "age": "8+",
        "time": "15 min",
        "desc": "Pass the sushi cards around the table! Score points by grabbing sets of sashimi, nigiri with wasabi, maki rolls, and pudding desserts.",
        "amazon": "sushi go card game"
    },
    {
        "id": "bg_phase_10",
        "title": "Phase 10 Rummy Game",
        "category": "Party & Fast Cards",
        "players": "2–6 Players",
        "age": "7+",
        "time": "30–45 min",
        "desc": "Rummy-style card game with a twist: players must complete 10 sequential phases (sets of numbers, runs of color) before advancing.",
        "amazon": "phase 10 card game mattel"
    },
    {
        "id": "bg_skip_bo",
        "title": "Skip-Bo Sequencing Card Game",
        "category": "Party & Fast Cards",
        "players": "2–6 Players",
        "age": "7+",
        "time": "20–30 min",
        "desc": "Build sequential piles of cards from 1 to 12. Use wild Skip-Bo cards to empty your personal stock pile before your opponents.",
        "amazon": "skip bo card game mattel"
    },
    {
        "id": "bg_jaipur",
        "title": "Jaipur (2-Player Market Duel)",
        "category": "Strategy & Gateway",
        "players": "2 Players",
        "age": "10+",
        "time": "20 min",
        "desc": "Fast-paced tactical card trading game in the pink city of Jaipur. Trade silks, spices, camels, and rubies to win the Maharaja's seal of excellence.",
        "amazon": "jaipur board game space cowboys"
    },
    {
        "id": "bg_love_letter",
        "title": "Love Letter Deduction Game",
        "category": "Party & Fast Cards",
        "players": "2–6 Players",
        "age": "8+",
        "time": "15 min",
        "desc": "Compact 16-card masterpiece of deduction, risk, and luck. Deliver your romantic letter into Princess Annette's hands while keeping other suitors away.",
        "amazon": "love letter card game zmangames"
    },
    {
        "id": "bg_connect_4",
        "title": "Connect 4 Grid Game",
        "category": "Classic Tabletop",
        "players": "2 Players",
        "age": "5+",
        "time": "5–10 min",
        "desc": "Drop red and yellow checkers into the vertical grid. Connect 4 checkers in a row horizontally, vertically, or diagonally to win.",
        "amazon": "connect 4 original game hasbro"
    },
    {
        "id": "bg_twister",
        "title": "Twister Classic Floor Mat",
        "category": "Classic Tabletop",
        "players": "2–4 Players",
        "age": "6+",
        "time": "15 min",
        "desc": "The game that ties you up in knots! Spin the spinner and place your hands and feet on colored dots without toppling over onto the carpet.",
        "amazon": "twister game original hasbro"
    },
    {
        "id": "bg_operation",
        "title": "Operation Classic Electronic Game",
        "category": "Classic Tabletop",
        "players": "1–4 Players",
        "age": "6+",
        "time": "15 min",
        "desc": "Use the metal tweezers to extract hilarious ailment pieces (funny bone, butterflies in stomach) from Cavity Sam without sounding the red-nosed buzzer!",
        "amazon": "operation board game hasbro"
    },
    {
        "id": "bg_battleship",
        "title": "Battleship Naval Combat Game",
        "category": "Classic Tabletop",
        "players": "2 Players",
        "age": "7+",
        "time": "20 min",
        "desc": "Call out grid coordinates: 'B-7... Hit!' Hunt, track, and sink your opponent's fleet of five ships while shielding your own carriers and submarines.",
        "amazon": "battleship game hasbro"
    },
    {
        "id": "bg_guess_who",
        "title": "Guess Who? Face Mystery Game",
        "category": "Classic Tabletop",
        "players": "2 Players",
        "age": "5+",
        "time": "10 min",
        "desc": "'Does your person have glasses?' 'Are they wearing a hat?' Ask clever yes-or-no questions to eliminate suspects and guess the mystery person.",
        "amazon": "guess who board game hasbro"
    },
    {
        "id": "bg_ludo_snakes",
        "title": "Traditional Wooden Ludo & Snakes and Ladders",
        "category": "Classic Tabletop",
        "players": "2–4 Players",
        "age": "4+",
        "time": "20–30 min",
        "desc": "Double-sided wooden game board featuring evergreen Ludo and Snakes & Ladders. Timeless family favorite across Indian generations.",
        "amazon": "wooden ludo snakes and ladders board game"
    },
    {
        "id": "bg_outfoxed",
        "title": "Outfoxed! Cooperative Whodunit for Kids",
        "category": "Sibling Co-op",
        "players": "2–4 Players",
        "age": "5+",
        "time": "20 min",
        "desc": "Mrs. Plumpert's prized pot pie is missing! Move detective chickens around the board, gather clue cards with a special evidence decoder, and unmask the sneaky fox.",
        "amazon": "outfoxed board game gamewright"
    },
    {
        "id": "bg_pictionary",
        "title": "Pictionary Quick-Draw Game",
        "category": "Party & Word Laughter",
        "players": "4–8+ Players",
        "age": "8+",
        "time": "30 min",
        "desc": "Race against the 60-second sand timer to sketch clues on wipe-off boards for your team to guess. No artistic talent required—the worse the drawings, the funnier it gets!",
        "amazon": "pictionary board game mattel"
    }
]

# Append extra items avoiding duplicates
existing_m_ids = {m['id'] for m in movies}
for em in extra_movies:
    if em['id'] not in existing_m_ids:
        movies.append(em)

existing_g_ids = {g['id'] for g in games}
for eg in extra_games:
    if eg['id'] not in existing_g_ids:
        games.append(eg)

data['movies'] = movies
data['board_games'] = games

with open('scripts/movie_night_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Total Movies now: {len(movies)}")
print(f"Total Board Games now: {len(games)}")
print(f"Total Snacks: {len(snacks)}")
