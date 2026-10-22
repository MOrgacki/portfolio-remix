import reflex as rx
from portfolio.translations import TRANSLATIONS


class State(rx.State):
    """The app state."""

    # Loading states
    is_loading: bool = True
    is_page_loading: bool = False

    # Language state
    language: str = "en"  # Default to English

    # Chat state
    chat_active: bool = False
    chat_messages: list[dict[str, str]] = []

    def on_load(self):
        """Called when page loads - detect browser language"""
        # This will be called on mount
        pass

    def detect_browser_language(self):
        """Detect and set language based on browser locale"""
        # Will be triggered by JavaScript
        return rx.call_script(
            """
            const browserLang = navigator.language || navigator.userLanguage;
            const lang = browserLang.toLowerCase().startsWith('pl') ? 'pl' : 'en';
            return lang;
            """,
            callback=State.set_language
        )

    async def finish_initial_load(self):
        """Called when initial app load is complete - minimum 2s display"""
        import asyncio
        await asyncio.sleep(2)
        self.is_loading = False

    def start_page_transition(self):
        """Called when navigating to a new page"""
        self.is_page_loading = True

    def finish_page_transition(self):
        """Called when new page is loaded"""
        self.is_page_loading = False

    def toggle_language(self):
        """Toggle between English and Polish"""
        self.language = "pl" if self.language == "en" else "en"

    def set_language(self, lang: str):
        """Set language explicitly"""
        if lang in ["en", "pl"]:
            self.language = lang

    # Computed vars for translations
    @rx.var
    def nav_home(self) -> str:
        return TRANSLATIONS[self.language]["nav_home"]

    @rx.var
    def nav_experience(self) -> str:
        return TRANSLATIONS[self.language]["nav_experience"]

    @rx.var
    def nav_projects(self) -> str:
        return TRANSLATIONS[self.language]["nav_projects"]

    @rx.var
    def nav_contact(self) -> str:
        return TRANSLATIONS[self.language]["nav_contact"]

    @rx.var
    def nav_blog(self) -> str:
        return TRANSLATIONS[self.language]["nav_blog"]

    @rx.var
    def nav_case_studies(self) -> str:
        return TRANSLATIONS[self.language]["nav_case_studies"]

    @rx.var
    def loader_loading(self) -> str:
        return TRANSLATIONS[self.language]["loader_loading"]

    @rx.var
    def loader_please_wait(self) -> str:
        return TRANSLATIONS[self.language]["loader_please_wait"]

    @rx.var
    def loader_loading_page(self) -> str:
        return TRANSLATIONS[self.language]["loader_loading_page"]

    # Timeline translations
    @rx.var
    def timeline_title(self) -> str:
        return TRANSLATIONS[self.language]["timeline_title"]

    @rx.var
    def timeline_step1(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step1"]

    @rx.var
    def timeline_step1_desc(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step1_desc"]

    @rx.var
    def timeline_step2(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step2"]

    @rx.var
    def timeline_step2_desc(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step2_desc"]

    @rx.var
    def timeline_step3(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step3"]

    @rx.var
    def timeline_step3_desc(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step3_desc"]

    @rx.var
    def timeline_step4(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step4"]

    @rx.var
    def timeline_step4_desc(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step4_desc"]

    @rx.var
    def timeline_step5(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step5"]

    @rx.var
    def timeline_step5_desc(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step5_desc"]

    @rx.var
    def timeline_step6(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step6"]

    @rx.var
    def timeline_step6_desc(self) -> str:
        return TRANSLATIONS[self.language]["timeline_step6_desc"]

    def init_chat(self):
        """Initialize chat with AI agent"""
        self.chat_active = True
        # Add initial greeting message from AI
        self.chat_messages = [
            {
                "role": "assistant",
                "content": self.chat_greeting
            }
        ]

    def close_chat(self):
        """Close chat and return to info view"""
        self.chat_active = False
        self.chat_messages = []

    # Services & Expertise translations
    @rx.var
    def services_title(self) -> str:
        return TRANSLATIONS[self.language]["services_title"]

    @rx.var
    def service_testing_title(self) -> str:
        return TRANSLATIONS[self.language]["service_testing_title"]

    @rx.var
    def service_testing_desc(self) -> str:
        return TRANSLATIONS[self.language]["service_testing_desc"]

    @rx.var
    def service_automation_title(self) -> str:
        return TRANSLATIONS[self.language]["service_automation_title"]

    @rx.var
    def service_automation_desc(self) -> str:
        return TRANSLATIONS[self.language]["service_automation_desc"]

    @rx.var
    def service_ai_title(self) -> str:
        return TRANSLATIONS[self.language]["service_ai_title"]

    @rx.var
    def service_ai_desc(self) -> str:
        return TRANSLATIONS[self.language]["service_ai_desc"]

    @rx.var
    def service_strategy_title(self) -> str:
        return TRANSLATIONS[self.language]["service_strategy_title"]

    @rx.var
    def service_strategy_desc(self) -> str:
        return TRANSLATIONS[self.language]["service_strategy_desc"]

    @rx.var
    def service_relations_title(self) -> str:
        return TRANSLATIONS[self.language]["service_relations_title"]

    @rx.var
    def service_relations_desc(self) -> str:
        return TRANSLATIONS[self.language]["service_relations_desc"]

    @rx.var
    def service_security_title(self) -> str:
        return TRANSLATIONS[self.language]["service_security_title"]

    @rx.var
    def service_security_desc(self) -> str:
        return TRANSLATIONS[self.language]["service_security_desc"]

    # Key Achievements translations
    @rx.var
    def achievements_title(self) -> str:
        return TRANSLATIONS[self.language]["achievements_title"]

    @rx.var
    def achievements_subtitle(self) -> str:
        return TRANSLATIONS[self.language]["achievements_subtitle"]

    @rx.var
    def achievements_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievements_problem"]

    @rx.var
    def achievements_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievements_solution"]

    @rx.var
    def achievements_result(self) -> str:
        return TRANSLATIONS[self.language]["achievements_result"]

    # Achievement 1
    @rx.var
    def achievement1_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievement1_problem"]

    @rx.var
    def achievement1_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievement1_solution"]

    @rx.var
    def achievement1_result(self) -> str:
        return TRANSLATIONS[self.language]["achievement1_result"]

    # Achievement 2
    @rx.var
    def achievement2_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievement2_problem"]

    @rx.var
    def achievement2_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievement2_solution"]

    @rx.var
    def achievement2_result(self) -> str:
        return TRANSLATIONS[self.language]["achievement2_result"]

    # Achievement 3
    @rx.var
    def achievement3_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievement3_problem"]

    @rx.var
    def achievement3_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievement3_solution"]

    @rx.var
    def achievement3_result(self) -> str:
        return TRANSLATIONS[self.language]["achievement3_result"]

    # Achievement 4
    @rx.var
    def achievement4_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievement4_problem"]

    @rx.var
    def achievement4_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievement4_solution"]

    @rx.var
    def achievement4_result(self) -> str:
        return TRANSLATIONS[self.language]["achievement4_result"]

    # Achievement 5
    @rx.var
    def achievement5_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievement5_problem"]

    @rx.var
    def achievement5_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievement5_solution"]

    @rx.var
    def achievement5_result(self) -> str:
        return TRANSLATIONS[self.language]["achievement5_result"]

    # Achievement 6
    @rx.var
    def achievement6_problem(self) -> str:
        return TRANSLATIONS[self.language]["achievement6_problem"]

    @rx.var
    def achievement6_solution(self) -> str:
        return TRANSLATIONS[self.language]["achievement6_solution"]

    @rx.var
    def achievement6_result(self) -> str:
        return TRANSLATIONS[self.language]["achievement6_result"]

    # Case Studies page translations
    @rx.var
    def case_studies_title(self) -> str:
        return TRANSLATIONS[self.language]["case_studies_title"]

    @rx.var
    def case_studies_subtitle(self) -> str:
        return TRANSLATIONS[self.language]["case_studies_subtitle"]

    @rx.var
    def case_studies_intro(self) -> str:
        return TRANSLATIONS[self.language]["case_studies_intro"]

    @rx.var
    def case_studies_cta(self) -> str:
        return TRANSLATIONS[self.language]["case_studies_cta"]

    # About window translations
    @rx.var
    def about_title(self) -> str:
        return TRANSLATIONS[self.language]["about_title"]

    @rx.var
    def about_intro_1(self) -> str:
        return TRANSLATIONS[self.language]["about_intro_1"]

    @rx.var
    def about_intro_2(self) -> str:
        return TRANSLATIONS[self.language]["about_intro_2"]

    @rx.var
    def about_chat_button(self) -> str:
        return TRANSLATIONS[self.language]["about_chat_button"]

    @rx.var
    def about_chat_title(self) -> str:
        return TRANSLATIONS[self.language]["about_chat_title"]

    @rx.var
    def about_file_title(self) -> str:
        return TRANSLATIONS[self.language]["about_file_title"]

    # Chat translations
    @rx.var
    def chat_greeting(self) -> str:
        return TRANSLATIONS[self.language]["chat_greeting"]

    @rx.var
    def chat_placeholder(self) -> str:
        return TRANSLATIONS[self.language]["chat_placeholder"]

    @rx.var
    def chat_close(self) -> str:
        return TRANSLATIONS[self.language]["chat_close"]

    # Experience page translations
    @rx.var
    def exp_title(self) -> str:
        return TRANSLATIONS[self.language]["exp_title"]

    @rx.var
    def exp_subtitle(self) -> str:
        return TRANSLATIONS[self.language]["exp_subtitle"]

    @rx.var
    def exp_description(self) -> str:
        return TRANSLATIONS[self.language]["exp_description"]

    @rx.var
    def exp_tech_stack(self) -> str:
        return TRANSLATIONS[self.language]["exp_tech_stack"]

    @rx.var
    def exp_testing_frameworks(self) -> str:
        return TRANSLATIONS[self.language]["exp_testing_frameworks"]

    @rx.var
    def exp_languages_tech(self) -> str:
        return TRANSLATIONS[self.language]["exp_languages_tech"]

    @rx.var
    def exp_devops(self) -> str:
        return TRANSLATIONS[self.language]["exp_devops"]

    @rx.var
    def exp_tools(self) -> str:
        return TRANSLATIONS[self.language]["exp_tools"]

    @rx.var
    def exp_ai_ml(self) -> str:
        return TRANSLATIONS[self.language]["exp_ai_ml"]

    @rx.var
    def exp_key_achievements(self) -> str:
        return TRANSLATIONS[self.language]["exp_key_achievements"]

    @rx.var
    def exp_languages(self) -> str:
        return TRANSLATIONS[self.language]["exp_languages"]

    @rx.var
    def exp_certificates(self) -> str:
        return TRANSLATIONS[self.language]["exp_certificates"]

    @rx.var
    def lang_english(self) -> str:
        return TRANSLATIONS[self.language]["lang_english"]

    @rx.var
    def lang_polish(self) -> str:
        return TRANSLATIONS[self.language]["lang_polish"]

    @rx.var
    def lang_german(self) -> str:
        return TRANSLATIONS[self.language]["lang_german"]

    @rx.var
    def lang_level_native(self) -> str:
        return TRANSLATIONS[self.language]["lang_level_native"]

    @rx.var
    def lang_level_upper_intermediate(self) -> str:
        return TRANSLATIONS[self.language]["lang_level_upper_intermediate"]

    @rx.var
    def lang_level_beginner(self) -> str:
        return TRANSLATIONS[self.language]["lang_level_beginner"]

    # Projects page translations
    @rx.var
    def proj_title(self) -> str:
        return TRANSLATIONS[self.language]["proj_title"]

    @rx.var
    def proj_description(self) -> str:
        return TRANSLATIONS[self.language]["proj_description"]

    @rx.var
    def proj_search(self) -> str:
        return TRANSLATIONS[self.language]["proj_search"]

    @rx.var
    def proj_technologies(self) -> str:
        return TRANSLATIONS[self.language]["proj_technologies"]

    @rx.var
    def proj_platform(self) -> str:
        return TRANSLATIONS[self.language]["proj_platform"]

    @rx.var
    def proj_domain(self) -> str:
        return TRANSLATIONS[self.language]["proj_domain"]

    @rx.var
    def proj_all(self) -> str:
        return TRANSLATIONS[self.language]["proj_all"]

    @rx.var
    def proj_personal(self) -> str:
        return TRANSLATIONS[self.language]["proj_personal"]

    @rx.var
    def proj_client(self) -> str:
        return TRANSLATIONS[self.language]["proj_client"]

    @rx.var
    def proj_clear_filters(self) -> str:
        return TRANSLATIONS[self.language]["proj_clear_filters"]

    @rx.var
    def proj_view_details(self) -> str:
        return TRANSLATIONS[self.language]["proj_view_details"]

    @rx.var
    def proj_achievements(self) -> str:
        return TRANSLATIONS[self.language]["proj_achievements"]

    @rx.var
    def proj_view_code(self) -> str:
        return TRANSLATIONS[self.language]["proj_view_code"]

    @rx.var
    def proj_live_demo(self) -> str:
        return TRANSLATIONS[self.language]["proj_live_demo"]
