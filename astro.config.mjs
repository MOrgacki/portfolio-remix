// @ts-check
import { defineConfig } from 'astro/config';

// Moving to a custom domain later: change `site`, set `base: '/'` and add public/CNAME.
export default defineConfig({
  site: 'https://morgacki.github.io',
  base: '/portfolio-remix',
  trailingSlash: 'always',
  output: 'static',
  build: {
    format: 'directory',
  },
});
