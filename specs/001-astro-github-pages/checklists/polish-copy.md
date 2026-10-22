# Polish Copy Review: texts the legacy site only had in English

**Purpose**: Owner review of Polish texts drafted during migration (T050, T051, T074).
**Source of drafts**: `scripts/migrate/polish_drafts.json`, merged into `src/data/projects.json` by
`scripts/migrate/export_projects.py`. Edit the draft file and rerun the export, or edit
`src/data/projects.json` directly after the legacy app is removed.

`[x]` = owner approved the Polish text.

## Project descriptions (12 drafts)

The legacy app looked up Polish descriptions by a non-unique project id, so these projects either
had no Polish text or showed another project's description.

- [ ] AI Research Analysis Platform (RAG) (legacy Polish text described an older version)
- [ ] NFT Marketplace Platform
- [ ] Client App & Partner Zone Platform
- [ ] Job Listings Web Scraper with CSV Export
- [ ] Job Market Statistics Web Scraper
- [ ] Web3 Staking & Vesting Platform
- [ ] MMORPG Game Bot - Tibia Automation
- [ ] Oil & Gas Tubular Goods Management System
- [ ] Welding Industry Management Platform
- [ ] Banking Products Sales Platform
- [ ] Medical Supplements E-commerce Platform
- [ ] Web3 Gaming Mobile App - Rewards Marketplace

## Project achievements (119 lines, 35 projects)

- [ ] All achievement lines in `polish_drafts.json` → `achievements` reviewed

## Labels that were hard-coded in English in the legacy pages

- [ ] Tech stack group names (`tech_group_*`)
- [ ] About tags (`about_tag_1..5`)
- [ ] Case studies: "Project", "View Project", "Get in Touch" (`case_*`)
- [ ] Project filter domains and platforms (`src/data/facets.json`)
- [ ] Technology category labels (`src/data/tech-categories.json`)
- [ ] Image alt texts ("<title> — zrzut ekranu")
- [ ] New UI strings: 404 page, menu labels, language button, page titles/descriptions
