// Hero — scroll-drawn signature, parallax portrait, word-by-word title

function Hero() {
  const { motion, useScroll, useTransform, useSpring, useMotionTemplate } = window.fm;
  const heroRef = React.useRef(null);

  const { scrollYProgress } = useScroll({
    target: heroRef,
    offset: ["start start", "end start"],
  });

  // Portrait pulls back & drifts up as the user scrolls past hero. Tier 3 #9.
  const portraitScale = useTransform(scrollYProgress, [0, 1], [1.04, 0.88]);
  const portraitY = useTransform(scrollYProgress, [0, 1], [0, -60]);
  const portraitOpacity = useTransform(scrollYProgress, [0, 0.85], [1, 0.35]);

  // Signature reveal — scroll-driven clip-path on the PNG signature. Tier 2 #6.
  // 0 → 1 maps to clip-path inset(0 100% 0 0) → inset(0 0 0 0). User literally draws it by scrolling.
  // Bound to first 60% of hero scroll so it completes well before exit.
  const sigProgress = useSpring(useTransform(scrollYProgress, [0, 0.55], [0, 1]), {
    stiffness: 90, damping: 22, mass: 0.6,
  });
  const sigInsetRight = useTransform(sigProgress, p => `${(1 - p) * 100}%`);
  const sigClipPath = useMotionTemplate`inset(0 ${sigInsetRight} 0 0)`;

  // The tracing dot rides along the right edge of the revealed portion.
  const sigTipLeft = useTransform(sigProgress, p => `${4 + p * 88}%`);
  const sigTipOpacity = useTransform(sigProgress, [0, 0.05, 0.92, 1], [0, 1, 1, 0]);

  // Glow line under signature reveals after the strokes complete.
  const sigGlowOpacity = useTransform(sigProgress, [0.6, 1], [0, 0.8]);
  const sigGlowScaleX = useTransform(sigProgress, [0.6, 1], [0.4, 1]);

  const titleWords = ["SARAVANAKUMAR", "MURUGAN"];

  return (
    <section className="hero-section" id="home" ref={heroRef}>
      <div className="hero-center">
        <motion.p
          className="hero-kicker"
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.1 }}
        >
          Digital Workplace Technology Head @ Tata Consultancy Services · Author · Builder
        </motion.p>

        {/* Word-by-word title reveal — Tier 3 #10 */}
        <motion.h1
          className="hero-title"
          initial="hidden"
          animate="show"
          variants={{
            hidden: {},
            show: { transition: { staggerChildren: 0.18, delayChildren: 0.2 } },
          }}
        >
          {titleWords.map((word, i) => (
            <React.Fragment key={word}>
              <motion.span
                className="title-word"
                variants={{
                  hidden: { opacity: 0, y: 42, filter: "blur(8px)" },
                  show: {
                    opacity: 1, y: 0, filter: "blur(0px)",
                    transition: { duration: 0.9, ease: [0.16, 1, 0.3, 1] },
                  },
                }}
              >
                {word}
              </motion.span>
              {i === 0 && <br />}
            </React.Fragment>
          ))}
        </motion.h1>

        <motion.p
          className="hero-text"
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          Writing stories, building workplaces of the future, and turning ideas into
          products, demos, books, and experiences.
        </motion.p>

        <motion.div
          className="hero-actions"
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.75 }}
        >
          <motion.a
            href="#books" className="btn btn-primary"
            whileHover={{ y: -2, scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            transition={{ type: "spring", stiffness: 320, damping: 22 }}
          >
            Explore My Books
          </motion.a>
          <motion.a
            href="#apps" className="btn btn-secondary"
            whileHover={{ y: -2, scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            transition={{ type: "spring", stiffness: 320, damping: 22 }}
          >
            See What I Build
          </motion.a>
        </motion.div>

        <motion.div
          className="hero-focus-row"
          initial="hidden"
          animate="show"
          variants={{
            hidden: {},
            show: { transition: { staggerChildren: 0.12, delayChildren: 0.9 } },
          }}
        >
          {[
            { eyebrow: "Current Focus", strong: "Future of Work", text: "GenAI · Digital Workplace · Storytelling" },
            { eyebrow: "Creative Universe", strong: "17 Books & Growing", text: "Romance · Reflection · Family · Leadership", center: true },
            { eyebrow: "Builder Side", strong: "Ideas into Products", text: "Apps · Demos · Systems · Experiences" },
          ].map((card, i) => (
            <motion.div
              key={i}
              className={"hero-focus-card" + (card.center ? " center" : "")}
              variants={{
                hidden: { opacity: 0, y: 24 },
                show: { opacity: 1, y: 0, transition: { duration: 0.7, ease: [0.16, 1, 0.3, 1] } },
              }}
              whileHover={{ y: -4, transition: { type: "spring", stiffness: 300, damping: 22 } }}
            >
              <span className="eyebrow">{card.eyebrow}</span>
              <strong>{card.strong}</strong>
              <p>{card.text}</p>
            </motion.div>
          ))}
        </motion.div>

        {/* Hero stage with scroll-bound portrait */}
        <motion.div
          className="hero-stage"
          initial={{ opacity: 0, y: 32 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 1.1, ease: [0.16, 1, 0.3, 1] }}
        >
          <div className="hero-stage-glow" />
          <div className="hero-light-sweep" />
          <motion.img
            src={window.IMG.saravMain}
            alt=""
            className="hero-portrait"
            style={{ scale: portraitScale, y: portraitY, opacity: portraitOpacity }}
          />
        </motion.div>

        {/* Scroll-drawn signature */}
        <div className="sign-shell">
          <div className="signature-track">
            <motion.div className="sign-png-wrap" style={{ clipPath: sigClipPath, WebkitClipPath: sigClipPath }}>
              <img src={window.IMG.saravSignWhite} alt="Sarav signature" />
            </motion.div>
            <motion.span className="signature-tip" style={{ left: sigTipLeft, opacity: sigTipOpacity }} />
            <motion.span
              className="signature-glow-line"
              style={{ opacity: sigGlowOpacity, scaleX: sigGlowScaleX }}
            />
          </div>
        </div>
      </div>
    </section>
  );
}

window.Hero = Hero;
