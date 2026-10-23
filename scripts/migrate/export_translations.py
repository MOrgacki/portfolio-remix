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
    "home_title_1",
    "home_title_2",
    "home_title_3",
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
    # Services added after the migration (Experience page)
    "service_testing_desc": (
        "A holistic approach to product quality: combining manual and automated testing, verifying that business requirements are correctly understood and delivered, and catching gaps before they reach users.",
        "Holistyczne podejście do jakości produktu: łączę testy manualne i automatyczne, weryfikuję, czy wymagania biznesowe zostały poprawnie zrozumiane i zrealizowane, oraz wychwytuję luki, zanim trafią do użytkowników.",
    ),
    "service_ai_quality_title": ("AI Quality & LLM Evaluation", "Jakość AI i ewaluacja LLM"),
    "service_ai_quality_desc": (
        "Testing AI-powered products (RAG, chatbots and agents): evaluation datasets, hallucination and "
        "accuracy checks, prompt-injection and guardrail testing, and regression testing after model or "
        "prompt changes.",
        "Testowanie produktów opartych na AI (RAG, chatbotów i agentów): zestawy ewaluacyjne, wykrywanie "
        "halucynacji i sprawdzanie trafności, testy prompt injection i guardrails oraz testy regresji po "
        "zmianie modelu lub promptu.",
    ),
    "service_data_title": ("Data Warehouse & ETL Testing", "Testowanie hurtowni danych i ETL"),
    "service_data_desc": (
        "Validating data pipelines end to end: source-to-target reconciliation, transformation and "
        "business-rule checks, data quality (completeness, duplicates, schema drift) and automated "
        "regression of ETL jobs and reports.",
        "Walidacja potoków danych od źródła do raportu: uzgadnianie danych źródło–cel, weryfikacja "
        "transformacji i reguł biznesowych, jakość danych (kompletność, duplikaty, zmiany schematu) oraz "
        "automatyczne testy regresji zadań ETL i raportów.",
    ),
    # Contact page sections added after the migration
    "contact_topics_title": (
        "What we can talk about",
        "O czym możemy porozmawiać",
    ),
    "contact_topic_qa_title": (
        "QA strategy and audits",
        "Strategia QA i audyty jakości",
    ),
    "contact_topic_qa_desc": (
        "Reviewing your current testing process, finding the gaps and building a quality plan that fits your team and budget.",
        "Przegląd obecnego procesu testowania, wskazanie luk i plan jakości dopasowany do zespołu i budżetu.",
    ),
    "contact_topic_automation_title": (
        "Test automation",
        "Automatyzacja testów",
    ),
    "contact_topic_automation_desc": (
        "Building or fixing E2E, API and regression suites and plugging them into CI/CD, so every release is checked automatically.",
        "Budowa lub naprawa testów E2E, API i regresji oraz podpięcie ich do CI/CD, aby każde wydanie było sprawdzane automatycznie.",
    ),
    "contact_topic_ai_title": (
        "AI product quality",
        "Jakość produktów AI",
    ),
    "contact_topic_ai_desc": (
        "Evaluating chatbots, RAG systems and AI agents: accuracy, hallucinations, guardrails and regression after model changes.",
        "Ewaluacja chatbotów, systemów RAG i agentów AI: trafność, halucynacje, guardrails i regresja po zmianie modelu.",
    ),
    "contact_topic_process_title": (
        "Process automation",
        "Automatyzacja procesów",
    ),
    "contact_topic_process_desc": (
        "Automating repetitive business work with scripts, integrations and AI agents, so your team can focus on what matters.",
        "Automatyzacja powtarzalnej pracy w firmie za pomocą skryptów, integracji i agentów AI, aby zespół mógł skupić się na tym, co ważne.",
    ),
    "contact_topic_data_title": (
        "Data and ETL testing",
        "Testowanie danych i ETL",
    ),
    "contact_topic_data_desc": (
        "Checking data pipelines, reports and integrations, so the numbers your business relies on are correct.",
        "Sprawdzanie potoków danych, raportów i integracji, aby liczby, na których opiera się firma, były poprawne.",
    ),
    "contact_topic_other_title": (
        "Something else?",
        "Coś innego?",
    ),
    "contact_topic_other_desc": (
        "Have a different challenge? Write to me anyway and I will tell you honestly whether I can help.",
        "Masz inne wyzwanie? Napisz mimo to, a szczerze powiem, czy mogę pomóc.",
    ),
    "contact_steps_title": (
        "How we start",
        "Jak zaczynamy",
    ),
    "contact_step_1_title": (
        "Send a message",
        "Napisz wiadomość",
    ),
    "contact_step_1_desc": (
        "Briefly describe your product, the problem you want to solve and your timeline.",
        "Krótko opisz produkt, problem do rozwiązania i oczekiwany termin.",
    ),
    "contact_step_2_title": (
        "Short call",
        "Krótka rozmowa",
    ),
    "contact_step_2_desc": (
        "A short online call to understand your goals, your team and the current state of the project.",
        "Krótka rozmowa online, żeby zrozumieć cele, zespół i obecny stan projektu.",
    ),
    "contact_step_3_title": (
        "Concrete proposal",
        "Konkretna propozycja",
    ),
    "contact_step_3_desc": (
        "You get a clear plan: scope, approach and next steps.",
        "Otrzymujesz jasny plan: zakres, podejście i kolejne kroki.",
    ),
    "contact_brief_title": (
        "What to include in your message",
        "Co warto napisać w wiadomości",
    ),
    "contact_brief_1": (
        "What the product does and who uses it",
        "Czym jest produkt i kto z niego korzysta",
    ),
    "contact_brief_2": (
        "The current state of testing and the tools you use",
        "Obecny stan testów i używane narzędzia",
    ),
    "contact_brief_3": (
        "The main problem or goal",
        "Główny problem lub cel",
    ),
    "contact_brief_4": (
        "Expected timeline and form of collaboration",
        "Oczekiwany termin i forma współpracy",
    ),
    "contact_languages_note": (
        "I communicate in Polish and English.",
        "Rozmawiam po polsku i angielsku.",
    ),
    "contact_cta_title": (
        "Let's talk about your project",
        "Porozmawiajmy o Twoim projekcie",
    ),
    "contact_cta_text": (
        "The easiest way to reach me is by email. You can also message me on LinkedIn.",
        "Najprostszy sposób kontaktu to e-mail. Możesz też napisać do mnie na LinkedIn.",
    ),
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
    "page_title_not_found": ("Marcin Orgacki | Page not found", "Marcin Orgacki | Nie znaleziono strony"),
    "page_description_home": (
        "Marcin Orgacki: quality assurance, test automation and AI-driven process automation.",
        "Marcin Orgacki: zapewnianie jakości, automatyzacja testów i automatyzacja procesów z wykorzystaniem AI.",
    ),
    "page_description_experience": (
        "8+ years of QA, test automation, AI and business process optimisation experience.",
        "Ponad 8 lat doświadczenia w QA, automatyzacji testów, AI i optymalizacji procesów biznesowych.",
    ),
    "page_description_case_studies": (
        "Real problems, real solutions, measurable results. Selected QA and automation case studies.",
        "Prawdziwe problemy, prawdziwe rozwiązania, mierzalne wyniki. Wybrane studia przypadków QA i automatyzacji.",
    ),
    "page_description_projects": (
        "Client and personal projects in fintech, AI, Web3, e-learning and more.",
        "Projekty komercyjne i własne z obszarów fintech, AI, Web3, e-learningu i innych.",
    ),
    "page_description_contact": (
        "Get in touch with Marcin Orgacki by email, LinkedIn or GitHub.",
        "Skontaktuj się z Marcinem Orgackim przez e-mail, LinkedIn lub GitHub.",
    ),
}


# The blog page was removed after go-live.
DROPPED_PREFIXES = ("proj_desc_", "blog_")


def keep(key: str) -> bool:
    return key not in DROPPED and key != "nav_blog" and not key.startswith(DROPPED_PREFIXES)


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
