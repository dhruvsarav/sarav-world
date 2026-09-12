# 🌐 Sarav World Project & Architecture Rules

> Repository: D:\Websites\SaravsWorld
> Production Site: https://iamsaravofficial.com
> Master Memory: D:\sdrv\docs\memory\Sarav_World_MasterContext.md

---

### 7. Universal Web App Architecture & Design Standards (STRICT MEMORIZED RULES)
Every web app hosted under `public/apps/` must adhere strictly to these rules:
1. **Playground Hub Section Nomenclature (`/apps/`)**:
   - Section 1: `⚡ Family & Interactive Web Apps Suite` (9 Live Apps)
   - Section 2: `❤️ Close to Heart Ecosystem`
2. **Canonical Suite Sequence (Strict 1–9 Standard across Hub and Ecosystem Dropdowns)**:
   1. `genzalphaslang` (GenZ & Alpha Slang Decoder)
   2. `salary-planner` (Salary Planner)
   3. `home-budget-planner` (Home Budget Planner)
   4. `retirement-planner` (Retirement Planner)
   5. `gold-price-estimator` (Metal Price Estimator)
   6. `gold-loan-calculator` (Gold Loan Calculator)
   7. `digigold-calculator` (DigiGold SIP Calculator)
   8. `fd-calculator` (FD Calculator)
   9. `rd-calculator` (RD Calculator)
3. **Footer Distinction**:
   - **Consumer Retail Web Apps (All Calculators & Utility Apps)**:
     `Web Apps Crafted by <b>Sarav</b> (<a href="https://iamsaravofficial.com/" target="_blank">Saravanakumar Murugan</a>).`
     `&copy; 2009–2026 <a href="https://iamsaravofficial.com/apps/">Sarav's Playground</a>. Zero telemetry. All calculations run strictly client-side.`
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
   - **All 9 Web Apps** must NEVER use blocking `alert()` or `prompt()` dialogs for copy or scenario saving.
   - Standardized `showToast(msg)` float element (`#toast`, 2.6s auto-dismiss) styled cleanly to match each app's palette.
    - **No Reset Button Policy**: Destructive global Reset buttons are removed from workflow calculators (e.g. Salary Planner) to prevent accidental data loss and keep the unified 4-button action bar clean.
7. **Strict Two-Family Color Palette Standard**:
   - **Family A — Precious Metals Suite (3 Apps)**: `/apps/gold-price-estimator/`, `/apps/gold-loan-calculator/`, `/apps/digigold-calculator/`
     * **Light Mode (Physical Gold)**: Outer canvas `#E6DFD5`, App canvas `#FFFBF0`, White cards `#FFFFFF`, Espresso headings `#3D2B00`, Muted text `#8A7554`, Primary Gold `#C1810A`, Dark Gold `#8B5E00`, Header banner `linear-gradient(180deg, #F9D77E, #F0B429)`, Gold leaf border `#E0B84B`, Chips `#F6E3B0`, Gains `#1B8A3D`, Risk `#D32F2F`.
     * **Dark Mode (Obsidian & Liquid Gold)**: Outer canvas `#0A0907`, App canvas `#12100C`, Dark bronze cards `#1D1913`, Ivory white text `#F7F2E8`, Sandstone muted text `#B0A28E`, Radiant gold accent `#E5A93C`, Bright gold `#FFC04D`, Header banner `linear-gradient(180deg, #38290E, #251A07)`, Bronze border `#52411E`, Chips `#2E2412`, Gains `#4CAF50`, Risk `#EF5350`.
     * **OG Card Theme**: **Light Mode Physical Gold** (`#F7F3EB` soft gold canvas, `#FFFFFF` card, `#E0B84B` border, `#2E1E05` deep espresso title, `#8B5E00` badge text).
   - **Family B & C — Family & Interactive Apps Suite (6 Apps Unified)**: `/apps/genzalphaslang/`, `/apps/salary-planner/`, `/apps/home-budget-planner/`, `/apps/retirement-planner/`, `/apps/fd-calculator/`, `/apps/rd-calculator/`, and `/apps/` (Playground Hub)
     * **Light Mode (Crisp Financial Slate)**: Canvas `#F5F7FA`, Level 1 Cards `#FFFFFF`, Level 2 Inputs `#F0F3F7`, Level 3 Elevated `#E4E9F0`, Headings `#1A202C`, Dim text `#4A5568`, Faint text `#718096`, Primary Amber Accent `#D97706`, Accent Ink `#FFFFFF`, Secondary Teal Accent `#0D9488`, Steel border `#D1D8E2`, Soft border `#E2E8F0`, Surplus/Liquid `#16A34A`, Deficit/TDS `#DC2626`, Shadow `0 8px 32px rgba(0,0,0,0.08)`.
     * **Dark Mode (Deep Space Navy)**: Canvas `#0C0F14`, Level 1 Cards `#141922`, Level 2 Inputs `#1B222D`, Level 3 Elevated `#222B39`, Headings `#EAEFF5`, Dim text `#94A0B2`, Faint text `#5C6B80`, Primary Amber Accent `#E3A63E`, Accent Ink `#141005`, Secondary Teal Accent `#4FB0A8`, Navy border `#2A3545`, Soft border `#1E2633`, Surplus/Liquid `#5FBF77`, Deficit/TDS `#E2665A`, Shadow `0 8px 32px rgba(0,0,0,0.40)`.
     * **OG Card Theme**: **Dark Mode Deep Space Navy** (`#0C0F14` canvas, `#141922` slate card, `#FFFFFF` title, `#E3A63E` & `#4FB0A8` accents).
8. **Header Row & Presets Layout Architecture**:
   - Header must use `.header-main-row` containing `.header-left` (`flex: 1; min-width: 0;`) and `.header-right` (`flex-shrink: 0; align-items: flex-end;`). The theme selector (`Auto | ☀️ Light | 🌙 Dark`) is **always anchored to the top-right end**.
   - Preset buttons (`.header-presets`) must always sit in a dedicated block directly underneath the header row, spanning full width with its own breathing room so chips never force horizontal flex-wrapping or push the theme toggle below them.
   - Home Budget Planner features 3 GenZ vibe presets: `💀 No Cap YOLO (95% Burn)`, `✨ Soft Life (65% Burn)`, `🗿 Monk Mode (35% Burn)`.
9. **Executive Digital Workplace & AI Suite Architecture (`/eapps/`)**:
   - Executive portal at `/eapps/` (`https://iamsaravofficial.com/eapps/`) crafted for CIOs, IT Directors, Heads of EUC, and Chief AI Architects.
   - Houses 3 deterministic decision engines:
     1. `tokenomics` (`/apps/tokenomics/`): Multi-LLM AI spend modeling, prompt caching discounts (up to 90%), contingency buffers, and human labor arbitrage ROI.
     2. `sdoptimizer` (`/apps/sdoptimizer/`): Erlang C queue simulation, L0 AI agentic deflection, Copilot L1 AHT compression, channel cost-to-serve economics.
     3. `dexadvisor` (`/apps/dexadvisor/`): Multi-Attribute Utility Theory (MAUT) vendor capability matrix (1E, Nexthink, Riverbed), 3-year TCO modeling, and 4-phase SLA-to-XLA migration playbook.
   - All enterprise apps retain strict client-side zero-telemetry computation.
   - Ecosystem Navigation Standard: `Apps ▾`, `E-Apps ▾`, `Projects ▾`, and right-anchored `🧠 Enterprise AI Economics` pill.
10. **Official Brand Icon Systems for Apps & E-Apps Suites**:
   - **Apps Hub (`/apps/`)**:
     * Official Brand Icon: **The Cosmic Glass Cube** (Isometric frosted glass sandbox with floating cyber gold `#E3A63E` and digital teal `#4FB0A8` spheres).
     * Production assets: `apps-full.png` (1024px), `apps-square.png` (512px), `favicon-192.png`, `apple-touch-icon-180.png`, `favicon-32.png`, `favicon-16.png`, `favicon.ico`.
   - **E-Apps Suite (`/eapps/`)**:
     * Official Brand Icon: **The Sovereign Hex Core** (Faceted titanium hexagonal core with precision gyroscopic telemetry rings and glowing amber/cyan dual-core neural processor).
     * Production assets: `eapps-full.png` (1024px), `eapps-square.png` (512px), `favicon-192.png`, `apple-touch-icon-180.png`, `favicon-32.png`, `favicon-16.png`, `favicon.ico`.
   - Both portals feature a responsive squircle brand badge in their respective hero headers.

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

# Git status & push
git -C "D:\Websites\SaravsWorld" status
git -C "D:\Websites\SaravsWorld" push origin main

# Re-run FactDrop generator
python "D:\Websites\SaravsWorld\scripts\factdrop\generate_factdrop.py"
```

---

