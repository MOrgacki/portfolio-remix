// @ts-check
import { defineConfig } from 'astro/config';

// Served from the custom domain in public/CNAME (GitHub Pages), so the base is the root.
export default defineConfig({
  site: 'https://marcinorgacki.com',
  base: '/',
  trailingSlash: 'always',
  output: 'static',
  build: {
    format: 'directory',
    // Inline CSS so an uncached first visit paints fully styled without an extra request.
    inlineStylesheets: 'always',
  },
});
