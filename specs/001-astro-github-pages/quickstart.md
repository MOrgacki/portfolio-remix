# Quickstart & Validation: Migrate Portfolio to a Static Site on GitHub Pages

**Feature**: `001-astro-github-pages` | **Date**: 2026-10-23

This guide proves the feature works end to end. Contracts:
[routes](./contracts/routes.md), [language runtime](./contracts/i18n.md),
[project data](./contracts/project.schema.json); entities in [data-model.md](./data-model.md).

## Prerequisites

- Node.js 24 (`nvm use` reads `.nvmrc`), npm 11.
- Repository setting **Pages → Build and deployment → Source = GitHub Actions** (one-time).
- For the side-by-side content comparison: the legacy app still runnable with `reflex run`.

## Setup

```bash
npm ci
npx playwright install --with-deps chromium
```

## Local run

| Command | Expected outcome |
|---|---|
| `npm run dev` | Dev server at `http://localhost:4321/portfolio-remix/` |
| `npm run check` | i18n parity check, `astro check`, Prettier check — all exit 0 |
| `npm run build` | `dist/` created, no errors or new warnings |
| `npm run preview` | Built site at `http://localhost:4321/portfolio-remix/` |
| `npm run test:e2e` | All Playwright + axe tests pass against the preview |

## Validation scenarios

Each maps to the spec; run automated ones via `npm run test:e2e`, manual ones in a browser on
the preview (and later on production).

1. **All pages reachable (US1, FR-001, FR-013)** — open each route in the routes contract
   directly and after refresh; each returns its page. `/portfolio-remix/does-not-exist/` shows
   the branded 404 with a Home link. *(automated)*
2. **Content parity (FR-002, FR-004, SC-001)** — run the legacy app and the preview side by side;
   walk every section of every page in EN and PL using the parity checklist produced during
   implementation; count projects on `/projects/` = 35. *(manual + project count automated)*
3. **Language (US2, FR-007–FR-010)** — with browser locale `pl-PL` the first visit shows Polish;
   with `en-US` English; toggle switches all text, alt texts and tab title; reload and navigate
   keep the choice; set `localStorage['portfolio.lang']='xx'` → falls back to locale.
   *(automated, Playwright `locale` option)*
4. **No flash (edge case)** — with stored `pl`, a screenshot taken at first paint (or the
   Performance panel filmstrip) contains no English text. *(automated)*
5. **No JavaScript (edge case)** — disable JS: all pages readable in English, nav and contact
   links work. *(automated, `javaScriptEnabled: false`)*
6. **Projects (US3, FR-016–FR-018, SC-008)** — search "Playwright" narrows the list; combine
   with a domain filter; nonsense query shows the empty-result message; "Clear filters"
   restores 35; open a project, close with button, Escape, and backdrop; focus returns to the
   card; URL never changes; no broken images or dead code/demo buttons. *(automated)*
7. **"Let's talk" (FR-005, US5)** — on Home the CTA opens `/contact/`; no chat UI exists;
   email link is `mailto:`; LinkedIn/GitHub open in a new tab. *(automated)*
8. **Accessibility & motion (FR-020, FR-021)** — axe reports no serious/critical violations on
   any page in either language; with `reducedMotion: 'reduce'` background animation is static;
   keyboard-only tab through each page shows visible focus. *(automated + manual tab-through)*
9. **Responsive (FR-015)** — at 320, 768, 1440 and 1920 px widths no page has horizontal
   scroll (`scrollWidth <= clientWidth`). *(automated)*
10. **Links (SC-003)** — crawl all internal links and image URLs from `/`; zero non-200 results.
    Repeat with base `/` (`npm run build -- --base /` then preview) to prove custom-domain
    readiness (FR-014). *(automated)*
11. **Nothing private published (FR-024)** — `dist/` contains no `.pdf` and no legacy Python
    files. *(CI step)*
12. **Performance (SC-004, SC-005)** — Lighthouse (mobile) on each page of the preview: all four
    categories ≥ 90; LCP ≤ 2 s on simulated 4G. *(manual)*
13. **Publish on push (US4, FR-023, SC-006)** — change one translation, push to `main`: the
    workflow is green and the change is live within 10 minutes. Then push a commit removing one
    key from `pl.json`: `check` fails, `deploy` is skipped, production still serves the
    previous version. *(manual, on GitHub)*
14. **No tracking (FR-026)** — DevTools → Application: no cookies; Network: no requests to
    third-party domains. *(automated network assertion)*

## Done when

All scenarios pass on the preview, scenarios 12–13 pass on production, and the legacy files are
removed in a separate commit with `CLAUDE.md` describing the new stack (FR-025).
