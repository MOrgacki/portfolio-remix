# Marcin Orgacki Portfolio Constitution

## Core Principles

### I. Bilingual Content Parity

- All user-visible text MUST come from a single translation source per language (e.g.
  `src/i18n/en.json` and `src/i18n/pl.json`); hard-coded UI strings in components are prohibited,
  except proper nouns (names, brands, technology names) and asset paths.
- Every translation key MUST exist in both `en` and `pl`. A change that adds, renames, or removes
  a key in one language MUST do the same in the other in the same commit. The build SHOULD fail
  on missing keys.
- English is the default language; Polish is selected from browser locale or the language toggle,
  entirely client-side or via pre-rendered per-language routes (e.g. `/pl/`). Both MUST render
  without missing-key fallbacks on every page.

Rationale: the site targets both international and Polish clients; a half-translated page reads
as careless, which directly undermines a quality-focused professional brand.

### II. Static-First Architecture

- The production site MUST be plain static files (HTML, CSS, JS, assets) produced by a build step.
  No server-side runtime, API server, or database is allowed in production.
- Any interactivity (language switch, theme toggle, animations, navigation) MUST run in the
  browser.
- Each page MUST be its own page/component module; shared layout (header, footer, navigation,
  background) MUST be defined once and reused, not copied per page.
- All internal links and asset URLs MUST respect the configured base path, so the site works both
  under `https://<user>.github.io/<repo>/` and on a custom domain without code changes.
- Every route MUST exist as a real built file (or a GitHub Pages–compatible `404.html` fallback
  for client-side routing); deep links and page refreshes MUST NOT return 404.
- Dead code, commented-out pages, and backup files (e.g. `*.backup`) MUST NOT be committed.

Rationale: GitHub Pages serves only static files; designing for that constraint from the start
avoids features that cannot be deployed.

### III. Responsive & Accessible by Default

- Every page MUST be usable at mobile (≤480px), tablet, and desktop widths with no horizontal
  page scroll; layouts MUST use responsive CSS (media/container queries, flex/grid).
- Pages MUST use semantic HTML (landmarks, heading order, `lang` attribute matching the active
  language).
- Images MUST have meaningful `alt` text; interactive elements MUST be keyboard reachable and
  have visible focus states.
- Text MUST keep sufficient contrast against the dark theme (WCAG 2.1 AA target).
- Animations MUST NOT block reading or navigation and MUST respect `prefers-reduced-motion`.

Rationale: recruiters and clients open portfolios mostly on phones; a QA professional's site is
itself judged as a test artifact.

### IV. Performance & Asset Discipline

- Static assets MUST live in the framework's public/static directory (e.g. `public/`) and be
  referenced through base-path-aware URLs.
- Images MUST be compressed and sized for their display use (WebP/AVIF preferred); a single image
  SHOULD NOT exceed 300 KB without a stated reason in the commit message.
- Asset file names MUST be lowercase, descriptive, and free of typos or spaces
  (e.g. `mining-app.webp`, not `project22.png`); unreferenced assets MUST be removed.
- Shipped JavaScript SHOULD stay under 150 KB gzipped per page; pages with no interactivity
  SHOULD ship no framework runtime.
- Artificial loading delays MUST NOT be used; loaders may only cover real loading work.
- Production builds SHOULD score ≥90 in Lighthouse Performance, Accessibility, Best Practices,
  and SEO on mobile.

Rationale: perceived speed is the first impression, and a static site has no excuse to be slow.

### V. Simplicity & Content-First Scope

- The site is a content showcase: new features MUST serve presenting experience, projects, case
  studies, blog content, or contact. Features outside that scope require a constitution amendment.
- Everything in the repository and the built bundle is public. Secrets, API keys, and private
  data MUST NOT be committed or embedded in client code. Private source documents (e.g. CV PDFs)
  MUST NOT be published unless explicitly intended for download.
- Contact MUST work without an own backend (`mailto:`, links to profiles, or a third-party static
  form service whose use is justified in the plan).
- New npm dependencies MUST be justified in the spec/plan; prefer platform features and the
  chosen framework's built-ins.
- YAGNI applies: no speculative abstractions, configuration layers, or CMS until a spec
  requires them.

Rationale: a small, focused codebase is cheaper to maintain and less likely to break in
production.

## Technology & Deployment Constraints

- Runtime for tooling: Node.js active LTS (version pinned in `.nvmrc` and the deploy workflow).
- Package manager: npm, with `package-lock.json` committed; CI MUST install with `npm ci`.
- Framework: a Node.js static site generator or bundler producing static output (Astro or Vite
  recommended); the choice is fixed in the first implementation plan and changing it later is a
  MINOR amendment of this constitution.
- Language: JavaScript or TypeScript; TypeScript is preferred for shared data (projects, case
  studies, translations).
- Build: `npm run build` MUST produce the deployable site in a single output directory
  (e.g. `dist/`); `npm run preview` MUST serve that output locally.
- Hosting: GitHub Pages, deployed by a GitHub Actions workflow on push to `main`. Build output
  MUST NOT be committed to `main`.
- Theme: dark appearance with the existing cyan accent and slate grays, defined once as CSS custom
  properties; new components MUST use these tokens rather than ad-hoc colors.

### Migration from the Legacy Reflex App

- The Python/Reflex app (`portfolio/`, `state.py`, `rxconfig.py`, `requirements.txt`,
  `Dockerfile`) is legacy. It is a content reference only and MUST NOT receive new features.
- Content (texts from `portfolio/translations.py`, project data, images in `assets/`) MUST be
  ported, not rewritten from memory, so no information is lost.
- Legacy files MUST be removed in a dedicated commit once the static site reaches content parity
  and is live on GitHub Pages.

## Development Workflow & Quality Gates

- Non-trivial features SHOULD follow the Spec Kit flow: `/speckit-specify` → `/speckit-plan` →
  `/speckit-tasks` → `/speckit-implement`; each plan MUST include a Constitution Check against
  Principles I–V.
- Before any commit to `main`, the author MUST:
  1. Run `npm run build` with no errors and no new warnings.
  2. Run `npm run preview` and visit every changed page in both EN and PL.
  3. Check changed pages at mobile and desktop widths.
- Linting/formatting configured in the project MUST pass before commit.
- The GitHub Pages deploy workflow MUST be green after merge; a failed deploy is fixed before any
  other work.
- Commit messages MUST use the existing convention: `(type): summary`, where type is one of
  `feat`, `fix`, `hotfix`, `chore`, `docs`, `refactor`, `style`.
- `CLAUDE.md` is the runtime development guidance file and MUST be updated to the new stack as
  part of the migration.

## Governance

- This constitution supersedes other project practices and guidance. Where `CLAUDE.md` or any
  spec/plan conflicts with it, the constitution wins until amended.
- Amendments are made via `/speckit-constitution`, MUST include a Sync Impact Report, and MUST be
  committed separately with a `docs:` message stating the new version.
- Versioning follows semantic versioning:
  - MAJOR: removal or backward-incompatible redefinition of a principle, governance rule, or the
    hosting platform.
  - MINOR: new principle or section, materially expanded guidance, or a change of build framework.
  - PATCH: clarifications, wording, and typo fixes.
- Compliance review: every Spec Kit plan MUST pass the Constitution Check gate; deviations MUST be
  recorded in the plan's Complexity Tracking with justification. The owner reviews the
  constitution at least once per year or on any framework major upgrade.

**Version**: 2.0.0 | **Ratified**: 2026-10-22 | **Last Amended**: 2026-10-23
