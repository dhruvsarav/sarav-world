// Journey — sticky scroll-pinned timeline. Each scroll unit advances one career step.

function Journey() {
  const { motion, useScroll, useTransform, useSpring, useMotionValueEvent, AnimatePresence } = window.fm;
  const jobs = window.JOURNEY_CARDS;
  const steps = jobs.length;

  const wrapRef = React.useRef(null);
  const [activeIndex, setActiveIndex] = React.useState(0);

  const { scrollYProgress } = useScroll({
    target: wrapRef,
    offset: ["start start", "end end"],
  });

  // Smoothed for nicer rail growth.
  const smoothProgress = useSpring(scrollYProgress, { stiffness: 80, damping: 22, mass: 0.4 });

  // Active step index derived from progress. We divide the section into N equal slabs.
  useMotionValueEvent(scrollYProgress, "change", (p) => {
    const idx = Math.min(steps - 1, Math.max(0, Math.floor(p * steps)));
    setActiveIndex((prev) => (prev === idx ? prev : idx));
  });

  // Rail progress bar scales 0→1 with smoothed scroll.
  const railScale = smoothProgress;

  return (
    <section className="section" id="journey" style={{ paddingTop: 88, paddingBottom: 0 }}>
      <p className="section-kicker center-copy">Career Journey</p>
      <SectionTitle text="Built across roles." />
      <p className="section-text center-copy journey-intro">
        The journey kept expanding — role by role, country by country, story by story.
      </p>

      <div
        className="journey-sticky-wrap"
        ref={wrapRef}
        style={{ "--journey-steps": steps }}
      >
        <div className="journey-sticky-stage">
          {/* Left rail with step labels */}
          <div className="journey-step-rail">
            <div className="journey-rail-track" />
            <motion.div
              className="journey-rail-progress"
              style={{ scaleY: railScale, height: "100%" }}
            />

            {jobs.map((job, i) => (
              <div
                key={job.title}
                className={"journey-step" + (i <= activeIndex ? " active" : "")}
                onClick={() => {
                  // Click-to-jump: scroll to the slice of the wrap that corresponds to step i.
                  const wrap = wrapRef.current;
                  if (!wrap) return;
                  const wrapTop = wrap.offsetTop;
                  const wrapHeight = wrap.offsetHeight;
                  const target = wrapTop + (i / steps) * wrapHeight + window.innerHeight * 0.1;
                  window.scrollTo({ top: target, behavior: "smooth" });
                }}
              >
                <span className="journey-step-node" />
                <span className="journey-step-year">{job.year}</span>
                <span className="journey-step-label">{job.title}</span>
              </div>
            ))}
          </div>

          {/* Right card stack — animated swap between jobs */}
          <div className="journey-card-stack">
            <AnimatePresence mode="wait">
              <motion.div
                key={activeIndex}
                className="journey-card-slide"
                initial={{ opacity: 0, x: 60, scale: 0.96 }}
                animate={{ opacity: 1, x: 0, scale: 1 }}
                exit={{ opacity: 0, x: -60, scale: 0.96 }}
                transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
              >
                <div className="journey-media">
                  <motion.img
                    src={jobs[activeIndex].image}
                    alt=""
                    initial={{ scale: 1.08 }}
                    animate={{ scale: 1 }}
                    transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
                    loading="lazy"
                  />
                </div>
                <div className="journey-copy">
                  <span className="journey-year">{jobs[activeIndex].year}</span>
                  <h3>{jobs[activeIndex].title}</h3>
                  <p>{jobs[activeIndex].text}</p>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}

window.Journey = Journey;
