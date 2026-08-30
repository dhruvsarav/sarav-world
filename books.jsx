// Books — scroll-bound orbit, magnetic active state, layoutId morph to detail panel.

function Books() {
  const {
    motion, useScroll, useTransform, useSpring, useMotionValueEvent,
    AnimatePresence,
  } = window.fm;

  const orbit = window.ORBIT_BOOKS;
  const allBooks = window.BOOKS;
  const orbitRef = React.useRef(null);

  const [activeOrbitIndex, setActiveOrbitIndex] = React.useState(0);
  const [selectedBook, setSelectedBook] = React.useState(null);
  const [isCompact, setIsCompact] = React.useState(false);

  React.useEffect(() => {
    const mq = window.matchMedia("(max-width: 1100px)");
    const update = () => setIsCompact(mq.matches);
    update();
    mq.addEventListener?.("change", update);
    return () => mq.removeEventListener?.("change", update);
  }, []);

  const { scrollYProgress } = useScroll({
    target: orbitRef,
    offset: ["start end", "end start"],
  });

  // Smoothed orbit rotation.
  const rotation = useSpring(useTransform(scrollYProgress, [0, 1], [0, 540]), {
    stiffness: 50, damping: 18, mass: 0.6,
  });

  // Derive active index from rotation.
  useMotionValueEvent(rotation, "change", (r) => {
    const step = 360 / orbit.length;
    const normalized = ((r % 360) + 360) % 360;
    const idx = Math.round(normalized / step) % orbit.length;
    setActiveOrbitIndex((prev) => (prev === idx ? prev : idx));
  });

  const activeBook = orbit[activeOrbitIndex] ?? orbit[0];

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

            {orbit.map((book, index) => {
              const angle = (360 / orbit.length) * index;
              return (
                <OrbitItem
                  key={book.id}
                  book={book}
                  angle={angle}
                  orbitRotation={rotation}
                  isActive={index === activeOrbitIndex}
                  onClick={() => setSelectedBook(book)}
                />
              );
            })}
          </div>
        </div>
      ) : (
        <MobileBooks activeBook={activeBook} onSelect={setSelectedBook} />
      )}

      {/* Full books grid */}
      <div className="books-grid">
        {allBooks.map((book) => (
          <BookCard key={book.id} book={book} onSelect={setSelectedBook} />
        ))}
      </div>

      {/* layoutId morph overlay */}
      <AnimatePresence>
        {selectedBook && (
          <BookDetail book={selectedBook} onClose={() => setSelectedBook(null)} />
        )}
      </AnimatePresence>
    </section>
  );
}

// ─── Orbit core (center pod) ───
function OrbitCore({ book }) {
  const { motion, AnimatePresence } = window.fm;
  return (
    <div className="orbit-core">
      <img src={window.IMG.coffeeReadsBadge} alt="" className="orbit-core-badge" />
      <span className="orbit-core-text">Now in Focus</span>
      <AnimatePresence mode="wait">
        <motion.strong
          key={book.id}
          className="orbit-active-title"
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -8 }}
          transition={{ duration: 0.34 }}
        >
          {book.title}
        </motion.strong>
      </AnimatePresence>
      <motion.a
        href={book.amazonUrl}
        target="_blank"
        rel="noreferrer"
        className="orbit-amazon-btn"
        whileHover={{ y: -2, scale: 1.04 }}
        whileTap={{ scale: 0.97 }}
        transition={{ type: "spring", stiffness: 320, damping: 22 }}
      >
        {book.isUpcoming ? "Author page" : "View on Amazon"}
      </motion.a>
    </div>
  );
}

// ─── Orbit item (a single book on the ring) ───
// Outer motion.div owns the positional MotionValues (x, y).
// Inner motion.div owns the state-driven scale/opacity/filter — they can't share a single
// motion.div in FM 10 because style transform MotionValues clobber animate's transform target.
function OrbitItem({ book, angle, orbitRotation, isActive, onClick }) {
  const { motion, useTransform } = window.fm;
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
          src={book.cover}
          alt={book.title}
          loading="lazy"
          decoding="async"
        />
      </div>
    </motion.div>
  );
}

// ─── Mobile books (grid + featured) ───
function MobileBooks({ activeBook, onSelect }) {
  const { motion } = window.fm;
  return (
    <div style={{ marginTop: 28 }}>
      <motion.div
        className="glass-card"
        style={{ padding: "22px 18px", textAlign: "center" }}
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
      >
        <img src={window.IMG.coffeeReadsBadge} alt="" style={{ width: 80, margin: "0 auto 12px" }} />
        <span className="orbit-core-text">Featured Book</span>
        <strong style={{ display: "block", marginTop: 8, fontSize: "1.18rem", lineHeight: 1.45 }}>
          {activeBook.title}
        </strong>
        <motion.a
          href={activeBook.amazonUrl}
          target="_blank"
          rel="noreferrer"
          className="orbit-amazon-btn"
          style={{ marginTop: 12, display: "inline-block" }}
          whileHover={{ y: -2 }}
          whileTap={{ scale: 0.97 }}
        >
          {activeBook.isUpcoming ? "Author page" : "View on Amazon"}
        </motion.a>
      </motion.div>
    </div>
  );
}

// ─── Book card in the grid ───
function BookCard({ book, onSelect }) {
  const { motion } = window.fm;
  return (
    <motion.article
      className="book-card"
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
      whileHover={{
        y: -6, scale: 1.025,
        transition: { type: "spring", stiffness: 320, damping: 22 },
      }}
      onClick={() => onSelect(book)}
    >
      {book.isUpcoming && <span className="book-upcoming-badge">Coming soon</span>}
      <div className="book-cover-wrap">
        <motion.img
          layoutId={`book-cover-${book.id}`}
          src={book.cover}
          alt={book.title}
          className="book-cover"
          loading="lazy"
          decoding="async"
        />
      </div>
      <div className="book-meta">
        <h3>{book.title}</h3>
        <span>Sarav</span>
      </div>
      <div className="book-actions">
        <motion.a
          href={book.amazonUrl}
          className="book-amazon-btn"
          target="_blank"
          rel="noreferrer"
          onClick={(e) => e.stopPropagation()}
          whileHover={{ scale: 1.03 }}
          whileTap={{ scale: 0.97 }}
        >
          {book.isUpcoming ? "Author page" : "View on Amazon"}
        </motion.a>
      </div>
    </motion.article>
  );
}

// ─── Book detail overlay (the layoutId morph target) ───
function BookDetail({ book, onClose }) {
  const { motion } = window.fm;

  // Esc to close
  React.useEffect(() => {
    const onKey = (e) => { if (e.key === "Escape") onClose(); };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <motion.div
      className="book-detail-backdrop"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.3 }}
      onClick={onClose}
    >
      <motion.div
        className="book-detail-panel"
        initial={{ y: 30 }}
        animate={{ y: 0 }}
        exit={{ y: 30 }}
        transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
        onClick={(e) => e.stopPropagation()}
      >
        <motion.img
          layoutId={`book-cover-${book.id}`}
          src={book.cover}
          alt={book.title}
          className="book-detail-cover"
        />
        <div className="book-detail-copy">
          <h2>{book.title}</h2>
          <div className="by">by Sarav · {book.isUpcoming ? "Coming soon" : "Available now"}</div>
          <p>
            {book.isUpcoming
              ? "This title isn't on Amazon yet — it's on the way. In the meantime, you can browse the full author shelf and follow for updates."
              : "Open the book on Amazon to read the full description, browse a sample, or pick up a copy in paperback or Kindle."}
          </p>
          <motion.a
            href={book.amazonUrl}
            className="orbit-amazon-btn"
            target="_blank"
            rel="noreferrer"
            style={{ marginTop: 22, display: "inline-flex" }}
            whileHover={{ y: -2, scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            transition={{ type: "spring", stiffness: 320, damping: 22 }}
          >
            {book.isUpcoming ? "Visit Author Page" : "View on Amazon"}
          </motion.a>
        </div>
        <button className="book-detail-close" onClick={onClose} aria-label="Close">✕</button>
      </motion.div>
    </motion.div>
  );
}

window.Books = Books;
