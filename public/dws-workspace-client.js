/**
 * Universal DWS Shared Workspace Client Bridge
 * Connects all 10 Enterprise Engines to Universal Shared Workspace (dwssharedworkspace).
 * Reads dws_workspace_v1, lists custom saved presets & built-in archetypes,
 * and auto-populates engine inputs with real-time recalculation.
 *
 * (c) 2026 Sarav's World · Zero Telemetry · 100% Client-Side
 */

(function(window) {
  'use strict';

  const WORKSPACE_KEY = 'dws_workspace_v1';

  const ARCHETYPES = {
    global: {
      name: 'Global Enterprise (Default)',
      orgProfile: { name: 'Titan Global Enterprises', assessor: 'Digital Workplace Strategy Lead', industry: 'Diversified Conglomerate', regionBlend: 'Global Multi-Region', employees: 45000, locations: 42, languages: 5, hybridRatio: { hybrid: 50, remote: 30, onSite: 20 } },
      supportOps: { monthlyTickets: 52000, shiftModel: '24x7 Follow-the-Sun', channelMix: { voice: 30, portalChat: 50, deskside: 20 } },
      financials: { blendedHourlyRate: 38, annualFteCost: 79040, currency: 'USD' },
      techStack: { primaryItsm: 'ServiceNow ITSM', primaryDex: 'Nexthink Infinity', primaryAiLlm: 'Azure OpenAI Service' }
    },
    midmarket: {
      name: 'Mid-Market Growth (10k seats)',
      orgProfile: { name: 'Apex Logistics & Services', assessor: 'Director of Enterprise IT', industry: 'Logistics & Supply Chain', regionBlend: 'North America Heavy', employees: 10000, locations: 14, languages: 1, hybridRatio: { hybrid: 30, remote: 20, onSite: 50 } },
      supportOps: { monthlyTickets: 11500, shiftModel: '16x5 Multi-Shift', channelMix: { voice: 40, portalChat: 35, deskside: 25 } },
      financials: { blendedHourlyRate: 34, annualFteCost: 70720, currency: 'USD' },
      techStack: { primaryItsm: 'Freshservice Enterprise', primaryDex: 'ControlUp Edge DX', primaryAiLlm: 'Anthropic Claude' }
    },
    publicsector: {
      name: 'Regional Public Sector (24k seats)',
      orgProfile: { name: 'State Dept of Transportation', assessor: 'Chief Technology Officer', industry: 'Public Sector & Utilities', regionBlend: 'North America', employees: 24000, locations: 34, languages: 2, hybridRatio: { hybrid: 20, remote: 10, onSite: 70 } },
      supportOps: { monthlyTickets: 32000, shiftModel: '24x7 On-Call Hybrid', channelMix: { voice: 50, portalChat: 25, deskside: 25 } },
      financials: { blendedHourlyRate: 39, annualFteCost: 81120, currency: 'USD' },
      techStack: { primaryItsm: 'BMC Helix', primaryDex: '1E Tachyon', primaryAiLlm: 'Azure OpenAI Service' }
    },
    aifirst: {
      name: 'AI-First Modern Org (15k seats)',
      orgProfile: { name: 'Synthetix Modern Enterprises', assessor: 'Chief AI & Digital Officer', industry: 'Technology & SaaS', regionBlend: 'Global Multi-Region', employees: 15000, locations: 12, languages: 4, hybridRatio: { hybrid: 40, remote: 50, onSite: 10 } },
      supportOps: { monthlyTickets: 12000, shiftModel: '24x7 Follow-the-Sun', channelMix: { voice: 15, portalChat: 70, deskside: 10 } },
      financials: { blendedHourlyRate: 45, annualFteCost: 93600, currency: 'USD' },
      techStack: { primaryItsm: 'ServiceNow ITSM', primaryDex: 'Nexthink Infinity', primaryAiLlm: 'Claude Enterprise / Anthropic' }
    }
  };

  const DwsWorkspaceClient = {
    appId: null,

    init: function(appId) {
      this.appId = appId || this.detectAppId();
      this.injectStyles();
      this.renderBar();
      this.bindStorageListener();
    },

    detectAppId: function() {
      const path = window.location.pathname;
      if (path.includes('tokenomics')) return 'tokenomics';
      if (path.includes('sdoptimizer')) return 'sdoptimizer';
      if (path.includes('fsoptimizer')) return 'fsoptimizer';
      if (path.includes('desksidestaffing')) return 'desksidestaffing';
      if (path.includes('dexadvisor')) return 'dexadvisor';
      if (path.includes('itsmadvisor')) return 'itsmadvisor';
      if (path.includes('rfpscorer')) return 'rfpscorer';
      if (path.includes('aiinitsm')) return 'aiinitsm';
      if (path.includes('automationscore')) return 'automationscore';
      if (path.includes('dwpassessment')) return 'dwpassessment';
      return 'unknown';
    },

    getWorkspace: function() {
      try {
        const raw = localStorage.getItem(WORKSPACE_KEY);
        if (!raw) return null;
        return JSON.parse(raw);
      } catch (e) {
        return null;
      }
    },

    saveWorkspace: function(ws) {
      try {
        localStorage.setItem(WORKSPACE_KEY, JSON.stringify(ws));
      } catch (e) {
        console.error('Failed to write workspace to localStorage', e);
      }
    },

    relativeTime: function(iso) {
      if (!iso) return 'recently';
      try {
        const diffMs = Date.now() - new Date(iso).getTime();
        const mins = Math.round(diffMs / 60000);
        if (mins < 1) return 'just now';
        if (mins < 60) return mins + 'm ago';
        const hrs = Math.round(mins / 60);
        if (hrs < 24) return hrs + 'h ago';
        return Math.round(hrs / 24) + 'd ago';
      } catch (e) {
        return 'earlier';
      }
    },

    injectStyles: function() {
      if (document.getElementById('dwsWsBridgeStyles')) return;
      const css = `
        .dws-ws-bridge {
          background: linear-gradient(90deg, rgba(20, 25, 34, 0.98) 0%, rgba(27, 34, 45, 0.98) 100%);
          border-bottom: 1px solid rgba(79, 176, 168, 0.35);
          padding: 8px 20px;
          font-family: 'Space Grotesk', -apple-system, sans-serif;
          font-size: 12.5px;
          color: #EAEFF5;
          position: relative;
          z-index: 85;
          box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
        }
        [data-theme="light"] .dws-ws-bridge {
          background: linear-gradient(90deg, #F0F4F8 0%, #E6EDF5 100%);
          border-bottom: 1px solid #CBD5E1;
          color: #1E293B;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        .dws-ws-inner {
          max-width: 1300px;
          margin: 0 auto;
          display: flex;
          align-items: center;
          justify-content: space-between;
          flex-wrap: wrap;
          gap: 10px;
        }
        .dws-ws-left {
          display: flex;
          align-items: center;
          gap: 10px;
          flex-wrap: wrap;
        }
        .dws-ws-pill {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          background: rgba(79, 176, 168, 0.15);
          border: 1px solid rgba(79, 176, 168, 0.5);
          color: #4FB0A8;
          padding: 3px 8px;
          border-radius: 6px;
          font-weight: 700;
          font-size: 11px;
          text-transform: uppercase;
          letter-spacing: 0.5px;
        }
        [data-theme="light"] .dws-ws-pill {
          background: rgba(13, 148, 136, 0.1);
          border-color: #0D9488;
          color: #0F766E;
        }
        .dws-ws-select {
          background: #141922;
          color: #EAEFF5;
          border: 1px solid #2A3545;
          padding: 5px 10px;
          border-radius: 6px;
          font-family: inherit;
          font-size: 12px;
          cursor: pointer;
          outline: none;
          max-width: 320px;
        }
        [data-theme="light"] .dws-ws-select {
          background: #FFFFFF;
          color: #0F172A;
          border-color: #CBD5E1;
        }
        .dws-ws-select:focus {
          border-color: #4FB0A8;
        }
        .dws-ws-btn-apply {
          background: #4FB0A8;
          color: #0A1118;
          border: none;
          padding: 5px 12px;
          border-radius: 6px;
          font-family: inherit;
          font-size: 12px;
          font-weight: 700;
          cursor: pointer;
          display: inline-flex;
          align-items: center;
          gap: 5px;
          transition: all 0.15s ease;
        }
        .dws-ws-btn-apply:hover {
          filter: brightness(1.1);
          transform: translateY(-1px);
        }
        .dws-ws-link {
          color: #94A0B2;
          text-decoration: none;
          font-size: 11.5px;
          display: inline-flex;
          align-items: center;
          gap: 4px;
        }
        .dws-ws-link:hover {
          color: #4FB0A8;
          text-decoration: underline;
        }
      `;
      const style = document.createElement('style');
      style.id = 'dwsWsBridgeStyles';
      style.textContent = css;
      document.head.appendChild(style);
    },

    renderBar: function() {
      if (document.getElementById('dwsWsBridge')) {
        this.updateDropdown();
        return;
      }

      // Hide legacy ws bar if present (e.g. in dwpassessment)
      const legacyBar = document.getElementById('wsStatusBar');
      if (legacyBar) {
        legacyBar.style.display = 'none';
        legacyBar.id = 'wsStatusBarLegacy';
      }

      const bar = document.createElement('div');
      bar.id = 'dwsWsBridge';
      bar.className = 'dws-ws-bridge';

      bar.innerHTML = `
        <div class="dws-ws-inner">
          <div class="dws-ws-left">
            <span class="dws-ws-pill">🗄️ Shared Workspace</span>
            <select id="dwsWsSelect" class="dws-ws-select" title="Select a configuration preset saved in Universal Shared Workspace">
              <option value="">Loading workspace presets...</option>
            </select>
            <button type="button" class="dws-ws-btn-apply" id="dwsWsApplyBtn" onclick="DwsWorkspaceClient.applySelectedPreset()">
              <span>⚡ Load into Engine</span>
            </button>
            <span id="dwsWsMeta" style="font-size: 11px; color: #8A99AD;"></span>
          </div>
          <div>
            <a href="https://iamsaravofficial.com/apps/dwssharedworkspace/" target="_blank" class="dws-ws-link">
              <span>Configure Workspace ↗</span>
            </a>
          </div>
        </div>
      `;

      // Find optimal anchor location: right after ecosystemBar or before stickyHeader
      const ecosystemBar = document.querySelector('.ecosystem-bar');
      const stickyHeader = document.querySelector('.sticky-header-wrapper') || document.querySelector('.topbar');

      if (ecosystemBar && ecosystemBar.nextSibling) {
        ecosystemBar.parentNode.insertBefore(bar, ecosystemBar.nextSibling);
      } else if (stickyHeader) {
        stickyHeader.parentNode.insertBefore(bar, stickyHeader);
      } else {
        document.body.insertBefore(bar, document.body.firstChild);
      }

      this.updateDropdown();
    },

    updateDropdown: function() {
      const select = document.getElementById('dwsWsSelect');
      const meta = document.getElementById('dwsWsMeta');
      if (!select) return;

      const ws = this.getWorkspace();
      let html = '';

      if (ws) {
        const activeName = ws.activePreset || (ws.orgProfile && ws.orgProfile.name) || 'Current Active Workspace';
        const updated = this.relativeTime(ws.lastUpdatedAt);
        html += `<option value="active">⭐ Active: ${activeName} (${updated})</option>`;

        // Custom Saved Presets
        const savedKeys = Object.keys(ws.savedPresets || {});
        if (savedKeys.length > 0) {
          html += `<optgroup label="Saved Presets (${savedKeys.length})">`;
          savedKeys.forEach(k => {
            html += `<option value="saved:${k}">📌 ${k}</option>`;
          });
          html += `</optgroup>`;
        }
      } else {
        html += `<option value="archetype:global">⚡ Default: Global Enterprise (Default)</option>`;
      }

      // Built-In Archetypes
      html += `<optgroup label="Built-In Enterprise Archetypes">`;
      html += `<option value="archetype:global">🏢 Global Enterprise (45k seats)</option>`;
      html += `<option value="archetype:midmarket">🌐 Mid-Market Growth (10k seats)</option>`;
      html += `<option value="archetype:publicsector">🏛️ Regional Public Sector (24k seats)</option>`;
      html += `<option value="archetype:aifirst">🚀 AI-First Modern Org (15k seats)</option>`;
      html += `</optgroup>`;

      select.innerHTML = html;

      if (meta && ws && ws.lastUpdatedAt) {
        meta.textContent = `• Updated ${this.relativeTime(ws.lastUpdatedAt)} via ${ws.lastUpdatedBy || 'Workspace'}`;
      }
    },

    bindStorageListener: function() {
      window.addEventListener('storage', (e) => {
        if (e.key === WORKSPACE_KEY) {
          this.updateDropdown();
        }
      });
    },

    getSelectedPresetData: function() {
      const select = document.getElementById('dwsWsSelect');
      if (!select) return null;
      const val = select.value;
      const ws = this.getWorkspace();

      if (val === 'active' && ws) {
        return {
          name: ws.activePreset || (ws.orgProfile && ws.orgProfile.name) || 'Active Workspace',
          orgProfile: ws.orgProfile || {},
          supportOps: ws.supportOps || {},
          financials: ws.financials || {},
          techStack: ws.techStack || {}
        };
      }

      if (val.startsWith('saved:') && ws && ws.savedPresets) {
        const k = val.replace('saved:', '');
        return ws.savedPresets[k] || null;
      }

      if (val.startsWith('archetype:')) {
        const k = val.replace('archetype:', '');
        return ARCHETYPES[k] || null;
      }

      return ARCHETYPES.global;
    },

    applySelectedPreset: function() {
      const data = this.getSelectedPresetData();
      if (!data) {
        this.notify('No workspace preset data found.');
        return;
      }

      const org = data.orgProfile || {};
      const ops = data.supportOps || {};
      const fin = data.financials || {};
      const tech = data.techStack || {};

      const employees = parseInt(org.employees, 10) || 10000;
      const tickets = parseInt(ops.monthlyTickets, 10) || 15000;
      const rate = parseFloat(fin.blendedHourlyRate) || 38;
      const fteCost = parseFloat(fin.annualFteCost) || (rate * 2080);
      const locations = parseInt(org.locations, 10) || 12;
      const languages = parseInt(org.languages, 10) || 2;
      const hybrid = org.hybridRatio || { hybrid: 40, remote: 30, onSite: 30 };
      const channelMix = ops.channelMix || { voice: 35, portalChat: 45, deskside: 20 };

      // Update active preset in localStorage so other tabs know
      const ws = this.getWorkspace();
      if (ws) {
        ws.activePreset = data.name;
        ws.orgProfile = org;
        ws.supportOps = ops;
        ws.financials = fin;
        ws.techStack = tech;
        ws.lastUpdatedAt = new Date().toISOString();
        ws.lastUpdatedBy = this.appId || 'Engine Bridge';
        this.saveWorkspace(ws);
      }

      // Dispatch helpers
      const setVal = (id, val) => {
        const el = document.getElementById(id);
        if (el) {
          el.value = val;
          el.dispatchEvent(new Event('input', { bubbles: true }));
          el.dispatchEvent(new Event('change', { bubbles: true }));
        }
      };

      // App-Specific Routing
      switch (this.appId) {
        case 'tokenomics':
          setVal('org_users', employees);
          setVal('org_devices', Math.round(employees * 1.25));
          setVal('vol_contacts', tickets);
          setVal('vol_incidents', Math.round(tickets * 0.45));
          setVal('vol_requests', Math.round(tickets * 0.55));
          setVal('vol_voice', Math.round(tickets * ((channelMix.voice || 35) / 100)));
          setVal('vol_teams', Math.round(tickets * ((channelMix.portalChat || 45) / 100)));
          setVal('human_cost_per_ticket', Math.round(rate * 0.4 * 10) / 10);
          break;

        case 'sdoptimizer':
          setVal('org_employees', employees);
          setVal('org_languages', languages);
          setVal('vol_total', tickets);
          setVal('vol_voice_pct', channelMix.voice || 35);
          setVal('vol_chat_pct', channelMix.portalChat || 45);
          setVal('vol_digital_pct', channelMix.deskside || 20);
          break;

        case 'fsoptimizer':
          setVal('svc_volume', Math.round(tickets * 0.15));
          setVal('geo_onsite', locations);
          setVal('econ_tech_cost', fteCost);
          break;

        case 'desksidestaffing':
          setVal('site_employees', employees);
          setVal('site_buildings', locations);
          setVal('site_hybrid_pct', (hybrid.hybrid || 40) + (hybrid.onSite || 30));
          setVal('vol_monthly', Math.round(tickets * ((channelMix.deskside || 20) / 100)));
          setVal('econ_tech_cost', fteCost);
          break;

        case 'dexadvisor':
          setVal('org_employees', employees);
          setVal('est_endpoints', Math.round(employees * 1.25));
          setVal('est_remote_pct', hybrid.remote || 30);
          if (org.industry) setVal('org_industry', org.industry);
          break;

        case 'itsmadvisor':
          setVal('org_employees', employees);
          setVal('org_agents', Math.max(5, Math.round(employees / 120)));
          setVal('est_volume', tickets);
          if (tech.primaryItsm) setVal('org_current', tech.primaryItsm);
          break;

        case 'rfpscorer':
          setVal('rfp_title', `${org.name || 'Enterprise'} — DWP Transformation RFP`);
          setVal('rfp_evaluator', org.assessor || 'Lead Evaluator');
          break;

        case 'aiinitsm':
          setVal('bc_title', `${org.name || 'Enterprise'} — AI in ITSM Business Case`);
          setVal('bc_preparedby', org.assessor || 'Chief AI Architect');
          setVal('prob_volume', tickets * 12);
          setVal('prob_costtoserve', Math.round(rate * 0.5));
          break;

        case 'automationscore':
          setVal('org_employees', employees);
          setVal('org_volume', tickets);
          break;

        case 'dwpassessment':
          setVal('org_name', org.name || 'Enterprise Workplace');
          setVal('org_assessor', org.assessor || 'Principal Architect');
          if (typeof window.wsSyncFromWorkspace === 'function') {
            try { window.wsSyncFromWorkspace(); } catch (e) {}
          }
          break;
      }

      // Trigger native calculation if available
      if (typeof window.recalcAll === 'function') {
        try { window.recalcAll(); } catch (e) {}
      } else if (typeof window.renderReport === 'function') {
        try { window.renderReport(); } catch (e) {}
      } else if (typeof window.recalculate === 'function') {
        try { window.recalculate(); } catch (e) {}
      }

      this.updateDropdown();
      this.notify(`✓ Loaded preset "${data.name}" from Shared Workspace`);
    },

    notify: function(msg) {
      if (typeof window.showToast === 'function') {
        window.showToast(msg);
        return;
      }
      const existing = document.getElementById('toast') || document.querySelector('.toast');
      if (existing) {
        existing.textContent = msg;
        existing.classList.add('show');
        setTimeout(() => existing.classList.remove('show'), 2600);
        return;
      }
      // Fallback banner toast
      let banner = document.getElementById('dwsWsToast');
      if (!banner) {
        banner = document.createElement('div');
        banner.id = 'dwsWsToast';
        banner.style.cssText = 'position:fixed;bottom:24px;right:24px;background:#1B222D;color:#4FB0A8;border:1px solid #4FB0A8;border-radius:8px;padding:10px 18px;font-size:13px;font-weight:600;z-index:9999;box-shadow:0 6px 20px rgba(0,0,0,0.4);transition:all 0.2s;';
        document.body.appendChild(banner);
      }
      banner.textContent = msg;
      banner.style.display = 'block';
      banner.style.opacity = '1';
      setTimeout(() => { banner.style.opacity = '0'; setTimeout(() => { banner.style.display = 'none'; }, 200); }, 2600);
    }
  };

  window.DwsWorkspaceClient = DwsWorkspaceClient;

  // Auto-initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { DwsWorkspaceClient.init(); });
  } else {
    DwsWorkspaceClient.init();
  }

})(window);
