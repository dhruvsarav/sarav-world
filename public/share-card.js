/**
 * Sarav's World — Universal Canvas Image Share Engine
 * 100% Client-Side • Zero Telemetry • Web Share API Level 2 with Clipboard/Download Fallback
 * 
 * Replicating Sahi Android "Share as Image" across consumer web apps and games.
 */
(function(window) {
  'use strict';

  const SaravShareCard = {};

  // --------------------------------------------------------------------------
  // Core Utilities & Primitives
  // --------------------------------------------------------------------------

  function setupCanvas(width, height) {
    const canvas = document.createElement('canvas');
    const dpr = Math.min(window.devicePixelRatio || 2, 3);
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);
    return { canvas, ctx, width, height, dpr };
  }

  function roundRect(ctx, x, y, w, h, r, fillStyle, strokeStyle, lineWidth) {
    if (w < 2 * r) r = w / 2;
    if (h < 2 * r) r = h / 2;
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
    if (fillStyle) {
      ctx.fillStyle = fillStyle;
      ctx.fill();
    }
    if (strokeStyle && lineWidth) {
      ctx.strokeStyle = strokeStyle;
      ctx.lineWidth = lineWidth;
      ctx.stroke();
    }
  }

  function drawWatermarkFooter(ctx, width, height, customSub) {
    const y = height - 54;
    ctx.save();
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(40, y);
    ctx.lineTo(width - 40, y);
    ctx.stroke();

    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.textAlign = 'left';
    ctx.fillText('Crafted by Sarav  •  iamsaravofficial.com', 40, y + 26);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#64748B';
    ctx.textAlign = 'right';
    ctx.fillText(customSub || '100% Client-Side Privacy  •  Zero Telemetry', width - 40, y + 26);
    ctx.restore();
  }

  function wrapText(ctx, text, x, y, maxWidth, lineHeight, maxLines = 4) {
    const words = (text || '').split(' ');
    let line = '';
    let currentY = y;
    let lineCount = 0;

    for (let n = 0; n < words.length; n++) {
      const testLine = line + words[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > maxWidth && n > 0) {
        ctx.fillText(line.trim(), x, currentY);
        line = words[n] + ' ';
        currentY += lineHeight;
        lineCount++;
        if (lineCount >= maxLines - 1 && n < words.length - 1) {
          line += '...';
          break;
        }
      } else {
        line = testLine;
      }
    }
    ctx.fillText(line.trim(), x, currentY);
    return currentY + lineHeight;
  }

  // --------------------------------------------------------------------------
  // Web Share API Level 2 Sharing with Fallbacks
  // --------------------------------------------------------------------------

  async function shareOrDownloadImage(canvas, filename, title, text, url, showToastFn) {
    const toast = typeof showToastFn === 'function' ? showToastFn : (msg => {
      const t = document.getElementById('toast');
      if (t) {
        t.textContent = msg;
        t.classList.add('show');
        setTimeout(() => t.classList.remove('show'), 2800);
      }
    });

    toast('⏳ Generating high-DPI image...');

    canvas.toBlob(async function(blob) {
      if (!blob) {
        toast('❌ Could not generate image.');
        return;
      }

      const file = new File([blob], filename, { type: 'image/png' });
      let sharedSuccessfully = false;

      // Check for Web Share API Level 2 file sharing (Android & iOS)
      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        try {
          await navigator.share({
            files: [file],
            title: title || 'Sarav\'s Playground',
            text: text || '',
            url: url || window.location.href
          });
          sharedSuccessfully = true;
          toast('✅ Shared successfully!');
          return;
        } catch (err) {
          if (err.name === 'AbortError') {
            // User cancelled share dialog intentionally
            return;
          }
          console.warn('Web Share API error, falling back:', err);
        }
      }

      // Fallback 1: Desktop Clipboard Copy
      let clipboardCopied = false;
      if (navigator.clipboard && window.ClipboardItem) {
        try {
          await navigator.clipboard.write([
            new ClipboardItem({ 'image/png': blob })
          ]);
          clipboardCopied = true;
          toast('📋 Image copied to clipboard! Paste directly into WhatsApp / chat.');
        } catch (clipErr) {
          console.warn('Clipboard write failed:', clipErr);
        }
      }

      // Fallback 2: Direct file download
      const a = document.createElement('a');
      a.download = filename;
      const objectUrl = URL.createObjectURL(blob);
      a.href = objectUrl;
      document.body.appendChild(a);
      a.click();
      setTimeout(() => {
        document.body.removeChild(a);
        URL.revokeObjectURL(objectUrl);
      }, 2000);

      if (!clipboardCopied) {
        toast('📥 Image saved to your device!');
      }
    }, 'image/png');
  }

  SaravShareCard.shareOrDownload = shareOrDownloadImage;

  // --------------------------------------------------------------------------
  // 1. School Tiffin & Lunchbox Planner Card
  // --------------------------------------------------------------------------

  SaravShareCard.shareLunchboxWeek = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 1150);

    // Canvas Background
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0F172A');
    bgGrad.addColorStop(1, '#090D16');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 30, 30, width - 60, 100, 14, '#1E293B', 'rgba(245, 158, 11, 0.4)', 1.5);
    ctx.font = '28px sans-serif';
    ctx.fillText('🍱', 50, 92);

    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.textAlign = 'left';
    ctx.fillText('Weekly School Tiffin & Lunch Schedule', 95, 72);

    ctx.font = '500 13.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    const menuTag = opts.presetName ? `Menu: ${opts.presetName}` : 'Personalized Family Menu';
    ctx.fillText(`${menuTag}  •  7-Day Nutritious Plan`, 95, 98);

    // 7 Day Grid Rows
    const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    const rowH = 110;
    const startY = 148;

    days.forEach((day, i) => {
      const y = startY + (i * (rowH + 12));
      const dayData = (opts.schedule && opts.schedule[day]) || {};

      // Row container
      roundRect(ctx, 30, y, width - 60, rowH, 12, '#141E2E', 'rgba(255, 255, 255, 0.08)', 1);

      // Day Chip
      roundRect(ctx, 46, y + 16, 105, 34, 8, 'rgba(245, 158, 11, 0.15)', '#F59E0B', 1);
      ctx.font = '700 13px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FCD34D';
      ctx.textAlign = 'center';
      ctx.fillText(day.slice(0, 3).toUpperCase(), 98, y + 38);

      if (dayData.note) {
        ctx.font = '500 10.5px system-ui, -apple-system, sans-serif';
        ctx.fillStyle = '#94A3B8';
        ctx.fillText(dayData.note.slice(0, 14), 98, y + 68);
      }

      // Column 1: Morning Tiffin
      const col1X = 175;
      ctx.textAlign = 'left';
      ctx.font = '700 11px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#F87171'; // Coral
      ctx.fillText('🥪 MORNING TIFFIN / SNACK', col1X, y + 36);

      ctx.font = '600 14px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#F1F5F9';
      const tiffinName = opts.resolveDish ? opts.resolveDish(dayData.tiffin) : (dayData.tiffin || 'Packed Snack');
      ctx.fillText(tiffinName.slice(0, 36), col1X, y + 62);

      // Column 2: School Lunch / Dabba
      const col2X = 520;
      ctx.font = '700 11px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#38BDF8'; // Blue
      ctx.fillText('🍱 SCHOOL DABBA / LUNCH', col2X, y + 36);

      ctx.font = '600 14px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#F1F5F9';
      const lunchName = opts.resolveDish ? opts.resolveDish(dayData.lunch) : (dayData.lunch || 'Wholesome Lunch');
      ctx.fillText(lunchName.slice(0, 36), col2X, y + 62);
    });

    drawWatermarkFooter(ctx, width, height, 'School Tiffin & Lunchbox Planner');

    await shareOrDownloadImage(
      canvas,
      'weekly-lunchbox-schedule.png',
      'Weekly Lunchbox & Tiffin Schedule',
      'Here is our family school lunchbox and snack schedule for the week!',
      'https://iamsaravofficial.com/apps/lunchbox-planner/'
    );
  };

  // --------------------------------------------------------------------------
  // 2. Home Budget Planner Financial Health Scorecard
  // --------------------------------------------------------------------------

  SaravShareCard.shareBudgetScorecard = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 940);

    // Canvas Background
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0B0F17');
    bgGrad.addColorStop(1, '#05070B');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 96, 14, '#151D2A', 'rgba(16, 185, 129, 0.4)', 1.5);
    ctx.font = '32px sans-serif';
    ctx.fillText('🏠', 60, 98);

    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.textAlign = 'left';
    ctx.fillText('Household Financial Health Scorecard', 115, 76);

    ctx.font = '500 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText(`Monthly Cashflow Snapshot  •  ${opts.monthName || 'Active Month'}  •  50/30/20 Discipline`, 115, 102);

    // 4 Key KPI Metric Boxes
    const kpiW = (width - 72 - 36) / 2;
    const kpis = [
      { label: 'TOTAL MONTHLY INCOME', val: `₹${(opts.income || 0).toLocaleString('en-IN')}`, color: '#38BDF8', icon: '💰' },
      { label: 'FIXED OBLIGATIONS & EMIs', val: `₹${(opts.fixed || 0).toLocaleString('en-IN')}`, color: '#F87171', icon: '📅' },
      { label: 'VARIABLE / DISCRETIONARY', val: `₹${(opts.variable || 0).toLocaleString('en-IN')}`, color: '#FBBF24', icon: '🛒' },
      { label: 'PROJECTED NET SURPLUS', val: `₹${(opts.surplus || 0).toLocaleString('en-IN')}`, color: (opts.surplus >= 0 ? '#34D399' : '#EF4444'), icon: '✨' }
    ];

    const boxY1 = 156;
    const boxY2 = 296;
    const boxPositions = [
      { x: 36, y: boxY1 },
      { x: 36 + kpiW + 36, y: boxY1 },
      { x: 36, y: boxY2 },
      { x: 36 + kpiW + 36, y: boxY2 }
    ];

    kpis.forEach((kpi, idx) => {
      const pos = boxPositions[idx];
      roundRect(ctx, pos.x, pos.y, kpiW, 120, 14, '#131B27', 'rgba(255, 255, 255, 0.08)', 1);

      ctx.font = '20px sans-serif';
      ctx.fillText(kpi.icon, pos.x + 20, pos.y + 38);

      ctx.font = '700 11px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#64748B';
      ctx.textAlign = 'left';
      ctx.fillText(kpi.label, pos.x + 50, pos.y + 36);

      ctx.font = '700 26px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = kpi.color;
      ctx.fillText(kpi.val, pos.x + 20, pos.y + 88);
    });

    // 50/30/20 Financial Health Bar & Verdict
    const barY = 446;
    roundRect(ctx, 36, barY, width - 72, 210, 16, '#131B27', 'rgba(255, 255, 255, 0.08)', 1);

    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E2E8F0';
    ctx.textAlign = 'left';
    ctx.fillText('50/30/20 BUDGET HEALTH ALLOCATION', 60, barY + 38);

    const savingsRate = opts.income > 0 ? Math.max(0, Math.round((opts.surplus / opts.income) * 100)) : 0;
    const fixedRate = opts.income > 0 ? Math.round((opts.fixed / opts.income) * 100) : 0;
    const varRate = opts.income > 0 ? Math.round((opts.variable / opts.income) * 100) : 0;

    // Multi-segment progress bar
    const barW = width - 120;
    const barH = 26;
    const trackX = 60;
    const trackY = barY + 60;

    roundRect(ctx, trackX, trackY, barW, barH, 8, '#0F172A', 'rgba(255,255,255,0.1)', 1);
    const seg1W = (barW * Math.min(fixedRate, 100)) / 100;
    const seg2W = (barW * Math.min(varRate, 100 - fixedRate)) / 100;
    const seg3W = (barW * Math.min(savingsRate, 100 - fixedRate - varRate)) / 100;

    if (seg1W > 0) roundRect(ctx, trackX, trackY, seg1W, barH, 8, '#F87171');
    if (seg2W > 0) roundRect(ctx, trackX + seg1W, trackY, seg2W, 8, '#FBBF24');
    if (seg3W > 0) roundRect(ctx, trackX + seg1W + seg2W, trackY, seg3W, 8, '#34D399');

    // Legend
    ctx.font = '600 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F87171';
    ctx.fillText(`■ Needs/Bills (${fixedRate}%)`, 60, barY + 118);
    ctx.fillStyle = '#FBBF24';
    ctx.fillText(`■ Wants/Spends (${varRate}%)`, 260, barY + 118);
    ctx.fillStyle = '#34D399';
    ctx.fillText(`■ Savings Stash (${savingsRate}%)`, 480, barY + 118);

    // Advisory Verdict
    const verdictY = barY + 158;
    ctx.font = '700 15px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    const verdictTitle = savingsRate >= 20 ? '✨ Healthy Household Surplus' : (savingsRate >= 5 ? '⚖️ Balanced Cashflow Discipline' : '⚠️ Low Margin for Contingencies');
    ctx.fillText(verdictTitle, 60, verdictY);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    const verdictSub = savingsRate >= 20 
      ? 'Strong savings cushion. Excellent discipline toward debt clearance and emergency reserve.'
      : 'Maintain vigilance on discretionary spending to safeguard the 20% savings buffer.';
    ctx.fillText(verdictSub, 60, verdictY + 22);

    // Bills cleared pill
    const billPillY = 684;
    roundRect(ctx, 36, billPillY, width - 72, 70, 12, 'rgba(56, 189, 248, 0.08)', 'rgba(56, 189, 248, 0.2)', 1);
    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E2E8F0';
    ctx.fillText(`📅 Fixed Bills Status: ${opts.billsPaidCount || 0} Paid  •  ${opts.billsPendingCount || 0} Pending Due`, 60, billPillY + 40);

    drawWatermarkFooter(ctx, width, height, 'Home Budget Planner');

    await shareOrDownloadImage(
      canvas,
      'household-budget-scorecard.png',
      'Household Financial Health Scorecard',
      'Check out our monthly budget summary on Sarav\'s Playground!',
      'https://iamsaravofficial.com/apps/home-budget-planner/'
    );
  };

  // --------------------------------------------------------------------------
  // 3. Gold Loan Calculator Quote Card
  // --------------------------------------------------------------------------

  SaravShareCard.shareGoldLoanQuote = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 960);
    const r = opts.result || {};

    // Obsidian & Liquid Gold luxury background
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0D0B08');
    bgGrad.addColorStop(1, '#050403');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Luxury Header
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#18140D', '#C1810A', 1.5);
    ctx.font = '32px sans-serif';
    ctx.fillText('🪙', 60, 98);

    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F7F2E8';
    ctx.textAlign = 'left';
    ctx.fillText('Gold Loan Eligibility & Valuation Quote', 115, 74);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E5A93C';
    ctx.fillText(`RBI Compliant 75% LTV  •  Appraised Rate: ₹${(r.effective24kRate || 0).toLocaleString('en-IN')}/gm (24K)`, 115, 100);

    // Collateral Summary Box
    roundRect(ctx, 36, 156, width - 72, 110, 14, '#14110B', 'rgba(229, 169, 60, 0.25)', 1);

    ctx.font = '700 11.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#B0A28E';
    ctx.fillText('COLLATERAL PLEDGED', 58, 186);

    ctx.font = '700 22px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F7F2E8';
    ctx.fillText(`${(r.netWeight || 0).toFixed(3)} gm (${r.purityLabel || '22K'})`, 58, 222);

    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E5A93C';
    ctx.textAlign = 'right';
    ctx.fillText(`Appraised Gold Value: ₹${Math.round(r.goldValue || 0).toLocaleString('en-IN')}`, width - 58, 222);

    // 4 Key Loan Sanction Metrics
    const rowY = 286;
    const colW = (width - 72 - 24) / 2;

    const metrics = [
      { label: 'LOAN PER GRAM (RBI CAP)', val: `₹${Math.round(r.loanPerGram || 0).toLocaleString('en-IN')}/gm`, color: '#E5A93C' },
      { label: 'SANCTIONED LOAN AMOUNT', val: `₹${Math.round(r.loanAmount || 0).toLocaleString('en-IN')}`, color: '#5FBF77' },
      { label: 'NET CASH DISBURSED', val: `₹${Math.round(r.netDisbursal || 0).toLocaleString('en-IN')}`, color: '#5FBF77' },
      { label: 'MONTHLY PAYMENT / EMI', val: `₹${Math.round(r.monthlyVal || 0).toLocaleString('en-IN')}`, color: '#E5A93C' }
    ];

    metrics.forEach((m, idx) => {
      const x = idx % 2 === 0 ? 36 : 36 + colW + 24;
      const y = rowY + Math.floor(idx / 2) * 116;
      roundRect(ctx, x, y, colW, 98, 12, '#14110B', 'rgba(255, 255, 255, 0.06)', 1);

      ctx.textAlign = 'left';
      ctx.font = '700 10.5px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#8A7554';
      ctx.fillText(m.label, x + 20, y + 32);

      ctx.font = '700 24px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = m.color;
      ctx.fillText(m.val, x + 20, y + 72);
    });

    // Repayment Scheme Breakdown Box
    const schY = 538;
    roundRect(ctx, 36, schY, width - 72, 190, 14, '#14110B', 'rgba(255, 255, 255, 0.06)', 1);

    ctx.font = '700 13.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F7F2E8';
    ctx.textAlign = 'left';
    ctx.fillText('REPAYMENT STRUCTURE', 60, schY + 36);

    const details = [
      { label: 'Repayment Scheme', val: r.schemeName || 'Monthly Interest Only' },
      { label: 'Interest Rate & Tenure', val: `${r.interestRate || 10.0}% p.a.  •  ${r.tenure || 6} Months` },
      { label: 'Total Interest Outflow', val: `₹${Math.round(r.totalInterest || 0).toLocaleString('en-IN')}` },
      { label: 'Total Amount Repaid', val: `₹${Math.round(r.totalRepayment || 0).toLocaleString('en-IN')}` }
    ];

    details.forEach((d, i) => {
      const lineY = schY + 70 + (i * 28);
      ctx.font = '500 13px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#B0A28E';
      ctx.textAlign = 'left';
      ctx.fillText(d.label, 60, lineY);

      ctx.font = '600 13px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#F7F2E8';
      ctx.textAlign = 'right';
      ctx.fillText(d.val, width - 60, lineY);
    });

    // Disclaimer pill
    const discY = 750;
    roundRect(ctx, 36, discY, width - 72, 60, 10, 'rgba(229, 169, 60, 0.08)', 'rgba(229, 169, 60, 0.2)', 1);
    ctx.font = '500 11.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E5A93C';
    ctx.textAlign = 'left';
    ctx.fillText('* Statutory RBI estimate. Final loan sanction subject to in-branch assay purity verification.', 56, discY + 36);

    drawWatermarkFooter(ctx, width, height, 'Gold Loan Calculator');

    await shareOrDownloadImage(
      canvas,
      'gold-loan-quote.png',
      'Gold Loan Valuation Quote',
      'Check out this gold loan eligibility quote on Sarav\'s Playground!',
      'https://iamsaravofficial.com/apps/gold-loan-calculator/'
    );
  };

  // --------------------------------------------------------------------------
  // 4. Kids' Piggy Bank Ledger Milestone Certificate
  // --------------------------------------------------------------------------

  SaravShareCard.sharePiggyBankGoal = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 940);
    const s = opts.state || {};
    const goal = s.goal || {};

    // Cheerful Vibrant Kids Theme
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#111827');
    bgGrad.addColorStop(1, '#0B0F17');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Certificate Ribbon Header
    roundRect(ctx, 36, 36, width - 72, 106, 16, '#1F2937', '#F59E0B', 2);
    ctx.font = '36px sans-serif';
    ctx.fillText(goal.icon || '🎯', 60, 102);

    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F9FAFB';
    ctx.textAlign = 'left';
    ctx.fillText('Junior Savings Milestone Certificate', 125, 78);

    ctx.font = '600 13.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FBBF24';
    ctx.fillText('Pocket Money & Piggy Bank Wisdom  •  Ages 6–14', 125, 106);

    // Dream Goal Showcase Box
    roundRect(ctx, 36, 164, width - 72, 230, 16, '#131D2E', 'rgba(245, 158, 11, 0.3)', 1.5);

    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('ACTIVE DREAM GOAL', 60, 204);

    ctx.font = '700 26px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.fillText(goal.title || 'Dream Goal', 60, 246);

    const savedAmount = s.save || 0;
    const targetAmount = goal.target || 1000;
    const pct = Math.min(100, Math.round((savedAmount / targetAmount) * 100));

    // Big Progress Bar
    const progX = 60;
    const progY = 276;
    const progW = width - 120;
    roundRect(ctx, progX, progY, progW, 30, 10, '#0F172A', 'rgba(255, 255, 255, 0.1)', 1);
    const fillW = (progW * pct) / 100;
    if (fillW > 0) {
      const fillGrad = ctx.createLinearGradient(progX, 0, progX + fillW, 0);
      fillGrad.addColorStop(0, '#F59E0B');
      fillGrad.addColorStop(1, '#10B981');
      roundRect(ctx, progX, progY, fillW, 30, 10, fillGrad);
    }

    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.textAlign = 'left';
    ctx.fillText(`Saved: ₹${savedAmount.toLocaleString('en-IN')} of ₹${targetAmount.toLocaleString('en-IN')}`, 60, 344);

    ctx.font = '700 18px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = pct >= 100 ? '#34D399' : '#FBBF24';
    ctx.textAlign = 'right';
    ctx.fillText(`${pct}% ACHIEVED ${pct >= 100 ? '🎉 GOAL UNLOCKED!' : '⭐'}`, width - 60, 344);

    // 3-Jar Breakdown Card
    const jarY = 416;
    roundRect(ctx, 36, jarY, width - 72, 170, 16, '#131D2E', 'rgba(255, 255, 255, 0.08)', 1);

    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#CBD5E1';
    ctx.textAlign = 'left';
    ctx.fillText('3-JAR ALLOCATOR DISCIPLINE (50 / 40 / 10)', 60, jarY + 36);

    const jarW = (width - 72 - 32) / 3;
    const jars = [
      { name: 'SPEND JAR (50%)', amount: s.spend || 0, icon: '🛍️', color: '#F87171' },
      { name: 'SAVE JAR (40%)', amount: s.save || 0, icon: '🏦', color: '#34D399' },
      { name: 'GIVE JAR (10%)', amount: s.give || 0, icon: '🎁', color: '#38BDF8' }
    ];

    jars.forEach((j, i) => {
      const x = 52 + i * (jarW + 8);
      const y = jarY + 54;
      roundRect(ctx, x, y, jarW, 90, 10, '#0F172A', 'rgba(255, 255, 255, 0.06)', 1);

      ctx.font = '16px sans-serif';
      ctx.fillText(j.icon, x + 14, y + 30);

      ctx.font = '700 10px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#94A3B8';
      ctx.textAlign = 'left';
      ctx.fillText(j.name, x + 38, y + 28);

      ctx.font = '700 20px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = j.color;
      ctx.fillText(`₹${j.amount.toLocaleString('en-IN')}`, x + 14, y + 68);
    });

    // Congratulations Banner
    const bannerY = 610;
    roundRect(ctx, 36, bannerY, width - 72, 80, 14, 'rgba(16, 185, 129, 0.1)', '#10B981', 1);
    ctx.font = '28px sans-serif';
    ctx.fillText('🏆', 60, bannerY + 52);

    ctx.font = '700 15px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#34D399';
    ctx.textAlign = 'left';
    ctx.fillText('Financial Literacy Champion!', 110, bannerY + 38);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E2E8F0';
    ctx.fillText('Learning delayed gratification, smart spending, and sharing with others.', 110, bannerY + 60);

    drawWatermarkFooter(ctx, width, height, 'Kids\' First Pocket Money & Piggy Bank Ledger');

    await shareOrDownloadImage(
      canvas,
      'junior-savings-certificate.png',
      'Junior Savings Milestone Certificate',
      'Look at my savings progress on Sarav\'s Piggy Bank Ledger!',
      'https://iamsaravofficial.com/apps/piggy-bank-ledger/'
    );
  };

  // --------------------------------------------------------------------------
  // 5. Family Jackpot Winner Arcade Poster
  // --------------------------------------------------------------------------

  SaravShareCard.shareFamilyJackpotWinner = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 1080);

    // Retro Arcade Stage Background
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0F0E17');
    bgGrad.addColorStop(1, '#050408');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Marquee Cabinet Header
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#1F1B2C', '#F59E0B', 2);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.textAlign = 'center';
    ctx.fillText('🎰 FAMILY JACKPOT ARCADE 🎰', width / 2, 78);

    ctx.font = '600 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('✦ MATCH ALL 5 REELS TO CROWN THE WINNER ✦', width / 2, 106);

    // Winner Crown & Title
    ctx.font = '54px sans-serif';
    ctx.fillText(opts.trophy || '👑', width / 2, 215);

    ctx.font = '800 36px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(opts.headerText || 'DADDY WINS!', width / 2, 275);

    // 5 Slot Reel Boxes
    const letters = (opts.letters || ['D', 'A', 'D', 'D', 'Y']).slice(0, 5);
    const reelW = 90;
    const reelH = 100;
    const reelGap = 16;
    const totalReelsW = (reelW * 5) + (reelGap * 4);
    const startX = (width - totalReelsW) / 2;
    const reelY = 320;

    letters.forEach((char, idx) => {
      const rx = startX + idx * (reelW + reelGap);
      roundRect(ctx, rx, reelY, reelW, reelH, 12, '#1E1A2E', '#F59E0B', 2);

      ctx.font = '800 48px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FDE047';
      ctx.textAlign = 'center';
      ctx.fillText(char, rx + (reelW / 2), reelY + 70);
    });

    // Stake Verdict Box
    const verdictY = 460;
    roundRect(ctx, 60, verdictY, width - 120, 110, 16, 'rgba(245, 158, 11, 0.12)', 'rgba(245, 158, 11, 0.35)', 1.5);
    ctx.font = '700 16px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.textAlign = 'center';
    wrapText(ctx, opts.verdict || 'All hail the king! Today\'s chores are officially excused!', width / 2, verdictY + 44, width - 180, 26, 3);

    // Session Scoreboard
    const scoreY = 600;
    roundRect(ctx, 60, scoreY, width - 120, 130, 14, '#13111C', 'rgba(255, 255, 255, 0.08)', 1);

    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.textAlign = 'center';
    ctx.fillText('HOUSEHOLD SESSION SCOREBOARD', width / 2, scoreY + 30);

    const scores = opts.scores || [
      { role: '👨‍💼 Daddy', count: 3 },
      { role: '👩‍💼 Mummy', count: 2 },
      { role: '🤵 Hubby', count: 1 },
      { role: '👰 Wifey', count: 2 },
      { role: '🧒 MyKid', count: 1 }
    ];

    const cardW = (width - 120 - 48) / 5;
    scores.forEach((s, idx) => {
      const sx = 72 + idx * (cardW + 8);
      const sy = scoreY + 46;
      roundRect(ctx, sx, sy, cardW, 64, 8, '#1A1726', 'rgba(255, 255, 255, 0.05)', 1);

      ctx.font = '600 11px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#94A3B8';
      ctx.textAlign = 'center';
      ctx.fillText(s.role, sx + (cardW / 2), sy + 24);

      ctx.font = '800 20px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FDE047';
      ctx.fillText(String(s.count), sx + (cardW / 2), sy + 52);
    });

    drawWatermarkFooter(ctx, width, height, 'Family Jackpot Winner • Arcade Suite');

    await shareOrDownloadImage(
      canvas,
      'family-jackpot-winner.png',
      'Family Jackpot Winner!',
      `🎰 ${opts.headerText || 'Someone'} won the Family Jackpot! Check out the verdict!`,
      'https://iamsaravofficial.com/games/familywinner/'
    );
  };

  // --------------------------------------------------------------------------
  // 6. Couples Senti-Meter Love Telepathy Scorecard
  // --------------------------------------------------------------------------

  SaravShareCard.shareSentimeterScore = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 1080);

    // Romantic Deep Space & Neon Rose Background
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#190A1B');
    bgGrad.addColorStop(1, '#0B050D');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#241028', '#F43F5E', 2);
    ctx.font = '36px sans-serif';
    ctx.fillText('💖', 60, 100);

    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFF1F2';
    ctx.textAlign = 'left';
    ctx.fillText('Couples Senti-Meter Telepathy Scorecard', 120, 76);

    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDA4AF';
    ctx.fillText('Hubby vs. Wifey  •  10 Secret Rapid-Fire Dilemmas', 120, 102);

    // Big Heart Percentage Badge
    const dialY = 160;
    roundRect(ctx, 60, dialY, width - 120, 220, 18, '#1C0E20', 'rgba(244, 63, 94, 0.3)', 1.5);

    ctx.font = '48px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(opts.badge || '☕❤️', width / 2, dialY + 70);

    ctx.font = '800 64px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FB7185';
    ctx.fillText(`${opts.percent || 80}%`, width / 2, dialY + 145);

    ctx.font = '700 16px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFE4E6';
    ctx.fillText(opts.diagnosisTitle || 'Soulmates with Filter Coffee Telepathy!', width / 2, dialY + 190);

    // Prescription Box
    const presY = 406;
    roundRect(ctx, 60, presY, width - 120, 160, 16, 'rgba(244, 63, 94, 0.12)', 'rgba(244, 63, 94, 0.35)', 1.5);

    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDA4AF';
    ctx.textAlign = 'center';
    ctx.fillText('MARITAL PRESCRIPTION & DIAGNOSIS', width / 2, presY + 34);

    ctx.font = '500 15px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    wrapText(ctx, opts.prescription || 'Supreme marital harmony! You operate on the exact same filter coffee wavelength.', width / 2, presY + 68, width - 180, 26, 3);

    // 10 Dilemmas Match Review Grid
    const revY = 590;
    roundRect(ctx, 60, revY, width - 120, 200, 16, '#1C0E20', 'rgba(255, 255, 255, 0.08)', 1);

    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDA4AF';
    ctx.textAlign = 'left';
    ctx.fillText(`MATCH BREAKDOWN (${opts.matchesCount || 8} / 10 MATCHES)`, 84, revY + 36);

    const history = (opts.history || []).slice(0, 10);
    const dotW = (width - 120 - 48) / 10;
    history.forEach((h, idx) => {
      const dx = 84 + idx * dotW;
      const dy = revY + 56;
      roundRect(ctx, dx, dy, dotW - 6, 44, 8, h.match ? 'rgba(52, 211, 153, 0.15)' : 'rgba(244, 63, 94, 0.15)', h.match ? '#34D399' : '#F43F5E', 1);

      ctx.font = '700 12px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FFFFFF';
      ctx.textAlign = 'center';
      ctx.fillText(`Q${idx + 1}`, dx + (dotW - 6) / 2, dy + 20);

      ctx.font = '14px sans-serif';
      ctx.fillText(h.match ? '✅' : '❌', dx + (dotW - 6) / 2, dy + 38);
    });

    // Fun Couple Prescriptions note
    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDA4AF';
    ctx.textAlign = 'center';
    ctx.fillText('🤵 Hubby  ✦  👰 Wifey  •  Tested on Couples Senti-Meter', width / 2, revY + 155);

    drawWatermarkFooter(ctx, width, height, 'Couples Senti-Meter • Family Arcade');

    await shareOrDownloadImage(
      canvas,
      'couples-sentimeter-scorecard.png',
      'Couples Senti-Meter Telepathy Scorecard',
      `💖 We scored ${opts.percent || 80}% on Couples Senti-Meter! Test your couple telepathy:`,
      'https://iamsaravofficial.com/games/sentimeter/'
    );
  };

  // --------------------------------------------------------------------------
  // 7. Samosa Snatch Victor Poster
  // --------------------------------------------------------------------------

  SaravShareCard.shareSamosaVictor = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 920);

    // Retro Pixel Duel Stage
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#18120A');
    bgGrad.addColorStop(1, '#080604');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#261C10', '#F59E0B', 2);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.textAlign = 'center';
    ctx.fillText('⚡ SAMOSA SNATCH BATTLE ⚡', width / 2, 78);

    ctx.font = '600 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('2-PLAYER RAPID FINGER-TAPPING TUG-OF-WAR', width / 2, 106);

    // Snack Prize Icon
    ctx.font = '72px sans-serif';
    ctx.fillText(opts.prizeIcon || '🥟', width / 2, 230);

    // Victor Title
    ctx.font = '800 36px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(`${(opts.winner || 'Player 1').toUpperCase()} SNATCHED IT!`, width / 2, 305);

    // Head-to-Head Scoreboard Box
    const scoreY = 356;
    roundRect(ctx, 60, scoreY, width - 120, 160, 16, '#1C150E', 'rgba(245, 158, 11, 0.3)', 1.5);

    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.textAlign = 'center';
    ctx.fillText('OFFICIAL HEAD-TO-HEAD TALLY', width / 2, scoreY + 36);

    // P1 Box
    roundRect(ctx, 90, scoreY + 54, 300, 80, 12, '#281E14', '#F59E0B', 1);
    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(opts.p1Name || 'Player 1', 240, scoreY + 84);
    ctx.font = '800 26px system-ui, -apple-system, sans-serif';
    ctx.fillText(`${opts.p1Wins || 0} WINS`, 240, scoreY + 118);

    // VS
    ctx.font = '800 22px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F87171';
    ctx.fillText('VS', width / 2, scoreY + 102);

    // P2 Box
    roundRect(ctx, width - 390, scoreY + 54, 300, 80, 12, '#281E14', '#F59E0B', 1);
    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(opts.p2Name || 'Player 2', width - 240, scoreY + 84);
    ctx.font = '800 26px system-ui, -apple-system, sans-serif';
    ctx.fillText(`${opts.p2Wins || 0} WINS`, width - 240, scoreY + 118);

    // Brag Banner
    const bragY = 550;
    roundRect(ctx, 60, bragY, width - 120, 90, 14, 'rgba(245, 158, 11, 0.1)', 'rgba(245, 158, 11, 0.25)', 1);
    ctx.font = '700 16px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.textAlign = 'center';
    ctx.fillText(`🏆 The ${opts.prizeIcon || '🥟'} belongs exclusively to ${opts.winner || 'the Champion'}!`, width / 2, bragY + 42);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('Certified victor of the single-phone household snack battle showdown.', width / 2, bragY + 68);

    drawWatermarkFooter(ctx, width, height, 'Samosa Snatch • Family Arcade');

    await shareOrDownloadImage(
      canvas,
      'samosa-snatch-victor.png',
      'Samosa Snatch Victor!',
      `🥟 ${opts.winner} won the Samosa Snatch battle! Play on Sarav's World:`,
      'https://iamsaravofficial.com/games/samosasnatch/'
    );
  };

  window.SaravShareCard = SaravShareCard;

})(window);
