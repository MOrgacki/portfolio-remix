# Performance & Budget Results

**Measured**: 2026-10-23 on the local production build (`npm run build` + `astro preview`),
Lighthouse 12, mobile emulation, simulated throttling (T069–T071).

## Lighthouse (mobile)

| Page | Performance | Accessibility | Best Practices | SEO | LCP |
|---|---|---|---|---|---|
| `/` | 100 | 100 | 100 | 100 | 1.2 s |
| `/experience/` | 100 | 100 | 100 | 100 | 1.2 s |
| `/case-studies/` | 100 | 100 | 100 | 100 | 1.2 s |
| `/projects/` | 100 | 100 | 100 | 100 | 1.3 s |
| `/contact/` | 100 | 100 | 100 | 100 | 1.2 s |
| `/blog/` | 100 | 100 | 100 | 92 | 1.2 s |

- [x] All categories ≥ 90 on every page (SC-005)
- [x] LCP ≤ 2 s (SC-004)

## JavaScript (gzip)

| File | Size |
|---|---|
| language runtime (`lang.*.js`) | 0.5 KB |
| projects search/filters/dialog | 0.8 KB |
| layout entry | 0.1 KB |

- [x] Every page < 150 KB gz (actual total ≈ 1.4 KB)

## Images

- [x] Largest emitted image 127 KB (WebP); none above 300 KB (legacy PNGs were up to 951 KB)
- [x] All images have width/height (no layout shift) and lazy loading below the fold

## To repeat on production

- [ ] Lighthouse on `https://morgacki.github.io/portfolio-remix/` after the first deploy
