"""One-off: export legacy Reflex translations to src/i18n/{en,pl}.json.

Run from the repository root:  python -I scripts/migrate/export_translations.py
Reads portfolio/translations.py only; never writes into legacy files.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from portfolio.translations import TRANSLATIONS  # noqa: E402

DROPPED = {
    "chat_greeting",
    "chat_placeholder",
    "chat_close",
    "about_chat_button",
    "about_chat_title",
}

ADDED = {
    "about_cta_lets_talk": ("Let's talk", "Porozmawiajmy"),
    "not_found_title": ("Page not found", "Nie znaleziono strony"),
    "not_found_text": (
        "The page you are looking for doesn't exist or has been moved.",
        "Strona, której szukasz, nie istnieje lub została przeniesiona.",
    ),
    "not_found_home": ("Back to home", "Wróć na stronę główną"),
    "projects_empty_result": (
        "No projects match your search and filters.",
        "Żaden projekt nie pasuje do wyszukiwania i filtrów.",
    ),
    "projects_count": ("Projects shown:", "Wyświetlone projekty:"),
    "proj_close": ("Close", "Zamknij"),
    "skip_to_content": ("Skip to content", "Przejdź do treści"),
    "lang_switch_label": ("Przełącz na polski", "Switch to English"),
    "menu_open": ("Open menu", "Otwórz menu"),
    "menu_close": ("Close menu", "Zamknij menu"),
    # Labels hard-coded in English in the legacy pages (experience.py, case_studies.py)
    "tech_group_languages": ("Programming Languages", "Języki programowania"),
    "tech_group_testing": ("Testing Tools", "Narzędzia testowe"),
    "tech_group_databases": ("Databases", "Bazy danych"),
    "tech_group_technologies": ("Technologies", "Technologie"),
    "tech_group_others": ("Others", "Inne"),
    "about_tag_1": ("AI Orchestration", "Orkiestracja AI"),
    "about_tag_2": ("Business Automation", "Automatyzacja biznesu"),
    "about_tag_3": ("Quality Strategy", "Strategia jakości"),
    "about_tag_4": ("AI Agents", "Agenci AI"),
    "about_tag_5": ("Process Design", "Projektowanie procesów"),
    "case_project_label": ("Project", "Projekt"),
    "case_view_project": ("View Project", "Zobacz projekt"),
    "case_get_in_touch": ("Get in Touch", "Skontaktuj się"),
    "page_title_home": ("Marcin Orgacki", "Marcin Orgacki"),
    "page_title_experience": ("Marcin Orgacki | Experience", "Marcin Orgacki | Doświadczenie"),
    "page_title_case_studies": ("Marcin Orgacki | Case Studies", "Marcin Orgacki | Studia przypadków"),
    "page_title_projects": ("Marcin Orgacki | Projects", "Marcin Orgacki | Projekty"),
    "page_title_contact": ("Marcin Orgacki | Contact", "Marcin Orgacki | Kontakt"),
    "page_title_blog": ("Marcin Orgacki | Blog", "Marcin Orgacki | Blog"),
    "page_title_not_found": ("Marcin Orgacki | Page not found", "Marcin Orgacki | Nie znaleziono strony"),
    "page_description_home": (
        "Marcin Orgacki — Quality Automation Architect, AI Solutions Advisor and Business Process Expert.",
        "Marcin Orgacki — architekt automatyzacji jakości, doradca ds. rozwiązań AI i ekspert procesów biznesowych.",
    ),
    "page_description_experience": (
        "7+ years of QA, test automation, AI and business process optimisation experience.",
        "Ponad 7 lat doświadczenia w QA, automatyzacji testów, AI i optymalizacji procesów biznesowych.",
    ),
    "page_description_case_studies": (
        "Real problems, real solutions, measurable results — selected QA and automation case studies.",
        "Prawdziwe problemy, prawdziwe rozwiązania, mierzalne wyniki — wybrane studia przypadków QA i automatyzacji.",
    ),
    "page_description_projects": (
        "Client and personal projects in fintech, AI, Web3, e-learning and more.",
        "Projekty komercyjne i własne z obszarów fintech, AI, Web3, e-learningu i innych.",
    ),
    "page_description_contact": (
        "Get in touch with Marcin Orgacki by email, LinkedIn or GitHub.",
        "Skontaktuj się z Marcinem Orgackim przez e-mail, LinkedIn lub GitHub.",
    ),
    "page_description_blog": (
        "Upcoming articles about QA strategy, test automation and software development.",
        "Nadchodzące artykuły o strategii QA, automatyzacji testów i wytwarzaniu oprogramowania.",
    ),
}


def keep(key: str) -> bool:
    return key not in DROPPED and not key.startswith("proj_desc_")


def main() -> None:
    out_dir = ROOT / "src" / "i18n"
    out_dir.mkdir(parents=True, exist_ok=True)
    for idx, lang in enumerate(("en", "pl")):
        data = {k: v for k, v in TRANSLATIONS[lang].items() if keep(k)}
        for key, values in ADDED.items():
            data[key] = values[idx]
        data = dict(sorted(data.items()))
        (out_dir / f"{lang}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"{lang}: {len(data)} keys")


if __name__ == "__main__":
    main()
