/**
 * Curated Store Telegram Bot & KV API - Cloudflare Worker
 * 
 * Automatically captures Amazon links shared by Vidhya/Sarav on Telegram,
 * resolves redirects, extracts ASIN, fetches product metadata (OpenGraph),
 * applies Amazon Associates tracking tag 'dhrav-21', and publishes to
 * the live store on https://iamsaravofficial.com/store/ via Cloudflare KV.
 */

const AMAZON_TAG = 'dhrav-21';

// Category mapping helper
function detectCategory(text) {
  const t = (text || '').toLowerCase();
  if (t.includes('lunch') || t.includes('tiffin') || t.includes('bottle') || t.includes('box') || t.includes('school') || t.includes('pencil') || t.includes('stationery')) {
    return { category: 'lunchbox', categoryName: 'School & Lunchbox' };
  }
  if (t.includes('book') || t.includes('novel') || t.includes('story') || t.includes('read') || t.includes('author')) {
    return { category: 'books', categoryName: "Kids' Books" };
  }
  if (t.includes('kitchen') || t.includes('home') || t.includes('pan') || t.includes('cook') || t.includes('fridge') || t.includes('organizer') || t.includes('bed') || t.includes('sheet') || t.includes('blanket') || t.includes('pillow') || t.includes('cushion') || t.includes('curtain') || t.includes('towel') || t.includes('bath') || t.includes('decor')) {
    return { category: 'home', categoryName: 'Home & Kitchen' };
  }
  if (t.includes('tech') || t.includes('cable') || t.includes('usb') || t.includes('wifi') || t.includes('watch') || t.includes('gadget') || t.includes('stand') || t.includes('phone')) {
    return { category: 'tech', categoryName: 'Tech & Desk' };
  }
  if (t.includes('toy') || t.includes('game') || t.includes('puzzle') || t.includes('lego') || t.includes('board')) {
    return { category: 'games', categoryName: 'Toys & Games' };
  }
  return { category: 'lifestyle', categoryName: 'Wellness & Lifestyle' };
}

// Extract Amazon URL from message text
function extractAmazonUrl(text) {
  const match = (text || '').match(/https?:\/\/(?:www\.)?(?:amazon\.in|amzn\.in|amzn\.to|amazon\.com)\/[^\s]+/i);
  if (!match) return null;
  return match[0].replace(/[,)>]+$/, '');
}

// Extract ASIN from URL
function extractAsin(url) {
  if (!url) return null;
  const patterns = [
    /(?:dp\/|gp\/product\/|\/d\/|product\/|ASIN=)([A-Z0-9]{10})/i,
    /\/([A-Z0-9]{10})(?:[/?&]|$)/i
  ];
  for (const p of patterns) {
    const m = url.match(p);
    if (m && m[1]) return m[1].toUpperCase();
  }
  return null;
}

// Send Telegram Message
async function sendTelegramMessage(botToken, chatId, text, options = {}) {
  const url = `https://api.telegram.org/bot${botToken}/sendMessage`;
  await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: chatId,
      text: text,
      parse_mode: 'Markdown',
      ...options
    })
  });
}

// Send Telegram Photo
async function sendTelegramPhoto(botToken, chatId, photoUrl, caption, options = {}) {
  const url = `https://api.telegram.org/bot${botToken}/sendPhoto`;
  await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: chatId,
      photo: photoUrl,
      caption: caption,
      parse_mode: 'Markdown',
      ...options
    })
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // CORS Headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // 1. PUBLIC API: GET /api/products -> returns all curated products
    if (url.pathname === '/api/products' || url.pathname === '/products.json') {
      let products = [];
      if (env.STORE_KV) {
        const rawIndex = await env.STORE_KV.get('products_index');
        const ids = rawIndex ? JSON.parse(rawIndex) : [];
        for (const id of ids) {
          const rawProd = await env.STORE_KV.get(`product:${id}`);
          if (rawProd) products.push(JSON.parse(rawProd));
        }
      }
      return new Response(JSON.stringify({ ok: true, count: products.length, products }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    // 2. TELEGRAM WEBHOOK: POST /webhook or POST /
    if (request.method === 'POST') {
      let body;
      try {
        body = await request.json();
      } catch (e) {
        return new Response('Invalid JSON', { status: 400 });
      }

      const message = body.message || body.channel_post;
      if (!message) return new Response('OK');

      const chatId = message.chat.id;
      const userId = message.from ? message.from.id : null;
      const text = message.text || message.caption || '';

      // Whitelist security check (if configured in env.ALLOWED_USER_IDS)
      if (env.ALLOWED_USER_IDS) {
        const allowed = env.ALLOWED_USER_IDS.split(',').map(s => s.trim());
        if (userId && !allowed.includes(String(userId)) && !allowed.includes(String(chatId))) {
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, '⚠️ *Access Denied*: You are not authorized to publish to the Curated Store.');
          return new Response('OK');
        }
      }

      // Handle Bot Commands
      if (text.startsWith('/start') || text.startsWith('/help')) {
        await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId,
          "✨ *Welcome to Vidhya's Curated Store Bot!*\n\n" +
          "Simply *share any Amazon product link* directly into this chat from the Amazon app or mobile browser.\n\n" +
          "💡 *Tips*:\n" +
          "• Add an optional note in your message, e.g.: `Kitchen: Our everyday steel lunchbox`\n" +
          "• I will automatically extract title, photo, and assign affiliate tag `dhrav-21`\n" +
          "• Products go live instantly on [iamsaravofficial.com/store/](https://iamsaravofficial.com/store/)\n\n" +
          "Commands:\n" +
          "• `/list` - View last 5 products\n" +
          "• `/delete <ASIN>` - Remove a product"
        );
        return new Response('OK');
      }

      if (text.startsWith('/list')) {
        if (!env.STORE_KV) {
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, "⚠️ KV store is not bound.");
          return new Response('OK');
        }
        const rawIndex = await env.STORE_KV.get('products_index');
        const ids = rawIndex ? JSON.parse(rawIndex) : [];
        if (ids.length === 0) {
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, "📦 No products listed yet.");
          return new Response('OK');
        }
        let listText = `📦 *Latest Curated Products (${ids.length} total)*:\n\n`;
        const recentIds = ids.slice(0, 5);
        for (const id of recentIds) {
          const raw = await env.STORE_KV.get(`product:${id}`);
          if (raw) {
            const p = JSON.parse(raw);
            listText += `• *${p.title.slice(0, 40)}...*\n  ID: \`${p.asin}\` | ${p.categoryName}\n`;
          }
        }
        await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, listText);
        return new Response('OK');
      }

      if (text.startsWith('/delete')) {
        const parts = text.split(' ');
        const asinToDelete = parts[1] ? parts[1].trim().toUpperCase() : null;
        if (!asinToDelete) {
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, "⚠️ Please specify ASIN to delete: `/delete B0BF54979B`");
          return new Response('OK');
        }
        if (env.STORE_KV) {
          await env.STORE_KV.delete(`product:${asinToDelete}`);
          const rawIndex = await env.STORE_KV.get('products_index');
          let ids = rawIndex ? JSON.parse(rawIndex) : [];
          ids = ids.filter(id => id !== asinToDelete);
          await env.STORE_KV.put('products_index', JSON.stringify(ids));
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, `🗑️ Deleted product \`${asinToDelete}\` from the store.`);
        }
        return new Response('OK');
      }

      // Check for Amazon URL
      const rawUrl = extractAmazonUrl(text);
      if (!rawUrl) {
        await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, "🤔 Please send an Amazon product link (e.g. from the Amazon App share sheet).");
        return new Response('OK');
      }

      // Acknowledge receipt
      await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, "🔍 *Processing product link...* Extracting details & applying tag `dhrav-21`.");

      try {
        // Resolve redirect if shortlink
        let targetUrl = rawUrl;
        if (rawUrl.includes('amzn.to') || rawUrl.includes('amzn.in')) {
          const headRes = await fetch(rawUrl, {
            method: 'GET',
            redirect: 'follow',
            headers: {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
          });
          targetUrl = headRes.url || rawUrl;
        }

        const asin = extractAsin(targetUrl);
        if (!asin) {
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, "❌ Could not find product ASIN in the link. Please share a direct product page.");
          return new Response('OK');
        }

        // Fetch product page metadata
        const prodPageUrl = `https://www.amazon.in/dp/${asin}`;
        const pageRes = await fetch(prodPageUrl, {
          headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-IN,en;q=0.9'
          }
        });
        const html = await pageRes.text();

        // Extract Title
        let title = '';
        const pTitle = html.match(/<span\s+id=["']productTitle["'][^>]*>(.*?)<\/span>/is);
        const ogTitle = html.match(/<meta\s+property=["']og:title["']\s+content=["'](.*?)["']/i);
        const titleTag = html.match(/<title>(.*?)<\/title>/i);

        if (pTitle && pTitle[1]) {
          title = pTitle[1].trim();
        } else if (ogTitle && ogTitle[1]) {
          title = ogTitle[1].trim();
        } else if (titleTag && titleTag[1]) {
          title = titleTag[1].replace(/: Amazon\.in.*$/i, '').trim();
        } else {
          title = `Curated Amazon Product (${asin})`;
        }
        title = title.replace(/&amp;/g, '&').replace(/&#39;/g, "'").replace(/&quot;/g, '"');

        // Clean up overly long titles
        if (title.length > 90) {
          title = title.slice(0, 90) + '...';
        }

        // Extract Image
        let imageUrl = '';
        const landingImg = html.match(/id=["']landingImage["'][^>]*data-old-hires=["'](.*?)["']/i) || 
                           html.match(/id=["']landingImage["'][^>]*src=["'](.*?)["']/i);
        const ogImg = html.match(/<meta\s+property=["']og:image["']\s+content=["'](.*?)["']/i);
        const jsonImg = html.match(/"large":"(https:\/\/[^"]+\.jpg)"/i);

        if (landingImg && landingImg[1]) {
          imageUrl = landingImg[1];
        } else if (ogImg && ogImg[1]) {
          imageUrl = ogImg[1];
        } else if (jsonImg && jsonImg[1]) {
          imageUrl = jsonImg[1];
        }

        // Extract Note from user message (strip the URL)
        let note = text.replace(rawUrl, '').trim();
        if (!note) {
          note = "Handpicked and personally recommended.";
        }

        // Detect Category
        const catInfo = detectCategory(note + ' ' + title);
        const hasTh = targetUrl.includes('th=1');
        const affiliateUrl = `https://www.amazon.in/dp/${asin}?tag=${AMAZON_TAG}&linkCode=ll2${hasTh ? '&th=1' : ''}`;

        const newProduct = {
          id: `prod_${asin}`,
          title: title,
          category: catInfo.category,
          categoryName: catInfo.categoryName,
          image: imageUrl || '/store/images/default-product.svg',
          asin: asin,
          amazonUrl: affiliateUrl,
          curatorNote: note,
          rating: '4.5',
          dateAdded: new Date().toISOString().split('T')[0],
          tags: [catInfo.categoryName, 'Curator Pick']
        };

        // Save to KV
        if (env.STORE_KV) {
          await env.STORE_KV.put(`product:${asin}`, JSON.stringify(newProduct));
          const rawIndex = await env.STORE_KV.get('products_index');
          let ids = rawIndex ? JSON.parse(rawIndex) : [];
          if (!ids.includes(asin)) {
            ids.unshift(asin); // newest first
            await env.STORE_KV.put('products_index', JSON.stringify(ids));
          }
        }

        // Reply to Telegram with Rich Card
        const confirmationText = 
          `✅ *Listed on Curated Store!*\n\n` +
          `📦 *${title}*\n` +
          `🏷️ Category: *${catInfo.categoryName}*\n` +
          `📝 Note: _${note}_\n` +
          `🔗 Tag: \`${AMAZON_TAG}\` applied\n\n` +
          `🌐 [View on iamsaravofficial.com/store/](https://iamsaravofficial.com/store/)`;

        if (imageUrl) {
          await sendTelegramPhoto(env.TELEGRAM_BOT_TOKEN, chatId, imageUrl, confirmationText);
        } else {
          await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, confirmationText);
        }

      } catch (err) {
        await sendTelegramMessage(env.TELEGRAM_BOT_TOKEN, chatId, `⚠️ Error processing product: ${err.message}`);
      }

      return new Response('OK');
    }

    return new Response("Vidhya's Curated Store API & Bot is running. Visit https://iamsaravofficial.com/store/");
  }
};
