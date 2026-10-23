// Renders public/og-image.jpg (1200x630), the link-preview image used by Open Graph / Twitter tags.
// Run from the repository root after changing the copy below:  node scripts/make-og-image.mjs
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { chromium } from '@playwright/test';

const logo = readFileSync(new URL('../src/assets/profile.png', import.meta.url)).toString('base64');

const html = `<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<style>
  * { margin: 0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 630px;
    overflow: hidden;
    font-family: 'Segoe UI', system-ui, sans-serif;
    color: #e2e8f0;
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    position: relative;
  }
  .glow { position: absolute; border-radius: 50%; filter: blur(90px); }
  .g1 { width: 520px; height: 520px; left: -140px; top: -180px; background: rgba(0, 212, 255, 0.28); }
  .g2 { width: 560px; height: 560px; right: -160px; bottom: -220px; background: rgba(139, 92, 246, 0.3); }
  .content {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    padding: 0 96px;
    gap: 28px;
  }
  .logo { width: 150px; }
  h1 {
    font-size: 96px;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    background: linear-gradient(90deg, #00d4ff, #5b73ff 55%, #8b5cf6);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    padding-bottom: 6px;
  }
  .tagline { font-size: 38px; font-weight: 600; color: #f1f5f9; }
  .chips { display: flex; gap: 14px; flex-wrap: wrap; }
  .chip {
    padding: 10px 22px;
    border: 1px solid rgba(0, 212, 255, 0.35);
    border-radius: 999px;
    background: rgba(0, 212, 255, 0.1);
    color: #7dd3fc;
    font-size: 24px;
    font-weight: 600;
  }
  .url {
    position: absolute;
    right: 96px;
    bottom: 56px;
    font-size: 26px;
    font-weight: 600;
    color: #94a3b8;
  }
</style>
</head>
<body>
  <div class="glow g1"></div>
  <div class="glow g2"></div>
  <div class="content">
    <img class="logo" src="data:image/png;base64,${logo}" alt="" />
    <h1>Marcin Orgacki</h1>
    <p class="tagline">QA, test automation and AI-driven process automation</p>
    <div class="chips">
      <span class="chip">8+ years</span>
      <span class="chip">Fintech</span>
      <span class="chip">AI</span>
      <span class="chip">Web · Mobile · Desktop · Cloud</span>
    </div>
  </div>
  <p class="url">marcinorgacki.com</p>
</body>
</html>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
await page.setContent(html, { waitUntil: 'load' });
await page.screenshot({
  path: fileURLToPath(new URL('../public/og-image.jpg', import.meta.url)),
  type: 'jpeg',
  quality: 88,
});
await browser.close();
console.log('public/og-image.jpg written');
