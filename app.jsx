// App — MotionConfig wrapper, header, ambient mouse-following orbs, mount.

function ScrollProgress() {
  const { motion, useScroll, useSpring } = window.fm;
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 24, mass: 0.3 });
  return <motion.div className="scroll-progress" style={{ scaleX }} />;
}

function Header() {
  const { motion } = window.fm;
  const nav = window.NAV_ITEMS;
  const [active, setActive] = React.useState("about");

  React.useEffect(() => {
    const update = () => {
      const point = window.scrollY + window.innerHeight * 0.28;
      let current = "about";
      for (const item of nav) {
        const el = document.getElementById(item.id);
        if (el && el.offsetTop <= point) current = item.id;
      }
      setActive((prev) => (prev === current ? prev : current));
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    return () => {
      window.removeEventListener("scroll", update);
      window.removeEventListener("resize", update);
    };
  }, [nav]);

  return (
    <motion.header
      className="site-header"
      initial={{ y: -40, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
    >
      <div className="site-header-inner">
        <a href="#home" className="site-brand">SARAV'S WORLD</a>
        <nav className="site-nav">
          {nav.map((item) => (
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

function AmbientOrbs({ mouseSpring }) {
  const { motion, useTransform } = window.fm;

  const orbStyle = (factorX, factorY) => ({
    x: useTransform(mouseSpring.x, (v) => v * factorX),
    y: useTransform(mouseSpring.y, (v) => v * factorY),
  });

  return (
    <>
      <motion.div className="orb orb-violet" style={orbStyle(1.4, 1.0)} />
      <motion.div className="orb orb-teal"   style={orbStyle(-1.2, 0.9)} />
      <motion.div className="orb orb-blue"   style={orbStyle(0.9, -1.1)} />
    </>
  );
}

function App() {
  const { MotionConfig, useReducedMotion, useMotionValue, useSpring } = window.fm;

  const reduced = useReducedMotion();

  // Single source of truth for mouse parallax. Updates a MotionValue (no React re-render),
  // and Writing + AmbientOrbs derive from a smoothed spring of that value.
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  const smoothX = useSpring(mouseX, { stiffness: 60, damping: 22, mass: 0.5 });
  const smoothY = useSpring(mouseY, { stiffness: 60, damping: 22, mass: 0.5 });

  React.useEffect(() => {
    if (reduced) return;
    const onMove = (e) => {
      // Centered, normalized to a moderate translation range.
      mouseX.set((e.clientX / window.innerWidth - 0.5) * 36);
      mouseY.set((e.clientY / window.innerHeight - 0.5) * 28);
    };
    window.addEventListener("mousemove", onMove, { passive: true });
    return () => window.removeEventListener("mousemove", onMove);
  }, [reduced, mouseX, mouseY]);

  const mouseSpring = { x: smoothX, y: smoothY };

  return (
    <MotionConfig
      reducedMotion={reduced ? "always" : "never"}
      transition={{ type: "spring", stiffness: 260, damping: 22 }}
    >
      <div className="site-shell">
        <ScrollProgress />
        <AmbientOrbs mouseSpring={mouseSpring} />
        <Header />

        <main id="home">
          <Hero />
          <About />
          <Work />
          <Journey />
          <Builder />
          <Books />
          <Writing mouseSpring={mouseSpring} />
          <Contact />
        </main>

        <Footer />
      </div>
    </MotionConfig>
  );
}

// ─── Mount ───
function mountApp() {
  if (!window.React || !window.ReactDOM || !window.fm ||
      !window.Hero || !window.Books || !window.Journey || !window.Footer) {
    return setTimeout(mountApp, 30);
  }
  const root = window.ReactDOM.createRoot(document.getElementById("root"));
  root.render(<App />);
}
mountApp();
