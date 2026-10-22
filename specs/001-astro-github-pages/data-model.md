# Data Model: Migrate Portfolio to a Static Site on GitHub Pages

**Feature**: `001-astro-github-pages` | **Date**: 2026-10-23

All data is static, read at build time from files in the repository. There is no runtime storage
except the visitor's language preference (see [contracts/i18n.md](./contracts/i18n.md)).

## Shared types

- **Lang**: `"en" | "pl"`.
- **Localized&lt;T&gt;**: `{ en: T; pl: T }` — both members required and non-empty.

## TranslationDictionary

Source: `src/i18n/en.json`, `src/i18n/pl.json` (migrated from `portfolio/translations.py`).

| Field | Type | Rules |
|---|---|---|
| key | string, `snake_case` | Unique; identical key set in both files (FR-011) |
| value | string | Non-empty; may contain emoji; no HTML |

- Removed in migration: `chat_greeting`, `chat_placeholder`, `chat_close`, `about_chat_button`,
  `about_chat_title` (FR-005).
- Added: `about_cta_lets_talk`, `page_title_<route>`, `page_description_<route>`,
  `not_found_title`, `not_found_text`, `projects_empty_result`.
- Project-specific `proj_desc_<id>` keys move into the Project entity and are removed from the
  dictionary.

## Project

Source: `src/data/projects.json`, validated by an Astro content collection schema equivalent to
[contracts/project.schema.json](./contracts/project.schema.json).

| Field | Type | Rules |
|---|---|---|
| id | integer ≥ 1 | Unique; display order is `id` descending (newest first) |
| slug | string, kebab-case | Unique; used for the image file name and `data-project` attribute only (no URL, Clarification Q2) |
| title | string | Non-empty; proper name, not translated |
| description | Localized&lt;string&gt; | Full text shown in the pop-up and searched |
| technologies | string[] | ≥ 1; every value MUST appear in exactly one TechCategory |
| domain | Domain | One of the Domain values |
| platform | Platform | `Web` \| `Mobile` \| `Desktop` \| `AI/Automation` |
| type | ProjectType | `personal` \| `client` |
| status | ProjectStatus | `completed` \| `in-progress` (legacy `"Completed"` etc. normalised) |
| achievements | Localized&lt;string[]&gt; | 0..n; `en` and `pl` arrays have equal length |
| image | image reference \| null | Path under `src/assets/projects/`; null → placeholder |
| imageAlt | Localized&lt;string&gt; | Required when `image` is set (FR-021) |
| github | URL \| null | Shown as "View code" only when set |
| demo | URL \| null | Shown as "Live demo" only when set |

Volume: 35 projects. Polish text exists for 26 of 35 descriptions; the other 9 descriptions,
all achievements and all image alt texts need Polish copy (see research R6).

## TechCategory

Source: `src/data/tech-categories.json` (from legacy `TECH_CATEGORIES`).

| Field | Type | Rules |
|---|---|---|
| id | string | `languages`, `testing`, `databases`, `frameworks`, `devops`, `other` |
| label | Localized&lt;string&gt; | Filter group heading |
| colorToken | string | CSS custom property name, e.g. `--tech-cyan` |
| techs | string[] | Only technologies used by at least one project are shown |

## Filter facets (derived, not stored)

- **Domain**: distinct `project.domain` values, sorted; filter offers "All" + values.
- **Platform**, **ProjectType**: fixed enums above; filter offers "All" + values.
- **FilterState** (in-browser only, not persisted, not in URL):
  `{ query: string; techs: Set<string>; domain: Domain | "all"; platform: Platform | "all";
  type: ProjectType | "all" }`. A project is visible when
  `matches(query) AND (techs empty OR project.technologies ∩ techs ≠ ∅) AND domain AND platform
  AND type`.

## Page content entities

Static content kept as translation keys plus small ordered lists in `src/data/`:

| Entity | Source file | Fields |
|---|---|---|
| Service | `services.json` | `id`, `icon`, `titleKey`, `descKey` (6 items) |
| Achievement (case study) | `achievements.json` | `id`, `problemKey`, `solutionKey`, `resultKey`, `projectId?` (6 items) |
| TimelineStep | `timeline.json` | `id`, `titleKey`, `descKey` (6 items) |
| SkillGroup | `skills.json` | `id`, `labelKey`, `items: string[]` |
| SpokenLanguage | `languages.json` | `nameKey`, `levelKey` |
| ContactChannel | `contact.json` | `id` (`email` \| `linkedin` \| `github`), `labelKey`, `href`, `icon` |

Rules: every `*Key` MUST exist in the TranslationDictionary (checked by `astro check` typing);
`Achievement.projectId`, when set, MUST reference an existing Project.

## Page

Defined by files in `src/pages/` (see [contracts/routes.md](./contracts/routes.md)).

| Field | Rules |
|---|---|
| route | One of the seven routes in the routes contract |
| titleKey / descriptionKey | `page_title_<route>` / `page_description_<route>`; English used in meta tags, tab title follows active language (FR-006) |
| navKey | Present for the six navigable pages |

## State transitions

- **Language** (per visitor device): `unset → detected(en|pl)` on first visit;
  `en ⇄ pl` on toggle, persisted immediately. No other runtime state is persisted.
- **Project pop-up**: `closed → open(projectId)` on card activation;
  `open → closed` on close button, Escape, or backdrop click; focus returns to the card.
