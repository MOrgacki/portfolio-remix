---

description: "Task list for migrating the portfolio to a static Astro site on GitHub Pages"
---

# Tasks: Migrate Portfolio to a Static Site on GitHub Pages

**Input**: Design documents from `/specs/001-astro-github-pages/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included. The plan (research R12) makes Playwright + axe tests a deploy gate and
quickstart.md marks scenarios as automated, so each story has its e2e tests. Write them before
or together with the implementation; they must fail before the story is implemented.

**Organization**: Tasks are grouped by user story so each story can be implemented and tested
on its own.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: User story from spec.md (US1–US5)
- Paths are relative to the repository root (single project, see plan.md → Project Structure)
- Legacy sources (`portfolio/`, `state.py`, `assets/`) are **read-only** until T078

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Astro project skeleton next to the legacy app, tooling and scripts

- [X] T001 Confirm the working tree is committed (legacy Reflex edits included) so exports are reproducible; record the legacy commit hash in specs/001-astro-github-pages/research.md under R13
- [X] T002 Create package.json at repo root with `"type": "module"`, `"private": true`, `engines.node: ">=24"`, and scripts `dev` (astro dev), `build` (astro build), `preview` (astro preview), `check:i18n` (node scripts/check-i18n.mjs), `check:dist` (node scripts/check-dist.mjs), `check` (npm run check:i18n && astro check && prettier --check .), `prebuild` (npm run check:i18n), `format` (prettier --write .), `test:e2e` (playwright test)
- [X] T003 Install `astro@^7.4.2` and `sharp` as dependencies, and `@astrojs/check`, `typescript` (version accepted by @astrojs/check's peer range; fall back to 5.x if 7.x is rejected), `prettier`, `prettier-plugin-astro`, `@playwright/test@^1.64`, `@axe-core/playwright@^4.14` as devDependencies; commit package-lock.json
- [X] T004 [P] Create .nvmrc containing `24`
- [X] T005 [P] Create astro.config.mjs with `site: 'https://morgacki.github.io'`, `base: '/portfolio-remix'`, `trailingSlash: 'always'`, `output: 'static'`, no adapter, and `build.format: 'directory'`
- [X] T006 [P] Create tsconfig.json extending `astro/tsconfigs/strict` with `resolveJsonModule: true` and include `src`, `tests`, `scripts`
- [X] T007 [P] Create .prettierrc (plugins: prettier-plugin-astro; printWidth 100) and .prettierignore (dist/, .astro/, node_modules/, portfolio/, assets/, specs/, .specify/, .claude/, *.pdf)
- [X] T008 [P] Update .gitignore to add `dist/`, `.astro/`, `node_modules/`, `playwright-report/`, `test-results/`, and `*.pdf` (FR-024: root PDFs are never published or committed)
- [X] T009 [P] Create playwright.config.ts: testDir `tests/e2e`, `webServer` runs `npm run build && npm run preview -- --port 4321`, `baseURL: 'http://localhost:4321/portfolio-remix/'`, projects `chromium-desktop` (1440×900) and `chromium-mobile` (Pixel 7), `reporter: [['list'], ['html', { open: 'never' }]]`
- [X] T010 [P] Create the empty directory layout from plan.md with `.gitkeep` where needed: src/{assets/projects,components/sections,data,i18n,layouts,lib,pages,scripts,styles}, public/, scripts/migrate/, tests/e2e/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Translations, bilingual text component, layout, styles and URL helper that every page needs

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T011 Write scripts/migrate/export_translations.py: import `TRANSLATIONS` from portfolio/translations.py (run from repo root with `python -I` and an explicit sys.path entry), drop keys `chat_greeting`, `chat_placeholder`, `chat_close`, `about_chat_button`, `about_chat_title` and all `proj_desc_*` keys, add `about_cta_lets_talk` (en "Let's talk", pl "Porozmawiajmy"), `not_found_title`, `not_found_text`, `projects_empty_result`, and `page_title_<route>` / `page_description_<route>` for routes home, experience, case_studies, projects, contact, blog (English values taken from the legacy `title=` strings, e.g. "Marcin Orgacki | Projects"); write src/i18n/en.json and src/i18n/pl.json sorted by key, UTF-8, 2-space indent
- [X] T012 Run scripts/migrate/export_translations.py, review the diff of src/i18n/en.json and src/i18n/pl.json, and fix legacy mojibake (e.g. "đź› ď¸Ź" → "🛠️") so every value is valid UTF-8 text
- [X] T013 [P] Write scripts/check-i18n.mjs: load src/i18n/en.json and src/i18n/pl.json, print keys missing in either file and keys with empty/whitespace values, exit 1 on any finding, exit 0 with a one-line summary otherwise (FR-011, contracts/i18n.md "Build-time guarantees")
- [X] T014 [P] Create src/i18n/index.ts exporting `type Lang = 'en' | 'pl'`, `type TKey = keyof typeof en`, `dict: Record<Lang, Record<TKey, string>>`, and `t(key: TKey, lang: Lang): string`
- [X] T015 Create src/components/T.astro: props `k: TKey`, optional `as` tag (default `span`); renders `<span lang="en">{t(k,'en')}</span><span lang="pl">{t(k,'pl')}</span>` inside the wrapper (contracts/i18n.md DOM contract)
- [X] T016 [P] Create src/lib/url.ts exporting `url(path: string): string` that joins `import.meta.env.BASE_URL` and `path`, guarantees exactly one slash between parts and a trailing slash for page paths (R3)
- [X] T017 [P] Create src/styles/tokens.css with CSS custom properties ported from portfolio/portfolio.py and portfolio/main.py: background gradient `#0f0f23 → #1a1a2e → #16213e`, `--accent` cyan, slate gray scale, radius large, tech category colors `--tech-cyan`, `--tech-blue`, `--tech-purple`, `--tech-pink`, `--tech-green`, `--tech-orange` (values from `TECH_CATEGORIES` in portfolio/projects.py), LinkedIn/GitHub brand colors from portfolio/main.py
- [X] T018 Create src/styles/global.css: modern reset, body background from tokens, typography scale for mobile/tablet/desktop, visible `:focus-visible` outline, `.visually-hidden`, and the language rule `html:not([data-lang="pl"]) [lang="pl"], html[data-lang="pl"] [lang="en"] { display: none !important }`, plus `@media (prefers-reduced-motion: reduce)` disabling animations/transitions
- [X] T019 [P] Create src/components/AnimatedBackground.astro: pure-CSS port of `animated_background()`, `background_shapes()`, `particle_field()` and `enhanced_gradient_overlay()` from portfolio/animations.py, `aria-hidden="true"`, `pointer-events: none`, static under reduced motion (FR-019, FR-020)
- [X] T020 [P] Port image assets: create scripts/migrate/image_map.json mapping every legacy file in assets/ to a kebab-case name derived from the project that uses it in portfolio/projects.py (`image` field; e.g. `/project1.png` used by "Waste Management Platform" → `waste-management-platform.png`, `minig_web.png` → `mining-web.png`, `insurance_App.png` → `insurance-app.png`, `panel_ai_gaminifaction.png` → `ai-gamification-panel.png`, `logo.png` → `profile.png`), then copy the files to src/assets/projects/ (and src/assets/profile.png) under the new names and copy assets/favicon.ico to public/favicon.ico; delete images not referenced by any project or page
- [X] T021 Create src/layouts/BaseLayout.astro: props `titleKey`, `descriptionKey`, `navKey?`; `<html lang="en" data-lang="en">`; head with charset, viewport, English `<title>` and `<meta name="description">`, `<meta name="i18n-title-pl">` with the Polish title, canonical URL from `Astro.site` + base, Open Graph tags (og:image = profile image via astro:assets), favicon via `url('favicon.ico')`, imports tokens.css and global.css; body with skip link, AnimatedBackground, `<slot name="header"/>`, `<main id="main">`, `<slot/>`, `<slot name="footer"/>`
- [X] T022 Run `npm run check` and `npm run build` with a placeholder src/pages/index.astro using BaseLayout and `<T k="home_hello"/>` to prove the foundation compiles under the `/portfolio-remix/` base

**Checkpoint**: Foundation ready — user story implementation can begin

---

## Phase 3: User Story 1 — Visitor browses the portfolio on the new public address (Priority: P1) 🎯 MVP

**Goal**: All six pages plus 404 with full English+Polish content (rendered, English visible by default), shared header/footer/navigation, responsive layout

**Independent Test**: `npm run preview`, open every route in contracts/routes.md directly and after refresh, compare each page section by section with the legacy app (`reflex run`); quickstart scenarios 1, 2 (pages part), 5, 9, 10

### Tests for User Story 1

- [X] T023 [P] [US1] Write tests/e2e/pages.spec.ts: for each route in contracts/routes.md assert HTTP 200, `<h1>` visible, `<title>` and meta description non-empty; `does-not-exist/` shows the 404 heading and a Home link; navigation has `aria-current="page"` on the current page; with `javaScriptEnabled: false` every page shows English text and nav links work
- [X] T024 [P] [US1] Add to tests/e2e/pages.spec.ts a responsive test: at widths 320, 768, 1440, 1920 assert `document.documentElement.scrollWidth <= clientWidth` on every page (FR-015)
- [X] T025 [P] [US1] Write tests/e2e/links.spec.ts: crawl from the base URL, collect every same-origin `href` and `img[src]`/`srcset`, request each and assert status 200 (SC-003)

### Implementation for User Story 1

- [X] T026 [P] [US1] Create src/components/Header.astro: logo/name linking to `url('')`, desktop nav (port `nav_item_desktop` from portfolio/header.py) with six links using `<T>` for labels (`nav_home`, `nav_experience`, `nav_case_studies`, `nav_projects`, `nav_contact`, `nav_blog`) and `aria-current="page"` for `navKey`, mobile menu button + panel (port `nav_item_mobile` and portfolio/sidebar.py), and a slot for the language button
- [X] T027 [P] [US1] Create src/scripts/menu.ts: toggle the mobile menu panel (`aria-expanded`, `hidden`), close on Escape, on link click and on outside click; return focus to the menu button
- [X] T028 [P] [US1] Create src/components/Footer.astro porting portfolio/footer.py (attribution text via `<T>`)
- [X] T029 [P] [US1] Create src/data/services.json (6 items: `id`, `icon`, `titleKey`, `descKey` from `service_*` keys), src/data/timeline.json (6 items from `timeline_step1..6` and `_desc`), src/data/achievements.json (6 items with `problemKey`, `solutionKey`, `resultKey` from `achievement1..6_*`, optional `projectTitle`/`projectLink` from portfolio/case_studies.py), src/data/skills.json and src/data/languages.json (from portfolio/experience.py and the "Languages" keys); every `*Key` must exist in src/i18n/en.json
- [X] T030 [P] [US1] Create section components in src/components/sections/: Hero.astro (hello/I'm/rotating titles `home_title_1..3`, profile image via astro:assets with alt), About.astro (port `_create_info_view` and `_create_window_box` from portfolio/main.py WITHOUT the chat view), Services.astro, Achievements.astro, Timeline.astro, Skills.astro, Domains.astro (port `_create_expertise_box` and `_create_badges`)
- [X] T031 [P] [US1] Create src/components/SocialLinks.astro from the `data` list in portfolio/main.py (GitHub `https://github.com/MOrgacki`, LinkedIn `https://www.linkedin.com/in/m-orgacki/`, Email `mailto:marcinorgacki@gmail.com`) with brand colors, accessible names, `target="_blank" rel="noopener noreferrer"` for external profiles only
- [X] T032 [US1] Build src/pages/index.astro with BaseLayout (`titleKey: 'page_title_home'`, `navKey: 'nav_home'`), Header, Footer and sections in legacy order from `Main.build_view()` in portfolio/main.py, including the contact section (`contact_section()`) and SocialLinks
- [X] T033 [P] [US1] Build src/pages/experience.astro porting every section of `experience_page()` in portfolio/experience.py (subtitle, description, tech stack groups, key achievements, languages with levels, certificates)
- [X] T034 [P] [US1] Build src/pages/case-studies.astro porting `case_studies_page()`, `achievement_card()` and `project_info_box()` from portfolio/case_studies.py using src/data/achievements.json; project links point to `url('projects/')`; CTA links to `url('contact/')`
- [X] T035 [P] [US1] Build src/pages/contact.astro porting `contact_page()` from portfolio/contact.py (Get in Touch texts + SocialLinks)
- [X] T036 [P] [US1] Build src/pages/blog.astro porting `blog_page()` from portfolio/blog.py: "coming soon" heading, `blog_topic_1..4` list, suggestions text, Home link (FR-003)
- [X] T037 [US1] Build the page shell src/pages/projects.astro (BaseLayout with `page_title_projects`, heading `proj_title`, intro `proj_description`, empty regions with ids `project-filters` and `project-list`) so all routes exist; cards, filters and the pop-up are added in US3
- [X] T038 [P] [US1] Build src/pages/404.astro with `not_found_title`, `not_found_text` and a Home link via `url('')`
- [X] T039 [US1] Run tests/e2e/pages.spec.ts and tests/e2e/links.spec.ts until green; walk each page against the legacy app in English and record any missing section in specs/001-astro-github-pages/checklists/parity.md (one checkbox per legacy section per page)

**Checkpoint**: All pages browsable with full content; English visible; deployable as MVP

---

## Phase 4: User Story 2 — Visitor reads the site in Polish or English (Priority: P1)

**Goal**: Language detection, toggle and persistence on shared addresses with no flash (contracts/i18n.md)

**Independent Test**: Quickstart scenarios 3 and 4 — Polish locale shows Polish on first visit, toggle switches everything including alt texts and tab title, choice persists, invalid storage falls back

### Tests for User Story 2

- [X] T040 [P] [US2] Write tests/e2e/i18n.spec.ts: context `locale: 'pl-PL'` → `html[data-lang="pl"]` and Polish nav text visible on first visit; `locale: 'en-US'` → English; clicking `[data-lang-toggle]` switches visible text, an image `alt`, and `document.title`; reload and navigation keep the choice; `localStorage['portfolio.lang']='xx'` → locale-based result; on every page in both languages no element with `[lang]` shows empty text
- [X] T041 [P] [US2] Add a no-flash test to tests/e2e/i18n.spec.ts: with `portfolio.lang='pl'` pre-seeded via `addInitScript`, assert `document.documentElement.dataset.lang === 'pl'` in a `DOMContentLoaded` handler registered by `addInitScript` (i.e. before first paint) and that no `[lang="en"]` text node inside `<main>` is visible at that moment

### Implementation for User Story 2

- [X] T042 [US2] Add the inline blocking script to the `<head>` of src/layouts/BaseLayout.astro (`<script is:inline>` placed before stylesheets): read `localStorage.getItem('portfolio.lang')` in try/catch, accept only `en`/`pl`, else check `navigator.languages[0] || navigator.language` starts with `pl`, else `en`; set `documentElement.dataset.lang` and `documentElement.lang`
- [X] T043 [US2] Create src/scripts/lang.ts: `applyLang(lang)` swaps attributes from `data-i18n-{alt|aria-label|placeholder|title}-{en|pl}` on all elements, sets `document.title` from `<title>` (en) or `meta[name="i18n-title-pl"]` (pl), updates the toggle's `aria-label`; on toggle click flip the language, persist `portfolio.lang` (try/catch), call `applyLang`, dispatch `window` event `langchange` with `{ detail: { lang } }`; run `applyLang` once on load
- [X] T044 [P] [US2] Create src/components/LanguageButton.astro porting `floating_language_button()` (portfolio/floating_button.py) and `language_switcher()` (portfolio/header.py): `<button type="button" data-lang-toggle>` showing "PL"/"EN" via `<T>`-style spans, `data-i18n-aria-label-en="Przełącz na polski"`-style labels naming the target language; mount it in Header.astro's slot and as the floating button in BaseLayout.astro
- [X] T045 [US2] Add bilingual attribute support: extend T.astro usage guidance and update every `<img>`/`<Image>` and `aria-label` in src/components/** and src/pages/** to carry `data-i18n-alt-en/pl` (or `-aria-label-`) with values from translation keys
- [X] T046 [US2] Switch through every page in Polish in the preview and complete the Polish column of specs/001-astro-github-pages/checklists/parity.md; fix any missing/incorrect Polish keys in src/i18n/pl.json

**Checkpoint**: US1 + US2 together satisfy both P1 stories

---

## Phase 5: User Story 3 — Visitor explores and filters projects (Priority: P2)

**Goal**: 35 projects with search, filters and a details pop-up, all texts bilingual (FR-004, FR-016–FR-018)

**Independent Test**: Quickstart scenario 6 — search "Playwright", combine with domain filter, empty state, clear filters → 35, open/close pop-up three ways, focus returns, URL unchanged

### Tests for User Story 3

- [X] T047 [P] [US3] Write tests/e2e/projects.spec.ts: initial visible card count is 35 and order is `id` descending; search "playwright" shows only cards whose title/description/technologies contain it (case-insensitive); search + domain filter combined; query "zzzz" shows `projects_empty_result`; "Clear filters" restores 35; technology chips are multi-select with ANY semantics; opening a card shows a `dialog[open]` with title, description, technologies, achievements; Escape, close button and backdrop click each close it; focus returns to the card; `page.url()` never changes; no `img` with `naturalWidth === 0`; no code/demo button when the link is null
- [X] T048 [P] [US3] Add to tests/e2e/projects.spec.ts: after switching to Polish, the open dialog and the card descriptions are Polish and searching a Polish-only word from a description matches

### Implementation for User Story 3

- [X] T049 [US3] Write scripts/migrate/export_projects.py: read `PROJECTS_DATA`, `TECH_CATEGORIES`, `PLATFORMS`, `DOMAINS` from portfolio/projects.py and `proj_desc_<id>` from portfolio/translations.py; emit src/data/projects.json matching contracts/project.schema.json — `id`, `slug` (kebab-case of title, unique), `title`, `description: { en: proj_desc_<id> en or legacy description, pl: proj_desc_<id> pl or "" }`, `technologies`, `domain`, `platform`, `type` (`"Client Projects"` → `"client"`, `"Personal Projects"` → `"personal"`), `status` (`"Completed"` → `"completed"`, other → `"in-progress"`), `achievements: { en: legacy list, pl: [] }`, `image` (new path from scripts/migrate/image_map.json, e.g. `./projects/mining-app.png`, or null), `imageAlt: { en: "<title> screenshot", pl: "" }`, `github`/`demo` (`""` → null); and emit src/data/tech-categories.json (`id` ∈ `languages|testing|databases|frameworks|devops|other`, `label {en,pl}`, `colorToken`, `techs`)
- [X] T050 [US3] Run scripts/migrate/export_projects.py and list every empty `pl` value it produced (expected: 9 descriptions, all achievements, all alt texts) in specs/001-astro-github-pages/checklists/polish-copy.md
- [X] T051 [US3] Draft the missing Polish texts directly in src/data/projects.json (translate the English source faithfully; do not invent facts), keeping `achievements.pl.length === achievements.en.length`; mark each drafted entry in specs/001-astro-github-pages/checklists/polish-copy.md as "draft — owner review"
- [X] T052 [US3] Create src/content.config.ts defining collection `projects` with the `file('src/data/projects.json')` loader and a Zod schema equivalent to contracts/project.schema.json: `description`/`imageAlt` = `{ en: string().min(1), pl: string().min(1) }`; `achievements` refine "en and pl arrays MUST have equal length"; `platform` enum `Web|Mobile|Desktop|AI/Automation`; `type` enum `personal|client`; `status` enum `completed|in-progress`; `image` via `image().nullable()`; `imageAlt` required when `image` is set; `github`/`demo` `url().nullable()`; plus a build-time check that every technology appears in exactly one category of src/data/tech-categories.json
- [X] T053 [P] [US3] Create src/components/ProjectCard.astro: `<article>` with a `<button>` covering the card that opens details, `data-project-id`, `data-techs` (pipe-joined), `data-domain`, `data-platform`, `data-type`, `data-search-en`/`data-search-pl` (lowercased, NFD-normalised title + description + technologies); image via astro:assets `<Image>` (width/height set, WebP, `loading="lazy"`) or a styled placeholder when `image` is null; title, short description (`<T>`-style spans from Localized fields), technology chips colored by category token, platform/domain/type badges
- [X] T054 [P] [US3] Create src/components/ProjectFilters.astro porting the filter UI from `ProjectsState` in portfolio/projects.py: search input (`proj_search` placeholder with bilingual `data-i18n-placeholder-*`), technology chip groups per category with the legacy "show more" collapse (native `<details>`), single-select radio groups for domain (distinct values sorted), platform and type, each with "All" (`proj_all`), and a "Clear filters" button (`proj_clear_filters`); a live region announcing the visible count
- [X] T055 [P] [US3] Create src/components/ProjectDialog.astro: one native `<dialog>` with title, Localized description and achievements (both language spans), technologies, badges, image, "View code"/"Live demo" links rendered only when non-null, close button with bilingual aria-label; plus `<script type="application/json" id="projects-data">` embedding the project data the dialog needs
- [X] T056 [US3] Create src/scripts/projects.ts: maintain FilterState `{ query, techs: Set, domain, platform, type }` (not persisted, not in the URL); visible = `matches(query in data-search-<activeLang>) AND (techs empty OR any tech in card) AND domain AND platform AND type`; toggle `hidden` on cards, show `projects_empty_result` when none, update live-region count; open dialog with `showModal()` filled from `#projects-data`, close on close button, Escape (native) and backdrop click (`event.target === dialog`), restore focus to the opening card button; listen to `langchange` to re-run filtering and refresh an open dialog
- [X] T057 [US3] Complete src/pages/projects.astro: load `getCollection('projects')`, sort by `id` desc, render ProjectFilters, the ProjectCard list and ProjectDialog, include src/scripts/projects.ts
- [X] T058 [US3] Run tests/e2e/projects.spec.ts until green and confirm the project count and each project's fields against portfolio/projects.py (35/35, SC-001)

**Checkpoint**: Projects page fully interactive in both languages

---

## Phase 6: User Story 4 — Owner publishes updates by pushing to the main branch (Priority: P2)

**Goal**: Automatic, gated deploy to `https://morgacki.github.io/portfolio-remix/` (FR-023, SC-006)

**Independent Test**: Quickstart scenario 13 — a content push goes live within 10 minutes; a push with a missing Polish key fails `check` and does not deploy

### Implementation for User Story 4

- [X] T059 [P] [US4] Write scripts/check-dist.mjs: walk dist/ and exit 1 if it contains any `.pdf`, `.py`, `.pyc`, or any path starting with `portfolio/` or `assets/` (legacy), or any HTML missing `<html` with `data-lang` (FR-024)
- [X] T060 [US4] Create .github/workflows/deploy.yml: triggers `push` to `main` and `workflow_dispatch`; `permissions: { contents: read, pages: write, id-token: write }`; `concurrency: { group: pages, cancel-in-progress: false }`; job `build` on ubuntu-latest: `actions/checkout`, `actions/setup-node` with `node-version-file: .nvmrc` and npm cache, `npm ci`, `npm run check`, `npm run build`, `npm run check:dist`, `npx playwright install --with-deps chromium`, `npm run test:e2e`, upload `playwright-report/` as an artifact on failure, `actions/upload-pages-artifact` with `path: dist`; job `deploy` with `needs: build`, `environment: { name: github-pages, url: ${{ steps.deployment.outputs.page_url }} }`, step `actions/deploy-pages` (id `deployment`)
- [ ] T061 [US4] Before the first push of .github/workflows/deploy.yml, have the owner set repository Settings → Pages → Source = "GitHub Actions" (prerequisite in specs/001-astro-github-pages/quickstart.md) and confirm it with `gh api repos/MOrgacki/portfolio-remix/pages --jq .build_type` returning `workflow`
- [ ] T062 [US4] After the first green run, verify on production: every route loads under `/portfolio-remix/`, then perform the negative check from quickstart scenario 13 on a throwaway branch with `workflow_dispatch` (remove one key from src/i18n/pl.json) and confirm `deploy` is skipped; revert

**Checkpoint**: Site is live and updates itself on push

---

## Phase 7: User Story 5 — Visitor contacts the owner (Priority: P3)

**Goal**: One-click email/LinkedIn/GitHub and the "Let's talk" CTA replacing the chat (FR-005)

**Independent Test**: Quickstart scenario 7 — CTA opens /contact/, mailto link correct, profiles open in a new tab, no chat UI anywhere

### Tests for User Story 5

- [X] T063 [P] [US5] Write tests/e2e/contact.spec.ts: on `/` the "Let's talk" link (`about_cta_lets_talk`) navigates to `contact/` and keeps the active language; on `/contact/` the email link `href` is `mailto:marcinorgacki@gmail.com`; LinkedIn and GitHub links have `target="_blank"` and `rel` containing `noopener`; no element on any page contains the legacy chat texts ("Chat interface coming soon", "AI assistant")

### Implementation for User Story 5

- [X] T064 [US5] Add the "Let's talk" CTA to src/components/sections/About.astro in place of the legacy chat button (`about_chat_button`), as an `<a href={url('contact/')}>` styled as the legacy button, label `<T k="about_cta_lets_talk"/>`
- [X] T065 [US5] Verify the home contact section (`contact_section()` port) and src/pages/contact.astro use SocialLinks consistently and that `_contact_button` from portfolio/main.py is ported as a mailto button; run tests/e2e/contact.spec.ts until green

**Checkpoint**: All user stories complete

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Accessibility, privacy, performance, parity sign-off, legacy removal

- [X] T066 [P] Write tests/e2e/a11y.spec.ts: run `@axe-core/playwright` on every route in English and in Polish and fail on `serious`/`critical` violations; with `reducedMotion: 'reduce'` assert the background animation's computed `animation-name` is `none`; tab through `/` and assert each focused element has a visible outline
- [X] T067 [P] Write tests/e2e/privacy.spec.ts: on every route record requests and assert all are same-origin; assert `context.cookies()` is empty after visiting all pages and toggling the language (FR-026)
- [X] T068 Fix every failure from T066/T067 in the affected components (contrast, labels, focus styles)
- [X] T069 [P] Optimise images: confirm astro:assets outputs WebP with explicit widths for each display size (card, dialog, hero) and that no emitted image in dist/ exceeds 300 KB; adjust `widths`/`quality` in ProjectCard.astro, ProjectDialog.astro and Hero.astro accordingly
- [X] T070 [P] Check JS budget: list dist/_astro/*.js sizes gzipped and confirm each page ships < 150 KB gz (expected < 15 KB); record numbers in specs/001-astro-github-pages/checklists/performance.md
- [X] T071 Run Lighthouse (mobile) on every route of `npm run preview` and record scores in specs/001-astro-github-pages/checklists/performance.md; fix anything below 90 in Performance, Accessibility, Best Practices or SEO (SC-005); confirm LCP ≤ 2 s on simulated 4G (SC-004)
- [X] T072 Prove custom-domain readiness: `npm run build -- --base /` then preview at `/` and run tests/e2e/links.spec.ts with `BASE_URL=http://localhost:4321/` (make playwright.config.ts read `process.env.BASE_URL`) (FR-014)
- [X] T073 Run `npm run format` and `npm run check`; resolve all warnings
- [ ] T074 Owner review: hand specs/001-astro-github-pages/checklists/polish-copy.md to the owner; apply corrections to src/data/projects.json and src/i18n/pl.json
- [ ] T075 Complete specs/001-astro-github-pages/checklists/parity.md for both languages against the legacy app (SC-001, SC-002) and get owner sign-off
- [ ] T076 Run every scenario in specs/001-astro-github-pages/quickstart.md on the preview and on production; record results at the bottom of quickstart.md
- [ ] T077 Commit with message `(feat): migrate portfolio to static Astro site on GitHub Pages` (or split per story) and push to `main`; confirm the deploy is green
- [ ] T078 Remove legacy files in a dedicated commit `(chore): remove legacy Reflex app`: portfolio/, state.py, rxconfig.py, requirements.txt, Dockerfile, assets/, scripts/migrate/, portfolio/experience.py.backup, any `.web/` or `__pycache__/` directories (FR-025, Constitution "Migration")
- [ ] T079 Rewrite CLAUDE.md for the new stack: Astro 7 + Node 24, commands (`npm run dev|check|build|preview|test:e2e`), structure from plan.md, i18n contract summary (shared addresses, `<T>`, `portfolio.lang`), base path note, deploy workflow; commit as `(docs): update CLAUDE.md for Astro site`
- [ ] T080 Final production check after legacy removal: deploy is green and quickstart scenarios 1, 3, 6, 10 still pass on `https://morgacki.github.io/portfolio-remix/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: no dependencies
- **Foundational (Phase 2)**: depends on Setup — blocks all stories
- **US1 (Phase 3)**: after Foundational
- **US2 (Phase 4)**: after Foundational; its tests and T045/T046 touch pages from US1, so run after US1 for full value
- **US3 (Phase 5)**: after Foundational; needs the projects page shell T037 from US1
- **US4 (Phase 6)**: after Foundational; meaningful once US1 exists (deploys whatever is built); its CI runs all e2e tests present at that time
- **US5 (Phase 7)**: after US1 (About section, contact page)
- **Polish (Phase 8)**: after all desired stories; T078–T080 strictly last

### User Story Dependencies

```text
Setup → Foundational → US1 ─┬─> US2
                            ├─> US3
                            ├─> US4  (can go live right after US1)
                            └─> US5
                       all ─> Polish → legacy removal (T078) → CLAUDE.md (T079) → T080
```

### Within Each User Story

- Tests first (they must fail), then data, then components, then pages/scripts, then the
  story's verification task
- Migration scripts run before the files they generate are used

### Parallel Opportunities

- Setup: T004–T010 in parallel after T002/T003
- Foundational: T013, T014, T016, T017, T019, T020 in parallel after T011–T012
- US1: tests T023–T025 together; components T026–T031 together; pages T033–T036, T038 together
- US2: T040, T041, T044 in parallel
- US3: T047, T048 in parallel; T053–T055 in parallel after T052
- US4 and US5 can run in parallel with US3 once US1 is done
- Polish: T066, T067, T069, T070 in parallel

---

## Parallel Example: User Story 1

```bash
# Tests
Task: "Write tests/e2e/pages.spec.ts (routes, 404, aria-current, no-JS)"
Task: "Write tests/e2e/links.spec.ts (internal link + image crawl)"

# Components
Task: "Create src/components/Header.astro"
Task: "Create src/components/Footer.astro"
Task: "Create src/components/SocialLinks.astro"
Task: "Create section components in src/components/sections/"

# Pages
Task: "Build src/pages/experience.astro"
Task: "Build src/pages/case-studies.astro"
Task: "Build src/pages/contact.astro"
Task: "Build src/pages/blog.astro"
```

## Parallel Example: User Story 3

```bash
Task: "Create src/components/ProjectCard.astro"
Task: "Create src/components/ProjectFilters.astro"
Task: "Create src/components/ProjectDialog.astro"
```

---

## Implementation Strategy

### MVP First

1. Phase 1 Setup → Phase 2 Foundational
2. Phase 3 US1 → validate with its independent test
3. Phase 6 US4 → site goes live in English (Polish text already in HTML, toggle comes next)
4. **STOP and VALIDATE** on production

### Incremental Delivery

1. MVP (US1 + US4) live
2. US2 → language switching live
3. US3 → interactive projects live
4. US5 → "Let's talk" CTA live
5. Polish phase → owner sign-off → legacy removal

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- Legacy files are read-only until T078; migration scripts never write into them
- Commit after each task or logical group using `(type): summary`
- Do not invent Polish content; drafts are flagged for owner review (T051, T074)
