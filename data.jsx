// Static data for Sarav's World — shared via window globals so all babel scripts can see them.

const RAW = "https://raw.githubusercontent.com/nalkudilstudio/sarav-world/main/src/assets";
const SARAV_AUTHOR_PAGE = "https://www.amazon.in/stores/Saravanakumar-Murugan/author/B01733TNC2";

const NAV_ITEMS = [
  { id: "about", label: "About" },
  { id: "work", label: "What I Do" },
  { id: "journey", label: "Journey" },
  { id: "apps", label: "Builder" },
  { id: "books", label: "Books" },
  { id: "writing", label: "Writing" },
  { id: "contact", label: "Contact" },
];

const WORK_CARDS = [
  {
    title: "Future of Work",
    text: "Enterprise storytelling, GenAI-led solutioning, digital workplace strategy, experience-led transformation, and operating model conversations.",
  },
  {
    title: "Builder of Ideas",
    text: "From product thoughts to visible experiences — apps, demos, showcases, systems, and digital properties shaped into something people can feel.",
  },
  {
    title: "Author & Storyteller",
    text: "Novels, reflections, emotional universes, and quiet stories that stay with people long after reading.",
  },
];

const APP_CARDS = [
  { title: "Spouse", subtitle: "A daily emotional connection engine for couples.", image: `${RAW}/aibuilder/spouse-showcase.png` },
  { title: "Chess Master for Kidz", subtitle: "Learning through challenge, pattern, and play.", image: `${RAW}/aibuilder/chessmaster-showcase.png` },
  { title: "Family Manager", subtitle: "Money, home, family, and planning in one place.", image: `${RAW}/aibuilder/family-manager-showcase.png` },
];

const JOURNEY_CARDS = [
  {
    year: "2026 — Present",
    title: "TCS · Digital Workplace Technology Head",
    text: "Digital Workplace Technology Head — leading workplace transformation strategy, practice growth, and enterprise solutioning at Tata Consultancy Services.",
    image: `production/tcs-officially-tcser.png`,
  },
  {
    year: "2022 — 2026",
    title: "Cognizant · Senior Manager → Associate Director",
    text: "Grew into Global Offering Lead for Future of Work Solutions — building AI-led workplace narratives, solution strategy, demos, and enterprise storytelling across a four-year run.",
    image: `${RAW}/aibuilder/cognizant-latest-role.png`,
  },
  {
    year: "2020 — 2022",
    title: "Atos · Technical Project Manager",
    text: "Managed service transition, delivery coordination, and client-facing execution through a period that changed the way work itself moved.",
    image: `${RAW}/timeline/covid-chapter-cue.png`,
  },
  {
    year: "2009 — 2020",
    title: "Wipro · Software Engineer → Project Manager",
    text: "Grew from engineering foundations into project and program leadership across India, UK, and Germany — building through roles, teams, and geographies.",
    image: `${RAW}/timeline/india-uk-germany.png`,
  },
];

// All books. Unpublished ones (no Amazon listing yet) get isUpcoming=true and fall back to the author page.
const BOOKS = [
  { id: "irritate",       title: "How (Not) to Irritate Your Wife",   cover: `${RAW}/books/book-hownottoirritateyourwife-bookcover-fc.png`, amazonUrl: SARAV_AUTHOR_PAGE, isUpcoming: true },
  { id: "purposeful",     title: "Purposeful Busyness",                cover: `${RAW}/books/book-purposefulbusyness-bookcover-fc.png`,       amazonUrl: "https://amzn.to/4mh45hZ" },
  { id: "coffeedate",     title: "Coffee Date",                        cover: `${RAW}/books/book-coffeedate-bookcover-fc.jpg`,               amazonUrl: "https://amzn.to/4dtBpjD" },
  { id: "miracles",       title: "Believe in Miracles",                cover: `${RAW}/books/book-believeinmiracles-bookcover-fc.jpg`,        amazonUrl: "https://amzn.to/4mh49yf" },
  { id: "homewasyou",     title: "Searching Her: Home Was You",        cover: `${RAW}/books/book-searchingher-paralleluniverse-bookcover-fc.jpg`, amazonUrl: "https://amzn.to/41es1ZQ" },
  { id: "searching",      title: "Searching Her",                      cover: `${RAW}/books/book-searchingher-bookcover-fc.png`,             amazonUrl: "https://amzn.to/4smLLpg" },
  { id: "letters",        title: "Letters to My Son",                  cover: `${RAW}/books/book-letterstomyson-bookcover-fc.jpg`,           amazonUrl: "https://amzn.to/4dyyRAH" },
  { id: "areyougame",     title: "Are You Game?",                      cover: `${RAW}/books/book-areyougame-bookcover-fc.jpg`,               amazonUrl: "https://amzn.to/4vuCDSi" },
  { id: "orange",         title: "Orange Orchard",                     cover: `${RAW}/books/book-orangeorchard-bookcover-fc.jpg`,            amazonUrl: "https://amzn.to/41japfi" },
  { id: "raneet",         title: "Raneet The Gift",                    cover: `${RAW}/books/book-raneetthegift-bookcover-fc.jpg`,            amazonUrl: "https://amzn.to/3OmHRyE" },
  { id: "firstcall",      title: "The First Call",                     cover: `${RAW}/books/book-thefirstcall-bookcover-fc.jpg`,             amazonUrl: "https://amzn.to/4smOSNH" },
  { id: "sixteen",        title: "Sixteen & Half",                     cover: `${RAW}/books/book-sixteen%26half-bookcover-fc.jpg`,           amazonUrl: "https://amzn.to/4dyrARn" },
  { id: "wildwish",       title: "A Wild Wish",                        cover: `${RAW}/books/book-awildwish-bookcover-fc.jpg`,                amazonUrl: "https://amzn.to/4bVOlxr" },
  { id: "loveat18",       title: "Love at 18",                         cover: `${RAW}/books/book-loveat18-bookcover-fc.png`,                 amazonUrl: SARAV_AUTHOR_PAGE, isUpcoming: true },
  { id: "adaywithyou",    title: "A Day With You",                     cover: `${RAW}/books/book-adaywithyou-bookcover-fc.png`,              amazonUrl: SARAV_AUTHOR_PAGE, isUpcoming: true },
  { id: "hundredyears",   title: "One Hundred Years",                  cover: `${RAW}/books/book-onehundredyears-bookcover-fc.png`,          amazonUrl: SARAV_AUTHOR_PAGE, isUpcoming: true },
  { id: "psserendipity",  title: "P.S. Serendipity",                   cover: `${RAW}/books/book-psserendipity-bookcover-fc.png`,            amazonUrl: SARAV_AUTHOR_PAGE, isUpcoming: true },
];

// The 8 books that orbit (curated mix of published + flagship covers).
const ORBIT_BOOK_IDS = ["orange", "psserendipity", "wildwish", "raneet", "letters", "miracles", "loveat18", "hundredyears"];
const ORBIT_BOOKS = ORBIT_BOOK_IDS.map(id => BOOKS.find(b => b.id === id));

const IMG = {
  saravMain: `${RAW}/hero/sarav-main.png`,
  saravSignWhite: `${RAW}/brand/Sarav-Sign-White.png`,
  appTrio: `${RAW}/aibuilder/app-trio.png`,
  ideaShipped: `${RAW}/aibuilder/idea-shipped.png`,
  controlRoomBg: `${RAW}/aibuilder/futuristic-control-room-bg.png`,
  androidBuildSuccess: `${RAW}/aibuilder/android-studio-build-success.png`,
  coffeeReadsBadge: `${RAW}/books/coffee-reads.png`,
  typewriter: `${RAW}/books/typewriter.png`,
  diaryPen: `${RAW}/books/diary-pen.png`,
  coffeeCup: `${RAW}/books/coffee-cup.png`,
  lettersBundle: `${RAW}/books/letters-bundle.png`,
  moonCrescent: `${RAW}/books/moon-crescent.png`,
  moonlitBalconyWriting: `${RAW}/books/moonlit-balcony-writing.png`,
  writersDeskBg: `${RAW}/books/writers-desk-bg.png`,
  blogFewMiles: `${RAW}/blog/blog-few-miles.jpg`,
  blogSaravsWorld: `${RAW}/blog/blog-saravs-world.jpg`,
};

Object.assign(window, {
  NAV_ITEMS, WORK_CARDS, APP_CARDS, JOURNEY_CARDS,
  BOOKS, ORBIT_BOOKS, IMG, SARAV_AUTHOR_PAGE,
});
