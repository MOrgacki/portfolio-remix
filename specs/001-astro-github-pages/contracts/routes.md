# Contract: Public Routes

Base URL (production): `https://morgacki.github.io/portfolio-remix/`. All paths below are
relative to the base and MUST work identically when the base is `/` (custom domain, FR-014).
Trailing slash is canonical; GitHub Pages redirects the slash-less form.

| Path | Source | Nav | Purpose |
|---|---|---|---|
| `/` | `src/pages/index.astro` | Home | Hero, about + "Let's talk" CTA, services, achievements, timeline, skills, domains, contact links |
| `/experience/` | `src/pages/experience.astro` | Experience | Tech stack, key achievements, languages, certificates |
| `/case-studies/` | `src/pages/case-studies.astro` | Case Studies | Problem → solution → result stories |
| `/projects/` | `src/pages/projects.astro` | Projects | 35 projects, search, filters, details pop-up |
| `/contact/` | `src/pages/contact.astro` | Contact | Email, LinkedIn, GitHub |
| any other path | `src/pages/404.astro` → `404.html` | — | Branded not-found page with link to Home |

## Guarantees

- Each route is a real file in `dist/` (`<route>/index.html`), so direct links and refresh never
  404 (FR-013).
- Every page responds with complete content in English without JavaScript (spec edge case).
- No route encodes language or project selection (Clarifications Q1, Q2); query strings and
  hashes are ignored.
- `<head>` of every page contains: `<title>` and `<meta name="description">` in English,
  canonical URL, Open Graph title/description/image, `<html lang>` updated to the active
  language at runtime.
- Navigation marks the current page with `aria-current="page"` (FR-012).
- The "Let's talk" CTA on `/` links to `/contact/` (FR-005).

## Not published

`dist/` MUST NOT contain any `.pdf` file, any file from `portfolio/`, or any legacy Python file
(FR-024). Verified by a CI check over the build output.
