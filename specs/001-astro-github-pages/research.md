# Research: Migrate Portfolio to a Static Site on GitHub Pages

**Feature**: `001-astro-github-pages` | **Date**: 2026-10-23 | **Spec**: [spec.md](./spec.md)

Versions below were checked against the npm registry on 2026-10-23.

## R1. Framework and output mode

- **Decision**: Astro 7.x (latest `7.4.2`) with the default static output (`output: 'static'`).
  No server adapter is installed.
- **Rationale**: User-mandated framework. Static output emits plain HTML/CSS/JS to `dist/`, which
  is all GitHub Pages can serve (Constitution II). Astro ships zero JS by default, so only the
  interactive parts (language switch, projects filters, pop-up, mobile menu) add script weight
  (Constitution IV).
- **Alternatives considered**: Vite + vanilla multi-page (more manual routing/layout work);
  Next.js static export (ships a React runtime on every page, against the JS budget).

## R2. Node.js and package manager

- **Decision**: Node.js 24 LTS (`.nvmrc` = `24`; local machine has 24.16.0, Astro 7 requires
  `>=22.23.4`). npm 11 with committed `package-lock.json`; CI uses `npm ci`.
- **Rationale**: Matches the constitution's "active LTS, pinned in `.nvmrc`" rule and the
  installed toolchain.
- **Alternatives considered**: pnpm (faster but adds a tool the constitution doesn't name).

## R3. Base path and public address

- **Decision**: `astro.config.mjs` sets `site: 'https://morgacki.github.io'` and
  `base: '/portfolio-remix'`, `trailingSlash: 'always'`. Every internal URL is built with a
  single helper `url(path)` that prefixes `import.meta.env.BASE_URL`; images go through
  `astro:assets`, which applies the base automatically.
- **Rationale**: Clarification Q3 (FR-014). Moving to a custom domain later means changing
  `site`/`base` and adding `public/CNAME` — configuration only, no content edits.
- **Alternatives considered**: hard-coded `/portfolio-remix/` prefixes (breaks on domain move);
  relative links (fragile across nested routes).

## R4. Bilingual rendering on shared addresses (no flash)

- **Decision**: Every page is pre-rendered once, containing **both** languages. A `<T k="…"/>`
  component renders `<span lang="en">…</span><span lang="pl">…</span>`. CSS hides the inactive
  language: `html:not([data-lang="pl"]) [lang="pl"], html[data-lang="pl"] [lang="en"]
  { display: none }`. A tiny inline, blocking script in `<head>` resolves the language
  (stored choice → browser locale → `en`) and sets `data-lang` and `lang` on `<html>` before the
  first paint. Translatable attributes (`alt`, `aria-label`, `placeholder`, `title`) carry
  `data-i18n-*` values that the language script swaps; `document.title` is swapped the same way.
- **Rationale**: Clarification Q1 (shared addresses, FR-007a). Because the inline script runs
  before the body is painted, Polish visitors never see English first (spec edge case). Without
  JS, CSS defaults to English (spec edge case). Hidden (`display:none`) text is not read by
  screen readers. Duplicated text is small (~185 keys + project texts), well within budget.
- **Alternatives considered**:
  - Client-side dictionary swap over `data-i18n` keys — needs JS for all text, risks flash,
    harder to keep markup semantic.
  - Fetching a Polish JSON on toggle — network dependency and visible delay.
  - Astro built-in i18n routing (`/pl/`) — rejected by Clarification Q1.

## R5. Language persistence and detection

- **Decision**: `localStorage` key `portfolio.lang` with values `en` | `pl`. Detection on first
  visit: `navigator.languages[0]` starts with `pl` → `pl`, else `en`. Invalid value or blocked
  storage (try/catch) → detection → `en`. No cookies (FR-026).
- **Rationale**: FR-008, FR-010, spec edge cases; local storage is not a cookie and needs no
  consent banner for a strictly functional preference.

## R6. Translation source and parity gate

- **Decision**: One-off migration script `scripts/migrate/export_translations.py` imports
  `TRANSLATIONS` from the legacy module and writes `src/i18n/en.json` and `src/i18n/pl.json`
  (keys sorted, UTF-8). The chat keys (`chat_*`, `about_chat_*`) are dropped and a new
  `about_cta_lets_talk` key is added (FR-005). `scripts/check-i18n.mjs` runs as `prebuild` and
  in CI and fails if key sets differ or any value is empty (FR-011). The `<T>` component is typed
  against `keyof typeof en`, so an unknown key fails `astro check`.
- **Rationale**: Port, don't rewrite (Constitution migration rule); parity enforced by the build
  (Constitution I "build SHOULD fail on missing keys").
- **Finding**: Legacy data has Polish descriptions for only **26 of 35** projects
  (`proj_desc_<id>` keys), and project `achievements` exist only in English. Reaching SC-002
  (0 untranslated texts) requires writing the missing Polish copy; this is a content task for
  the owner to review, not something to invent silently.

## R7. Project data

- **Decision**: An Astro content collection `projects` backed by `src/data/projects.json`
  (file loader) and validated by a Zod schema mirroring
  [contracts/project.schema.json](./contracts/project.schema.json). Localised fields are
  `{ en, pl }` objects inside each project. A migration script
  `scripts/migrate/export_projects.py` builds the JSON from `PROJECTS_DATA`, the `proj_desc_*`
  keys and `TECH_CATEGORIES`.
- **Rationale**: Build-time validation catches missing fields, bad image paths, or missing
  Polish text (FR-004, SC-001). Keeping each project self-contained makes adding a project a
  one-file edit (User Story 4).
- **Alternatives considered**: Keep project texts as translation keys (scatters one project over
  three files); Markdown file per project (overkill for short texts).

## R8. Projects interactivity

- **Decision**: All 35 cards are rendered at build time (newest first, by `id` desc, as in the
  legacy app). One vanilla TypeScript module (`src/scripts/projects.ts`) handles search and
  filters by toggling the `hidden` attribute, reading filter facts from `data-*` attributes on
  each card. Semantics preserved from legacy: technologies = multi-select, match **any**;
  domain, platform, type = single select; all combined with AND. Search matches title,
  description (active language) and technologies, case-insensitive, after Unicode
  normalisation (FR-016 widens the legacy title-only search). Details use one native
  `<dialog>` filled from an embedded JSON island; `showModal()` provides Escape-to-close and
  inert background, a backdrop click closes it, and focus is returned to the opening card
  (FR-018). The page address never changes (Clarification Q2).
- **Rationale**: No UI framework needed; keeps per-page JS far under 150 KB gz.
- **Alternatives considered**: Preact/React island (adds ~10–45 KB runtime for simple filtering);
  Pagefind/Fuse search (overkill for 35 items).

## R9. Images

- **Decision**: Source images move to `src/assets/` with descriptive kebab-case names (e.g.
  `project22.png` → `staking-app.png`, mapped in the migration script). Rendering uses
  `astro:assets` `<Image>`/`<Picture>` to emit WebP/AVIF at display sizes with width/height
  (no layout shift). `favicon.ico` goes to `public/`. Projects without an image show a styled
  placeholder, never a broken image.
- **Rationale**: Constitution IV (≤300 KB per image, descriptive names), SC-004/SC-005.

## R10. Visual identity and motion

- **Decision**: Theme tokens as CSS custom properties in `src/styles/tokens.css` (dark gradient
  `#0f0f23 → #1a1a2e → #16213e`, cyan accent, slate grays) ported from the legacy styles. The
  animated background is pure CSS and is disabled under `prefers-reduced-motion: reduce`. The
  initial 2-second loader and page-transition loader are dropped (FR-022).
- **Rationale**: FR-019, FR-020, FR-022, Constitution III/IV.

## R11. Deployment

- **Decision**: `.github/workflows/deploy.yml` on push to `main` (+ manual dispatch):
  job `build` (checkout → setup-node from `.nvmrc` → `npm ci` → `npm run check` → `npm run build`
  → `npm run test:e2e` against the preview → upload Pages artifact) and job `deploy`
  (`actions/deploy-pages`, `needs: build`). Repository setting *Pages → Source* must be
  "GitHub Actions" (one-time manual step).
- **Rationale**: If any step fails, `deploy` never runs, so the live site stays unchanged
  (FR-023, User Story 4). Typical runtime 2–4 minutes, within SC-006 (10 minutes).
- **Alternatives considered**: `withastro/action` (convenient but hides the build steps we want
  to gate with tests); `gh-pages` branch push (commits build output, against the constitution).

## R12. Quality tooling

- **Decision**:
  - `astro check` (type checking of `.astro`/`.ts`), Prettier + `prettier-plugin-astro`.
  - Playwright (`@playwright/test` 1.64) end-to-end tests against `astro preview` with the base
    path: page smoke for all routes, language detection/toggle/persistence, no-flash check,
    projects filters/search/pop-up, 404, internal link crawl (SC-003), reduced motion.
  - `@axe-core/playwright` for automated accessibility checks on every page (FR-021).
  - Lighthouse run manually per [quickstart.md](./quickstart.md) for SC-005 (not in CI, to avoid
    flaky score gates).
- **Rationale**: Constitution requires lint/format to pass and manual EN/PL + mobile checks;
  automating them fits an owner who is a QA automation professional and protects User Story 4.
  New dependencies are dev-only and justified here (Constitution V).
- **TypeScript**: use the version satisfying `@astrojs/check`'s peer range (verify at install;
  TypeScript 7.x was just released and may not yet be supported).

## R13. Repository layout and legacy cut-over

- **Decision**: The Astro project lives at the repository root next to the legacy app during
  migration. Astro uses `src/`, `public/`, `astro.config.mjs`, `package.json`; legacy uses
  `portfolio/`, `state.py`, `rxconfig.py`, `requirements.txt`, `Dockerfile`, `assets/` — no path
  collisions. Migration scripts read legacy files; nothing writes into them. After content
  parity is verified and the site is live, a separate commit removes the legacy files,
  `.web/`-style Reflex artefacts and the Dockerfile, and rewrites `CLAUDE.md` (FR-025).
  Root PDFs are never copied into `public/` and are added to `.gitignore` (FR-024).
- **Rationale**: Constitution "Migration from the Legacy Reflex App"; keeps the legacy app
  runnable as a side-by-side reference until parity is signed off.

**Legacy export source (T001)**: commit `cf13481` — "(feat): legacy Reflex app final content
before Astro migration". All migration scripts were run against this content.
