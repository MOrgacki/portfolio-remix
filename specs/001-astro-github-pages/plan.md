# Implementation Plan: Migrate Portfolio to a Static Site on GitHub Pages

**Branch**: `001-astro-github-pages` | **Date**: 2026-10-23 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-astro-github-pages/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Rebuild the Reflex portfolio as a static Astro 7 site published to
`https://morgacki.github.io/portfolio-remix/` by GitHub Actions. All six pages and the 35 projects
are ported from the legacy Python sources by one-off export scripts into JSON (translations,
projects, small content lists) validated at build time. Both languages are pre-rendered into
every page on shared addresses; a blocking head script picks the language before first paint,
so there is no flash and no JS is needed to read English. Interactivity (language toggle,
projects search/filters, native `<dialog>` details, mobile menu) is vanilla TypeScript. The
artificial loader and AI-chat placeholder are dropped ("Let's talk" CTA instead). Playwright +
axe tests gate the deploy job, so a failed build never replaces the live site.

## Technical Context

**Language/Version**: TypeScript (version within `@astrojs/check` peer range), HTML, CSS;
Node.js 24 LTS for tooling. Python 3.11 only for one-off migration scripts.

**Primary Dependencies**: `astro` 7.4.x (static output, `astro:assets` + `sharp` for images,
content collections). Dev: `@astrojs/check`, `prettier` + `prettier-plugin-astro`,
`@playwright/test` 1.64, `@axe-core/playwright` 4.14. No UI framework, no runtime libraries.

**Storage**: Files in the repo (`src/i18n/*.json`, `src/data/*.json`); visitor language in
`localStorage` only.

**Testing**: `npm run check` (i18n parity script, `astro check`, Prettier), Playwright e2e +
axe against `astro preview`, manual Lighthouse and parity walkthrough
([quickstart.md](./quickstart.md)).

**Target Platform**: Evergreen browsers (last 2 versions of Chrome, Edge, Firefox, Safari incl.
iOS Safari); GitHub Pages static hosting.

**Project Type**: Static website (single project).

**Performance Goals**: Lighthouse mobile ≥ 90 in all four categories; LCP ≤ 2 s on simulated 4G;
≤ 150 KB gz JS per page (expected < 15 KB); images ≤ 300 KB.

**Constraints**: No server runtime; base path `/portfolio-remix/` today, `/` later by config;
no cookies or third-party requests; no visible language flash; works without JS in English.

**Scale/Scope**: 7 routes (6 pages + 404), ~185 translation keys × 2 languages, 35 projects,
~30 images, one maintainer.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Constitution v2.0.0.

| Principle / rule | Pre-research | Post-design | Evidence |
|---|---|---|---|
| I. Bilingual parity — single source per language, key parity, build fails on missing keys | PASS | PASS | `src/i18n/{en,pl}.json`, `check:i18n` prebuild, typed `<T>`; Localized fields in project schema (R6, contracts/i18n.md) |
| I. Client-side switching or per-language routes | PASS | PASS | Shared routes + head script (R4, Clarification Q1) |
| II. Static output only, no server/DB | PASS | PASS | Astro static output, no adapter (R1) |
| II. Base-path aware links, deep links work, 404 fallback | PASS | PASS | `url()` helper, `trailingSlash`, real files per route, `404.astro` (R3, contracts/routes.md) |
| II. Shared layout once; no dead/backup files | PASS | PASS | `BaseLayout.astro` + components; legacy removed in separate commit (R13) |
| III. Responsive, semantic, alt text, focus, AA contrast, reduced motion | PASS | PASS | FR-015/020/021, axe + viewport tests (R10, R12) |
| IV. Assets in public/static dir, base-aware, compressed, descriptive names, JS budget, no artificial delay, Lighthouse ≥ 90 | PASS | PASS | `astro:assets` from `src/assets/` (processed; only favicon in `public/`), rename map, loader dropped (R9, R10) |
| V. Content-first scope; no secrets; contact without backend; dependencies justified; YAGNI | PASS | PASS | mailto/profile links, no tracking (FR-026), dev-only deps justified (R12), no CMS/UI framework |
| Tech: Node LTS in `.nvmrc`, npm + lockfile, `npm ci`, `npm run build` → `dist/`, `npm run preview`, Actions deploy, no build output on `main`, theme tokens | PASS | PASS | R2, R11, `src/styles/tokens.css` |
| Migration: legacy is reference only, content ported not rewritten, removal in dedicated commit | PASS | PASS | Export scripts read legacy files read-only (R6, R7, R13) |
| Workflow: build + preview + EN/PL + mobile checks, lint passes, green deploy, commit convention, CLAUDE.md updated | PASS | PASS | quickstart scenarios; CLAUDE.md rewrite in cut-over (FR-025) |

Note on IV: assets live in `src/assets/` rather than `public/` so they can be optimised by
`astro:assets`; the constitution names `public/` only as an example ("e.g."), so this is
compliant and not a deviation.

**Result**: no violations; Complexity Tracking not needed.

## Project Structure

### Documentation (this feature)

```text
specs/001-astro-github-pages/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   ├── routes.md
│   ├── i18n.md
│   └── project.schema.json
├── checklists/
│   └── requirements.md
└── tasks.md             # Phase 2 output (/speckit-tasks — not created here)
```

### Source Code (repository root)

```text
astro.config.mjs            # site, base '/portfolio-remix', trailingSlash 'always'
package.json                # scripts: dev, check, check:i18n, build, preview, test:e2e, format
package-lock.json
.nvmrc                      # 24
tsconfig.json
playwright.config.ts
.github/workflows/deploy.yml

public/
└── favicon.ico

src/
├── assets/
│   ├── profile.png
│   └── projects/           # renamed, kebab-case project images
├── components/
│   ├── T.astro             # bilingual text <span lang="en|pl">
│   ├── Header.astro        # nav + mobile menu + language button
│   ├── Footer.astro
│   ├── AnimatedBackground.astro
│   ├── LanguageButton.astro
│   ├── SocialLinks.astro
│   ├── ProjectCard.astro
│   ├── ProjectFilters.astro
│   ├── ProjectDialog.astro
│   └── sections/           # Hero, About, Services, Achievements, Timeline, Skills, Domains…
├── content.config.ts       # projects collection + Zod schema
├── data/
│   ├── projects.json
│   ├── tech-categories.json
│   ├── services.json
│   ├── achievements.json
│   ├── timeline.json
│   ├── skills.json
│   ├── languages.json
│   └── contact.json
├── i18n/
│   ├── en.json
│   ├── pl.json
│   └── index.ts            # types, t(), Lang
├── layouts/
│   └── BaseLayout.astro    # head (meta, inline lang script), header, footer, background
├── lib/
│   └── url.ts              # base-aware url() helper
├── pages/
│   ├── index.astro
│   ├── experience.astro
│   ├── case-studies.astro
│   ├── projects.astro
│   ├── contact.astro
│   ├── blog.astro
│   └── 404.astro
├── scripts/
│   ├── lang.ts             # toggle, attribute/title swap, langchange event
│   ├── projects.ts         # search, filters, dialog
│   └── menu.ts             # mobile navigation
└── styles/
    ├── tokens.css
    └── global.css

scripts/
├── check-i18n.mjs          # parity gate (prebuild + CI)
├── check-dist.mjs          # no PDFs / legacy files in dist (CI)
└── migrate/                # one-off, removed with legacy app
    ├── export_translations.py
    ├── export_projects.py
    └── image_map.json      # old file name → new slug

tests/
└── e2e/
    ├── pages.spec.ts       # routes, 404, no-JS, responsive, links
    ├── i18n.spec.ts        # detection, toggle, persistence, no flash
    ├── projects.spec.ts    # search, filters, dialog, count
    ├── a11y.spec.ts        # axe, reduced motion, focus
    └── privacy.spec.ts     # no cookies, no third-party requests

# Legacy (reference only, removed in a dedicated commit after go-live):
portfolio/  state.py  rxconfig.py  requirements.txt  Dockerfile  assets/
```

**Structure Decision**: Single static-site project at the repository root, next to the legacy
Reflex app (no path collisions, see research R13). `src/` holds the site, `scripts/` holds build
gates and one-off migration scripts, `tests/e2e/` holds Playwright tests. The legacy directories
are removed in a separate commit once content parity is confirmed and the site is live.

## Complexity Tracking

No constitution violations; nothing to justify.

## Risks & Follow-ups

- **Missing Polish copy** (research R6): 9 project descriptions, all achievements and image alt
  texts need Polish text before SC-002 can pass. Tasks should draft them and flag for owner
  review.
- **TypeScript 7 compatibility**: confirm `@astrojs/check` peer range at install; fall back to
  TypeScript 5.x if needed.
- **One-time GitHub setting**: Pages source must be switched to "GitHub Actions" by the owner.
- **Uncommitted legacy changes**: the working tree has uncommitted edits to the Reflex app; commit
  or stash them before migration scripts read the legacy sources so the export is reproducible.
