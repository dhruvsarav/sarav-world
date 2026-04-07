import { useEffect, useMemo, useRef, useState } from "react"
import { motion } from "framer-motion"

import saravMain from "./assets/hero/sarav-main.png"
import saravSignWhite from "./assets/brand/Sarav-Sign-White.png"

import spouseShowcase from "./assets/aibuilder/spouse-showcase.png"
import chessmasterShowcase from "./assets/aibuilder/chessmaster-showcase.png"
import familyManagerShowcase from "./assets/aibuilder/family-manager-showcase.png"
import appTrio from "./assets/aibuilder/app-trio.png"
import ideaShipped from "./assets/aibuilder/idea-shipped.png"
import controlRoomBg from "./assets/aibuilder/futuristic-control-room-bg.png"
import androidBuildSuccess from "./assets/aibuilder/android-studio-build-success.png"
import cognizantLatestRole from "./assets/aibuilder/cognizant-latest-role.png"

import airplaneTravelCue from "./assets/timeline/airplane-travel-cue.png"
import covidChapterCue from "./assets/timeline/covid-chapter-cue.png"
import indiaUkGermany from "./assets/timeline/india-uk-germany.png"

import typewriter from "./assets/books/typewriter.png"
import diaryPen from "./assets/books/diary-pen.png"
import coffeeCup from "./assets/books/coffee-cup.png"
import lettersBundle from "./assets/books/letters-bundle.png"
import moonCrescent from "./assets/books/moon-crescent.png"
import moonlitBalconyWriting from "./assets/books/moonlit-balcony-writing.png"
import writersDeskBg from "./assets/books/writers-desk-bg.png"
import coffeeReadsBadge from "./assets/books/coffee-reads.png"

import blogSaravsWorld from "./assets/blog/blog-saravs-world.jpg"
import blogFewMiles from "./assets/blog/blog-few-miles.jpg"

import bookADayWithYou from "./assets/books/book-adaywithyou-bookcover-fc.png"
import bookAreYouGame from "./assets/books/book-areyougame-bookcover-fc.jpg"
import bookAWildWish from "./assets/books/book-awildwish-bookcover-fc.jpg"
import bookBelieveInMiracles from "./assets/books/book-believeinmiracles-bookcover-fc.jpg"
import bookCoffeeDate from "./assets/books/book-coffeedate-bookcover-fc.jpg"
import bookHowNotToIrritateYourWife from "./assets/books/book-hownottoirritateyourwife-bookcover-fc.png"
import bookLettersToMySon from "./assets/books/book-letterstomyson-bookcover-fc.jpg"
import bookLoveAt18 from "./assets/books/book-loveat18-bookcover-fc.png"
import bookOneHundredYears from "./assets/books/book-onehundredyears-bookcover-fc.png"
import bookOrangeOrchard from "./assets/books/book-orangeorchard-bookcover-fc.jpg"
import bookPsSerendipity from "./assets/books/book-psserendipity-bookcover-fc.png"
import bookPurposefulBusyness from "./assets/books/book-purposefulbusyness-bookcover-fc.png"
import bookRaneetTheGift from "./assets/books/book-raneetthegift-bookcover-fc.jpg"
import bookSearchingHer from "./assets/books/book-searchingher-bookcover-fc.png"
import bookSearchingHerParallelUniverse from "./assets/books/book-searchingher-paralleluniverse-bookcover-fc.jpg"
import bookSixteenAndHalf from "./assets/books/book-sixteen&half-bookcover-fc.jpg"
import bookTheFirstCall from "./assets/books/book-thefirstcall-bookcover-fc.jpg"

const clamp = (value, min, max) => Math.min(max, Math.max(min, value))

const fadeUp = {
  hidden: { opacity: 0, y: 28 },
  show: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.72, ease: [0.22, 1, 0.36, 1] },
  },
}

const stagger = {
  hidden: {},
  show: {
    transition: { staggerChildren: 0.08 },
  },
}

const navItems = [
  { id: "about", label: "About" },
  { id: "work", label: "What I Do" },
  { id: "journey", label: "Journey" },
  { id: "apps", label: "Builder" },
  { id: "books", label: "Books" },
  { id: "writing", label: "Writing" },
  { id: "contact", label: "Contact" },
]

const workCards = [
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
]

const appCards = [
  {
    title: "Spouse",
    subtitle: "A daily emotional connection engine for couples.",
    image: spouseShowcase,
  },
  {
    title: "Chess Master for Kidz",
    subtitle: "Learning through challenge, pattern, and play.",
    image: chessmasterShowcase,
  },
  {
    title: "Family Manager",
    subtitle: "Money, home, family, and planning in one place.",
    image: familyManagerShowcase,
  },
]

const journeyCards = [
  {
    year: "2025 — Present",
    title: "Cognizant · Associate Director",
    text: "Global Offering Lead for Future of Work Solutions — shaping AI-led workplace narratives, solution strategy, demos, and enterprise storytelling.",
    image: cognizantLatestRole,
  },
  {
    year: "2022 — 2025",
    title: "Cognizant · Senior Manager",
    text: "Built stronger Future of Work and solution narratives with enterprise travel, modern workplace thinking, and transformation-led client conversations.",
    image: airplaneTravelCue,
  },
  {
    year: "2020 — 2022",
    title: "Atos · Technical Project Manager",
    text: "Managed service transition, delivery coordination, and client-facing execution through a period that changed the way work itself moved.",
    image: covidChapterCue,
  },
  {
    year: "2009 — 2020",
    title: "Wipro · Software Engineer → Project Manager",
    text: "Grew from engineering foundations into project and program leadership across India, UK, and Germany — building through roles, teams, and geographies.",
    image: indiaUkGermany,
  },
]

const books = [
  { title: "How (Not) to Irritate Your Wife", cover: bookHowNotToIrritateYourWife, amazonUrl: "#" },
  { title: "Purposeful Busyness", cover: bookPurposefulBusyness, amazonUrl: "https://amzn.to/4mh45hZ" },
  { title: "Coffee Date", cover: bookCoffeeDate, amazonUrl: "https://amzn.to/4dtBpjD" },
  { title: "Believe in Miracles", cover: bookBelieveInMiracles, amazonUrl: "https://amzn.to/4mh49yf" },
  { title: "Searching Her: Home Was You", cover: bookSearchingHerParallelUniverse, amazonUrl: "https://amzn.to/41es1ZQ" },
  { title: "Searching Her", cover: bookSearchingHer, amazonUrl: "https://amzn.to/4smLLpg" },
  { title: "Letters to My Son", cover: bookLettersToMySon, amazonUrl: "https://amzn.to/4dyyRAH" },
  { title: "Are You Game?", cover: bookAreYouGame, amazonUrl: "https://amzn.to/4vuCDSi" },
  { title: "Orange Orchard", cover: bookOrangeOrchard, amazonUrl: "https://amzn.to/41japfi" },
  { title: "Raneet The Gift", cover: bookRaneetTheGift, amazonUrl: "https://amzn.to/3OmHRyE" },
  { title: "The First Call", cover: bookTheFirstCall, amazonUrl: "https://amzn.to/4smOSNH" },
  { title: "Sixteen & Half", cover: bookSixteenAndHalf, amazonUrl: "https://amzn.to/4dyrARn" },
  { title: "A Wild Wish", cover: bookAWildWish, amazonUrl: "https://amzn.to/4bVOlxr" },
  { title: "Love at 18", cover: bookLoveAt18, amazonUrl: "#" },
  { title: "A Day With You", cover: bookADayWithYou, amazonUrl: "#" },
  { title: "One Hundred Years", cover: bookOneHundredYears, amazonUrl: "#" },
    { title: "P.S. Serendipity", cover: bookPsSerendipity, amazonUrl: "#" },
]

const orbitBooks = [
  books[8],
  books[15],
  books[12],
  books[9],
  books[6],
  books[3],
  books[13],
  books[16],
]

function Reveal({ id, className = "", children }) {
  return (
    <motion.section
      id={id}
      className={className}
      variants={fadeUp}
      initial="hidden"
      whileInView="show"
      viewport={{ once: true, amount: 0.18 }}
    >
      {children}
    </motion.section>
  )
}

export default function App() {
  const journeyRef = useRef(null)

  const [orbitRotation, setOrbitRotation] = useState(0)
  const [activeOrbitIndex, setActiveOrbitIndex] = useState(0)
  const [journeyProgress, setJourneyProgress] = useState(0)
  const [activeSection, setActiveSection] = useState("about")
  const [scene, setScene] = useState({
    mouseX: 0,
    mouseY: 0,
    scrollY: 0,
    vh: 900,
  })

  useEffect(() => {
    let rafId = null

    const updateJourneyProgress = () => {
      const el = journeyRef.current
      if (!el) return

      const rect = el.getBoundingClientRect()
      const vh = window.innerHeight || 900
      const start = vh * 0.78
      const distance = rect.height - vh * 0.26
      const travelled = start - rect.top
      const progress = clamp(travelled / Math.max(distance, 1), 0, 1)

      setJourneyProgress(progress)
    }

    const updateActiveSection = () => {
      const scrollPoint = window.scrollY + (window.innerHeight || 900) * 0.28
      let current = "about"

      navItems.forEach((item) => {
        const el = document.getElementById(item.id)
        if (el && el.offsetTop <= scrollPoint) {
          current = item.id
        }
      })

      setActiveSection(current)
    }

    const updateScene = () => {
      rafId = null
      setScene({
        mouseX: window.__saravMx ?? 0,
        mouseY: window.__saravMy ?? 0,
        scrollY: window.scrollY || 0,
        vh: window.innerHeight || 900,
      })
    }

    const requestTick = () => {
      if (!rafId) rafId = window.requestAnimationFrame(updateScene)
    }

    const onMouseMove = (e) => {
      const mx = (e.clientX / window.innerWidth - 0.5) * 36
      const my = (e.clientY / window.innerHeight - 0.5) * 28
      window.__saravMx = mx
      window.__saravMy = my
      requestTick()
    }

    const onScroll = () => {
      requestTick()

      const y = window.scrollY || 0
      const rotation = y * 0.05
      setOrbitRotation(rotation)

      const step = 360 / orbitBooks.length
      const normalized = ((rotation % 360) + 360) % 360
      const index = Math.round(normalized / step) % orbitBooks.length
      setActiveOrbitIndex(index)

      updateJourneyProgress()
      updateActiveSection()
    }

    const onResize = () => {
      requestTick()
      updateJourneyProgress()
      updateActiveSection()
    }

    window.__saravMx = 0
    window.__saravMy = 0

    updateScene()
    updateJourneyProgress()
    updateActiveSection()

    window.addEventListener("mousemove", onMouseMove, { passive: true })
    window.addEventListener("scroll", onScroll, { passive: true })
    window.addEventListener("resize", onResize)

    return () => {
      if (rafId) window.cancelAnimationFrame(rafId)
      window.removeEventListener("mousemove", onMouseMove)
      window.removeEventListener("scroll", onScroll)
      window.removeEventListener("resize", onResize)
    }
  }, [])

  const activeBook = useMemo(
    () => orbitBooks[activeOrbitIndex] ?? orbitBooks[0],
    [activeOrbitIndex]
  )

  const activeJourneyIndex = useMemo(() => {
    return clamp(Math.floor(journeyProgress * journeyCards.length), 0, journeyCards.length - 1)
  }, [journeyProgress])

  const heroCycle = Math.floor(scene.scrollY / Math.max(scene.vh * 0.55, 1))

  const floatingStyle = (depth = 1, phase = 0, rotation = 0, yRange = 14, xRange = 10) => {
    const scrollWaveY = Math.sin(scene.scrollY * 0.004 + phase) * yRange * depth
    const scrollWaveX = Math.cos(scene.scrollY * 0.003 + phase) * xRange * depth
    const tx = scene.mouseX * depth + scrollWaveX
    const ty = scene.mouseY * depth + scrollWaveY
    const rz = scene.mouseX * 0.06 * depth + rotation

    return {
      transform: `translate3d(${tx}px, ${ty}px, 0) rotate(${rz}deg)`,
    }
  }

  return (
    <div className="site-shell">
      <div className="orb orb-violet" />
      <div className="orb orb-teal" />
      <div className="orb orb-blue" />

      <header className="site-header">
        <div className="site-header-inner">
          <a href="#home" className="site-brand">
            SARAV'S WORLD
          </a>

          <nav className="site-nav">
            {navItems.map((item) => (
              <a
                key={item.id}
                href={`#${item.id}`}
                className={`nav-link ${activeSection === item.id ? "is-active" : ""}`}
                aria-current={activeSection === item.id ? "page" : undefined}
              >
                {item.label}
              </a>
            ))}
          </nav>
        </div>
      </header>

      <main id="home">
        <section className="hero-section">
          <motion.div
            className="hero-center"
            initial={{ opacity: 0, y: 26 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.85, ease: [0.22, 1, 0.36, 1] }}
          >
            <p className="hero-kicker">
              Associate Director · Author · Builder of Future Work
            </p>

            <h1 className="hero-title">
              <span>SARAVANAKUMAR</span>
              <br />
              <span>MURUGAN</span>
            </h1>

            <p className="hero-text">
              Writing stories, building workplaces of the future, and turning ideas into
              products, demos, books, and experiences.
            </p>

            <div className="hero-actions">
              <a href="#books" className="btn btn-primary">
                Explore My Books
              </a>
              <a href="#apps" className="btn btn-secondary">
                See What I Build
              </a>
            </div>

            <div className="hero-focus-row">
              <div className="hero-focus-card">
                <span className="eyebrow">Current Focus</span>
                <strong>Future of Work</strong>
                <p>GenAI · Digital Workplace · Storytelling</p>
              </div>

              <div className="hero-focus-card center">
                <span className="eyebrow">Creative Universe</span>
                <strong>17 Books & Growing</strong>
                <p>Romance · Reflection · Family · Leadership</p>
              </div>

              <div className="hero-focus-card">
                <span className="eyebrow">Builder Side</span>
                <strong>Ideas into Products</strong>
                <p>Apps · Demos · Systems · Experiences</p>
              </div>
            </div>

            <div className="hero-stage">
              <div className="hero-stage-glow" />
              <div className="hero-light-sweep" />
              <img src={saravMain} alt="Sarav portrait" className="hero-portrait" />
            </div>

            <div
              className="hero-sign sign-shell"
              style={{
                transform: `translateY(${Math.sin(scene.scrollY * 0.01) * 3}px) rotate(${scene.mouseX * 0.025}deg)`,
              }}
            >
              <div className="signature-track">
                <img
                  key={heroCycle}
                  src={saravSignWhite}
                  alt="Sarav signature"
                  className="sign-draw-scroll"
                />
                <span className="signature-tip" />
                <span className="signature-glow-line" />
              </div>
            </div>
          </motion.div>
        </section>

        <Reveal id="about" className="section section-narrow">
          <div className="section-copy center-copy">
            <p className="section-kicker">About</p>
            <h2 className="section-title">
              Strategy by profession. Storytelling by instinct. Systems by design.
            </h2>
            <p className="section-text">
              I work at the intersection of enterprise transformation, AI-led workplace
              thinking, and personal creative expression. Some ideas become demos. Some
              become products. Some become books that stay with people.
            </p>
          </div>
        </Reveal>

        <Reveal id="work" className="section">
          <p className="section-kicker center-copy">What I Do</p>
          <h2 className="section-title center-copy">Three worlds. One voice.</h2>

          <motion.div
            className="card-grid three"
            variants={stagger}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.18 }}
          >
            {workCards.map((item) => (
              <motion.article key={item.title} variants={fadeUp} className="glass-card">
                <div className="card-accent" />
                <h3>{item.title}</h3>
                <p>{item.text}</p>
              </motion.article>
            ))}
          </motion.div>
        </Reveal>

        <Reveal id="journey" className="section">
          <p className="section-kicker center-copy">Career Journey</p>
          <h2 className="section-title center-copy">Built across roles.</h2>
          <p className="section-text center-copy journey-intro">
            The journey kept expanding — role by role, country by country, story by story.
          </p>

          <div className="journey-timeline" ref={journeyRef}>
            <div className="journey-line-track" aria-hidden="true">
              <span className="journey-line-base" />
              <span
                className="journey-line-progress"
                style={{ height: `${journeyProgress * 100}%` }}
              />
              <span
                className="journey-line-glow"
                style={{ top: `calc(${journeyProgress * 100}% - 44px)` }}
              />
            </div>

            {journeyCards.map((item, index) => (
              <div
                key={`${item.year}-${item.title}`}
                className={`journey-item ${index <= activeJourneyIndex ? "is-active" : ""} ${index % 2 === 0 ? "is-left" : "is-right"}`}
              >
                <div className="journey-node-wrap">
                  <span className="journey-node" />
                  <span className="journey-node-ring" />
                </div>

                <motion.article
                  className="glass-card journey-card"
                  initial={{ opacity: 0, x: index % 2 === 0 ? -36 : 36, y: 18 }}
                  whileInView={{ opacity: 1, x: 0, y: 0 }}
                  viewport={{ once: true, amount: 0.2 }}
                  transition={{ duration: 0.72, ease: [0.22, 1, 0.36, 1] }}
                >
                  <div className="journey-media">
                    <img src={item.image} alt={item.title} loading="lazy" />
                  </div>

                  <div className="journey-copy">
                    <span className="journey-year">{item.year}</span>
                    <h3>{item.title}</h3>
                    <p>{item.text}</p>
                  </div>
                </motion.article>
              </div>
            ))}
          </div>
        </Reveal>

        <Reveal id="apps" className="section">
          <p className="section-kicker center-copy">Builder of Ideas</p>
          <h2 className="section-title center-copy">
            Ideas that did not stay in notes.
          </h2>
          <p className="section-text center-copy builder-intro">
            Actively vibe coded with Vidhya using ChatGPT and Claude — turning ideas into
            visible, usable experiences.
          </p>

          <div className="builder-hero">
            <img src={controlRoomBg} alt="Builder control room" className="builder-bg" loading="lazy" />
            <div className="builder-overlay">
              <div className="builder-panel float-slow hover-tilt">
                <img src={appTrio} alt="App trio" loading="lazy" />
              </div>

              <div className="builder-side-stack">
                <div className="mini-panel float-medium hover-tilt-alt">
                  <img src={ideaShipped} alt="Idea shipped" loading="lazy" />
                </div>
                <div className="mini-panel float-fast hover-tilt">
                  <img src={androidBuildSuccess} alt="Android build success" loading="lazy" />
                </div>
              </div>
            </div>
          </div>

          <div className="card-grid three app-grid">
            {appCards.map((app) => (
              <article key={app.title} className="glass-card app-card">
                <div className="app-shot-wrap">
                  <img src={app.image} alt={app.title} className="app-shot" loading="lazy" />
                </div>
                <h3>{app.title}</h3>
                <p>{app.subtitle}</p>
              </article>
            ))}
          </div>
        </Reveal>

        <Reveal id="books" className="section books-section">
          <p className="section-kicker center-copy">Books</p>
          <h2 className="section-title center-copy">
            A circle of stories, and a shelf that keeps growing.
          </h2>
          <p className="section-text center-copy books-intro">
            Scroll the page and the orbit turns. The active story stays highlighted.
          </p>

          <div className="orbit-books-wrap">
            <div className="book-orbit">
              <div className="orbit-core">
                <img src={coffeeReadsBadge} alt="Coffee Reads" className="orbit-core-badge" loading="lazy" />
                <span className="orbit-core-text">Now in Focus</span>
                <strong className="orbit-active-title">{activeBook.title}</strong>
                <a
                  href={activeBook.amazonUrl}
                  className="orbit-amazon-btn"
                  target="_blank"
                  rel="noreferrer"
                >
                  View on Amazon
                </a>
              </div>

              {orbitBooks.map((book, index) => {
                const angle = (360 / orbitBooks.length) * index
                const isActive = index === activeOrbitIndex
                const transform = `rotate(${angle + orbitRotation}deg) translateY(-270px) rotate(${-angle - orbitRotation}deg) scale(${isActive ? 1.12 : 0.9})`

                return (
                  <div
                    key={book.title}
                    className={`orbit-item ${isActive ? "active" : ""}`}
                    style={{ transform }}
                  >
                    <img src={book.cover} alt={book.title} loading="lazy" />
                  </div>
                )
              })}
            </div>
          </div>

          <div className="books-grid">
            {books.map((book) => (
              <article key={book.title} className="book-card">
                <div className="book-cover-wrap">
                  <img src={book.cover} alt={book.title} className="book-cover" loading="lazy" />
                </div>
                <div className="book-meta">
                  <h3>{book.title}</h3>
                  <span>Sarav</span>
                </div>
                <div className="book-actions">
                  <a
                    href={book.amazonUrl}
                    className="book-amazon-btn"
                    target="_blank"
                    rel="noreferrer"
                  >
                    View on Amazon
                  </a>
                </div>
              </article>
            ))}
          </div>
        </Reveal>

        <Reveal id="writing" className="section writing-section">
          <p className="section-kicker center-copy">Writing Universe</p>
          <h2 className="section-title center-copy">
            Letters, coffee, moonlight, and quiet rooms.
          </h2>

          <div className="writing-scene clean-writing-banner">
            <img src={writersDeskBg} alt="Writer's desk" className="writing-scene-bg" loading="lazy" />
          </div>

          <div className="writing-split-stage">
            <div className="writing-split">
              <article className="glass-card writing-card balcony-card">
                <img src={moonlitBalconyWriting} alt="Moonlit balcony writing" loading="lazy" />
              </article>

              <article className="glass-card writing-copy-card">
                <span className="eyebrow">Some stories</span>
                <span className="typing-line">Welcome to the romance-o-sphere.</span>
                <h3>Some arrive with letters. Some arrive with silence.</h3>
                <p>
                  The writing side of this world is built on memory, longing, family,
                  reflection, old letters, late evenings, and the small emotional moments
                  that quietly become stories.
                </p>
                <p>
                  Coffee Reads. Romance. Quiet healing. Night skies. New beginnings.
                </p>
              </article>
            </div>

            <div
              className="writing-float balcony-letters"
              style={floatingStyle(0.92, 1.4, -2.2, 12, 10)}
            >
              <img src={lettersBundle} alt="Letters bundle" loading="lazy" />
            </div>

            <div
              className="writing-float balcony-typewriter"
              style={floatingStyle(1.08, 0.5, -1.6, 10, 8)}
            >
              <img src={typewriter} alt="Typewriter" loading="lazy" />
            </div>

            <div
              className="writing-float balcony-diary"
              style={floatingStyle(0.9, 2.4, 1.4, 14, 12)}
            >
              <img src={diaryPen} alt="Diary and pen" loading="lazy" />
            </div>

            <div
              className="writing-float balcony-coffee"
              style={floatingStyle(0.86, 3.6, 1.2, 10, 8)}
            >
              <img src={coffeeCup} alt="Coffee cup" loading="lazy" />
            </div>

            <div
              className="writing-float balcony-moon"
              style={floatingStyle(0.48, 4.6, 0, 8, 6)}
            >
              <img src={moonCrescent} alt="Moon" loading="lazy" />
            </div>
          </div>

          <div className="glass-card blogs-shell">
            <div className="blog-section-head">
              <span className="eyebrow">From the archives</span>
              <h3>Two blogs. Two voices. One long journey.</h3>
              <p>
                One holds the romance, poetry, and emotional reflections. The other holds
                the systems, work, leadership, and digital thinking.
              </p>
            </div>

            <div className="blog-blocks">
              <article className="blog-visual-card">
                <div className="blog-visual-wrap">
                  <img src={blogFewMiles} alt="Few Miles" className="blog-shot" loading="lazy" />
                  <div className="blog-visual-overlay" />
                  <div className="blog-badge">A romantic journey</div>
                </div>

                <div className="blog-card-copy">
                  <span className="eyebrow">Blog</span>
                  <h3>Few Miles</h3>
                  <p>
                    Poems, reflections, love-soaked memories, and the quieter emotional
                    universe behind many of the stories.
                  </p>

                  <div className="blog-cta-row">
                    <a
                      href="https://pendownmythought.blogspot.com/"
                      target="_blank"
                      rel="noreferrer"
                      className="blog-cta-btn"
                    >
                      Visit Few Miles
                    </a>
                  </div>
                </div>
              </article>

              <article className="blog-visual-card">
                <div className="blog-visual-wrap">
                  <img src={blogSaravsWorld} alt="Sarav’s World" className="blog-shot" loading="lazy" />
                  <div className="blog-visual-overlay" />
                  <div className="blog-badge">Thoughts on work and writing</div>
                </div>

                <div className="blog-card-copy">
                  <span className="eyebrow">Blog</span>
                  <h3>Sarav’s World</h3>
                  <p>
                    Reflections on AI, leadership, digital workplace thinking, books, and
                    the systems side of this journey.
                  </p>

                  <div className="blog-cta-row">
                    <a
                      href="https://saravsworld.wordpress.com/"
                      target="_blank"
                      rel="noreferrer"
                      className="blog-cta-btn"
                    >
                      Visit Sarav’s World
                    </a>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </Reveal>

        <Reveal id="contact" className="section section-narrow contact-section">
          <div className="glass-card contact-card">
            <div className="thanks-icon-wrap">
              <span className="thanks-icon">🙏</span>
            </div>

            <p className="section-kicker">Thank You</p>
            <h2 className="section-title">Thank you for visiting Sarav’s World.</h2>
            <p className="section-text">
              I hope something here stayed with you — a book, a thought, a memory, or an
              idea. Thoughtful feedback and sincere encouragement both help a writer grow.
              If a story spoke to you, I would be grateful if you shared a note, a reflection,
              or a testimonial. Thank you for reading, and for being part of this journey.
            </p>

            <div className="contact-links">
              <a href="mailto:sarav@iamsaravofficial.com">sarav@iamsaravofficial.com</a>
              <span>Chennai, India</span>
            </div>
          </div>
        </Reveal>
      </main>

      <footer className="site-footer">
        <div className="site-footer-inner">
          <div className="site-footer-top">
            <div className="footer-left">
              <h3>Sarav’s World</h3>
              <p>
                Stories, systems, books, products, and reflections — built across years,
                roles, and quiet obsessions.
              </p>
            </div>

            <div className="footer-right">
              <span className="footer-mini-kicker">Until the next page</span>
              <p>
                Thank you for visiting. Hope you enjoyed the books, the stories, and the
                world behind them.
              </p>
            </div>
          </div>

          <div className="site-footer-bottom">
            <span className="copyright-line">Copyright © 2009-2030 · Sarav</span>

            <div className="footer-links">
              <a href="/copyright/">Copyright</a>
              <a href="/privacy-policy/">Privacy</a>
              <a href="/terms/">Terms</a>
              <a href="#contact">Feedback</a>
              <a href="#home" className="back-to-top">
                Back to top ↑
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
