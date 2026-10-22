# Content Parity Checklist: Legacy Reflex app → Astro site

**Purpose**: Section-by-section comparison with the legacy app (SC-001, SC-002). One line per legacy
section and language. `[x]` = present on the new site with the same content.
**Legacy source**: commit `cf13481` (legacy Reflex app final content).

## Home (`/`) — legacy `Main.build_view()` in portfolio/main.py

- [x] EN: "Hello, I'm Marcin Orgacki 👋" heading
- [x] PL: "Cześć, Jestem Marcin Orgacki 👋" heading
- [x] EN/PL: three title badges (were hard-coded English in legacy; now `home_title_1..3`)
- [x] EN/PL: GitHub / LinkedIn / Email links
- [x] EN/PL: about window (title bar file name, title, two intro paragraphs, five tags)
- [x] EN/PL: chat button replaced by "Let's talk" → /contact/ (FR-005)
- Note: legacy `_create_expertise_box()` (skills_*) was built but never rendered — not ported.

## Experience (`/experience/`) — legacy `experience_page()`

- [x] EN/PL: title, subtitle, description
- [x] EN/PL: Services & Expertise (6 cards)
- [x] EN/PL: Tech Stack (5 groups; group labels were hard-coded English, now translated)
- [x] EN/PL: Languages (en B2+, pl C2, de A1 with bars)
- [x] EN/PL: Certificates (4)
- [x] EN/PL: My Journey timeline (6 steps)
- [x] EN/PL: Get in Touch contact section

## Case Studies (`/case-studies/`) — legacy `case_studies_page()`

- [x] EN/PL: title, subtitle, intro
- [x] EN/PL: 6 problem → solution → result cards with project boxes
- [x] EN/PL: CTA text + "Get in Touch" button (legacy linked to `/#contact`, now `/contact/`)

## Projects (`/projects/`) — legacy `projects_page()`

- [ ] EN: title, description, filters, 35 project cards, details pop-up
- [ ] PL: same, with Polish descriptions/achievements (see polish-copy.md)

## Contact (`/contact/`)

- [x] EN/PL: Get in Touch title, description, social links, "Contact Me" mail button
- Note: legacy `/contact` repeated the home view; the new page focuses on contact channels.

## Blog (`/blog/`) — legacy `blog_page()`

- [x] EN/PL: title, description, "coming soon" box, 4 topics, suggestion text, Home button
  (legacy texts were hard-coded English; now translated keys)

## Sign-off

- [ ] Owner reviewed every page in both languages against the legacy app (T075)
