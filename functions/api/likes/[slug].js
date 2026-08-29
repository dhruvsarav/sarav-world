// functions/api/likes/[slug].js
//
// Cloudflare Pages Function. Lives at repo root under functions/ — a SIBLING
// of public/, not inside it. Cloudflare auto-detects this folder and deploys
// it as a serverless endpoint on every push, on the SAME domain as the site
// (iamsaravofficial.com/api/likes/:slug) — no separate `wrangler deploy`,
// no CORS config, no new deploy step. It rides the same "git push = live"
// workflow as everything else in this project.
//
// One-time manual setup required (Cloudflare dashboard, not this repo):
//   1. Cloudflare dashboard -> Workers & Pages -> KV -> create a namespace,
//      e.g. named "factdrop-likes".
//   2. sarav-world Pages project -> Settings -> Functions ->
//      KV namespace bindings -> add binding:
//        Variable name: LIKES_KV
//        KV namespace:  factdrop-likes (the one just created)
//   3. Push this functions/ folder. Done — no further deploy step.
//
// Storage shape: one KV key per fact, "likes:<slug>" -> string integer.

export async function onRequestGet(context) {
  const slug = context.params.slug;
  if (!slug) {
    return new Response(JSON.stringify({ error: "missing slug" }), { status: 400 });
  }
  const raw = await context.env.LIKES_KV.get(`likes:${slug}`);
  const count = parseInt(raw || "0", 10);
  return new Response(JSON.stringify({ slug, count }), {
    headers: { "content-type": "application/json" },
  });
}

export async function onRequestPost(context) {
  const slug = context.params.slug;
  if (!slug) {
    return new Response(JSON.stringify({ error: "missing slug" }), { status: 400 });
  }
  const key = `likes:${slug}`;
  const raw = await context.env.LIKES_KV.get(key);
  const next = (parseInt(raw || "0", 10)) + 1;
  await context.env.LIKES_KV.put(key, String(next));
  return new Response(JSON.stringify({ slug, count: next }), {
    headers: { "content-type": "application/json" },
  });
}
