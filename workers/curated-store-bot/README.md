# Curated Store Telegram Bot Setup Guide

Automated product listing bot for Vidhya and Sarav.

---

## 3-Minute Deployment Steps

### 1. Create your Telegram Bot
1. Open Telegram and search for `@BotFather`.
2. Send `/newbot` and follow the prompts:
   - Name: `Vidhya Curates Store`
   - Username: `VidhyaCuratesBot` (or your preferred unique handle)
3. Copy the **HTTP API Token** provided by BotFather (e.g. `123456789:ABCdefGHIjkl...`).

### 2. Deploy Cloudflare Worker
Navigate to this directory:
```bash
cd workers/curated-store-bot
```

Create the KV namespace:
```bash
npx wrangler kv:namespace create STORE_KV
```
Copy the output `id` into `wrangler.toml` under `[[kv_namespaces]]`.

Set your secrets:
```bash
npx wrangler secret put TELEGRAM_BOT_TOKEN
# Paste your Bot Token

npx wrangler secret put ALLOWED_USER_IDS
# Enter comma-separated Telegram user IDs (e.g. Vidhya's and Sarav's user IDs from @userinfobot)
```

Deploy the worker:
```bash
npx wrangler deploy
```
Copy your worker URL (e.g. `https://curated-store-bot.<your-cloudflare-subdomain>.workers.dev`).

### 3. Register the Webhook
In your browser or terminal, open:
```bash
https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook?url=https://curated-store-bot.<your-cloudflare-subdomain>.workers.dev
```
You will see: `{"ok":true,"result":true,"description":"Webhook was set"}`.

---

## How Vidhya Uses It
1. Vidhya finds any item on Amazon India.
2. Taps **Share** -> selects **Telegram** -> chooses **VidhyaCuratesBot**.
3. (Optional) Adds a note: *"Kitchen: Our everyday steel lunchbox"*.
4. Taps **Send**.
5. Within 2 seconds, the bot replies with the product picture and confirms it is live on `iamsaravofficial.com/store/` with tag `dhrav-21`!
