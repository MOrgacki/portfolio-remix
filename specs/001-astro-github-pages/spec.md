# Feature Specification: Migrate Portfolio to a Static Site on GitHub Pages

**Feature Branch**: `001-astro-github-pages`

**Created**: 2026-10-23

**Status**: Draft

**Input**: User description: "przenieś portfolio na Astro pod GitHub Pages"
(move the portfolio to Astro, hosted on GitHub Pages)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Visitor browses the portfolio on the new public address (Priority: P1)

A recruiter or potential client opens the portfolio link, lands on the home page, and navigates
to Experience, Case Studies, Projects, Contact, and Blog. Every page shows the same content as
the current site (texts, images, achievements, timeline, services, skills, social links), styled
in the existing dark theme with the cyan accent.

**Why this priority**: The whole point of the migration is that the portfolio is publicly
reachable on free static hosting with no content lost. Without this, nothing else matters.

**Independent Test**: Open the published address, visit all six pages via navigation and via
direct links, and compare each page section by section with the current site.

**Acceptance Scenarios**:

1. **Given** the site is published, **When** a visitor opens the root address, **Then** the home
   page loads with hero, about section, services, key achievements, timeline, skills, domains,
   and contact/social links.
2. **Given** a visitor is on any page, **When** they use the header or mobile navigation,
   **Then** they reach each of Home, Experience, Case Studies, Projects, Contact, and Blog.
3. **Given** a visitor has a direct link to a subpage (e.g. Projects), **When** they open it or
   refresh the page, **Then** that page loads (no "page not found").
4. **Given** a visitor opens an address that does not exist, **When** the page loads, **Then**
   they see a branded "page not found" page with a link back to Home.

---

### User Story 2 - Visitor reads the site in Polish or English (Priority: P1)

A visitor whose browser is set to Polish sees the site in Polish on first visit; any visitor can
switch between English and Polish with the language button, and the choice persists while they
browse other pages and on their next visit.

**Why this priority**: Bilingual content is a constitutional principle and the current site
already serves both audiences; losing it would be a regression.

**Independent Test**: Visit with a Polish browser locale, then with an English one; toggle the
language on each page and navigate between pages.

**Acceptance Scenarios**:

1. **Given** a first-time visitor with a Polish browser locale, **When** they open the site,
   **Then** content is shown in Polish.
2. **Given** a first-time visitor with any other locale, **When** they open the site, **Then**
   content is shown in English.
3. **Given** a visitor on any page, **When** they press the language button, **Then** all text on
   the page switches language without losing their place in the site.
4. **Given** a visitor chose a language, **When** they navigate to another page or return later,
   **Then** the chosen language is kept.
5. **Given** either language, **When** any page is viewed, **Then** no text appears untranslated,
   empty, or as a raw key.

---

### User Story 3 - Visitor explores and filters projects (Priority: P2)

A visitor on the Projects page searches by keyword, filters by technology, platform, domain, and
personal/client type, clears filters, and opens a project to see its full details (description,
technologies, achievements, image, and code/demo links where available).

**Why this priority**: Projects are the strongest proof of experience, and the current site
offers this interaction; it is valuable but the site is still useful without it.

**Independent Test**: On the Projects page, combine search and filters, verify the result list,
open and close a project's details, and clear filters.

**Acceptance Scenarios**:

1. **Given** the Projects page, **When** it loads, **Then** all 35 projects from the current site
   are listed with title, image, short description, and technologies.
2. **Given** a search term, **When** the visitor types it, **Then** only projects whose title,
   description, or technologies match are shown.
3. **Given** one or more filters selected, **When** applied together with search, **Then** only
   projects matching all criteria are shown, and an empty-result message appears if none match.
4. **Given** active filters, **When** the visitor clears them, **Then** the full list returns.
5. **Given** a project in the list, **When** the visitor opens its details, **Then** a details
   view shows full description, technologies, achievements, and code/demo links only when they
   exist; it can be closed with a button, the Escape key, or clicking outside.

---

### User Story 4 - Owner publishes updates by pushing to the main branch (Priority: P2)

The site owner edits content (e.g. adds a project or fixes a translation), pushes to the main
branch, and the updated site appears on the public address automatically, without manual
uploads or server maintenance.

**Why this priority**: Low-effort publishing is the main operational benefit of moving to static
hosting.

**Independent Test**: Change one visible text, push to main, and confirm the change is live on
the public address; introduce a broken build and confirm the live site is not replaced.

**Acceptance Scenarios**:

1. **Given** a successful change pushed to main, **When** the automated publish finishes,
   **Then** the public site shows the change.
2. **Given** a change that fails to build (e.g. a missing translation key), **When** it is pushed,
   **Then** publishing fails visibly and the previously published site stays online unchanged.

---

### User Story 5 - Visitor contacts the owner (Priority: P3)

A visitor on the Contact page or home contact section reaches the owner by email, LinkedIn, or
GitHub with one click.

**Why this priority**: Conversion point of the portfolio; simple links already cover it.

**Independent Test**: Click each contact option and confirm it opens the right destination.

**Acceptance Scenarios**:

1. **Given** the Contact page, **When** the visitor clicks Email, **Then** their mail client opens
   addressed to the owner's published email.
2. **Given** the Contact page, **When** the visitor clicks LinkedIn or GitHub, **Then** the
   matching profile opens in a new tab.
3. **Given** the "About me" section on Home, **When** the visitor clicks "Let's talk", **Then**
   the Contact page opens in the current language.

---

### Clarifications

#### Session 2026-10-23

- Q: What happens to the "About me" AI chat placeholder, given static hosting has no server? →
  A: Replace it with a "Let's talk" call-to-action leading to the Contact page (FR-005).
- Q: Should Polish have its own addresses (e.g. `/pl/projects/`) or share addresses with English
  and switch in the browser? → A: Shared addresses; language is switched in the browser and
  remembered on the device (FR-007a, FR-006).
- Q: Should project details open only in a pop-up on the Projects page, or should each project
  have its own shareable address? → A: Pop-up only, no per-project address, as on the current
  site (FR-018).
- Q: Under which public address should the portfolio run? → A:
  `https://morgacki.github.io/portfolio-remix/` (current repository); a custom domain may be
  added later without content changes (FR-014).
- Q: Do you want visitor statistics on the portfolio? → A: No statistics; no third-party
  tracking scripts or cookies (FR-026).

### Edge Cases

- JavaScript disabled or failed to load: all page content, navigation, and contact links remain
  readable in the default language; only search/filters, project details, and language
  switching may be unavailable.
- Site published under a sub-path (`/portfolio-remix/`) vs. a custom domain at the root: all
  links, images, and the favicon must work in both without content edits.
- Visitor prefers reduced motion: background and decorative animations are disabled or static.
- Project without image, code link, or demo link: card and details show no broken image and no
  dead buttons.
- Very narrow screens (320px) and very wide screens (≥1920px): no horizontal scrolling, readable
  layout.
- Visitor's stored language preference is invalid or storage is blocked: site falls back to
  browser-locale detection, then English.
- Visitor whose saved or detected language is Polish: the page MUST NOT visibly flash English
  text before switching to Polish.
- Shared link: because addresses carry no language, the recipient sees the page in their own
  saved or detected language, not the sender's.
- Search with no matches or with special characters: friendly empty state, no errors.

## Requirements *(mandatory)*

### Functional Requirements

**Content & pages**

- **FR-001**: The site MUST provide five pages — Home, Experience, Case Studies, Projects, Contact —
  plus a "page not found" page. (The Blog page was removed by the owner on 2026-10-23.)
- **FR-002**: Each page MUST contain all content currently shown on its counterpart in the
  existing site, in both languages, with no section dropped or rewritten from memory.
- **FR-003**: *(Removed 2026-10-23: the Blog page is out of scope.)*
- **FR-004**: All 35 existing projects MUST be carried over with their title, descriptions,
  technologies, domain, platform, type (personal/client), status, achievements, image, and links.
- **FR-005**: The "About me" AI chat placeholder MUST be removed and replaced by a "Let's talk"
  call-to-action button (in both languages) that takes the visitor to the Contact page. No
  chat-related texts (greeting, input placeholder, close button) remain on the site.
- **FR-006**: Each page MUST have a distinct title and description. Search engines and link
  previews use the English version; the browser tab title MUST follow the active language.

**Language**

- **FR-007**: The site MUST offer every page in English and Polish, with English as the default.
- **FR-007a**: Both languages MUST share the same page addresses; the language is not part of the
  address and is switched in the browser without reloading to a different address.
- **FR-008**: On first visit, the language MUST be chosen from the browser locale (Polish locale →
  Polish, otherwise English).
- **FR-009**: A language button MUST be available on every page and switch all page text.
- **FR-010**: The chosen language MUST persist across pages and later visits on the same device.
- **FR-011**: Publishing MUST be blocked if any text exists in one language but not the other.

**Navigation & layout**

- **FR-012**: Header navigation on desktop and a menu on mobile MUST link to all six pages and
  indicate the current page.
- **FR-013**: Every page MUST be reachable by direct link and survive a refresh.
- **FR-014**: The site MUST be published at `https://morgacki.github.io/portfolio-remix/` and MUST
  also work unchanged at a domain root, so a custom domain can be added later by configuration
  only.
- **FR-015**: Layouts MUST adapt to mobile, tablet, and desktop with no horizontal scrolling.

**Projects interaction**

- **FR-016**: Visitors MUST be able to search projects by keyword across title, description, and
  technologies.
- **FR-017**: Visitors MUST be able to filter projects by technology, platform, domain, and
  personal/client type, combine filters with search, and clear all filters in one action.
- **FR-018**: Visitors MUST be able to open a project's details in a pop-up on the Projects page
  and close it via button, Escape key, or clicking outside; focus MUST return to the triggering
  element. Projects have no individual addresses; opening or closing the pop-up does not change
  the page address.

**Visual & accessibility**

- **FR-019**: The site MUST keep the current visual identity: dark gradient background, cyan
  accent, slate grays, profile photo, and decorative animated background.
- **FR-020**: Decorative animations MUST be disabled when the visitor prefers reduced motion.
- **FR-021**: All images MUST have meaningful alternative text; all interactive elements MUST be
  keyboard operable with visible focus.
- **FR-022**: The site MUST NOT show an artificial loading screen or delay before content appears.

**Publishing & legacy**

- **FR-023**: Pushing to the main branch MUST automatically publish the site; a failed build MUST
  NOT replace the live site.
- **FR-024**: Private documents in the repository (CV/LinkedIn PDFs, project description PDF)
  MUST NOT be published on the site.
- **FR-025**: After the new site is live with full content parity, the legacy application files
  MUST be removed from the repository in a separate change, and project guidance (CLAUDE.md)
  MUST describe the new setup.

**Privacy**

- **FR-026**: The site MUST NOT include visitor statistics, third-party tracking scripts, or
  cookies; the only data stored on the visitor's device is the chosen language. No cookie consent
  banner is therefore shown.

### Key Entities

- **Page**: One of the six site sections; has a route, per-language title and description, and
  ordered content sections.
- **Translation entry**: A keyed piece of visible text with an English and a Polish value
  (~370 entries today).
- **Project**: A portfolio item with title, short and full description (both languages),
  technologies, domain, platform, type (personal/client), status, achievements, image, optional
  code and demo links.
- **Case study / Achievement**: A problem → solution → result story, optionally linked to a
  project.
- **Timeline step / Service / Skill / Domain**: Small content items shown on Home and Experience.
- **Contact channel**: Email, LinkedIn, GitHub, each with a label, icon, and destination.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of pages, sections, projects (35/35), and translation entries from the current
  site are present on the new site, verified by a section-by-section comparison checklist.
- **SC-002**: 0 missing or untranslated texts across all pages in both languages.
- **SC-003**: 0 broken internal links, images, or direct-link/refresh failures across all pages,
  under both the sub-path address and a root domain preview.
- **SC-004**: Main content of each page is visible within 2 seconds on a mid-range phone over a
  typical 4G connection.
- **SC-005**: Each page scores at least 90 in performance, accessibility, best-practices, and SEO
  audits on mobile.
- **SC-006**: A content change pushed to main is live on the public address within 10 minutes,
  with no manual steps.
- **SC-007**: Running cost of hosting is zero, and no server needs to be maintained.
- **SC-008**: A visitor can find a project by technology (e.g. "Playwright") in under 15 seconds
  from landing on the Projects page.

## Assumptions

- The framework (Astro) and host (GitHub Pages) are fixed by the user's request and the project
  constitution v2.0.0; this spec intentionally describes outcomes, and technical design belongs
  in the plan.
- The site is published from the existing repository `MOrgacki/portfolio-remix` (confirmed in
  Clarifications); no repository rename or domain purchase is part of this feature.
- Content is migrated as-is; copy-editing, new projects, or redesign are out of scope (fixing
  obvious typos and renaming image files to descriptive names is in scope).
- Language is persisted on the visitor's device only; there are no user accounts (statistics
  and tracking are excluded by FR-026).
- Images may be converted to lighter formats and resized as long as visual quality is preserved.
- The legacy Docker deployment is retired once the new site is live; no parallel hosting is kept.
- The legacy application files remain in the repository only until content parity is confirmed.
