# 🌐 Sarav World Project & Architecture Rules

> Repository: D:\Websites\SaravsWorld
> Production Site: https://iamsaravofficial.com
> Master Memory: D:\sdrv\docs\memory\Sarav_World_MasterContext.md

---

### 7. Universal Web App Architecture & Design Standards (STRICT MEMORIZED RULES)
Every web app hosted under `public/apps/` must adhere strictly to these rules:
1. **Playground Hub Section Nomenclature (`/apps/`)**:
   - Top Flagship Spotlight: `🧠 Tokenomics (Enterprise AI Economics)`
   - Section 1: `⚡ Family & Interactive Web Suite` (10 Live Apps)
   - Section 2: `🌟 Family Planner Suite` (10 Live Planners)
2. **Canonical Suite Sequence (Strict 1–20 Standard across Hub and Ecosystem Dropdowns)**:
   *Section 1: Family & Interactive Web Suite (10 Apps)*:
   1. `genzalphaslang` (GenZ & Alpha Slang Decoder)
   2. `salary-planner` (Salary Planner)
   3. `home-budget-planner` (Home Budget Planner)
   4. `retirement-planner` (Retirement Planner)
   5. `gold-price-estimator` (Metal Price Estimator)
   6. `gold-loan-calculator` (Gold Loan Calculator)
   7. `digigold-calculator` (DigiGold SIP Calculator)
   8. `fd-calculator` (FD Calculator)
   9. `rd-calculator` (RD Calculator)
   10. `home-loan-accelerometer` (Home Loan Prepayment & Debt-Free Accelerometer)
   *Section 2: Family Planner Suite (10 Planners)*:
   11. `glow-up-grid` (Glow Up Grid — Colorful Kid Routine Planner & Habit Tracker)
   12. `lunchbox-planner` (School Tiffin & Family Lunchbox Planner)
   13. `study-sprint` (Study Sprint & Exam Revision Matrix)
   14. `piggy-bank-ledger` (Kids' First Pocket Money & Piggy Bank Ledger)
   15. `chore-quest-board` (Kids' Chore & Quest Board — Gamified RPG Chores)
   16. `screen-time-passes` (Screen-Time Swap Tickets & Family Reward Passes)
   17. `boredom-buster` (Kids' Screen-Free Boredom Buster Adventure Wheel)
   18. `family-movie-night` (Family Movie & Board Game Night Decider)
   19. `book-nook` (Kids' Book Nook & 100-Book Quest)
   20. `birthday-gift-matrix` (Family Birthday & Milestone Gift Wishlist Matrix)
   *Amazon Associates Tracking ID*: `dhrav-21` strictly applied to curated shopping links across relevant planners (`piggy-bank-ledger`, `boredom-buster`, `family-movie-night`, `book-nook`, `birthday-gift-matrix`).
3. **Footer Distinction**:
   - **Consumer Retail Web Apps (Non-Affiliate)**:
     `[App Name] Crafted by <b>Sarav</b> (<a href="https://iamsaravofficial.com/" target="_blank">Saravanakumar Murugan</a>).`
     `&copy; 2009–2026 <a href="https://iamsaravofficial.com/apps/">Sarav's Playground</a>. Zero telemetry. All calculations run strictly client-side.`
   - **Curated Planners with Amazon Affiliate (`dhrav-21`)**:
     `[Planner Name] Crafted by <b>Sarav</b> (<a href="https://iamsaravofficial.com/" target="_blank">Saravanakumar Murugan</a>).`
     `&copy; 2009–2026 <a href="https://iamsaravofficial.com/apps/">Sarav's Playground</a>. 100% Client-Side Privacy &bull; Zero Telemetry &bull; LocalStorage Persistence`
     `Amazon Associates Disclosure: As an Amazon Associate, Sarav's World earns from qualifying purchases made via links featuring tracking ID <code>dhrav-21</code>.`
   - **Family Games Arcade & Individual Games**:
     `[Game Name] Crafted by <b>Sarav</b> (<a href="https://iamsaravofficial.com/" target="_blank">Saravanakumar Murugan</a>).`
     `&copy; 2009–2026 <a href="https://iamsaravofficial.com/">Sarav's World</a>. Engineered with zero external trackers, zero ads, and pure client-side code.`
   - **Enterprise AI Economics (Tokenomics — ALWAYS SEPARATE)**:
     `Tokenomics Crafted by <b>Sarav</b> (<a href="https://iamsaravofficial.com/" target="_blank">Saravanakumar Murugan</a>). <b>Digital Workplace Technology Head</b>.`
     `&copy; 2009–2026 <a href="https://iamsaravofficial.com/apps/">Sarav's Playground</a>. Zero telemetry. All calculations run strictly client-side.`
4. **Theme Selector Standard**:
   - Segmented `Auto | ☀️ Light | 🌙 Dark` control is aligned to the **top-right** corner in the header banner, matching `gold-price-estimator` (`align-items: flex-end`).
5. **Universal 4-Action Suite Across All Calculators & Utility Apps**:
   - `📱 Share on WhatsApp`: Clean formatted WhatsApp share with structured bullets, dividers, and direct tool URL.
   - `🖨️ Print / Save PDF`: Clean `window.print()` with `@media print` rules hiding menubars, themes, and action buttons.
   - `📋 Copy Summary`: Structured text summary copied to clipboard using `navigator.clipboard.writeText` with automatic hidden textarea fallback (`fallbackCopy`). Displays non-blocking floating toast.
   - `💾 Save to History / Favorites / Backup`: Client-side `localStorage` persistence with timestamp, load, delete, backup/restore JSON, and clear actions, accompanied by non-blocking toast feedback.
6. **Zero Blocking Alert/Prompt Modals & Toast Standard (Gold Price Estimator Benchmark)**:
   - **All 15 Web Apps** must NEVER use blocking `alert()` or `prompt()` dialogs for copy or scenario saving.
   - Standardized `showToast(msg)` float element (`#toast`, 2.6s auto-dismiss) styled cleanly to match each app's palette.
    - **No Reset Button Policy**: Destructive global Reset buttons are removed from workflow calculators (e.g. Salary Planner) to prevent accidental data loss and keep the unified 4-button action bar clean.
7. **Strict Two-Family Color Palette Standard**:
   - **Family A — Precious Metals Suite (3 Apps)**: `/apps/gold-price-estimator/`, `/apps/gold-loan-calculator/`, `/apps/digigold-calculator/`
     * **Light Mode (Physical Gold)**: Outer canvas `#E6DFD5`, App canvas `#FFFBF0`, White cards `#FFFFFF`, Espresso headings `#3D2B00`, Muted text `#8A7554`, Primary Gold `#C1810A`, Dark Gold `#8B5E00`, Header banner `linear-gradient(180deg, #F9D77E, #F0B429)`, Gold leaf border `#E0B84B`, Chips `#F6E3B0`, Gains `#1B8A3D`, Risk `#D32F2F`.
     * **Dark Mode (Obsidian & Liquid Gold)**: Outer canvas `#0A0907`, App canvas `#12100C`, Dark bronze cards `#1D1913`, Ivory white text `#F7F2E8`, Sandstone muted text `#B0A28E`, Radiant gold accent `#E5A93C`, Bright gold `#FFC04D`, Header banner `linear-gradient(180deg, #38290E, #251A07)`, Bronze border `#52411E`, Chips `#2E2412`, Gains `#4CAF50`, Risk `#EF5350`.
     * **OG Card Theme**: **Light Mode Physical Gold** (`#F7F3EB` soft gold canvas, `#FFFFFF` card, `#E0B84B` border, `#2E1E05` deep espresso title, `#8B5E00` badge text).
   - **Family B & C — Family & Interactive Apps Suite (11 Apps Unified + Hub)**: `/apps/genzalphaslang/`, `/apps/salary-planner/`, `/apps/home-budget-planner/`, `/apps/retirement-planner/`, `/apps/fd-calculator/`, `/apps/rd-calculator/`, `/apps/glow-up-grid/`, `/apps/lunchbox-planner/`, `/apps/study-sprint/`, `/apps/piggy-bank-ledger/`, `/apps/chore-quest-board/`, `/apps/screen-time-passes/`, and `/apps/` (Playground Hub)
     * **Light Mode (Crisp Financial Slate)**: Canvas `#F5F7FA`, Level 1 Cards `#FFFFFF`, Level 2 Inputs `#F0F3F7`, Level 3 Elevated `#E4E9F0`, Headings `#1A202C`, Dim text `#4A5568`, Faint text `#718096`, Primary Amber Accent `#D97706`, Accent Ink `#FFFFFF`, Secondary Teal Accent `#0D9488`, Steel border `#D1D8E2`, Soft border `#E2E8F0`, Surplus/Liquid `#16A34A`, Deficit/TDS `#DC2626`, Shadow `0 8px 32px rgba(0,0,0,0.08)`.
     * **Dark Mode (Deep Space Navy)**: Canvas `#0C0F14`, Level 1 Cards `#141922`, Level 2 Inputs `#1B222D`, Level 3 Elevated `#222B39`, Headings `#EAEFF5`, Dim text `#94A0B2`, Faint text `#5C6B80`, Primary Amber Accent `#E3A63E`, Accent Ink `#141005`, Secondary Teal Accent `#4FB0A8`, Navy border `#2A3545`, Soft border `#1E2633`, Surplus/Liquid `#5FBF77`, Deficit/TDS `#E2665A`, Shadow `0 8px 32px rgba(0,0,0,0.40)`.
     * **OG Card Theme**: **Dark Mode Deep Space Navy** (`#0C0F14` canvas, `#141922` slate card, `#FFFFFF` title, `#E3A63E` & `#4FB0A8` accents).
8. **Header Row & Presets Layout Architecture**:
   - Header must use `.header-main-row` containing `.header-left` (`flex: 1; min-width: 0;`) and `.header-right` (`flex-shrink: 0; align-items: flex-end;`). The theme selector (`Auto | ☀️ Light | 🌙 Dark`) is **always anchored to the top-right end**.
   - Preset buttons (`.header-presets`) must always sit in a dedicated block directly underneath the header row, spanning full width with its own breathing room so chips never force horizontal flex-wrapping or push the theme toggle below them.
   - Home Budget Planner features 3 GenZ vibe presets: `💀 No Cap YOLO (95% Burn)`, `✨ Soft Life (65% Burn)`, `🗿 Monk Mode (35% Burn)`.
9. **Executive Digital Workplace & Enterprise AI Economics Suite Architecture (`/eapps/`)**:
   - Executive portal at `/eapps/` (`https://iamsaravofficial.com/eapps/`) crafted for CXOs, Directors of IT and DWP, Heads of EUC, Chief AI Architects, Sales Heads, Pre-Sales Heads, Solution Directors, and strategic pursuit teams.
     - Houses 11 deterministic decision engines plus the Universal Shared Workspace in canonical sequence:
       1. `dwssharedworkspace` (`/apps/dwssharedworkspace/`): Universal Enterprise Shared Workspace (Configure once, 5 architecture pillars, unlimited named custom presets + 4 archetypes, real-time client-side sync across all 11 engines).
       2. `tokenomics` (`/apps/tokenomics/`): Multi-LLM AI spend modeling, prompt caching discounts (up to 90%), contingency buffers, and human labor arbitrage ROI.
       3. `sdoptimizer` (`/apps/sdoptimizer/`): Erlang C queue simulation, L0 AI agentic deflection, Copilot L1 AHT compression, channel cost-to-serve economics.
       4. `fsoptimizer` (`/apps/fsoptimizer/`): Field Services hub-and-spoke dispatch optimization using square-root travel law, AI remote deflection, and vehicle OPEX modeling.
       5. `desksidestaffing` (`/apps/desksidestaffing/`): Deskside, Tech Bar, and smart locker staffing capacity engine with dual-tier Erlang C queueing and hybrid office attendance factors.
       6. `dexadvisor` (`/apps/dexadvisor/`): Multi-Attribute Utility Theory (MAUT) vendor capability matrix (Nexthink, ControlUp, Lakeside, 1E, ServiceNow), 7-year XPI projections, and XLA playbook.
       7. `itsmadvisor` (`/apps/itsmadvisor/`): Trigger-weighted ITSM platform fit (ServiceNow, Jira, Freshservice, BMC Helix, Ivanti), urgency scoring, directional TCO envelope, and phased migration playbook.
       8. `rfpscorer` (`/apps/rfpscorer/`): Generic multi-attribute decision matrix with disqualifying must-have gates, custom weights, and built-in templates (DWP MSP, ITSM, DEX).
       9. `aiinitsm` (`/apps/aiinitsm/`): AI-in-ITSM Business Case Builder (Discounted cash flows, NPV/payback/ROI rollup, live SD Optimizer scenario recomputation, 5x5 risk register).
       10. `automationscore` (`/apps/automationscore/`): Automation Potential Advisor (Bottom-up tech stack ceiling across 50 call drivers, digital reachability bounds, 5–7 year realization curve).
       11. `dwpassessment` (`/apps/dwpassessment/`): Digital Workplace Maturity Assessment (8 operational pillars, 48 capabilities, SVG radar spider chart, priority gap auto-routing).
       12. `ticketanalyzer` (`/apps/ticketanalyzer/`): ITSM Ticket Analyzer (On-device neural vector clustering via WebAssembly MiniLM-L6, semantic deduplication, 50-driver ITIL categorization, tri-axis Automation/GenAI/DEX potential ceilings, 500-ticket demo dataset, and zero telemetry).
     - **Universal Shared Workspace Client Bridge (`/dws-workspace-client.js`)**:
       * Injected across all 11 enterprise decision engines via `<script src="/dws-workspace-client.js" defer></script>`.
       * Connects reactively to `localStorage` key `dws_workspace_v1`.
       * Renders `.dws-ws-bridge` sub-bar allowing instant selection of Active profile, Custom named presets saved from `dwssharedworkspace`, or 4 Built-In Enterprise Archetypes (Global Enterprise, Mid-Market Growth, Regional Public Sector, AI-First Modern Org).
       * `[⚡ Load into Engine]` automatically maps 4 pillars (`orgProfile`, `supportOps`, `financials`, `techStack`) to each app's native form fields and calls `recalcAll()` or native render function with non-blocking `#toast` feedback.
       * Multi-tab sync via `window.addEventListener('storage', ...)`.
     - All enterprise apps retain strict client-side zero-telemetry computation and zero blocking alerts (`showToast()` standard).
     - **Topbar Badging Standards**:
       * `/apps/tokenomics/`: `🧠 Enterprise AI Economics · Version 2026.09`
       * All other 10 engines + Shared Workspace + `/eapps/` hub: `<img src="https://iamsaravofficial.com/eapps/eapps-square.png" ...>Digital Workplace Suite · Version 2026.09`
     - **Ecosystem Navigation Standard for Enterprise Apps**: **Strictly ONE** dropdown: `E-Apps ▾` (linking `/eapps/`, Universal Shared Workspace, and all 11 enterprise engines in canonical sequence). Consumer `Apps ▾`, `Games ▾`, and `Projects ▾` dropdowns are completely excluded.
    - **Footer Standard for Enterprise Apps**:
       Line 1: `[App Name] Crafted by <b>Sarav</b> (<a href="https://iamsaravofficial.com/" target="_blank">Saravanakumar Murugan</a>). Digital Workplace Technology Head &amp; Chief AI Architect.` (only `<b>Sarav</b>` in bold; title in normal font)
       Line 2: `<a href="https://iamsaravofficial.com/eapps/">2026 Executive Design Engines</a>. Zero telemetry. [Engine tail: All calculations run strictly client-side / All scoring runs client-side / Independent assessment, not vendor-sponsored / Universal Shared Workspace: 100% Client-Side Private Local Storage · Zero Cloud Telemetry · Designed for Global Architects & CXOs].` (copyright year range removed, strictly `2026 Executive Design Engines`)
       Line 3 (for `dwpassessment`): `Level descriptions are Executive Design Engines' independent maturity-model design (Ad Hoc → Optimized). Not a certified or licensed framework — use as a structured self-assessment starting point.`
10. **Official Brand Icon Systems across All 5 Portals**:
   - **Playground Gateway (`/playground/`)**:
     * Official Brand Icon: **The Celestial 4-Way Nexus Portal** (Isometric futuristic crystal nexus uniting cyber gold, digital cyan, neon magenta, and sacred gold beams converging on a quantum orb).
     * Production assets: `playground-square.png` (512px), `favicon-32.png`, `apple-touch-icon.png`.
   - **Apps Hub (`/apps/`)**:
     * Official Brand Icon: **The Cosmic Glass Cube** (Isometric frosted glass sandbox with floating cyber gold `#E3A63E` and digital teal `#4FB0A8` spheres).
     * Production assets: `apps-full.png` (1024px), `apps-square.png` (512px), `favicon-192.png`, `apple-touch-icon-180.png`, `favicon-32.png`, `favicon-16.png`, `favicon.ico`.
   - **E-Apps Suite (`/eapps/`)**:
     * Official Brand Icon: **The Sovereign Hex Core** (Faceted titanium hexagonal core with precision gyroscopic telemetry rings and glowing amber/cyan dual-core neural processor).
     * Production assets: `eapps-full.png` (1024px), `eapps-square.png` (512px), `favicon-192.png`, `apple-touch-icon-180.png`, `favicon-32.png`, `favicon-16.png`, `favicon.ico`.
   - **Family Games Arcade (`/games/`)**:
     * Official Brand Icon: **The Arcade Hologram Core** (Isometric glowing retro-modern arcade cabinet with neon magenta/pink and gold lighting, holographic controller, and floating dice).
     * Production assets: `games-square.png` (512px), `favicon-32.png`, `apple-touch-icon.png`.
   - **Cultural Projects Hub (`/projects/`)**:
     * Official Brand Icon: **The Heritage Golden Codex** (Isometric South Indian Dravidian temple gopuram kalasam pinnacle floating above an ancient sacred engraved palm-leaf manuscript with Thiruvalluvar glyph).
     * Production assets: `projects-square.png` (512px), `favicon-32.png`, `apple-touch-icon.png`.
   - All 5 portals feature their respective responsive squircle brand badges in hero headers and across the Playground 4-quadrant grid.
11. **Interactive Family Games Arcade Suite (`/games/`)**:
    - Master Family Games Hub at `https://iamsaravofficial.com/games/` uniting 10 interactive games with zero telemetry, procedural Web Audio effects, canvas physics, family roster turn selectors, and 1-tap WhatsApp boast sharing:
      1. `familywinner` (`/games/familywinner/`): 5-reel Amazon-style arcade slot machine household decider with 3D mechanical lever, calibrated odds (`DADDY` 35%, `MUMMY` 20%, `HUBBY` 15%, `WIFEY` 15%, `MYKID` 15%), Vegas bell clangs, brass victory fanfare, and coin cascade shower.
      2. `sentimeter` (`/games/sentimeter/`): Couples telepathy challenge (Hubby vs. Wifey) played on a single phone via Pass & Guess, featuring edge-to-edge full-card privacy barrier masking active choices, live Senti-Meter gauge, romantic chimes / mismatch slide whistles, and cheeky marital prescriptions.
      3. `secretbox` (`/games/secretbox/`): 3D antique mystery chest dispensing 4 card decks (Wholesome Memories, Cheeky Truths, Mild Desi Dares, and Family Mimicry) with 30s ticking timer and Chicken-Out Penalty Wheel.
      4. `cuptoss` (`/games/cuptoss/`): 2.5D dining table ping-pong cup toss with trajectory drag aim, bounce physics, moving obstacle, and leaderboard. Fullscreen `100dvh` HUD and 75px thumb grab.
      5. `bottleflip` (`/games/bottleflip/`): Angular velocity swipe bottle flip physics simulator with water weight customization, multiple bottle skins, and 10x cap-landing bonus.
      6. `samosasnatch` (`/games/samosasnatch/`): 2-Player rapid finger-tapping tug-of-war on ONE phone with 180° inverted split-screen and Freeze shock penalty. Non-passive touch listeners eliminate zoom/bounce.
      7. `chitcharades` (`/games/chitcharades/`): Forehead tilt party guessing game with DeviceOrientation sensor, 4 Desi decks, 60s countdown, auto-fullscreen entry and floating exit button.
      8. `snackroulette` (`/games/snackroulette/`): Carnival treat & dare spin wheel with angular momentum, ratchet clicks, custom slice editor, turn ledger log, and top player-switcher HUD.
      9. `dialoguedetective` (`/games/dialoguedetective/`): Household quote trivia showdown with suspect voting, streak multiplier, custom family quote studio, and 1-screen zero-scroll mobile layout.
      10. `gulelstrike` (`/games/gulelstrike/`): Traditional village orchard slingshot game with rubber band pull mechanics, 95px thumb grab radius, wind drift, fruit sway, and monkey obstacle.
    - **Header & Footer Standards**: Header is named strictly `Family Games Arcade` (no personal names). Standard footer: `Games crafted for Sarav... Engineered with zero external trackers, zero ads, and pure client-side code`.
    - **Universal Mobile Arcade Fullscreen Architecture**: Dual-layer fullscreen combining native `requestFullscreen()` with `.is-fullscreen` on body (`100dvh`, fixed inset 0), non-passive touch listeners (`{ passive: false }` + `e.preventDefault()`), floating top HUDs with quick `🗗 Exit`, and non-blocking in-game modal cards.
12. **Ecosystem Navigation Rules for Consumer Apps & Games**:
   - All Consumer Apps & Games pages (`/apps/`, 15 live tools, `/games/`, and 10 arcade games) feature **strictly THREE** dropdowns in canonical sequential order: `Apps ▾` | `Games ▾` | `Projects ▾`.
   - `E-Apps ▾` dropdown is completely excluded from consumer apps and games.
   - **Canonical Dropdown Items (Strict Standards)**:
     * `Apps ▾` (16 items): `🎡 Playground Hub`, `GenZ & Alpha Slang`, `Salary Planner`, `Home Budget Planner`, `Retirement Planner`, `Gold Price Estimator`, `Gold Loan Calculator`, `DigiGold Calculator`, `FD Calculator`, `RD Calculator`, `Glow Up Grid`, `Lunchbox & Meal Planner`, `Study Sprint & Exam Matrix`, `Piggy Bank & Money Ledger`, `Chore & Quest Board`, `Screen-Time Passes`.
     * `Games ▾` (11 items): `🎰 Games Arcade Hub`, `🎰 Family Jackpot`, `💖 Senti-Meter`, `🎁 Secret Box`, `🏓 Ping-Pong Cup Toss`, `🍾 Bottle Flip Showdown`, `⚡ Samosa Snatch`, `🗣️ Chit-Charades`, `🎡 Snack Roulette`, `🎙️ Dialogue Detective`, `🎯 Desi Gulel Strike`.
     * `Projects ▾` (4 items): `🏛️ Projects Hub`, `Temples of Tamil Gods`, `FactDrop`, `Thirukkural Hub`.
     * **Right Side**: `🎪 Playground` link + `🧠 Enterprise AI Economics` badge.
   - **Zero Placeholder Policy**: Fictitious, speculative, or unreleased apps (e.g. `Doc Vault`, `Voice Notes`, `Task Zen`, `Family Ledger`, `Family Recipe Vault`, `Desi Food Explorer`, `Heritage Weaver`, `Folk Soundscape`, `Mythos Interactive`) must **NEVER** be placed in navigation menus.
   - **Hover Stability Standard**: All `.eco-menu` elements must include the invisible hover bridge `.eco-menu::before { content: ""; position: absolute; top: -10px; left: 0; right: 0; height: 10px; }` to eliminate cursor dropoff when moving from the button to the dropdown menu.
13. **Cultural Heritage & Open Knowledge Projects Hub (`/projects/`)**:
   - Unites all 3 cultural databases: Temples of Tamil Gods, Thirukkural Hub, and FactDrop.
   - Features complete 4-tier navigation: `Apps ▾`, `E-Apps ▾`, `Games ▾`, `Projects ▾`.
   - Features official brand icon `projects-square.png` in hero.
14. **Master Playground Gateway Portal (`/playground/`)**:
   - Permanent, decoupled master 4-quadrant gateway routing directly to `/apps/`, `/eapps/`, `/games/`, and `/projects/`.
   - Features official brand icon `playground-square.png` in hero.
   - All 4 quadrant cards feature official brand squircle icons (`apps-square.png`, `eapps-square.png`, `games-square.png`, `projects-square.png`).
   - Reflects full live suite metrics: 20 Apps, 11 Engines, 10 Games, 3 Projects (44 Interactive Destinations across 46 Synchronized Ecosystem Pages).
   - Full 4-tier ecosystem navigation matching canonical inventories.

---

## ⚙️ Development, CLI & Operational Notes

### ⚠️ Windows PowerShell Environment Note
On this Windows machine, the agent framework must execute commands using:
- **`Cwd`**: `C:\Windows\System32\WindowsPowerShell\v1.0`
- Target repo via flags:
  - Git commands: `git -C "D:\Websites\SaravsWorld" <command>`
  - NPM commands: `npm --prefix "D:\Websites\SaravsWorld" <command>`
  - Python commands: `python "D:\Websites\SaravsWorld\scripts\..."`

### Key Commands
```powershell
# Build verification
npm --prefix "D:\Websites\SaravsWorld" run build

# Synchronize all ecosystem menubars (Maker-checker depth parser, dry-run or --write)
python "D:\Websites\SaravsWorld\scripts\sync_ecosystem_nav.py" --write

# Git status & push
git -C "D:\Websites\SaravsWorld" status
git -C "D:\Websites\SaravsWorld" push origin main

# Re-run FactDrop generator
python "D:\Websites\SaravsWorld\scripts\factdrop\generate_factdrop.py"
```

---

## 🌟 Flagship Homepage & Apps Hub Standards

### 1. Root Flagship Homepage (`/` - `src/App.jsx` & `src/index.css`)
- **Hero Kicker:** `Digital Workplace Technology Head · Author · Builder` (employer tag omitted for clean executive brand).
- **Sticky Topbar:** Includes dedicated glowing `Playground ✦` pill (`.nav-playground-pill`) linking to `/playground/` with cyan/teal ambient aura and pulse animation.
- **Typography & Descenders:** `.section-title` maintains `line-height: 1.25` and `.title-word` has vertical breathing clearance (`padding-bottom: 0.16em; margin-bottom: -0.16em;`) so letters with descenders (`g`, `y`, `p`, `j`, `q`) never clip.
- **Builder Section (`#apps`):** Focuses on Enterprise AI & Workplace tools:
  - Dual central action buttons: `Enterprise AI Suite →` (`/eapps/`) and `Explore Playground ✦` (`/playground/`).
  - 3 flagship cards with official og-images: *Tokenomics* (`/apps/tokenomics/icons/brain-full.png`), *SD Optimizer* (`/apps/sdoptimizer/og-image.png`), *Deskside Staffing* (`/apps/desksidestaffing/og-image.png`).
- **Footer Directory:** Comprehensive directory links: *Copyright* (`/copyright/`), *Privacy* (`/privacy-policy/`), *Terms* (`/terms/`), *Fact Sheet* (`/fact-sheet/`), *Feedback* (`/feedback/`), *Social* (`/social/`). Formatted as `Copyright © 2009–{currentYear} · Sarav`.

### 2. Apps Hub (`/apps/` - `public/apps/index.html`)
- **Clean Structure:** Laser-focused exclusively on web applications.
- **Layout Flow:** Header & Ecosystem Bar → Hero → Featured Spotlight (*Enterprise AI Economics (Tokenomics)*) → Family & Interactive Suite (12 live consumer tools) → Zero-telemetry footer.
- Cultural platforms (*Temples of Tamil Gods*, *Thirukkural*, *FactDrop*) live strictly on the dedicated [`/projects/`](https://iamsaravofficial.com/projects/) hub.

---

### 11. Curated Store Architecture & Live Telegram Ingestion Standards (`/store/`)
- **Production Storefront URL**: `https://iamsaravofficial.com/store/`
- **Purpose**: Handpicked, home-tested lifestyle, bedding, kitchen, tech, children's books, school gear, and family games curated by Vidhya & Sarav.
- **Amazon Associates Tracking Standard**: Strictly encoded with `tag=dhrav-21&linkCode=ll2` across all Amazon outbound links and share buttons.
- **Zero Local Product Image Policy**: Product images load directly from Amazon's high-speed CDN via scraped OpenGraph/product image URLs. Fallback placeholder is `/store/images/default-product.svg`.
- **Live Curation Workflow via Telegram**:
  - **Telegram Bot**: `@SaravVidhyaStoreBot` (used by Vidhya and Sarav to curate products instantly by sharing Amazon URLs).
  - **Cloudflare Worker**: `https://curated-store-bot.nalkudilstudio.workers.dev` (source in `workers/curated-store-bot/index.js`).
  - **Cloudflare KV**: `STORE_KV` (`309e95eb480849caa8d912a8ec2a5c5f`).
  - **Automated Pipeline**: Resolves shortened/affiliate redirects (`amzn.to`, `amzn.in`), extracts ASIN, scrapes OpenGraph metadata and images, auto-classifies into categories (`home`, `tech`, `lifestyle`, `lunchbox`, `books`, `games`), formats modern affiliate URL, and writes to KV index (`products_index` + `product:{asin}`).
  - **Hybrid Client-Side Rendering**: Instant initial render from `/store/products.json` fallback, followed immediately by background fetch to `/api/products` worker endpoint for real-time reactivity without redeploying the site.
- **Storefront Navigation Architecture**:
  - Top ecosystem bar features a streamlined two-link layout: `← Sarav's World` root link and `🛍️ Curated Store ▾` hover/click dropdown.
  - Dropdown exposes all 7 canonical categories: `🌟 All Curated Items`, `🏠 Home & Kitchen`, `⚡ Tech & Desk`, `🌿 Lifestyle & Wellness`, `🍱 School & Lunchbox`, `📚 Kids & Books`, `🧩 Toys & Games`.
  - Selecting any dropdown category syncs the filter studio chips, filters the product grid, highlights the active menu item, smoothly scrolls to the results, and supports deep linking via URL params (`?cat=tech` or `#home`).
- **Official Brand Assets Suite (`/store/`)**:
  - Generator script: `scripts/generate_store_assets.py` (Pillow + SVG with supersampling).
  - Assets: `favicon.svg`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon-180.png`, `favicon.ico`, `store-full.png` (512x512), and `og-image.png` (1200x630 with category pills and Amazon tag disclosure).

---

### 12. Homepage `#apps` Interactive Showcase & Scroller Architecture
- **Dual CSS Synchronization**: Both `src/index.css` and `src/App.css` are kept in sync and explicitly imported in `src/main.jsx`.
- **Spotlight Preview Containment**: `.tool-spotlight-shot-wrap` is capped with `aspect-ratio: 16 / 9; max-height: 280px; overflow: hidden;` to ensure screenshots/brain graphics never blow up beyond their designed card boundaries regardless of viewport resolution.
- **Scroller Mechanics**: `.tool-scroller-track` renders all 11 enterprise architecture engines with active selection state, smooth scrolling, left/right track nav arrows, and responsive mobile padding (`@media (max-width: 640px)`).

### 13. Games 5 to 10 Canonical Footer Rules
- **Containment Rule**: For arcade games with centered layouts (`cuptoss`, `bottleflip`, `chitcharades`, `snackroulette`, `dialoguedetective`, `gulelstrike`), `<footer>` must reside *inside* `<div class="game-container">` before its closing tag to preserve centered max-width alignment.
- **Split-Screen Exception**: Full-screen 100dvh split-screen touch battle games like `samosasnatch` must NOT have an outer `<footer>` on the gameplay page, as this triggers vertical viewport scrolling on touch/tap. The footer attribution is placed inside the setup modal (`#setupModal .modal-box`).
- **Fullscreen Invisibility**: All arcade games with fullscreen modes must declare `body.is-fullscreen footer { display: none !important; }`.
- **Canonical Typography**:
  ```css
  footer {
    text-align: center; padding: 30px 16px 10px; font-size: 12.5px;
    color: var(--text-faint); border-top: 1px solid var(--border-soft);
    margin-top: 40px; line-height: 1.6;
  }
  footer a { color: var(--text-dim); text-decoration: none; }
  footer a:hover { color: var(--accent); text-decoration: underline; }
  footer b { color: var(--text); }
  footer p { margin: 4px 0; }
  ```

