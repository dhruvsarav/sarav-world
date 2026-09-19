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

  // --------------------------------------------------------------------------
  // 8. Glow Up Grid — Weekly Habit Champion Card
  // --------------------------------------------------------------------------
  SaravShareCard.shareGlowUpHabit = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 1020);

    // Dark slate starry canvas
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0F172A');
    bgGrad.addColorStop(1, '#090D16');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 110, 16, '#1E293B', 'rgba(245, 158, 11, 0.4)', 1.5);
    ctx.font = '36px sans-serif';
    ctx.fillText(opts.avatar || '⭐', 60, 104);

    ctx.font = '800 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.textAlign = 'left';
    ctx.fillText(`${opts.kidName || 'Kid Champ'}'s Weekly Habit Grid`, 115, 80);

    ctx.font = '600 13.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F59E0B';
    ctx.fillText('🌟 GLOW UP GRID • CERTIFIED WEEKLY STAR CHAMPION', 115, 108);

    // Super Kid Goal Box
    const goalY = 166;
    roundRect(ctx, 36, goalY, width - 72, 80, 14, '#172033', 'rgba(255, 255, 255, 0.08)', 1);
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('🏆 SUPER KID WEEKLY GOAL', 60, goalY + 30);

    ctx.font = '700 17px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(opts.goal || 'Read books & morning smile!', 60, goalY + 58);

    // Big Stats Grid
    const statY = 264;
    const statW = (width - 72 - 16) / 2;
    // Left: Tasks Completed
    roundRect(ctx, 36, statY, statW, 110, 14, '#1E293B', 'rgba(16, 185, 129, 0.3)', 1.5);
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('TASKS COMPLETED THIS WEEK', 56, statY + 32);

    ctx.font = '800 32px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#10B981';
    ctx.fillText(`${opts.completedTasks || 0} of ${opts.totalTasks || 0}`, 56, statY + 76);

    ctx.font = '600 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#6EE7B7';
    ctx.fillText(`${opts.streakPct || 0}% completion streak`, 56, statY + 96);

    // Right: Stars Earned
    roundRect(ctx, 36 + statW + 16, statY, statW, 110, 14, '#1E293B', 'rgba(245, 158, 11, 0.3)', 1.5);
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('TOTAL GOLD STARS GLOWED', 36 + statW + 36, statY + 32);

    ctx.font = '800 32px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F59E0B';
    ctx.fillText(`⭐ ${opts.completedTasks || 0} Stars`, 36 + statW + 36, statY + 76);

    ctx.font = '600 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('Building healthy lifelong habits', 36 + statW + 36, statY + 96);

    // 7-Day Mini Cards
    const daysY = 394;
    roundRect(ctx, 36, daysY, width - 72, 380, 14, '#141E2E', 'rgba(255, 255, 255, 0.08)', 1);
    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('📅 7-DAY GLOW TRAIL & ROUTINE BREAKDOWN', 56, daysY + 34);

    const daysList = opts.dayStats || [
      { day: 'Mon', done: 8, total: 10 },
      { day: 'Tue', done: 9, total: 10 },
      { day: 'Wed', done: 10, total: 10 },
      { day: 'Thu', done: 8, total: 10 },
      { day: 'Fri', done: 9, total: 10 },
      { day: 'Sat', done: 7, total: 8 },
      { day: 'Sun', done: 8, total: 8 }
    ];

    const cardW = (width - 72 - 40 - (6 * 10)) / 7;
    daysList.forEach((d, idx) => {
      const dx = 56 + (idx * (cardW + 10));
      const dy = daysY + 54;
      const isPerfect = d.done >= d.total && d.total > 0;
      roundRect(ctx, dx, dy, cardW, 120, 10, isPerfect ? 'rgba(245, 158, 11, 0.18)' : '#1E293B', isPerfect ? '#F59E0B' : 'rgba(255,255,255,0.06)', 1);
      
      ctx.textAlign = 'center';
      ctx.font = '800 13px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = isPerfect ? '#FDE047' : '#F8FAFC';
      ctx.fillText(d.day.slice(0, 3).toUpperCase(), dx + cardW / 2, dy + 28);

      ctx.font = '22px sans-serif';
      ctx.fillText(isPerfect ? '🌟' : '⭐', dx + cardW / 2, dy + 62);

      ctx.font = '700 12px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = isPerfect ? '#FCD34D' : '#94A3B8';
      ctx.fillText(`${d.done}/${d.total}`, dx + cardW / 2, dy + 92);
      ctx.fillText('tasks', dx + cardW / 2, dy + 108);
    });

    // Sample Habits Highlights Box
    const habY = daysY + 194;
    roundRect(ctx, 56, habY, width - 72 - 40, 150, 10, '#1E293B', 'rgba(255,255,255,0.05)', 1);
    ctx.textAlign = 'left';
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText('✨ ROUTINE HIGHLIGHTS & HABIT ANCHORS:', 74, habY + 30);

    const habits = opts.highlightHabits || ['Morning Routine & Hygiene', 'Reading & Learning Sprint', 'Sports & Outdoor Play', 'Restful Early Bedtime'];
    habits.slice(0, 4).forEach((h, hIdx) => {
      const col = hIdx % 2;
      const row = Math.floor(hIdx / 2);
      const hx = 74 + (col * 380);
      const hy = habY + 62 + (row * 36);
      ctx.font = '600 13px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#F1F5F9';
      ctx.fillText(`⭐ ${h}`, hx, hy);
    });

    // Honor Ribbon Box
    const ribY = 794;
    roundRect(ctx, 36, ribY, width - 72, 90, 14, 'rgba(245, 158, 11, 0.12)', 'rgba(245, 158, 11, 0.3)', 1.5);
    ctx.textAlign = 'center';
    ctx.font = '800 17px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(`🏆 OFFICIAL SUPER KID OF THE WEEK AWARD`, width / 2, ribY + 38);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('Awarded for consistency, positive effort, and glowing through daily routines.', width / 2, ribY + 64);

    drawWatermarkFooter(ctx, width, height, 'Glow Up Grid • Habit Tracker');

    await shareOrDownloadImage(
      canvas,
      `glow-up-${(opts.kidName || 'kid').toLowerCase().replace(/[^a-z0-9]/g, '-')}-champ.png`,
      'Weekly Habit Champion Certificate!',
      `🌟 Check out ${(opts.kidName || 'Kid Champ')}'s weekly habit achievements on Glow Up Grid!`,
      'https://iamsaravofficial.com/apps/glow-up-grid/'
    );
  };

  // --------------------------------------------------------------------------
  // 9. Home Loan Prepayment & Debt-Free Certificate
  // --------------------------------------------------------------------------
  SaravShareCard.shareHomeLoanFreedom = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 1080);

    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0C0F14');
    bgGrad.addColorStop(1, '#151C28');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 105, 16, '#141922', 'rgba(227, 166, 62, 0.4)', 1.5);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.textAlign = 'left';
    ctx.fillText('Home Loan Prepayment Accelerometer', 60, 78);

    ctx.font = '700 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E3A63E';
    ctx.fillText('⚡ OFFICIAL DEBT-FREE FREEDOM & INTEREST SAVINGS CERTIFICATE', 60, 106);

    // Hero Freedom Banner
    const freeY = 160;
    roundRect(ctx, 36, freeY, width - 72, 160, 16, '#182232', '#10B981', 2);

    ctx.font = '700 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#6EE7B7';
    ctx.fillText('PROJECTED DEBT-FREE FREEDOM DATE', 60, freeY + 36);

    ctx.font = '900 36px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(opts.debtFreeDate || 'Mortgage-Free by 2038', 60, freeY + 84);

    ctx.font = '700 15px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(`⚡ Shaves ${opts.tenureCut || '8+ Years'} off your total mortgage tenure!`, 60, freeY + 124);

    // Two-Column Metrics
    const rowY = 340;
    const colW = (width - 72 - 16) / 2;

    // Col 1: Total Interest Saved
    roundRect(ctx, 36, rowY, colW, 140, 14, '#141922', 'rgba(16, 185, 129, 0.3)', 1.5);
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('TOTAL INTEREST AVOIDED / SAVED', 56, rowY + 34);

    ctx.font = '800 34px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#10B981';
    ctx.fillText(opts.interestSaved || '₹24,82,410', 56, rowY + 80);

    ctx.font = '600 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#6EE7B7';
    ctx.fillText(`${opts.interestSavedPct || '46.5%'} total interest shaved off`, 56, rowY + 112);

    // Col 2: Baseline Loan Terms
    roundRect(ctx, 36 + colW + 16, rowY, colW, 140, 14, '#141922', 'rgba(227, 166, 62, 0.3)', 1.5);
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('ORIGINAL BASELINE LOAN', 36 + colW + 36, rowY + 34);

    ctx.font = '800 30px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.fillText(opts.loanAmount || '₹50 Lakhs', 36 + colW + 36, rowY + 78);

    ctx.font = '600 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E3A63E';
    ctx.fillText(`@ ${opts.interestRate || '8.5%'} p.a. • Base EMI: ${opts.baseEmi || '₹43,391'}`, 36 + colW + 36, rowY + 112);

    // Strategic Action Plan Card
    const planY = 500;
    roundRect(ctx, 36, planY, width - 72, 330, 14, '#121822', 'rgba(255, 255, 255, 0.08)', 1);
    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText('🎯 ACCELERATOR STRATEGY ROADMAP', 56, planY + 36);

    const stratItems = [
      { label: 'Extra Monthly Prepayment', val: opts.extraMonthly || '+₹5,000 / month' },
      { label: 'Annual Extra EMIs', val: opts.annualExtraEmis || '1 Extra EMI / Year' },
      { label: 'Annual EMI Step-Up %', val: opts.stepUpPercent || '5% Annual Compounding' },
      { label: 'Principal Crossover Month', val: opts.crossoverMonth || 'Month 26 (Principal > Interest)' }
    ];

    stratItems.forEach((st, sIdx) => {
      const sy = planY + 70 + (sIdx * 62);
      roundRect(ctx, 56, sy, width - 72 - 40, 50, 10, '#1B2433', 'rgba(255, 255, 255, 0.04)', 1);
      
      ctx.textAlign = 'left';
      ctx.font = '600 13.5px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#E2E8F0';
      ctx.fillText(st.label, 74, sy + 31);

      ctx.textAlign = 'right';
      ctx.font = '700 14px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FDE047';
      ctx.fillText(st.val, width - 74, sy + 31);
    });

    // Guaranteed ROI Banner
    const roiY = 850;
    roundRect(ctx, 36, roiY, width - 72, 90, 14, 'rgba(16, 185, 129, 0.12)', 'rgba(16, 185, 129, 0.3)', 1.5);
    ctx.textAlign = 'center';
    ctx.font = '800 16px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#6EE7B7';
    ctx.fillText(`💎 Guaranteed Risk-Free ${opts.interestRate || '8.5%'} Post-Tax Yield`, width / 2, roiY + 40);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#A7F3D0';
    ctx.fillText('Every rupee prepaid saves compounding interest directly off your principal balance.', width / 2, roiY + 66);

    drawWatermarkFooter(ctx, width, height, 'Home Loan Accelerometer • Sarav\'s Playground');

    await shareOrDownloadImage(
      canvas,
      'home-loan-debt-free-certificate.png',
      'Home Loan Debt-Free Certificate!',
      `⚡ I am shaving ${opts.tenureCut || 'years'} and saving ${opts.interestSaved || 'lakhs'} on my home loan with Sarav's Accelerometer:`,
      'https://iamsaravofficial.com/apps/home-loan-accelerometer/'
    );
  };

  // --------------------------------------------------------------------------
  // 10. GenZ & Alpha Slang Decoder — Flashcard
  // --------------------------------------------------------------------------
  SaravShareCard.shareSlangCard = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 840);

    // Cyberpunk Dark Background
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0B0E14');
    bgGrad.addColorStop(1, '#151924');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Badge
    roundRect(ctx, 36, 36, width - 72, 90, 14, '#141923', '#F59E0B', 1.5);
    ctx.font = '700 22px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.textAlign = 'left';
    ctx.fillText('🗣️ GenZ & Alpha Slang Decoder', 58, 76);

    ctx.font = '600 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('MODERN SOCIOLINGUISTICS • THEN & NOW FLASHCARD', 58, 102);

    // Generation Tag Pill
    roundRect(ctx, width - 180, 58, 120, 32, 16, 'rgba(245, 158, 11, 0.15)', '#F59E0B', 1);
    ctx.font = '800 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.textAlign = 'center';
    ctx.fillText((opts.gen || 'Gen Z').toUpperCase(), width - 120, 79);

    // Main Flashcard Container
    const fcY = 146;
    roundRect(ctx, 36, fcY, width - 72, 490, 18, '#131822', 'rgba(255, 255, 255, 0.08)', 1);

    // Millennial Reference ("Then")
    ctx.textAlign = 'left';
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#64748B';
    ctx.fillText('MILLENNIAL TRANSLATION ("THEN")', 64, fcY + 44);

    ctx.font = '600 18px monospace';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText(opts.then || 'Charisma / Charm', 64, fcY + 74);

    // Modern Term ("Now")
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText('MODERN SLANG ("NOW")', 64, fcY + 126);

    ctx.font = '900 48px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(opts.now || 'Rizz', 64, fcY + 180);

    // Divider
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(64, fcY + 214);
    ctx.lineTo(width - 64, fcY + 214);
    ctx.stroke();

    // Where you'll hear it
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F43F5E';
    ctx.fillText("WHERE YOU'LL HEAR IT & CONTEXT", 64, fcY + 248);

    ctx.font = '600 15px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#E2E8F0';
    wrapText(ctx, opts.context || 'Social media feeds, school corridors, gaming chats.', 64, fcY + 276, width - 128, 24, 2);

    // Real-World Sentence Example Box
    const exY = fcY + 340;
    roundRect(ctx, 64, exY, width - 128, 115, 12, '#1A2230', '#38BDF8', 1);

    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText('IN A REAL-WORLD SENTENCE:', 84, exY + 32);

    ctx.font = 'italic 600 15px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    wrapText(ctx, `"${opts.example || 'Bro walked in with unspoken rizz.'}"`, 84, exY + 62, width - 168, 24, 2);

    // Footer banner
    const btmY = 656;
    roundRect(ctx, 36, btmY, width - 72, 85, 14, 'rgba(245, 158, 11, 0.1)', 'rgba(245, 158, 11, 0.25)', 1);
    ctx.textAlign = 'center';
    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText('⚡ 156 Verified Modern Slang Terms with Pre-Generated Neural Voice Audio', width / 2, btmY + 36);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('Zero telemetry • 100% Client-Side Linguistics • Sarav\'s Playground', width / 2, btmY + 60);

    drawWatermarkFooter(ctx, width, height, 'GenZ & Alpha Slang Decoder');

    const slug = (opts.now || 'slang').toLowerCase().replace(/[^a-z0-9]/g, '-');
    await shareOrDownloadImage(
      canvas,
      `slang-${slug}-card.png`,
      `Slang of the Day: ${opts.now}!`,
      `🗣️ Slang of the Day: "${opts.now}" (Then: "${opts.then}"). Decode 156 terms on Sarav's World:`,
      'https://iamsaravofficial.com/apps/genzalphaslang/'
    );
  };

  // --------------------------------------------------------------------------
  // 11. Family Movie & Game Night — Souvenir Cinema Ticket Pass
  // --------------------------------------------------------------------------
  SaravShareCard.shareMovieTicketPass = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 920);

    // Cinema Red & Velvet Midnight
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#160B0F');
    bgGrad.addColorStop(1, '#0A0507');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Ticket Stub Outline Card
    const tX = 36;
    const tY = 36;
    const tW = width - 72;
    const tH = height - 120;

    roundRect(ctx, tX, tY, tW, tH, 20, '#1F1117', '#E11D48', 2);

    // Header Strip
    roundRect(ctx, tX + 16, tY + 16, tW - 32, 90, 12, '#2A131C', 'rgba(225, 29, 72, 0.4)', 1);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFF1F2';
    ctx.textAlign = 'left';
    ctx.fillText('🎬 FAMILY CINEMA & GAME NIGHT', tX + 36, tY + 54);

    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FB7185';
    ctx.fillText('OFFICIAL WEEKEND ADMIT-ALL SOUVENIR PASS • ZERO ARGUMENTS', tX + 36, tY + 80);

    // Ticket Perforated Dashed Line
    ctx.save();
    ctx.setLineDash([8, 8]);
    ctx.strokeStyle = 'rgba(225, 29, 72, 0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(tX + 16, tY + 128);
    ctx.lineTo(tX + tW - 16, tY + 128);
    ctx.stroke();
    ctx.restore();

    // Feature Presentation Title
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F43F5E';
    ctx.fillText("TONIGHT'S FEATURE SELECTION:", tX + 36, tY + 168);

    ctx.font = '900 38px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(opts.title || 'Spirited Away', tX + 36, tY + 220);

    // Meta Chips Row (Genre, Runtime/Players, Platform)
    const metaY = tY + 242;
    const tags = [
      opts.type || 'Movie',
      opts.genre || 'Family Animation',
      opts.runtime || '125 Mins',
      opts.ott ? `Streaming: ${opts.ott}` : 'Living Room Screening'
    ];

    let curX = tX + 36;
    tags.forEach(tag => {
      ctx.font = '600 12px system-ui, -apple-system, sans-serif';
      const tw = ctx.measureText(tag).width + 22;
      roundRect(ctx, curX, metaY, tw, 28, 14, '#361522', 'rgba(225, 29, 72, 0.3)', 1);
      ctx.fillStyle = '#FECDD3';
      ctx.fillText(tag, curX + 11, metaY + 19);
      curX += tw + 10;
    });

    // 2-Box Split: Crown Picker vs Gourmet Snack
    const boxY = tY + 300;
    const halfW = (tW - 32 - 16) / 2;

    // Box 1: Picker
    roundRect(ctx, tX + 16, boxY, halfW, 140, 14, '#2A131C', 'rgba(245, 158, 11, 0.3)', 1.5);
    ctx.font = '700 11.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F59E0B';
    ctx.fillText('👑 CHOSEN BY (FAIR TURN)', tX + 36, boxY + 34);

    ctx.font = '800 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(opts.pickerName || 'Kid 1 (Elder Child)', tX + 36, boxY + 76);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('Protected by Friday Harmony Turn Rotator', tX + 36, boxY + 108);

    // Box 2: Snack Pairing
    roundRect(ctx, tX + 16 + halfW + 16, boxY, halfW, 140, 14, '#2A131C', 'rgba(225, 29, 72, 0.3)', 1.5);
    ctx.font = '700 11.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FB7185';
    ctx.fillText('🍿 GOURMET SNACK PAIRING', tX + 36 + halfW + 16, boxY + 34);

    ctx.font = '800 20px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFF1F2';
    ctx.fillText(`${opts.snackIcon || '🍿'} ${opts.snackTitle || 'Truffle Butter Popcorn'}`, tX + 36 + halfW + 16, boxY + 76);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDA4AF';
    ctx.fillText('Freshly prepared for the entire household', tX + 36 + halfW + 16, boxY + 108);

    // Showtime Clock Box
    const showY = tY + 460;
    roundRect(ctx, tX + 16, showY, tW - 32, 100, 14, '#230E17', '#E11D48', 1.5);

    ctx.textAlign = 'left';
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F43F5E';
    ctx.fillText('🕒 SHOWTIME / GATHERING SCHEDULE:', tX + 36, showY + 36);

    ctx.font = '800 28px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(opts.showtime || 'Tonight @ 8:00 PM Sharp', tX + 36, showY + 76);

    ctx.textAlign = 'right';
    ctx.font = '700 18px monospace';
    ctx.fillStyle = '#FB7185';
    ctx.fillText('🎟️ TICKET #2026-FMN', tX + tW - 36, showY + 60);

    // Rule Banner
    const ruleY = tY + 580;
    roundRect(ctx, tX + 16, ruleY, tW - 32, 90, 12, 'rgba(245, 158, 11, 0.08)', 'rgba(245, 158, 11, 0.2)', 1);
    ctx.textAlign = 'center';
    ctx.font = '700 14.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText('✨ House Rule: No Phones During the Feature • Snacks Shared Fairly', width / 2, ruleY + 38);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText("101 Vetted Cinema Gems & 40 Tabletop Games • Sarav's Playground", width / 2, ruleY + 64);

    drawWatermarkFooter(ctx, width, height, 'Family Movie Night Decider');

    await shareOrDownloadImage(
      canvas,
      'family-movie-night-pass.png',
      'Movie Night Pass!',
      `🎬 Tonight's feature: "${opts.title || 'Movie'}" picked by ${opts.pickerName || 'the family'}! See you at ${opts.showtime || '8:00 PM'}!`,
      'https://iamsaravofficial.com/apps/family-movie-night/'
    );
  };

  // --------------------------------------------------------------------------
  // 12. Gold Price Estimator — Jewellery Valuation Quote Card
  // --------------------------------------------------------------------------
  SaravShareCard.shareGoldJewelleryQuote = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 980);

    // Physical Gold Theme (Soft warm cream canvas)
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#FFFBF0');
    bgGrad.addColorStop(1, '#F7F1E1');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 110, 16, '#FFFFFF', '#D4AF37', 2);
    ctx.font = '36px sans-serif';
    ctx.fillText('🥇', 60, 104);

    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#3D2B00';
    ctx.textAlign = 'left';
    ctx.fillText('Precious Metals Suite • Jewellery Quote', 115, 80);

    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#C1810A';
    ctx.fillText('INDIAN RETAIL JEWELLERY VALUATION & SPOT RATE SNAPSHOT', 115, 108);

    // Hero Market Value Card
    const heroY = 166;
    roundRect(ctx, 36, heroY, width - 72, 170, 16, '#FFFFFF', '#E0B84B', 1.5);

    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#8A7554';
    ctx.fillText(`${(opts.metalPurity || 'Gold 22K (916)').toUpperCase()} CURRENT MARKET VALUATION`, 60, heroY + 38);

    ctx.font = '900 44px monospace';
    ctx.fillStyle = '#3D2B00';
    ctx.fillText(opts.currentVal || '₹1,25,600', 60, heroY + 95);

    ctx.font = '600 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#C1810A';
    ctx.fillText(`Today's Spot Rate: ₹${opts.marketRate || '7,850'}/gm • Net Metal: ${opts.weight || '16.000'} gm`, 60, heroY + 138);

    // Bill Breakdown Table Card
    const billY = 356;
    roundRect(ctx, 36, billY, width - 72, 380, 14, '#FFFFFF', 'rgba(212, 175, 55, 0.4)', 1);
    ctx.font = '700 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#8B5E00';
    ctx.fillText('🧾 DETAILED RETAIL BILL BREAKDOWN', 56, billY + 36);

    const billItems = [
      { label: 'Net Metal Weight', val: `${opts.weight || '16.000'} gm` },
      { label: 'Wastage / Value Addition (VA)', val: `${opts.wastageGm || '1.600'} gm (${opts.wastagePct || '10'}%)` },
      { label: 'Effective Billed Weight', val: `${opts.effectiveWeight || '17.600'} gm` },
      { label: 'Original Buy Cost / Invoiced', val: opts.totalCost || '₹1,15,200' },
      { label: 'Total Appreciation / Gain', val: `${opts.gainVal || '+₹10,400'} (${opts.gainPct || '+9.0%'})`, isGain: true }
    ];

    billItems.forEach((item, bIdx) => {
      const by = billY + 64 + (bIdx * 58);
      roundRect(ctx, 56, by, width - 72 - 40, 48, 8, '#FFFDF8', 'rgba(212, 175, 55, 0.2)', 1);

      ctx.textAlign = 'left';
      ctx.font = '600 14px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#3D2B00';
      ctx.fillText(item.label, 74, by + 30);

      ctx.textAlign = 'right';
      ctx.font = '700 15px monospace';
      ctx.fillStyle = item.isGain ? '#1B8A3D' : '#3D2B00';
      ctx.fillText(item.val, width - 74, by + 30);
    });

    // Invoicing Compliance Banner
    const compY = 756;
    roundRect(ctx, 36, compY, width - 72, 85, 12, '#F6E3B0', '#E0B84B', 1);
    ctx.textAlign = 'center';
    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#3D2B00';
    ctx.fillText('🏛️ Conforms to Standard Indian Retail Jewellery Billing & GST Rules', width / 2, compY + 36);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#8B5E00';
    ctx.fillText("100% Client-Side Privacy • Zero Telemetry • Sarav's Playground", width / 2, compY + 60);

    // Custom Gold Watermark Footer
    const y = height - 54;
    ctx.save();
    ctx.strokeStyle = 'rgba(212, 175, 55, 0.4)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(40, y);
    ctx.lineTo(width - 40, y);
    ctx.stroke();

    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#8A7554';
    ctx.textAlign = 'left';
    ctx.fillText('Crafted by Sarav  •  iamsaravofficial.com', 40, y + 26);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#8B5E00';
    ctx.textAlign = 'right';
    ctx.fillText('Gold Price & Valuation Estimator', width - 40, y + 26);
    ctx.restore();

    await shareOrDownloadImage(
      canvas,
      'gold-jewellery-valuation-quote.png',
      'Gold Jewellery Valuation Quote!',
      `🥇 Gold Jewellery Valuation: ${opts.currentVal || '₹0'} for ${opts.weight || '0'}g. Calculate on Sarav's World:`,
      'https://iamsaravofficial.com/apps/gold-price-estimator/'
    );
  };

  // --------------------------------------------------------------------------
  // 13. Master Bottle Flip Showdown — Pro Flipper Record
  // --------------------------------------------------------------------------
  SaravShareCard.shareBottleFlipRecord = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 880);

    // Cyber Obsidian Canvas
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#090D16');
    bgGrad.addColorStop(1, '#020617');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#131D2E', '#F59E0B', 2);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.textAlign = 'center';
    ctx.fillText('🍾 MASTER BOTTLE FLIP SHOWDOWN 🍾', width / 2, 78);

    ctx.font = '600 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('OFFICIAL LIVING-ROOM FLIPPER RECORD & ACCURACY TALLY', width / 2, 106);

    // Player Crown & Name
    ctx.font = '800 32px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.fillText(`${(opts.playerName || 'Player').toUpperCase()}`, width / 2, 196);

    // Big Hero Streak Box
    const streakY = 226;
    roundRect(ctx, 50, streakY, width - 100, 140, 18, '#182438', '#F59E0B', 2);

    ctx.font = '700 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('CURRENT CONSECUTIVE STREAK', width / 2, streakY + 36);

    ctx.font = '900 48px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(`🔥 ${opts.streak || 0} FLIPS IN A ROW`, width / 2, streakY + 92);

    ctx.font = '600 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText(`Personal All-Time Best: ${opts.bestStreak || 0} Flips`, width / 2, streakY + 122);

    // 3-Stat Split Grid
    const statY = 388;
    const cardW = (width - 100 - 24) / 3;

    // Stat 1: Cap Landings
    roundRect(ctx, 50, statY, cardW, 120, 14, '#131D2E', 'rgba(245, 158, 11, 0.3)', 1);
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('CAP LANDINGS (10X)', 50 + cardW / 2, statY + 30);
    ctx.font = '800 28px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(`🧢 ${opts.capsLanded || 0}`, 50 + cardW / 2, statY + 70);
    ctx.font = '500 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('Bonus Landings', 50 + cardW / 2, statY + 98);

    // Stat 2: Accuracy
    roundRect(ctx, 50 + cardW + 12, statY, cardW, 120, 14, '#131D2E', 'rgba(16, 185, 129, 0.3)', 1);
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('LANDING ACCURACY', 50 + cardW + 12 + cardW / 2, statY + 30);
    ctx.font = '800 28px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#10B981';
    ctx.fillText(`🎯 ${opts.accuracyPct || 0}%`, 50 + cardW + 12 + cardW / 2, statY + 70);
    ctx.font = '500 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#6EE7B7';
    ctx.fillText(`${opts.totalLands || 0}/${opts.totalFlips || 0} Successful`, 50 + cardW + 12 + cardW / 2, statY + 98);

    // Stat 3: Bottle Spec
    roundRect(ctx, 50 + (cardW * 2) + 24, statY, cardW, 120, 14, '#131D2E', 'rgba(56, 189, 248, 0.3)', 1);
    ctx.font = '700 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#94A3B8';
    ctx.fillText('BOTTLE SPEC', 50 + (cardW * 2) + 24 + cardW / 2, statY + 30);
    ctx.font = '800 20px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText(opts.bottleType || 'Bisleri', 50 + (cardW * 2) + 24 + cardW / 2, statY + 68);
    ctx.font = '500 11px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#7DD3FC';
    ctx.fillText(`${opts.waterLevel || '35%'} Water Ballast`, 50 + (cardW * 2) + 24 + cardW / 2, statY + 98);

    // Challenge Banner
    const chY = 534;
    roundRect(ctx, 50, chY, width - 100, 100, 16, 'rgba(245, 158, 11, 0.12)', 'rgba(245, 158, 11, 0.3)', 1.5);
    ctx.font = '800 17px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(`🏆 Living Room Bottle Flip Legend Certified!`, width / 2, chY + 42);

    ctx.font = '600 13px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText("Can anyone in the family beat this streak? Challenge accepted on Sarav's World!", width / 2, chY + 70);

    drawWatermarkFooter(ctx, width, height, 'Bottle Flip Showdown • Family Arcade');

    await shareOrDownloadImage(
      canvas,
      'bottle-flip-record.png',
      'Bottle Flip Record!',
      `🍾 ${opts.playerName} just flipped ${opts.streak} in a row on Bottle Flip Showdown! Can you beat it?`,
      'https://iamsaravofficial.com/games/bottleflip/'
    );
  };

  // --------------------------------------------------------------------------
  // 14. Chit-Charades — Forehead Showdown MVP Scorecard
  // --------------------------------------------------------------------------
  SaravShareCard.shareChitCharadesScore = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 940);

    // Festive Stage Canvas
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#0B0E14');
    bgGrad.addColorStop(1, '#111726');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Card
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#172033', '#F59E0B', 2);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.textAlign = 'center';
    ctx.fillText('🗣️ CHIT-CHARADES • FOREHEAD SHOWDOWN', width / 2, 78);

    ctx.font = '600 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('OFFICIAL HOUSEHOLD ROUND RECAP & TELEPATHY SCOREBOARD', width / 2, 106);

    // Guesser & Deck Info
    ctx.font = '800 28px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F8FAFC';
    ctx.fillText(`👑 GUESSER MVP: ${(opts.guesser || 'Daddy').toUpperCase()}`, width / 2, 186);

    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#38BDF8';
    ctx.fillText(`Deck: ${opts.deckTitle || 'Bollywood Masala'} • 60-Second Blitz`, width / 2, 214);

    // Scoreboard Stat Strip
    const scY = 240;
    const scW = (width - 72 - 16) / 2;

    // Left: Correct
    roundRect(ctx, 36, scY, scW, 120, 16, '#132820', '#10B981', 2);
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#6EE7B7';
    ctx.fillText('GUESSED CORRECTLY', 36 + scW / 2, scY + 36);

    ctx.font = '900 48px monospace';
    ctx.fillStyle = '#10B981';
    ctx.fillText(`✅ ${opts.correctCount || 0}`, 36 + scW / 2, scY + 88);

    // Right: Passed
    roundRect(ctx, 36 + scW + 16, scY, scW, 120, 16, '#281313', '#EF4444', 1.5);
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCA5A5';
    ctx.fillText('PASSED / SKIPPED', 36 + scW + 16 + scW / 2, scY + 36);

    ctx.font = '900 48px monospace';
    ctx.fillStyle = '#EF4444';
    ctx.fillText(`⏭️ ${opts.passedCount || 0}`, 36 + scW + 16 + scW / 2, scY + 88);

    // Words Guessed Pill Cloud
    const wordY = 384;
    roundRect(ctx, 36, wordY, width - 72, 290, 16, '#151D2C', 'rgba(255, 255, 255, 0.08)', 1);

    ctx.textAlign = 'left';
    ctx.font = '700 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText('⭐ WORDS NAILED IN THIS ROUND:', 60, wordY + 36);

    const words = (opts.wordsList && opts.wordsList.length > 0) ? opts.wordsList : ['Sholay', 'Dilwale', 'Lagaan', 'Dangal', '3 Idiots', 'Chennai Express'];
    let wX = 60;
    let wY = wordY + 60;
    const maxW = width - 120;

    words.slice(0, 10).forEach(w => {
      ctx.font = '700 14px system-ui, -apple-system, sans-serif';
      const textW = ctx.measureText(w).width + 30;
      if (wX + textW > maxW) {
        wX = 60;
        wY += 46;
      }
      roundRect(ctx, wX, wY, textW, 36, 18, 'rgba(16, 185, 129, 0.15)', '#10B981', 1);
      ctx.fillStyle = '#A7F3D0';
      ctx.fillText(`✓ ${w}`, wX + 12, wY + 23);
      wX += textW + 10;
    });

    // Award Verdict Banner
    const awY = 696;
    roundRect(ctx, 36, awY, width - 72, 90, 14, 'rgba(245, 158, 11, 0.12)', 'rgba(245, 158, 11, 0.3)', 1.5);
    ctx.textAlign = 'center';
    ctx.font = '800 17px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText('🏆 Telepathy & Acting MVP of the Night!', width / 2, awY + 38);

    ctx.font = '500 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText("Single-phone forehead charades with zero tilt friction • Sarav's Playground", width / 2, awY + 64);

    drawWatermarkFooter(ctx, width, height, 'Chit-Charades • Family Arcade');

    await shareOrDownloadImage(
      canvas,
      'chit-charades-score.png',
      'Chit-Charades Scorecard!',
      `🗣️ ${opts.guesser || 'Player'} scored ${opts.correctCount || 0} in Chit-Charades! Play with family on Sarav's World:`,
      'https://iamsaravofficial.com/games/chitcharades/'
    );
  };

  // --------------------------------------------------------------------------
  // 15. Family Secret Box — Mystery Confession / Dare Slip
  // --------------------------------------------------------------------------
  SaravShareCard.shareSecretBoxPrompt = async function(opts) {
    if (document.fonts) await document.fonts.ready;
    const { canvas, ctx, width, height } = setupCanvas(900, 860);

    // Mystical Mahogany & Gold Velvet
    const bgGrad = ctx.createLinearGradient(0, 0, 0, height);
    bgGrad.addColorStop(0, '#1E121E');
    bgGrad.addColorStop(1, '#0C060E');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Header Box
    roundRect(ctx, 36, 36, width - 72, 100, 16, '#2D192E', '#F59E0B', 2);
    ctx.font = '700 24px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.textAlign = 'center';
    ctx.fillText('🎁 FAMILY SECRET BOX 🎁', width / 2, 78);

    ctx.font = '600 12.5px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText('OFFICIAL 3D MYSTERY CHEST DRAWN SLIP', width / 2, 106);

    // Drawn For & Category Banner
    const catY = 160;
    roundRect(ctx, 36, catY, width - 72, 60, 12, '#231324', 'rgba(255, 255, 255, 0.08)', 1);

    ctx.textAlign = 'left';
    ctx.font = '800 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#F43F5E';
    ctx.fillText(opts.categoryTitle || '🌶️ CHEEKY TRUTH', 60, catY + 36);

    ctx.textAlign = 'right';
    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FDE047';
    ctx.fillText(`Drawn for: ${opts.playerTarget || 'Anyone'}`, width - 60, catY + 36);

    // Parchment Scroll / Mystery Slip
    const slipY = 242;
    roundRect(ctx, 36, slipY, width - 72, 360, 20, '#160E18', '#F59E0B', 1.5);

    ctx.textAlign = 'center';
    ctx.font = '700 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#A855F7';
    ctx.fillText('📜 THE CONFESSION / DARE CHALLENGE', width / 2, slipY + 44);

    ctx.font = 'italic 700 26px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    wrapText(ctx, `"${opts.promptText || 'Reveal the funniest childhood secret you never told your parents!'}"`, width / 2 - 360, slipY + 110, 720, 38, 4);

    if (opts.penaltyText) {
      const penY = slipY + 250;
      roundRect(ctx, 60, penY, width - 120, 80, 12, 'rgba(239, 68, 68, 0.15)', '#EF4444', 1);
      ctx.font = '700 11.5px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FCA5A5';
      ctx.fillText('🐔 CHICKEN OUT PENALTY CONSEQUENCE:', width / 2, penY + 30);

      ctx.font = '700 15px system-ui, -apple-system, sans-serif';
      ctx.fillStyle = '#FFFFFF';
      ctx.fillText(opts.penaltyText, width / 2, penY + 58);
    }

    // Seal of Authenticity Banner
    const sealY = 624;
    roundRect(ctx, 36, sealY, width - 72, 85, 14, 'rgba(245, 158, 11, 0.1)', 'rgba(245, 158, 11, 0.25)', 1);
    ctx.textAlign = 'center';
    ctx.font = '700 14px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText('🔒 Sealed inside the Family Mystery Chest • Preserving Unfiltered Family Memories', width / 2, sealY + 36);

    ctx.font = '500 12px system-ui, -apple-system, sans-serif';
    ctx.fillStyle = '#FCD34D';
    ctx.fillText("Truths, Desi Dares & Penalty Wheel • Sarav's Playground", width / 2, sealY + 60);

    drawWatermarkFooter(ctx, width, height, 'Family Secret Box • Family Arcade');

    await shareOrDownloadImage(
      canvas,
      'secret-box-slip.png',
      'Family Secret Box Slip!',
      `🎁 Drawn from Family Secret Box for ${opts.playerTarget || 'the family'}: "${opts.promptText || ''}"!`,
      'https://iamsaravofficial.com/games/secretbox/'
    );
  };

  window.SaravShareCard = SaravShareCard;

})(window);
