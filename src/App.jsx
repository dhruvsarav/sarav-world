/* eslint-disable react/no-unescaped-entities */
// Sarav's World v2 — scroll-driven Framer Motion rebuild
// Drop-in replacement for src/App.jsx
//
// What changed vs. v1:
//   • Foundation: every scroll-driven effect now uses MotionValues + useScroll/useTransform/useSpring.
//     No more window.addEventListener + setState on every scroll tick — the entire tree no longer
//     re-renders as the user scrolls. Major perf + smoothness win on mobile.
//   • Hero: signature now SCROLL-DRAWN (clip-path bound to scrollYProgress). Portrait pulls back +
//     fades on scroll. Title reveals word-by-word with stagger + blur entrance.
//   • Journey: replaced with a sticky scroll-pinned cinematic — one screen per role, scroll advances
//     the active job. AnimatePresence handles the slide swap.
//   • Books orbit: rotation is now scroll-bound to the section (not the whole page), with spring
//     smoothing. Each cover position is computed as (x, y) from the rotation MotionValue — no more
//     binary "active vs not" snap; the magnetic effect is continuous.
//   • Book detail modal via layoutId — covers morph from grid → orbit → detail panel. Esc/click closes.
//   • Upcoming books (5 unpublished titles) → link to Sarav's Amazon author page with a "Coming soon"
//     badge instead of href="#".
//   • Mouse parallax (writing scene + ambient orbs) now driven by MotionValue → useSpring. Smooth,
//     no re-renders.
//   • useReducedMotion + MotionConfig at root — respects prefers-reduced-motion across the whole tree.
//   • Scroll progress bar in the header.

import React, { useEffect, useMemo, useRef, useState } from "react";
import {
  motion,
  MotionConfig,
  AnimatePresence,
  useScroll,
  useTransform,
  useSpring,
  useMotionValue,
  useMotionValueEvent,
  useMotionTemplate,
  useReducedMotion,
} from "framer-motion";

import saravMain from "./assets/hero/sarav-main.png";
import saravSignWhite from "./assets/brand/Sarav-Sign-White.png";

import spouseShowcase from "./assets/aibuilder/spouse-showcase.png";
import chessmasterShowcase from "./assets/aibuilder/chessmaster-showcase.png";
import familyManagerShowcase from "./assets/aibuilder/family-manager-showcase.png";
import appTrio from "./assets/aibuilder/app-trio.png";
import ideaShipped from "./assets/aibuilder/idea-shipped.png";
import controlRoomBg from "./assets/aibuilder/futuristic-control-room-bg.png";
import androidBuildSuccess from "./assets/aibuilder/android-studio-build-success.png";
import cognizantLatestRole from "./assets/aibuilder/cognizant-latest-role.png";
import tcsOfficiallyTcser from "./assets/timeline/tcs-officially-tcser.png";

import airplaneTravelCue from "./assets/timeline/airplane-travel-cue.png";
import covidChapterCue from "./assets/timeline/covid-chapter-cue.png";
import indiaUkGermany from "./assets/timeline/india-uk-germany.png";

import typewriter from "./assets/books/typewriter.png";
import diaryPen from "./assets/books/diary-pen.png";
import coffeeCup from "./assets/books/coffee-cup.png";
import lettersBundle from "./assets/books/letters-bundle.png";
import moonCrescent from "./assets/books/moon-crescent.png";
import moonlitBalconyWriting from "./assets/books/moonlit-balcony-writing.png";
import writersDeskBg from "./assets/books/writers-desk-bg.png";
import coffeeReadsBadge from "./assets/books/coffee-reads.png";

import blogSaravsWorld from "./assets/blog/blog-saravs-world.jpg";
import blogFewMiles from "./assets/blog/blog-few-miles.jpg";

import bookADayWithYou from "./assets/books/book-adaywithyou-bookcover-fc.png";
import bookAreYouGame from "./assets/books/book-areyougame-bookcover-fc.jpg";
import bookAWildWish from "./assets/books/book-awildwish-bookcover-fc.jpg";
import bookBelieveInMiracles from "./assets/books/book-believeinmiracles-bookcover-fc.jpg";
import bookCoffeeDate from "./assets/books/book-coffeedate-bookcover-fc.jpg";
import bookHowNotToIrritateYourWife from "./assets/books/book-hownottoirritateyourwife-bookcover-fc.png";
import bookLettersToMySon from "./assets/books/book-letterstomyson-bookcover-fc.jpg";
import bookLoveAt18 from "./assets/books/book-loveat18-bookcover-fc.png";
import bookOneHundredYears from "./assets/books/book-onehundredyears-bookcover-fc.png";
import bookOrangeOrchard from "./assets/books/book-orangeorchard-bookcover-fc.jpg";
import bookPsSerendipity from "./assets/books/book-psserendipity-bookcover-fc.png";
import bookPurposefulBusyness from "./assets/books/book-purposefulbusyness-bookcover-fc.png";
import bookRaneetTheGift from "./assets/books/book-raneetthegift-bookcover-fc.jpg";
import bookSearchingHer from "./assets/books/book-searchingher-bookcover-fc.png";
import bookSearchingHerParallelUniverse from "./assets/books/book-searchingher-paralleluniverse-bookcover-fc.jpg";
import bookSixteenAndHalf from "./assets/books/book-sixteen&half-bookcover-fc.jpg";
import bookTheFirstCall from "./assets/books/book-thefirstcall-bookcover-fc.jpg";

// ──────────────────────────────────────────────────────────────
// Data
// ──────────────────────────────────────────────────────────────

const AUTHOR_PAGE = "https://www.amazon.in/stores/Saravanakumar-Murugan/author/B01733TNC2";

const navItems = [
  { id: "about", label: "About" },
  { id: "work", label: "What I Do" },
  { id: "journey", label: "Journey" },
  { id: "apps", label: "Builder" },
  { id: "books", label: "Books" },
  { id: "writing", label: "Writing" },
  { id: "contact", label: "Contact" },
];

const workCards = [
  { title: "Future of Work",   text: "Enterprise storytelling, GenAI-led solutioning, digital workplace strategy, experience-led transformation, and operating model conversations." },
  { title: "Builder of Ideas", text: "From product thoughts to visible experiences — apps, demos, showcases, systems, and digital properties shaped into something people can feel." },
  { title: "Author & Storyteller", text: "Novels, reflections, emotional universes, and quiet stories that stay with people long after reading." },
];

const appCards = [
  { title: "Spouse",                subtitle: "A daily emotional connection engine for couples.", image: spouseShowcase },
  { title: "Chess Master for Kidz", subtitle: "Learning through challenge, pattern, and play.",   image: chessmasterShowcase },
  { title: "Family Manager",        subtitle: "Money, home, family, and planning in one place.",  image: familyManagerShowcase },
];

const journeyCards = [
  { year: "2026 — Present", title: "TCS · Digital Workplace Technology Head",
    text: "Digital Workplace Technology Head — leading workplace transformation strategy, practice growth, and enterprise solutioning at Tata Consultancy Services.",
    image: tcsOfficiallyTcser },
  { year: "2022 — 2026", title: "Cognizant · Associate Director",
    text: "Global Offering Lead for Future of Work Solutions — shaping AI-led workplace narratives, solution strategy, demos, and enterprise storytelling.",
    image: cognizantLatestRole },
  { year: "2022 — 2025", title: "Cognizant · Senior Manager",
    text: "Built stronger Future of Work and solution narratives with enterprise travel, modern workplace thinking, and transformation-led client conversations.",
    image: airplaneTravelCue },
  { year: "2020 — 2022", title: "Atos · Technical Project Manager",
    text: "Managed service transition, delivery coordination, and client-facing execution through a period that changed the way work itself moved.",
    image: covidChapterCue },
  { year: "2009 — 2020", title: "Wipro · Software Engineer → Project Manager",
    text: "Grew from engineering foundations into project and program leadership across India, UK, and Germany — building through roles, teams, and geographies.",
    image: indiaUkGermany },
];

// Unpublished titles get isUpcoming=true and link to the author page.
const books = [
  { id: "irritate",      title: "How (Not) to Irritate Your Wife",  cover: bookHowNotToIrritateYourWife,   amazonUrl: AUTHOR_PAGE,           isUpcoming: true },
  { id: "purposeful",    title: "Purposeful Busyness",              cover: bookPurposefulBusyness,         amazonUrl: "https://amzn.to/4mh45hZ" },
  { id: "coffeedate",    title: "Coffee Date",                      cover: bookCoffeeDate,                 amazonUrl: "https://amzn.to/4dtBpjD" },
  { id: "miracles",      title: "Believe in Miracles",              cover: bookBelieveInMiracles,          amazonUrl: "https://amzn.to/4mh49yf" },
  { id: "homewasyou",    title: "Searching Her: Home Was You",      cover: bookSearchingHerParallelUniverse, amazonUrl: "https://amzn.to/41es1ZQ" },
  { id: "searching",     title: "Searching Her",                    cover: bookSearchingHer,               amazonUrl: "https://amzn.to/4smLLpg" },
  { id: "letters",       title: "Letters to My Son",                cover: bookLettersToMySon,             amazonUrl: "https://amzn.to/4dyyRAH" },
  { id: "areyougame",    title: "Are You Game?",                    cover: bookAreYouGame,                 amazonUrl: "https://amzn.to/4vuCDSi" },
  { id: "orange",        title: "Orange Orchard",                   cover: bookOrangeOrchard,              amazonUrl: "https://amzn.to/41japfi" },
  { id: "raneet",        title: "Raneet The Gift",                  cover: bookRaneetTheGift,              amazonUrl: "https://amzn.to/3OmHRyE" },
  { id: "firstcall",     title: "The First Call",                   cover: bookTheFirstCall,               amazonUrl: "https://amzn.to/4smOSNH" },
  { id: "sixteen",       title: "Sixteen & Half",                   cover: bookSixteenAndHalf,             amazonUrl: "https://amzn.to/4dyrARn" },
  { id: "wildwish",      title: "A Wild Wish",                      cover: bookAWildWish,                  amazonUrl: "https://amzn.to/4bVOlxr" },
  { id: "loveat18",      title: "Love at 18",                       cover: bookLoveAt18,                   amazonUrl: AUTHOR_PAGE,           isUpcoming: true },
  { id: "adaywithyou",   title: "A Day With You",                   cover: bookADayWithYou,                amazonUrl: AUTHOR_PAGE,           isUpcoming: true },
  { id: "hundredyears",  title: "One Hundred Years",                cover: bookOneHundredYears,            amazonUrl: AUTHOR_PAGE,           isUpcoming: true },
  { id: "psserendipity", title: "P.S. Serendipity",                 cover: bookPsSerendipity,              amazonUrl: AUTHOR_PAGE,           isUpcoming: true },
];

const ORBIT_BOOK_IDS = ["orange", "psserendipity", "wildwish", "raneet", "letters", "miracles", "loveat18", "hundredyears"];
const orbitBooks = ORBIT_BOOK_IDS.map(id => books.find(b => b.id === id));

const ease = [0.16, 1, 0.3, 1];
const easeOut = [0.22, 1, 0.36, 1];

// ──────────────────────────────────────────────────────────────
// Reusable bits
// ──────────────────────────────────────────────────────────────

function SectionTitle({ text, className = "section-title center-copy" }) {
  const words = text.split(" ");
  return (
    <motion.h2
      className={className}
      initial="hidden"
      whileInView="show"
      viewport={{ once: true, amount: 0.4 }}
      variants={{ hidden: {}, show: { transition: { staggerChildren: 0.08 } } }}
    >
      {words.map((w, i) => (
        <motion.span
          key={i}
          className="title-word"
          variants={{
            hidden: { opacity: 0, y: 24, filter: "blur(6px)" },
            show: { opacity: 1, y: 0, filter: "blur(0px)", transition: { duration: 0.75, ease } },
          }}
        >
          {w}
        </motion.span>
      ))}
    </motion.h2>
  );
}

function ScrollProgress() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 24, mass: 0.3 });
  return <motion.div className="scroll-progress" style={{ scaleX }} />;
}

// ──────────────────────────────────────────────────────────────
// Header
// ──────────────────────────────────────────────────────────────

function Header() {
  const [active, setActive] = useState("about");

  useEffect(() => {
    const update = () => {
      const point = window.scrollY + window.innerHeight * 0.28;
      let current = "about";
      for (const item of navItems) {
        const el = document.getElementById(item.id);
        if (el && el.offsetTop <= point) current = item.id;
      }
      setActive(prev => (prev === current ? prev : current));
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    return () => {
      window.removeEventListener("scroll", update);
      window.removeEventListener("resize", update);
    };
  }, []);

  return (
    <motion.header
      className="site-header"
      initial={{ y: -40, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.7, ease }}
    >
      <div className="site-header-inner">
        <a href="#home" className="site-brand">SARAV'S WORLD</a>
        <nav className="site-nav">
          {navItems.map((item) => (
            <a
              key={item.id}
              href={`#${item.id}`}
              className={"nav-link" + (active === item.id ? " is-active" : "")}
              aria-current={active === item.id ? "page" : undefined}
            >
              {item.label}
            </a>
          ))}
        </nav>
      </div>
    </motion.header>
  );
}

// ──────────────────────────────────────────────────────────────
// Hero — scroll-drawn signature, parallax portrait
// ──────────────────────────────────────────────────────────────

function Hero() {
  const heroRef = useRef(null);

  const { scrollYProgress } = useScroll({
    target: heroRef,
    offset: ["start start", "end start"],
  });

  // Portrait pulls back & drifts up as the user scrolls past hero.
  const portraitScale = useTransform(scrollYProgress, [0, 1], [1.04, 0.88]);
  const portraitY = useTransform(scrollYProgress, [0, 1], [0, -60]);
  const portraitOpacity = useTransform(scrollYProgress, [0, 0.85], [1, 0.35]);

  // Signature draws itself as the user scrolls. Clip-path inset goes 100% → 0%.
  const sigProgress = useSpring(useTransform(scrollYProgress, [0, 0.55], [0, 1]), {
    stiffness: 90, damping: 22, mass: 0.6,
  });
  const sigInsetRight = useTransform(sigProgress, (p) => `${(1 - p) * 100}%`);
  const sigClipPath = useMotionTemplate`inset(0 ${sigInsetRight} 0 0)`;
  const sigTipLeft = useTransform(sigProgress, (p) => `${4 + p * 88}%`);
  const sigTipOpacity = useTransform(sigProgress, [0, 0.05, 0.92, 1], [0, 1, 1, 0]);
  const sigGlowOpacity = useTransform(sigProgress, [0.6, 1], [0, 0.8]);
  const sigGlowScaleX = useTransform(sigProgress, [0.6, 1], [0.4, 1]);

  const titleWords = ["SARAVANAKUMAR", "MURUGAN"];

  const focusCards = [
    { eyebrow: "Current Focus",     strong: "Future of Work",       text: "GenAI · Digital Workplace · Storytelling" },
    { eyebrow: "Creative Universe", strong: "17 Books & Growing",   text: "Romance · Reflection · Family · Leadership", center: true },
    { eyebrow: "Builder Side",      strong: "Ideas into Products",  text: "Apps · Demos · Systems · Experiences" },
  ];

  return (
    <section className="hero-section" id="home" ref={heroRef}>
      <div className="hero-center">
        <motion.p className="hero-kicker"
          initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.1 }}>
          Digital Workplace Technology Head @ Tata Consultancy Services · Author · Builder
        </motion.p>

        <motion.h1 className="hero-title"
          initial="hidden" animate="show"
          variants={{ hidden: {}, show: { transition: { staggerChildren: 0.18, delayChildren: 0.2 } } }}
        >
          {titleWords.map((word, i) => (
            <React.Fragment key={word}>
              <motion.span className="title-word"
                variants={{
                  hidden: { opacity: 0, y: 42, filter: "blur(8px)" },
                  show:   { opacity: 1, y: 0,  filter: "blur(0px)", transition: { duration: 0.9, ease } },
                }}
              >{word}</motion.span>
              {i === 0 && <br />}
            </React.Fragment>
          ))}
        </motion.h1>

        <motion.p className="hero-text"
          initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.6 }}>
          Writing stories, building workplaces of the future, and turning ideas into
          products, demos, books, and experiences.
        </motion.p>

        <motion.div className="hero-actions"
          initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.75 }}>
          <motion.a href="#books" className="btn btn-primary"
            whileHover={{ y: -2, scale: 1.02 }} whileTap={{ scale: 0.98 }}
            transition={{ type: "spring", stiffness: 320, damping: 22 }}>
            Explore My Books
          </motion.a>
          <motion.a href="#apps" className="btn btn-secondary"
            whileHover={{ y: -2, scale: 1.02 }} whileTap={{ scale: 0.98 }}
            transition={{ type: "spring", stiffness: 320, damping: 22 }}>
            See What I Build
          </motion.a>
        </motion.div>

        <motion.div className="hero-focus-row"
          initial="hidden" animate="show"
          variants={{ hidden: {}, show: { transition: { staggerChildren: 0.12, delayChildren: 0.9 } } }}>
          {focusCards.map((card, i) => (
            <motion.div key={i} className={"hero-focus-card" + (card.center ? " center" : "")}
              variants={{
                hidden: { opacity: 0, y: 24 },
                show:   { opacity: 1, y: 0, transition: { duration: 0.7, ease } },
              }}
              whileHover={{ y: -4, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <span className="eyebrow">{card.eyebrow}</span>
              <strong>{card.strong}</strong>
              <p>{card.text}</p>
            </motion.div>
          ))}
        </motion.div>

        <motion.div className="hero-stage"
          initial={{ opacity: 0, y: 32 }} animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 1.1, ease }}
        >
          <div className="hero-stage-glow" />
          <div className="hero-light-sweep" />
          <motion.img src={saravMain} alt="" className="hero-portrait"
            style={{ scale: portraitScale, y: portraitY, opacity: portraitOpacity }} />
        </motion.div>

        <div className="sign-shell">
          <div className="signature-track">
            <motion.div className="sign-png-wrap" style={{ clipPath: sigClipPath, WebkitClipPath: sigClipPath }}>
              <img src={saravSignWhite} alt="Sarav signature" />
            </motion.div>
            <motion.span className="signature-tip" style={{ left: sigTipLeft, opacity: sigTipOpacity }} />
            <motion.span className="signature-glow-line" style={{ opacity: sigGlowOpacity, scaleX: sigGlowScaleX }} />
          </div>
        </div>
      </div>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// Journey — sticky scroll-pinned
// ──────────────────────────────────────────────────────────────

function Journey() {
  const steps = journeyCards.length;
  const wrapRef = useRef(null);
  const [activeIndex, setActiveIndex] = useState(0);

  const { scrollYProgress } = useScroll({
    target: wrapRef,
    offset: ["start start", "end end"],
  });
  const smoothProgress = useSpring(scrollYProgress, { stiffness: 80, damping: 22, mass: 0.4 });

  useMotionValueEvent(scrollYProgress, "change", (p) => {
    const idx = Math.min(steps - 1, Math.max(0, Math.floor(p * steps)));
    setActiveIndex(prev => (prev === idx ? prev : idx));
  });

  return (
    <section className="section" id="journey" style={{ paddingTop: 88, paddingBottom: 0 }}>
      <p className="section-kicker center-copy">Career Journey</p>
      <SectionTitle text="Built across roles." />
      <p className="section-text center-copy journey-intro">
        The journey kept expanding — role by role, country by country, story by story.
      </p>

      <div className="journey-sticky-wrap" ref={wrapRef} style={{ "--journey-steps": steps }}>
        <div className="journey-sticky-stage">
          <div className="journey-step-rail">
            <div className="journey-rail-track" />
            <motion.div className="journey-rail-progress"
              style={{ scaleY: smoothProgress, height: "100%" }} />

            {journeyCards.map((job, i) => (
              <div key={job.title}
                className={"journey-step" + (i <= activeIndex ? " active" : "")}
                onClick={() => {
                  const wrap = wrapRef.current;
                  if (!wrap) return;
                  const target = wrap.offsetTop + (i / steps) * wrap.offsetHeight + window.innerHeight * 0.1;
                  window.scrollTo({ top: target, behavior: "smooth" });
                }}
              >
                <span className="journey-step-node" />
                <span className="journey-step-year">{job.year}</span>
                <span className="journey-step-label">{job.title}</span>
              </div>
            ))}
          </div>

          <div className="journey-card-stack">
            <AnimatePresence mode="wait">
              <motion.div key={activeIndex} className="journey-card-slide"
                initial={{ opacity: 0, x: 60, scale: 0.96 }}
                animate={{ opacity: 1, x: 0, scale: 1 }}
                exit={{ opacity: 0, x: -60, scale: 0.96 }}
                transition={{ duration: 0.6, ease }}
              >
                <div className="journey-media">
                  <motion.img src={journeyCards[activeIndex].image} alt=""
                    initial={{ scale: 1.08 }} animate={{ scale: 1 }}
                    transition={{ duration: 1.2, ease }} loading="lazy" />
                </div>
                <div className="journey-copy">
                  <span className="journey-year">{journeyCards[activeIndex].year}</span>
                  <h3>{journeyCards[activeIndex].title}</h3>
                  <p>{journeyCards[activeIndex].text}</p>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// About + Work
// ──────────────────────────────────────────────────────────────

function About() {
  return (
    <section className="section section-narrow" id="about">
      <div className="center-copy">
        <motion.p className="section-kicker"
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.6 }}
        >About</motion.p>
        <SectionTitle text="Strategy by profession. Storytelling by instinct. Systems by design." />
        <motion.p className="section-text"
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          I work at the intersection of enterprise transformation, AI-led workplace
          thinking, and personal creative expression. Some ideas become demos. Some
          become products. Some become books that stay with people.
        </motion.p>
      </div>
    </section>
  );
}

function Work() {
  return (
    <section className="section" id="work">
      <motion.p className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >What I Do</motion.p>
      <SectionTitle text="Three worlds. One voice." />

      <motion.div className="card-grid three"
        initial="hidden" whileInView="show"
        viewport={{ once: true, amount: 0.2 }}
        variants={{ hidden: {}, show: { transition: { staggerChildren: 0.12 } } }}
      >
        {workCards.map((item) => (
          <motion.article key={item.title} className="glass-card"
            variants={{
              hidden: { opacity: 0, y: 32 },
              show:   { opacity: 1, y: 0, transition: { duration: 0.75, ease } },
            }}
            whileHover={{ y: -6, transition: { type: "spring", stiffness: 300, damping: 22 } }}
          >
            <div className="card-accent" />
            <h3>{item.title}</h3>
            <p>{item.text}</p>
          </motion.article>
        ))}
      </motion.div>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// Builder
// ──────────────────────────────────────────────────────────────

function Builder() {
  const sectionRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start end", "end start"],
  });

  const bgY = useTransform(scrollYProgress, [0, 1], ["8%", "-12%"]);
  const trioY = useSpring(useTransform(scrollYProgress, [0, 1], [60, -60]), { stiffness: 60, damping: 18 });
  const ideaY = useSpring(useTransform(scrollYProgress, [0, 1], [40, -40]), { stiffness: 60, damping: 18 });
  const buildY = useSpring(useTransform(scrollYProgress, [0, 1], [80, -80]), { stiffness: 60, damping: 18 });

  return (
    <section className="section" id="apps" ref={sectionRef}>
      <motion.p className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >Builder of Ideas</motion.p>
      <SectionTitle text="Ideas that did not stay in notes." />
      <motion.p className="section-text center-copy builder-intro"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.4 }}
        transition={{ duration: 0.8 }}
      >
        Actively vibe-coded with Vidhya using ChatGPT and Claude — turning ideas into
        visible, usable experiences.
      </motion.p>

      <div className="builder-hero">
        <motion.img src={controlRoomBg} alt="" className="builder-bg"
          style={{ y: bgY }} loading="lazy" />
        <div className="builder-overlay">
          <motion.div className="builder-panel" style={{ y: trioY }}
            whileHover={{ scale: 1.02, rotate: -1, transition: { type: "spring", stiffness: 300, damping: 22 } }}
          >
            <img src={appTrio} alt="App trio" loading="lazy" />
          </motion.div>

          <div className="builder-side-stack">
            <motion.div className="mini-panel" style={{ y: ideaY }}
              whileHover={{ scale: 1.04, rotate: 1, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <img src={ideaShipped} alt="Idea shipped" loading="lazy" />
            </motion.div>
            <motion.div className="mini-panel" style={{ y: buildY }}
              whileHover={{ scale: 1.04, rotate: -1, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <img src={androidBuildSuccess} alt="Android build success" loading="lazy" />
            </motion.div>
          </div>
        </div>
      </div>

      <motion.div className="card-grid three app-grid"
        initial="hidden" whileInView="show"
        viewport={{ once: true, amount: 0.2 }}
        variants={{ hidden: {}, show: { transition: { staggerChildren: 0.12 } } }}
      >
        {appCards.map((app) => (
          <motion.article key={app.title} className="glass-card app-card"
            variants={{
              hidden: { opacity: 0, y: 32 },
              show:   { opacity: 1, y: 0, transition: { duration: 0.7, ease } },
            }}
            whileHover={{ y: -5, transition: { type: "spring", stiffness: 300, damping: 22 } }}
          >
            <div className="app-shot-wrap">
              <img src={app.image} alt={app.title} className="app-shot" loading="lazy" />
            </div>
            <h3 style={{ marginTop: 18 }}>{app.title}</h3>
            <p>{app.subtitle}</p>
          </motion.article>
        ))}
      </motion.div>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// Books — scroll-bound orbit, layoutId morph
// ──────────────────────────────────────────────────────────────

function OrbitCore({ book }) {
  return (
    <div className="orbit-core">
      <img src={coffeeReadsBadge} alt="" className="orbit-core-badge" />
      <span className="orbit-core-text">Now in Focus</span>
      <AnimatePresence mode="wait">
        <motion.strong key={book.id} className="orbit-active-title"
          initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }}
          transition={{ duration: 0.34 }}
        >{book.title}</motion.strong>
      </AnimatePresence>
      <motion.a href={book.amazonUrl} target="_blank" rel="noreferrer" className="orbit-amazon-btn"
        whileHover={{ y: -2, scale: 1.04 }} whileTap={{ scale: 0.97 }}
        transition={{ type: "spring", stiffness: 320, damping: 22 }}
      >{book.isUpcoming ? "Author page" : "View on Amazon"}</motion.a>
    </div>
  );
}

function OrbitItem({ book, angle, orbitRotation, isActive, onClick }) {
  const RADIUS = 270;
  const x = useTransform(orbitRotation, (r) => Math.sin((r + angle) * Math.PI / 180) * RADIUS);
  const y = useTransform(orbitRotation, (r) => -Math.cos((r + angle) * Math.PI / 180) * RADIUS);

  return (
    <motion.div className="orbit-item-pos" style={{ x, y }}>
      <div
        className={
          "orbit-item-inner"
          + (isActive ? " is-active" : "")
          + (book.isUpcoming ? " upcoming-badge" : "")
        }
        onClick={onClick}
      >
        <motion.img
          layoutId={`book-cover-${book.id}`}
          src={book.cover} alt={book.title}
          loading="lazy" decoding="async"
        />
      </div>
    </motion.div>
  );
}

function BookCard({ book, onSelect }) {
  return (
    <motion.article className="book-card"
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: 0.6, ease }}
      whileHover={{ y: -6, scale: 1.025, transition: { type: "spring", stiffness: 320, damping: 22 } }}
      onClick={() => onSelect(book)}
    >
      {book.isUpcoming && <span className="book-upcoming-badge">Coming soon</span>}
      <div className="book-cover-wrap">
        <motion.img layoutId={`book-cover-${book.id}`}
          src={book.cover} alt={book.title} className="book-cover"
          loading="lazy" decoding="async" />
      </div>
      <div className="book-meta">
        <h3>{book.title}</h3>
        <span>Sarav</span>
      </div>
      <div className="book-actions">
        <motion.a href={book.amazonUrl} className="book-amazon-btn"
          target="_blank" rel="noreferrer"
          onClick={(e) => e.stopPropagation()}
          whileHover={{ scale: 1.03 }} whileTap={{ scale: 0.97 }}
        >{book.isUpcoming ? "Author page" : "View on Amazon"}</motion.a>
      </div>
    </motion.article>
  );
}

function BookDetail({ book, onClose }) {
  useEffect(() => {
    const onKey = (e) => { if (e.key === "Escape") onClose(); };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <motion.div className="book-detail-backdrop"
      initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
      transition={{ duration: 0.3 }} onClick={onClose}
    >
      <motion.div className="book-detail-panel"
        initial={{ y: 30 }} animate={{ y: 0 }} exit={{ y: 30 }}
        transition={{ duration: 0.4, ease }}
        onClick={(e) => e.stopPropagation()}
      >
        <motion.img layoutId={`book-cover-${book.id}`}
          src={book.cover} alt={book.title} className="book-detail-cover" />
        <div className="book-detail-copy">
          <h2>{book.title}</h2>
          <div className="by">by Sarav · {book.isUpcoming ? "Coming soon" : "Available now"}</div>
          <p>
            {book.isUpcoming
              ? "This title isn't on Amazon yet — it's on the way. In the meantime, you can browse the full author shelf and follow for updates."
              : "Open the book on Amazon to read the full description, browse a sample, or pick up a copy in paperback or Kindle."}
          </p>
          <motion.a href={book.amazonUrl} className="orbit-amazon-btn"
            target="_blank" rel="noreferrer"
            style={{ marginTop: 22, display: "inline-flex" }}
            whileHover={{ y: -2, scale: 1.03 }} whileTap={{ scale: 0.97 }}
            transition={{ type: "spring", stiffness: 320, damping: 22 }}
          >{book.isUpcoming ? "Visit Author Page" : "View on Amazon"}</motion.a>
        </div>
        <button className="book-detail-close" onClick={onClose} aria-label="Close">✕</button>
      </motion.div>
    </motion.div>
  );
}

function MobileBooks({ activeBook }) {
  return (
    <div style={{ marginTop: 28 }}>
      <motion.div className="glass-card" style={{ padding: "22px 18px", textAlign: "center" }}
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.7, ease }}
      >
        <img src={coffeeReadsBadge} alt="" style={{ width: 80, margin: "0 auto 12px" }} />
        <span className="orbit-core-text">Featured Book</span>
        <strong style={{ display: "block", marginTop: 8, fontSize: "1.18rem", lineHeight: 1.45 }}>
          {activeBook.title}
        </strong>
        <motion.a href={activeBook.amazonUrl} target="_blank" rel="noreferrer"
          className="orbit-amazon-btn"
          style={{ marginTop: 12, display: "inline-block" }}
          whileHover={{ y: -2 }} whileTap={{ scale: 0.97 }}
        >{activeBook.isUpcoming ? "Author page" : "View on Amazon"}</motion.a>
      </motion.div>
    </div>
  );
}

function Books() {
  const orbitRef = useRef(null);
  const [activeOrbitIndex, setActiveOrbitIndex] = useState(0);
  const [selectedBook, setSelectedBook] = useState(null);
  const [isCompact, setIsCompact] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia("(max-width: 1100px)");
    const update = () => setIsCompact(mq.matches);
    update();
    if (mq.addEventListener) {
      mq.addEventListener("change", update);
      return () => mq.removeEventListener("change", update);
    }
    mq.addListener(update);
    return () => mq.removeListener(update);
  }, []);

  const { scrollYProgress } = useScroll({
    target: orbitRef,
    offset: ["start end", "end start"],
  });

  const rotation = useSpring(useTransform(scrollYProgress, [0, 1], [0, 540]), {
    stiffness: 50, damping: 18, mass: 0.6,
  });

  useMotionValueEvent(rotation, "change", (r) => {
    const step = 360 / orbitBooks.length;
    const normalized = ((r % 360) + 360) % 360;
    const idx = Math.round(normalized / step) % orbitBooks.length;
    setActiveOrbitIndex(prev => (prev === idx ? prev : idx));
  });

  const activeBook = orbitBooks[activeOrbitIndex] ?? orbitBooks[0];

  return (
    <section className="section books-section" id="books" ref={orbitRef}>
      <p className="section-kicker center-copy">Books</p>
      <SectionTitle text="A circle of stories that keeps growing." />
      <p className="section-text center-copy books-intro">
        Scroll the page and the orbit turns. Click any cover to open the story.
      </p>

      {!isCompact ? (
        <div className="orbit-books-wrap">
          <div className="book-orbit">
            <OrbitCore book={activeBook} />
            {orbitBooks.map((book, index) => {
              const angle = (360 / orbitBooks.length) * index;
              return (
                <OrbitItem key={book.id} book={book} angle={angle}
                  orbitRotation={rotation}
                  isActive={index === activeOrbitIndex}
                  onClick={() => setSelectedBook(book)}
                />
              );
            })}
          </div>
        </div>
      ) : (
        <MobileBooks activeBook={activeBook} />
      )}

      <div className="books-grid">
        {books.map((book) => (
          <BookCard key={book.id} book={book} onSelect={setSelectedBook} />
        ))}
      </div>

      <AnimatePresence>
        {selectedBook && (
          <BookDetail book={selectedBook} onClose={() => setSelectedBook(null)} />
        )}
      </AnimatePresence>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// Swastikastra — Kids Fantasy Book Series
// ──────────────────────────────────────────────────────────────

const swastikastraBooks = [
  { id: 1, title: "Book One", subtitle: "The Golden Ripe Mango", badge: "Available Now", cover: "/swastikastra/art/book-1-the-golden-ripe-mango.png" },
  { id: 2, title: "Book Two", subtitle: "The Hidden Ember", badge: "Coming Soon", cover: "/swastikastra/art/book-2-the-hidden-ember.png" },
  { id: 3, title: "Book Three", subtitle: "The Hidden Well", badge: "Coming Soon", cover: "/swastikastra/art/book-3-the-hidden-well.png" },
  { id: 4, title: "Book Four", subtitle: "The Banyan's Secret", badge: "Coming Soon", cover: "/swastikastra/art/book-4-the-banyans-secret.png" },
  { id: 5, title: "Book Five", subtitle: "The Red Moon", badge: "Coming Soon", cover: "/swastikastra/art/book-5-the-red-moon.png" },
];

function Swastikastra() {
  return (
    <section className="section swastikastra-section" id="swastikastra">
      <motion.p className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >Kids Fantasy Book Series</motion.p>
      <SectionTitle text="Swastikastra: A Five-Book Mythological Epic" />
      <motion.p className="section-text center-copy swastikastra-intro"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.4 }}
        transition={{ duration: 0.8, delay: 0.2 }}
      >
        Ten elements. One destiny. A grand Tamil mythological fantasy saga by Saravanakumar Murugan —
        follow young Balan, Sengodan, and Yazhini through ancient Gurukula houses, elemental Astras,
        and legendary vahanams.
      </motion.p>

      <motion.div className="glass-card swastikastra-card"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.2 }}
        transition={{ duration: 0.85, ease }}
      >
        <div className="swastikastra-hero-grid">
          <div className="swastikastra-banner-wrap">
            <img
              src="/swastikastra/art/series-five-books.png"
              alt="Swastikastra: The Five-Book Series"
              className="swastikastra-banner-img"
              loading="lazy"
            />
            <div className="swastikastra-glow" />
          </div>
          <div className="swastikastra-lead-copy">
            <span className="swastikastra-pill">Epic Fantasy Universe</span>
            <h3>Begin the Journey with Book One: The Golden Ripe Mango</h3>
            <p>
              When an ancient mystery awakens in the sacred hills, three young initiates are summoned
              to uncover the lost knowledge of the Astras. What begins at the Gurukula becomes an unforgettable
              five-book adventure across mythic Tamil history and magical realms.
            </p>
            <div className="swastikastra-tags">
              <span>✦ 10 Elemental Astras</span>
              <span>✦ 3 Gurukula Houses</span>
              <span>✦ Mythological Fantasy</span>
            </div>
            <div className="swastikastra-cta-group">
              <motion.a
                href="/swastikastra/"
                className="btn btn-primary"
                whileHover={{ y: -2, scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                transition={{ type: "spring", stiffness: 320, damping: 22 }}
              >
                Enter Swastikastra Universe →
              </motion.a>
              <motion.a
                href="/swastikastra/#books"
                className="btn btn-secondary"
                whileHover={{ y: -2, scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                transition={{ type: "spring", stiffness: 320, damping: 22 }}
              >
                Explore the 5 Books
              </motion.a>
            </div>
          </div>
        </div>

        <div className="swastikastra-shelf">
          <div className="swastikastra-shelf-title">
            <span className="eyebrow">The Five Books</span>
            <h4>The Complete Series Timeline</h4>
          </div>
          <div className="swastikastra-books-row">
            {swastikastraBooks.map((b) => (
              <a key={b.id} href={`/swastikastra/#book-${b.id}`} className="swastikastra-book-tile">
                <div className="swastikastra-tile-cover">
                  <img src={b.cover} alt={`${b.title}: ${b.subtitle}`} loading="lazy" />
                  <span className={`swastikastra-tile-badge ${b.id === 1 ? 'live' : 'soon'}`}>
                    {b.badge}
                  </span>
                </div>
                <div className="swastikastra-tile-meta">
                  <span className="tile-vol">{b.title}</span>
                  <strong className="tile-sub">{b.subtitle}</strong>
                </div>
              </a>
            ))}
          </div>
        </div>
      </motion.div>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// Writing
// ──────────────────────────────────────────────────────────────

function WritingFloat({ className, src, mouseX, mouseY, depthX, depthY }) {
  const x = useTransform(mouseX, (v) => v * depthX);
  const y = useTransform(mouseY, (v) => v * depthY);
  return (
    <motion.div className={className} style={{ x, y }}>
      <img src={src} alt="" loading="lazy" />
    </motion.div>
  );
}

function Writing({ mouseX, mouseY }) {
  return (
    <section className="section writing-section" id="writing">
      <motion.p className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >Writing Universe</motion.p>
      <SectionTitle text="Letters, coffee, moonlight, and quiet rooms." />

      <motion.div className="writing-scene"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.2 }}
        transition={{ duration: 0.9, ease }}
      >
        <img src={writersDeskBg} alt="" className="writing-scene-bg" loading="lazy" />
      </motion.div>

      <div className="writing-split-stage">
        <div className="writing-split">
          <motion.article className="glass-card balcony-card"
            initial={{ opacity: 0, x: -32 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.8, ease }}
          >
            <img src={moonlitBalconyWriting} alt="" loading="lazy" />
          </motion.article>

          <motion.article className="glass-card writing-copy-card"
            initial={{ opacity: 0, x: 32 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.8, ease }}
          >
            <span className="eyebrow">Some stories</span>
            <span className="typing-line">Welcome to the romance-o-sphere.</span>
            <h3 style={{ marginTop: 8 }}>Some arrive with letters. Some arrive with silence.</h3>
            <p>
              The writing side of this world is built on memory, longing, family,
              reflection, old letters, late evenings, and the small emotional moments
              that quietly become stories.
            </p>
            <p>Coffee Reads. Romance. Quiet healing. Night skies. New beginnings.</p>
          </motion.article>
        </div>

        <WritingFloat className="writing-float balcony-letters"    src={lettersBundle}        mouseX={mouseX} mouseY={mouseY} depthX={20} depthY={14} />
        <WritingFloat className="writing-float balcony-typewriter" src={typewriter}           mouseX={mouseX} mouseY={mouseY} depthX={28} depthY={18} />
        <WritingFloat className="writing-float balcony-diary"      src={diaryPen}             mouseX={mouseX} mouseY={mouseY} depthX={22} depthY={16} />
        <WritingFloat className="writing-float balcony-coffee"     src={coffeeCup}            mouseX={mouseX} mouseY={mouseY} depthX={18} depthY={12} />
        <WritingFloat className="writing-float balcony-moon"       src={moonCrescent}         mouseX={mouseX} mouseY={mouseY} depthX={10} depthY={8} />
      </div>

      <motion.div className="glass-card blogs-shell"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.15 }}
        transition={{ duration: 0.9, ease }}
      >
        <div className="blog-section-head">
          <span className="eyebrow">From the archives</span>
          <h3>Two blogs. Two voices. One long journey.</h3>
          <p>
            One holds the romance, poetry, and emotional reflections. The other holds
            the systems, work, leadership, and digital thinking.
          </p>
        </div>

        <div className="blog-blocks">
          {[
            { img: blogFewMiles, badge: "A romantic journey", h3: "Few Miles", p: "Poems, reflections, love-soaked memories, and the quieter emotional universe behind many of the stories.", href: "https://pendownmythought.blogspot.com/" },
            { img: blogSaravsWorld, badge: "Thoughts on work and writing", h3: "Sarav's World", p: "Reflections on AI, leadership, digital workplace thinking, books, and the systems side of this journey.", href: "https://saravsworld.wordpress.com/" },
          ].map((blog, i) => (
            <motion.article key={i} className="blog-visual-card"
              whileHover={{ y: -6, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <div className="blog-visual-wrap">
                <motion.img src={blog.img} alt="" className="blog-shot" loading="lazy"
                  whileHover={{ scale: 1.05, transition: { duration: 0.4 } }} />
                <div className="blog-visual-overlay" />
                <div className="blog-badge">{blog.badge}</div>
              </div>
              <div className="blog-card-copy">
                <span className="eyebrow">Blog</span>
                <h3>{blog.h3}</h3>
                <p>{blog.p}</p>
                <div className="blog-cta-row">
                  <motion.a href={blog.href} target="_blank" rel="noreferrer"
                    className="blog-cta-btn"
                    whileHover={{ y: -2, scale: 1.04 }} whileTap={{ scale: 0.97 }}
                    transition={{ type: "spring", stiffness: 320, damping: 22 }}
                  >Visit {blog.h3}</motion.a>
                </div>
              </div>
            </motion.article>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

// ──────────────────────────────────────────────────────────────
// Contact + Footer
// ──────────────────────────────────────────────────────────────

function Contact() {
  return (
    <section className="section section-narrow contact-section" id="contact">
      <motion.div className="glass-card contact-card"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.9, ease }}
      >
        <div className="thanks-icon-wrap">
          <motion.span className="thanks-icon"
            animate={{ scale: [1, 1.12, 1], rotate: [0, -4, 0] }}
            transition={{ duration: 2.6, repeat: Infinity, ease: "easeInOut" }}
          >🙏</motion.span>
        </div>
        <p className="section-kicker">Thank You</p>
        <SectionTitle text="Thank you for visiting Sarav's World." className="section-title" />
        <p className="section-text">
          I hope something here stayed with you — a book, a thought, a memory, or an
          idea. If a story spoke to you, I would be grateful for a note or a reflection.
          Thank you for reading, and for being part of this journey.
        </p>
        <div className="contact-links">
          <a href="mailto:sarav@iamsaravofficial.com">sarav@iamsaravofficial.com</a>
          <span>Chennai, India</span>
        </div>
      </motion.div>
    </section>
  );
}

function Footer() {
  return (
    <motion.footer className="site-footer"
      initial={{ opacity: 0 }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: 0.8 }}
    >
      <div className="site-footer-inner">
        <div className="site-footer-top">
          <div className="footer-left">
            <h3>Sarav's World</h3>
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
          <span className="copyright-line">
            Copyright © 2009-{new Date().getFullYear()} · Sarav
          </span>
          <div className="footer-links">
            <a href="/copyright/">Copyright</a>
            <a href="/privacy-policy/">Privacy</a>
            <a href="/terms/">Terms</a>
            <a href="#contact">Feedback</a>
            <motion.a href="#home" className="back-to-top"
              whileHover={{ y: -2 }}
              transition={{ type: "spring", stiffness: 320, damping: 22 }}
            >Back to top ↑</motion.a>
          </div>
        </div>
      </div>
    </motion.footer>
  );
}

// ──────────────────────────────────────────────────────────────
// Ambient cursor-following orbs (cheap, lovely)
// ──────────────────────────────────────────────────────────────

function AmbientOrbs({ mouseX, mouseY }) {
  return (
    <>
      <motion.div className="orb orb-violet" style={{
        x: useTransform(mouseX, (v) => v * 1.4),
        y: useTransform(mouseY, (v) => v * 1.0),
      }} />
      <motion.div className="orb orb-teal" style={{
        x: useTransform(mouseX, (v) => v * -1.2),
        y: useTransform(mouseY, (v) => v * 0.9),
      }} />
      <motion.div className="orb orb-blue" style={{
        x: useTransform(mouseX, (v) => v * 0.9),
        y: useTransform(mouseY, (v) => v * -1.1),
      }} />
    </>
  );
}

// ──────────────────────────────────────────────────────────────
// App root
// ──────────────────────────────────────────────────────────────

export default function App() {
  const reduced = useReducedMotion();

  // Single source of truth for mouse parallax — no setState on every move.
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  const smoothX = useSpring(mouseX, { stiffness: 60, damping: 22, mass: 0.5 });
  const smoothY = useSpring(mouseY, { stiffness: 60, damping: 22, mass: 0.5 });

  useEffect(() => {
    if (reduced) return;
    const onMove = (e) => {
      mouseX.set((e.clientX / window.innerWidth - 0.5) * 36);
      mouseY.set((e.clientY / window.innerHeight - 0.5) * 28);
    };
    window.addEventListener("mousemove", onMove, { passive: true });
    return () => window.removeEventListener("mousemove", onMove);
  }, [reduced, mouseX, mouseY]);

  return (
    <MotionConfig
      reducedMotion={reduced ? "always" : "never"}
      transition={{ type: "spring", stiffness: 260, damping: 22 }}
    >
      <div className="site-shell">
        <ScrollProgress />
        <AmbientOrbs mouseX={smoothX} mouseY={smoothY} />
        <Header />

        <main id="home">
          <Hero />
          <About />
          <Work />
          <Journey />
          <Builder />
          <Books />
          <Swastikastra />
          <Writing mouseX={smoothX} mouseY={smoothY} />
          <Contact />
        </main>

        <Footer />
      </div>
    </MotionConfig>
  );
}
