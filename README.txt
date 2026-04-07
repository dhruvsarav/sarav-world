SARAV GO-LIVE PATCH

Files included:
- src/App.jsx
- src/index.css
- index.html
- public/legal.css
- public/copyright/index.html
- public/privacy-policy/index.html
- public/terms/index.html
- public/404.html
- public/favicon.svg
- public/og-cover.svg

Before publishing:
1. Ensure these images exist in your project:
   - src/assets/blog/blog-few-miles.jpg
   - src/assets/blog/blog-saravs-world.jpg
   - src/assets/aibuilder/cognizant-latest-role.png

2. Replace all amazonUrl: "#" entries in src/App.jsx with real Amazon links.

3. Test:
   - Hero signature animation
   - Journey timeline
   - Blog buttons
   - Legal pages
   - Mobile layout

4. Build:
   npm run build

5. Publish the dist folder.

Note:
- Existing image compression is not part of this patch.
- This patch adds lazy-loading to non-hero visuals for better performance.
