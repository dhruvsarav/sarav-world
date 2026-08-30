// Shared SectionTitle + remaining sections (About, Work, Builder, Writing, Contact, Footer)

// Word-by-word reveal title used across the page.
function SectionTitle({ text, className = "section-title center-copy" }) {
  const { motion } = window.fm;
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
            show: {
              opacity: 1, y: 0, filter: "blur(0px)",
              transition: { duration: 0.75, ease: [0.16, 1, 0.3, 1] },
            },
          }}
        >
          {w}
        </motion.span>
      ))}
    </motion.h2>
  );
}

// ───────────── About ─────────────
function About() {
  const { motion } = window.fm;
  return (
    <section className="section section-narrow" id="about">
      <div className="center-copy">
        <motion.p
          className="section-kicker"
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.6 }}
        >
          About
        </motion.p>
        <SectionTitle text="Strategy by profession. Storytelling by instinct. Systems by design." />
        <motion.p
          className="section-text"
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

// ───────────── What I Do ─────────────
function Work() {
  const { motion } = window.fm;
  return (
    <section className="section" id="work">
      <motion.p
        className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >
        What I Do
      </motion.p>
      <SectionTitle text="Three worlds. One voice." />

      <motion.div
        className="card-grid three"
        initial="hidden"
        whileInView="show"
        viewport={{ once: true, amount: 0.2 }}
        variants={{ hidden: {}, show: { transition: { staggerChildren: 0.12 } } }}
      >
        {window.WORK_CARDS.map((item) => (
          <motion.article
            key={item.title}
            className="glass-card"
            variants={{
              hidden: { opacity: 0, y: 32 },
              show: { opacity: 1, y: 0, transition: { duration: 0.75, ease: [0.16, 1, 0.3, 1] } },
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

// ───────────── Builder ─────────────
function Builder() {
  const { motion, useScroll, useTransform, useSpring } = window.fm;
  const sectionRef = React.useRef(null);

  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start end", "end start"],
  });

  // Background drifts upward across the section.
  const bgY = useTransform(scrollYProgress, [0, 1], ["8%", "-12%"]);

  // Floating panels: gentle scroll-bound parallax.
  const trioY = useSpring(useTransform(scrollYProgress, [0, 1], [60, -60]), { stiffness: 60, damping: 18 });
  const ideaY = useSpring(useTransform(scrollYProgress, [0, 1], [40, -40]), { stiffness: 60, damping: 18 });
  const buildY = useSpring(useTransform(scrollYProgress, [0, 1], [80, -80]), { stiffness: 60, damping: 18 });

  return (
    <section className="section" id="apps" ref={sectionRef}>
      <motion.p
        className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >
        Builder of Ideas
      </motion.p>
      <SectionTitle text="Ideas that did not stay in notes." />
      <motion.p
        className="section-text center-copy builder-intro"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.4 }}
        transition={{ duration: 0.8 }}
      >
        Actively vibe-coded with Vidhya using ChatGPT and Claude — turning ideas into
        visible, usable experiences.
      </motion.p>

      <div className="builder-hero">
        <motion.img
          src={window.IMG.controlRoomBg}
          alt=""
          className="builder-bg"
          style={{ y: bgY }}
          loading="lazy"
        />
        <div className="builder-overlay">
          <motion.div
            className="builder-panel"
            style={{ y: trioY }}
            whileHover={{ scale: 1.02, rotate: -1, transition: { type: "spring", stiffness: 300, damping: 22 } }}
          >
            <img src={window.IMG.appTrio} alt="App trio" loading="lazy" />
          </motion.div>

          <div className="builder-side-stack">
            <motion.div
              className="mini-panel"
              style={{ y: ideaY }}
              whileHover={{ scale: 1.04, rotate: 1, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <img src={window.IMG.ideaShipped} alt="Idea shipped" loading="lazy" />
            </motion.div>
            <motion.div
              className="mini-panel"
              style={{ y: buildY }}
              whileHover={{ scale: 1.04, rotate: -1, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <img src={window.IMG.androidBuildSuccess} alt="Android build success" loading="lazy" />
            </motion.div>
          </div>
        </div>
      </div>

      <motion.div
        className="card-grid three app-grid"
        initial="hidden"
        whileInView="show"
        viewport={{ once: true, amount: 0.2 }}
        variants={{ hidden: {}, show: { transition: { staggerChildren: 0.12 } } }}
      >
        {window.APP_CARDS.map((app) => (
          <motion.article
            key={app.title}
            className="glass-card app-card"
            variants={{
              hidden: { opacity: 0, y: 32 },
              show: { opacity: 1, y: 0, transition: { duration: 0.7, ease: [0.16, 1, 0.3, 1] } },
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

// ───────────── Writing ─────────────
function Writing({ mouseSpring }) {
  const { motion, useTransform } = window.fm;

  // Each float reads from the smoothed mouse springs with its own depth.
  // depth × spring → translate. No setState. No re-renders on mouse move.
  const floatStyle = (depthX, depthY) => ({
    x: useTransform(mouseSpring.x, (v) => v * depthX),
    y: useTransform(mouseSpring.y, (v) => v * depthY),
  });

  return (
    <section className="section writing-section" id="writing">
      <motion.p
        className="section-kicker center-copy"
        initial={{ opacity: 0, y: 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.5 }}
      >
        Writing Universe
      </motion.p>
      <SectionTitle text="Letters, coffee, moonlight, and quiet rooms." />

      <motion.div
        className="writing-scene"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.2 }}
        transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
      >
        <img src={window.IMG.writersDeskBg} alt="" className="writing-scene-bg" loading="lazy" />
      </motion.div>

      <div className="writing-split-stage">
        <div className="writing-split">
          <motion.article
            className="glass-card balcony-card"
            initial={{ opacity: 0, x: -32 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          >
            <img src={window.IMG.moonlitBalconyWriting} alt="" loading="lazy" />
          </motion.article>

          <motion.article
            className="glass-card writing-copy-card"
            initial={{ opacity: 0, x: 32 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
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

        {/* Floating decorations driven by smoothed mouse springs */}
        <motion.div className="writing-float balcony-letters"    style={floatStyle(20, 14)}>
          <img src={window.IMG.lettersBundle} alt="" loading="lazy" />
        </motion.div>
        <motion.div className="writing-float balcony-typewriter" style={floatStyle(28, 18)}>
          <img src={window.IMG.typewriter} alt="" loading="lazy" />
        </motion.div>
        <motion.div className="writing-float balcony-diary"      style={floatStyle(22, 16)}>
          <img src={window.IMG.diaryPen} alt="" loading="lazy" />
        </motion.div>
        <motion.div className="writing-float balcony-coffee"     style={floatStyle(18, 12)}>
          <img src={window.IMG.coffeeCup} alt="" loading="lazy" />
        </motion.div>
        <motion.div className="writing-float balcony-moon"       style={floatStyle(10, 8)}>
          <img src={window.IMG.moonCrescent} alt="" loading="lazy" />
        </motion.div>
      </div>

      <motion.div
        className="glass-card blogs-shell"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.15 }}
        transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
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
            { img: window.IMG.blogFewMiles, badge: "A romantic journey", h3: "Few Miles", p: "Poems, reflections, love-soaked memories, and the quieter emotional universe behind many of the stories.", href: "https://pendownmythought.blogspot.com/" },
            { img: window.IMG.blogSaravsWorld, badge: "Thoughts on work and writing", h3: "Sarav's World", p: "Reflections on AI, leadership, digital workplace thinking, books, and the systems side of this journey.", href: "https://saravsworld.wordpress.com/" },
          ].map((blog, i) => (
            <motion.article
              key={i}
              className="blog-visual-card"
              whileHover={{ y: -6, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <div className="blog-visual-wrap">
                <motion.img
                  src={blog.img} alt="" className="blog-shot" loading="lazy"
                  whileHover={{ scale: 1.05, transition: { duration: 0.4 } }}
                />
                <div className="blog-visual-overlay" />
                <div className="blog-badge">{blog.badge}</div>
              </div>
              <div className="blog-card-copy">
                <span className="eyebrow">Blog</span>
                <h3>{blog.h3}</h3>
                <p>{blog.p}</p>
                <div className="blog-cta-row">
                  <motion.a
                    href={blog.href} target="_blank" rel="noreferrer"
                    className="blog-cta-btn"
                    whileHover={{ y: -2, scale: 1.04 }}
                    whileTap={{ scale: 0.97 }}
                    transition={{ type: "spring", stiffness: 320, damping: 22 }}
                  >
                    Visit {blog.h3}
                  </motion.a>
                </div>
              </div>
            </motion.article>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

// ───────────── Contact ─────────────
function Contact() {
  const { motion } = window.fm;
  return (
    <section className="section section-narrow contact-section" id="contact">
      <motion.div
        className="glass-card contact-card"
        initial={{ opacity: 0, y: 32 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
      >
        <div className="thanks-icon-wrap">
          <motion.span
            className="thanks-icon"
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

// ───────────── Footer ─────────────
function Footer() {
  const { motion } = window.fm;
  return (
    <motion.footer
      className="site-footer"
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
          <span className="copyright-line">Copyright © 2009-{new Date().getFullYear()} · Sarav</span>
          <div className="footer-links">
            <a href="/copyright/">Copyright</a>
            <a href="/privacy-policy/">Privacy</a>
            <a href="/terms/">Terms</a>
            <a href="#contact">Feedback</a>
            <motion.a
              href="#home" className="back-to-top"
              whileHover={{ y: -2 }}
              transition={{ type: "spring", stiffness: 320, damping: 22 }}
            >
              Back to top ↑
            </motion.a>
          </div>
        </div>
      </div>
    </motion.footer>
  );
}

Object.assign(window, { SectionTitle, About, Work, Builder, Writing, Contact, Footer });
