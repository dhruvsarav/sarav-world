/**
 * 🌐 Sarav's World — Centralized Ecosystem Navigation Component (EcoNav)
 * Single Source of Truth for all topbar dropdowns across:
 * - Enterprise Decision Engines (mode: 'enterprise')
 * - Consumer Web Apps & Family Arcade Games (mode: 'consumer')
 * - Master Gateway Portals (mode: 'gateway')
 *
 * (c) 2009–2026 Saravanakumar Murugan (iamsaravofficial.com)
 */
(function() {
  'use strict';

  var APPS = [
    { name: '🎡 Playground Hub', url: 'https://iamsaravofficial.com/apps/' },
    { name: 'GenZ & Alpha Slang', url: 'https://iamsaravofficial.com/apps/genzalphaslang/' },
    { name: 'Salary Planner', url: 'https://iamsaravofficial.com/apps/salary-planner/' },
    { name: 'Home Budget Planner', url: 'https://iamsaravofficial.com/apps/home-budget-planner/' },
    { name: 'Retirement Planner', url: 'https://iamsaravofficial.com/apps/retirement-planner/' },
    { name: 'Gold Price Estimator', url: 'https://iamsaravofficial.com/apps/gold-price-estimator/' },
    { name: 'Gold Loan Calculator', url: 'https://iamsaravofficial.com/apps/gold-loan-calculator/' },
    { name: 'DigiGold Calculator', url: 'https://iamsaravofficial.com/apps/digigold-calculator/' },
    { name: 'FD Calculator', url: 'https://iamsaravofficial.com/apps/fd-calculator/' },
    { name: 'RD Calculator', url: 'https://iamsaravofficial.com/apps/rd-calculator/' }
  ];

  var EAPPS = [
    { name: '🏢 Executive Suite Hub', url: 'https://iamsaravofficial.com/eapps/' },
    { name: '🧠 Tokenomics (AI Economics)', url: 'https://iamsaravofficial.com/apps/tokenomics/' },
    { name: '👷 SD Optimizer', url: 'https://iamsaravofficial.com/apps/sdoptimizer/' },
    { name: '🗺️ Field Services Hub-Spoke', url: 'https://iamsaravofficial.com/apps/fsoptimizer/' },
    { name: '🖥️ Deskside Support Staffing', url: 'https://iamsaravofficial.com/apps/desksidestaffing/' },
    { name: '🧭 DEX Advisor', url: 'https://iamsaravofficial.com/apps/dexadvisor/' },
    { name: '🎫 ITSM Platform Advisor', url: 'https://iamsaravofficial.com/apps/itsmadvisor/' },
    { name: '⚖️ Vendor RFP Weighted Scorer', url: 'https://iamsaravofficial.com/apps/rfpscorer/' }
  ];

  var GAMES = [
    { name: '🎰 Games Arcade Hub', url: 'https://iamsaravofficial.com/games/' },
    { name: '🎰 Family Jackpot', url: 'https://iamsaravofficial.com/games/familywinner/' },
    { name: '💖 Senti-Meter', url: 'https://iamsaravofficial.com/games/sentimeter/' },
    { name: '🎁 Secret Box', url: 'https://iamsaravofficial.com/games/secretbox/' },
    { name: '🏓 Ping-Pong Cup Toss', url: 'https://iamsaravofficial.com/games/cuptoss/' },
    { name: '🍾 Bottle Flip Showdown', url: 'https://iamsaravofficial.com/games/bottleflip/' },
    { name: '⚡ Samosa Snatch', url: 'https://iamsaravofficial.com/games/samosasnatch/' },
    { name: '🗣️ Chit-Charades', url: 'https://iamsaravofficial.com/games/chitcharades/' },
    { name: '🎡 Snack Roulette', url: 'https://iamsaravofficial.com/games/snackroulette/' },
    { name: '🎙️ Dialogue Detective', url: 'https://iamsaravofficial.com/games/dialoguedetective/' },
    { name: '🎯 Desi Gulel Strike', url: 'https://iamsaravofficial.com/games/gulelstrike/' }
  ];

  var PROJECTS = [
    { name: '🏛️ Projects Hub', url: 'https://iamsaravofficial.com/projects/' },
    { name: 'Temples of Tamil Gods', url: 'https://iamsaravofficial.com/temples/' },
    { name: 'FactDrop', url: 'https://iamsaravofficial.com/factdrop/' },
    { name: 'Thirukkural Hub', url: 'https://iamsaravofficial.com/thirukkural/' }
  ];

  function getMode(target) {
    var explicit = target.getAttribute('data-mode') || target.getAttribute('data-suite');
    if (explicit) return explicit.toLowerCase();

    var path = window.location.pathname.toLowerCase();
    if (path.indexOf('/playground') === 0 || path.indexOf('/projects') === 0) {
      return 'gateway';
    }
    if (
      path.indexOf('/eapps') === 0 ||
      path.indexOf('/tokenomics') !== -1 ||
      path.indexOf('/sdoptimizer') !== -1 ||
      path.indexOf('/fsoptimizer') !== -1 ||
      path.indexOf('/desksidestaffing') !== -1 ||
      path.indexOf('/dexadvisor') !== -1 ||
      path.indexOf('/itsmadvisor') !== -1 ||
      path.indexOf('/rfpscorer') !== -1
    ) {
      return 'enterprise';
    }
    return 'consumer';
  }

  function isCurrent(url) {
    var current = window.location.pathname.replace(/\/index\.html$/, '').replace(/\/$/, '');
    var target = url.replace('https://iamsaravofficial.com', '').replace(/\/index\.html$/, '').replace(/\/$/, '');
    return current === target;
  }

  function buildDropdown(title, items) {
    var isAnyActive = items.some(function(it) { return isCurrent(it.url); });
    var html = '<div class="eco-dropdown' + (isAnyActive ? ' is-active-cat' : '') + '">';
    html += '<button type="button" class="eco-dropbtn" aria-haspopup="true"' + (isAnyActive ? ' style="color:var(--accent,#E3A63E);"' : '') + '>';
    html += title + ' <span class="eco-caret">▾</span></button>';
    html += '<div class="eco-menu">';
    items.forEach(function(item) {
      var active = isCurrent(item.url);
      html += '<a href="' + item.url + '"' + (active ? ' class="current"' : '') + '>' + item.name + '</a>';
    });
    html += '</div></div>';
    return html;
  }

  function buildRightSide(mode) {
    var path = window.location.pathname.toLowerCase();
    if (mode === 'enterprise') {
      if (path.indexOf('tokenomics') !== -1) {
        return '<div><span class="eco-suite-badge">🧠 Enterprise AI Economics &middot; Version 2026.09</span></div>';
      }
      return '<div><span class="eco-suite-badge"><img src="https://iamsaravofficial.com/eapps/eapps-square.png" alt="" style="width:14px; height:14px; border-radius:3px; vertical-align:middle; margin-right:4px;">Digital Workplace Suite &middot; Version 2026.09</span></div>';
    }

    if (mode === 'gateway') {
      var isProjects = path.indexOf('/projects') === 0;
      var out = '<div style="display:flex; align-items:center; gap:12px;">';
      if (isProjects) {
        out += '<a href="https://iamsaravofficial.com/playground/" style="text-decoration:none; color:var(--text-dim,#94A0B2); font-size:12.5px; font-weight:600;">🎪 Playground</a>';
      }
      out += '<a href="https://iamsaravofficial.com/apps/tokenomics/" class="eco-tokenomics">🧠 Enterprise AI Economics</a>';
      out += '</div>';
      return out;
    }

    // consumer mode
    return '<div style="display:flex; align-items:center; gap:12px;">' +
           '<a href="https://iamsaravofficial.com/playground/" style="text-decoration:none; color:var(--text-dim,#94A0B2); font-size:12.5px; font-weight:600;">🎪 Playground</a>' +
           '<a href="https://iamsaravofficial.com/apps/tokenomics/" class="eco-tokenomics">🧠 Enterprise AI Economics</a>' +
           '</div>';
  }

  function injectStyles() {
    if (document.getElementById('econav-unified-css')) return;
    var css = `
      .ecosystem-bar {
        background: var(--surface-2, #141922); border-bottom: 1px solid var(--border-soft, #1E2633);
        padding: 7px 20px; font-size: 12.5px; color: var(--text-dim, #94A0B2);
        position: relative; z-index: 1000;
      }
      .ecosystem-inner {
        max-width: 1240px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;
      }
      .ecosystem-links { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
      .eco-brand { font-weight: 700 !important; color: var(--text, #EAEFF5) !important; text-decoration: none; transition: color 0.15s ease; }
      .eco-brand:hover { color: var(--accent, #E3A63E) !important; text-decoration: none; }
      .eco-divider { color: var(--border, #2A3545); font-weight: 300; margin: 0 4px; user-select: none; }
      .eco-dropdown { position: relative; display: inline-block; }
      .eco-dropbtn {
        background: transparent; border: none; color: var(--text-dim, #94A0B2);
        font-family: inherit; font-size: 12.5px; font-weight: 600;
        padding: 4px 8px; border-radius: 6px; cursor: pointer;
        display: flex; align-items: center; gap: 4px; transition: all 0.15s ease;
      }
      .eco-dropbtn:hover, .eco-dropdown:hover .eco-dropbtn, .eco-dropdown.open .eco-dropbtn {
        color: var(--accent, #E3A63E); background: var(--accent-soft, rgba(227,166,62,0.14));
      }
      .eco-caret { font-size: 9px; transition: transform 0.2s ease; display: inline-block; }
      .eco-dropdown:hover .eco-caret, .eco-dropdown.open .eco-caret { transform: rotate(180deg); }
      .eco-menu {
        display: none; position: absolute; top: 100%; left: 0;
        padding: 6px; min-width: 230px; background: var(--surface, #0C0F14);
        border: 1px solid var(--border, #2A3545); border-radius: 10px;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45); z-index: 2000;
        backdrop-filter: blur(12px);
      }
      .eco-menu::before { content: ""; position: absolute; top: -10px; left: 0; right: 0; height: 10px; background: transparent; }
      .eco-dropdown:hover .eco-menu, .eco-dropdown.open .eco-menu { display: block; }
      .eco-menu a {
        display: block; padding: 7px 10px; border-radius: 6px;
        color: var(--text-dim, #94A0B2); font-size: 12.5px; font-weight: 500; text-decoration: none;
        transition: all 0.12s ease; white-space: nowrap;
      }
      .eco-menu a:hover { background: var(--surface-2, #141922); color: var(--accent, #E3A63E); }
      .eco-menu a.current { color: var(--accent, #E3A63E); font-weight: 600; background: var(--accent-soft, rgba(227,166,62,0.14)); }
      .eco-tokenomics {
        color: #14B8A6 !important; font-weight: 600; display: inline-flex; align-items: center; gap: 4px;
        padding: 3px 8px; border-radius: 6px; background: rgba(20, 184, 166, 0.12); text-decoration: none; font-size: 12px;
      }
      .eco-tokenomics:hover { text-decoration: underline; }
      .eco-suite-badge {
        display: inline-flex; align-items: center; font-size: 12px; font-weight: 600;
        color: var(--text-dim, #94A0B2); font-family: 'IBM Plex Mono', monospace;
      }
    `;
    var style = document.createElement('style');
    style.id = 'econav-unified-css';
    style.textContent = css;
    document.head.appendChild(style);
  }

  function render(container) {
    var mode = getMode(container);
    var html = '<div class="ecosystem-inner"><div class="ecosystem-links">';
    html += '<a href="https://iamsaravofficial.com/" class="eco-brand">← Sarav\'s World</a>';

    if (mode === 'enterprise') {
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('E-Apps', EAPPS);
    } else if (mode === 'gateway') {
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('Apps', APPS);
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('E-Apps', EAPPS);
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('Games', GAMES);
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('Projects', PROJECTS);
    } else {
      // consumer mode
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('Apps', APPS);
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('Games', GAMES);
      html += '<span class="eco-divider">│</span>';
      html += buildDropdown('Projects', PROJECTS);
    }

    html += '</div>';
    html += buildRightSide(mode);
    html += '</div>';

    container.className = 'ecosystem-bar';
    container.innerHTML = html;

    // Attach click/esc listeners for mobile
    container.querySelectorAll('.eco-dropdown').forEach(function(drop) {
      var btn = drop.querySelector('.eco-dropbtn');
      if (!btn) return;
      btn.addEventListener('click', function(e) {
        e.stopPropagation();
        var wasOpen = drop.classList.contains('open');
        container.querySelectorAll('.eco-dropdown').forEach(function(d) { d.classList.remove('open'); });
        if (!wasOpen) drop.classList.add('open');
      });
    });
  }

  function init() {
    injectStyles();

    // Look for element with id="ecosystem-nav" or nav[data-ecosystem-nav] or .ecosystem-bar
    var targets = document.querySelectorAll('#ecosystem-nav, nav[data-ecosystem-nav], .ecosystem-bar[data-eco-managed]');
    if (targets.length === 0) {
      var bars = document.querySelectorAll('.ecosystem-bar');
      if (bars.length > 0 && bars[0].getAttribute('data-eco-ignore') === null) {
        targets = bars;
      }
    }

    targets.forEach(function(el) {
      render(el);
    });

    document.addEventListener('click', function() {
      document.querySelectorAll('.eco-dropdown').forEach(function(d) { d.classList.remove('open'); });
    });
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.querySelectorAll('.eco-dropdown').forEach(function(d) { d.classList.remove('open'); });
      }
    });
  }

  // Auto-init on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose global API
  window.EcoNav = {
    init: init,
    render: render,
    APPS: APPS,
    EAPPS: EAPPS,
    GAMES: GAMES,
    PROJECTS: PROJECTS
  };
})();
