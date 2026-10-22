import reflex as rx
from reflex.components.radix.themes.layout.box import Box
from reflex.components.radix.themes.layout.stack import HStack, VStack

css: dict = {
    "main": {
        "width": "100%",
        "padding": ["1rem", "1rem", "2rem", "2rem", "2rem"],
        "align_items": "center",
        "justify_content": "center",
        "flex": "1",
        "display": "flex",
        "flexDirection": "column"
    }
}

wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(25deg)"},
        "100%": {"transform": "rotate(-15deg)"},
    },
    "@keyframes slideInUp": {
        "0%": {"opacity": "0", "transform": "translateY(30px)"},
        "100%": {"opacity": "1", "transform": "translateY(0)"}
    },
    "@keyframes slideInLeft": {
        "0%": {"opacity": "0", "transform": "translateX(-30px)"},
        "100%": {"opacity": "1", "transform": "translateX(0)"}
    },
    "@keyframes slideInRight": {
        "0%": {"opacity": "0", "transform": "translateX(30px)"},
        "100%": {"opacity": "1", "transform": "translateX(0)"}
    },
    "@keyframes fadeIn": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"}
    }
}


def contact_section() -> rx.Component:
    """Contact section with social links - can be used on any page"""
    from state import State
    from portfolio.translations import get_translation

    def _create_breadcrumb_item(icon: str, title: str, url: str) -> rx.Component:
        # Brand colors for dark theme
        brand_colors = {
            "GitHub": {"bg": "rgba(36, 41, 47, 0.8)", "hover_bg": "rgba(36, 41, 47, 1)", "icon_color": "white"},
            "LinkedIn": {"bg": "rgba(0, 119, 181, 0.8)", "hover_bg": "rgba(0, 119, 181, 1)", "icon_color": "white"},
            "Email": {"bg": "rgba(0, 212, 255, 0.8)", "hover_bg": "rgba(0, 212, 255, 1)", "icon_color": "white"},
        }
        colors = brand_colors.get(title, {"bg": "rgba(100, 116, 139, 0.8)", "hover_bg": "rgba(100, 116, 139, 1)", "icon_color": "gray.300"})

        return rx.link(
            rx.button(
                rx.flex(
                    rx.icon(icon, size=20, color=colors["icon_color"]),
                    rx.tablet_and_desktop(
                        rx.text(
                            title,
                            size="3",
                            weight="bold",
                            color="white",
                            margin_left="0.5rem"
                        )
                    ),
                    align="center",
                    justify="center",
                    gap="2"
                ),
                size="3",
                radius="full",
                style={
                    "background": colors["bg"],
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "boxShadow": "0 8px 32px rgba(0, 0, 0, 0.3)",
                    "transition": "all 0.3s ease",
                    "cursor": "pointer",
                    "minWidth": ["50px", "50px", "120px", "120px", "120px"],
                    "height": "44px",
                    "_hover": {
                        "background": colors["hover_bg"],
                        "transform": "translateY(-2px)",
                        "boxShadow": "0 12px 40px rgba(0, 0, 0, 0.4)"
                    }
                }
            ),
            href=url,
            target="_blank",
        )

    data = [
        ("github", "GitHub", "https://github.com/MOrgacki"),
        ("linkedin", "LinkedIn", "https://www.linkedin.com/in/m-orgacki/"),
        ("mail", "Email", "mailto:marcinorgacki@gmail.com")
    ]

    return rx.box(
        rx.vstack(
            rx.heading(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "contact_title"),
                    get_translation("en", "contact_title")
                ),
                size="7",
                text_align="center",
                margin_bottom="1rem",
                font_weight="700",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                }
            ),
            rx.text(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "contact_description"),
                    get_translation("en", "contact_description")
                ),
                color="gray.300",
                text_align="center",
                font_size="1.1rem",
                margin_bottom="2rem",
                max_width="600px"
            ),
            rx.hstack(
                *[_create_breadcrumb_item(icon, title, url) for icon, title, url in data],
                spacing="4",
                justify="center",
                wrap="wrap"
            ),
            spacing="4",
            align="center",
            padding="4rem 2rem",
            width="100%"
        ),
        width="100%",
        style={
            "background": "rgba(15, 23, 42, 0.5)",
            "backdropFilter": "blur(10px)"
        }
    )


class Main:
    def __init__(self) -> None:
        from state import State
        from portfolio.translations import get_translation
        self.box: Box = rx.box(width="100%")
        self.a, self.b, *self.rest = [
            rx.heading(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "home_hello"),
                    get_translation("en", "home_hello")
                ),
                font_size=["1.35rem", "1.75rem",
                           "3rem", "4rem", "4rem"],
                font_weight="600",
                line_height="1.2",
                color="gray.100"),
            rx.heading(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "home_im"),
                    get_translation("en", "home_im")
                ),
                font_size=["1.35rem", "1.75rem",
                           "3rem", "4rem", "4rem"],
                font_weight="600",
                line_height="1.2",
                color="gray.100"),
            rx.heading(
                "Marcin",
                font_size=["2.5rem", "2.5rem",
                           "3rem", "4rem", "4rem"],
                font_weight="700",
                line_height="1.2",
                text_align="center",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                    "paddingBottom": "0.1rem"
                }

            ), rx.heading(
                "Orgacki",
                font_size=["2.5rem", "2.5rem",
                           "3rem", "4rem", "4rem"],
                font_weight="700",
                line_height="1.2",
                text_align="center",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                    "paddingBottom": "0.1rem"
                }),
            rx.heading("👋", font_size=["1.35rem", "1.75rem",
                                       "3rem", "4rem", "4rem"], style={
                **wave,  # Spread the keyframes here
                "animation": "wave 0.8s cubic-bezier(0.25,0.46,0.45,0.94) infinite alternate-reverse both"
            },)]

        self.badge_stack_max: rx.Component = rx.hstack(spacing="4")
        self.badge_stack_min: rx.Component = rx.hstack(
            spacing="2", align="center")
        self.name_mobile: VStack = rx.vstack(rx.hstack(self.a, self.b), *self.rest, align="center"
                                             )
        self.name_desktop: HStack = rx.hstack(self.a, self.b, *self.rest,
                                              spacing="4", line_height="1", padding=["0.5rem",],)
        titles: list = ["Quality Automation Architect",
                        "AI Solutions Advisor", "Business Process Expert"]
        self.badge_stack_max.children = [
            self._create_badges(title) for title in titles]
        self.badge_stack_min.children = [
            self._create_badges(title) for title in titles]

        self.crumbs: rx.Component = rx.hstack(spacing="4")
        data: list = [("github", "GitHub", "https://github.com/MOrgacki"),
                      ("linkedin", "LinkedIn", "https://www.linkedin.com/in/m-orgacki/"),
                      ("mail", "Email", "mailto:marcinorgacki@gmail.com")]
        self.crumbs.children = [
            self._create_breadcrumb_item(icon, title, url) for icon, title, url in data]

        # Expertise box
        self.expertise_box = self._create_expertise_box()

    def build_view(self):
        self.box.children = [self._build_desktop(), self._build_mobile()]
        return self.box

    def _contact_button(self):
        return rx.link(
            rx.button(
                rx.flex(
                    rx.icon("mail", size=20, color="white"),
                    rx.text(
                        "Contact Me",
                        size="3",
                        weight="bold",
                        color="white",
                        margin_left="0.5rem"
                    ),
                    align="center",
                    justify="center",
                    gap="2"
                ),
                size="3",
                radius="full",
                margin_y="4",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "boxShadow": "0 8px 32px rgba(0, 212, 255, 0.3)",
                    "transition": "all 0.3s ease",
                    "cursor": "pointer",
                    "minWidth": "120px",
                    "height": "44px",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "boxShadow": "0 12px 40px rgba(0, 212, 255, 0.4)"
                    }
                }
            ),
            href="mailto:marcinorgacki@gmail.com",
            target="_blank"
        )

    def _create_info_view(self) -> rx.Component:
        """Create the info view with a button to start chat"""
        from state import State
        from portfolio.translations import get_translation
        return rx.vstack(
            rx.text(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "about_title"),
                    get_translation("en", "about_title")
                ),
                font_size="1.5rem",
                font_weight="700",
                color="cyan.300",
                margin_bottom="1rem"
            ),
            rx.text(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "about_intro_1"),
                    get_translation("en", "about_intro_1")
                ),
                color="gray.300",
                line_height="1.7",
                text_align="center",
                margin_bottom="0.5rem"
            ),
            rx.text(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "about_intro_2"),
                    get_translation("en", "about_intro_2")
                ),
                color="gray.300",
                line_height="1.7",
                text_align="center",
                margin_bottom="1rem"
            ),

            # Skills tags
            rx.flex(
                rx.badge("AI Orchestration", color_scheme="cyan"),
                rx.badge("Business Automation", color_scheme="blue"),
                rx.badge("Quality Strategy", color_scheme="purple"),
                rx.badge("AI Agents", color_scheme="pink"),
                rx.badge("Process Design", color_scheme="orange"),
                gap="0.5rem",
                wrap="wrap",
                justify="center",
                margin_top="1rem",
                margin_bottom="1.5rem"
            ),

            # Chat init button
            rx.button(
                rx.hstack(
                    rx.icon("bot", size=20, color="white"),
                    rx.text(
                        rx.cond(
                            State.language == "pl",
                            get_translation("pl", "about_chat_button"),
                            get_translation("en", "about_chat_button")
                        ),
                        color="white",
                        font_weight="600"
                    ),
                    spacing="2",
                    align="center"
                ),
                on_click=State.init_chat,
                size="3",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "boxShadow": "0 8px 20px rgba(0, 212, 255, 0.4)"
                    }
                }
            ),

            padding="2rem",
            spacing="3",
            align="center",
            width="100%",
            flex="1",
        )

    def _create_chat_view(self) -> rx.Component:
        """Create the chat view"""
        from state import State
        from portfolio.translations import get_translation
        return rx.vstack(
            # Chat messages area
            rx.vstack(
                rx.foreach(
                    State.chat_messages,
                    lambda msg: rx.box(
                        rx.hstack(
                            rx.box(
                                rx.icon("bot", size=16, color="cyan.300"),
                                padding="0.5rem",
                                border_radius="50%",
                                style={
                                    "background": "rgba(0, 212, 255, 0.1)",
                                    "border": "1px solid rgba(0, 212, 255, 0.3)"
                                }
                            ),
                            rx.text(
                                msg["content"],
                                color="gray.300",
                                line_height="1.6",
                                font_size="0.95rem"
                            ),
                            spacing="3",
                            align="start"
                        ),
                        padding="1rem",
                        border_radius="lg",
                        width="100%",
                        style={
                            "background": "rgba(0, 212, 255, 0.05)",
                            "border": "1px solid rgba(0, 212, 255, 0.1)"
                        }
                    )
                ),
                spacing="3",
                width="100%",
                min_height="200px",
                max_height="300px",
                overflow_y="auto",
                padding="1rem",
                style={
                    "scrollbarWidth": "thin",
                    "scrollbarColor": "rgba(0, 212, 255, 0.3) transparent"
                }
            ),

            # Input area placeholder
            rx.hstack(
                rx.box(
                    rx.text(
                        rx.cond(
                            State.language == "pl",
                            get_translation("pl", "chat_placeholder"),
                            get_translation("en", "chat_placeholder")
                        ),
                        color="gray.500",
                        font_size="0.9rem",
                        font_style="italic"
                    ),
                    padding="0.75rem 1rem",
                    border_radius="lg",
                    flex="1",
                    style={
                        "background": "rgba(30, 41, 59, 0.5)",
                        "border": "1px solid rgba(100, 116, 139, 0.3)"
                    }
                ),
                width="100%",
                padding="0 1rem 1rem 1rem"
            ),

            # Close button
            rx.button(
                rx.hstack(
                    rx.icon("x", size=16),
                    rx.text(
                        rx.cond(
                            State.language == "pl",
                            get_translation("pl", "chat_close"),
                            get_translation("en", "chat_close")
                        ),
                        font_size="0.85rem"
                    ),
                    spacing="2"
                ),
                on_click=State.close_chat,
                size="2",
                variant="soft",
                color_scheme="gray",
                style={
                    "cursor": "pointer",
                    "alignSelf": "center",
                    "marginBottom": "1rem"
                }
            ),

            spacing="0",
            width="100%",
            flex="1",
        )

    def _create_window_box(self) -> rx.Component:
        """Create a macOS/Windows style window with floating emojis"""
        from state import State
        return rx.box(
            # Floating emojis/icons around the window
            rx.box(
                "🚀",
                position="absolute",
                top="-20px",
                left="-20px",
                font_size="2.5rem",
                style={
                    "animation": "float 3s ease-in-out infinite",
                    "zIndex": "15"
                }
            ),
            rx.box(
                "✨",
                position="absolute",
                top="-15px",
                right="40px",
                font_size="2rem",
                style={
                    "animation": "float 3s ease-in-out infinite 0.5s",
                    "zIndex": "15"
                }
            ),
            rx.box(
                "🎯",
                position="absolute",
                bottom="-20px",
                right="-20px",
                font_size="2.5rem",
                style={
                    "animation": "float 3s ease-in-out infinite 1s",
                    "zIndex": "15"
                }
            ),
            rx.box(
                "💡",
                position="absolute",
                bottom="30px",
                left="-25px",
                font_size="2rem",
                style={
                    "animation": "float 3s ease-in-out infinite 1.5s",
                    "zIndex": "15"
                }
            ),

            # Window container
            rx.vstack(
                # Window title bar (macOS style)
                rx.hstack(
                    # Traffic light buttons
                    rx.hstack(
                        rx.box(
                            width="12px",
                            height="12px",
                            border_radius="50%",
                            background="#ff5f57",
                            style={
                                "boxShadow": "0 0 0 1px rgba(0,0,0,0.1)"
                            }
                        ),
                        rx.box(
                            width="12px",
                            height="12px",
                            border_radius="50%",
                            background="#febc2e",
                            style={
                                "boxShadow": "0 0 0 1px rgba(0,0,0,0.1)"
                            }
                        ),
                        rx.box(
                            width="12px",
                            height="12px",
                            border_radius="50%",
                            background="#28c840",
                            style={
                                "boxShadow": "0 0 0 1px rgba(0,0,0,0.1)"
                            }
                        ),
                        spacing="2"
                    ),

                    # Window title
                    rx.text(
                        rx.cond(
                            State.chat_active,
                            rx.cond(
                                State.language == "pl",
                                "asystent_ai.czat",
                                "ai_assistant.chat"
                            ),
                            rx.cond(
                                State.language == "pl",
                                "o_mnie.txt",
                                "about_me.txt"
                            )
                        ),
                        color="gray.400",
                        font_size="0.85rem",
                        font_weight="500",
                        position="absolute",
                        left="50%",
                        style={
                            "transform": "translateX(-50%)"
                        }
                    ),

                    width="100%",
                    padding="0.75rem 1rem",
                    position="relative",
                    style={
                        "background": "rgba(30, 41, 59, 0.95)",
                        "borderBottom": "1px solid rgba(100, 116, 139, 0.3)"
                    }
                ),

                # Window content - conditionally render info or chat view
                rx.cond(
                    State.chat_active,
                    self._create_chat_view(),
                    self._create_info_view()
                ),

                width="100%",
                min_height="480px",
                spacing="0",
                border_radius="12px",
                overflow="hidden",
                style={
                    "background": "rgba(30, 41, 59, 0.8)",
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(100, 116, 139, 0.3)",
                    "boxShadow": "0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05)"
                }
            ),

            position="relative",
            width=["95%", "90%", "600px", "650px", "700px"],
            min_height="480px",
            margin_x="auto",
            margin_y="3rem",
            style={
                **wave,
                "@keyframes float": {
                    "0%, 100%": {"transform": "translateY(0px)"},
                    "50%": {"transform": "translateY(-10px)"}
                },
                "animation": "slideInUp 0.8s ease-out 0.6s both",
                "zIndex": "10"
            }
        )

    def _build_desktop(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                rx.box(
                    self.name_desktop,
                    margin_bottom="4",
                    style={
                        **wave,
                        "animation": "slideInUp 0.8s ease-out",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    self.badge_stack_min,
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.2s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    rx.hstack(self.crumbs, justify="center", wrap="wrap", spacing="4"),
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.4s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),

                # Add the window box
                self._create_window_box(),

                spacing="4",
                align="center",
                style=css.get("main")
            )
        )

    def _build_mobile(self):
        return rx.mobile_only(
            rx.vstack(
                rx.box(
                    self.name_mobile,
                    margin_bottom="4",
                    style={
                        **wave,
                        "animation": "slideInUp 0.8s ease-out",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    self.badge_stack_min,
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.2s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(self.crumbs, justify="center", wrap="wrap", spacing="2"),
                        spacing="3",
                        align="center"
                    ),
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.4s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),

                # Add the window box for mobile too
                self._create_window_box(),

                spacing="4",
                align="center",
                style=css.get("main")
            )
        )

    def _create_badges(self, title: str) -> rx.Component:
        return rx.badge(
            title,
            variant="solid",
            padding=["0.10rem 0.25rem", "0.10rem 0.25rem",
                     "0.10rem 0.7rem", "0.10rem 0.7rem", "0.10rem 0.7rem",],
            font_size=["0.55rem", "0.55rem",
                       "0.75rem", "0.75rem", "0.75rem"],
            style={
                "background": "rgba(0, 212, 255, 0.1)",
                "color": "cyan.300",
                "border": "1px solid rgba(0, 212, 255, 0.2)",
                "backdropFilter": "blur(10px)"
            }
        )

    def _create_breadcrumb_item(self, icon: str, title: str, url: str | None) -> rx.Component:
        # Brand colors for dark theme
        brand_colors = {
            "GitHub": {"bg": "rgba(36, 41, 47, 0.8)", "hover_bg": "rgba(36, 41, 47, 1)", "icon_color": "white"},
            "LinkedIn": {"bg": "rgba(0, 119, 181, 0.8)", "hover_bg": "rgba(0, 119, 181, 1)", "icon_color": "white"},
            "Email": {"bg": "rgba(0, 212, 255, 0.8)", "hover_bg": "rgba(0, 212, 255, 1)", "icon_color": "white"},
        }
        colors = brand_colors.get(title, {"bg": "rgba(100, 116, 139, 0.8)", "hover_bg": "rgba(100, 116, 139, 1)", "icon_color": "gray.300"})
        
        return rx.link(
            rx.button(
                rx.flex(
                    rx.icon(icon, size=20, color=colors["icon_color"]),
                    rx.tablet_and_desktop(
                        rx.text(
                            title,
                            size="3",
                            weight="bold",
                            color="white",
                            margin_left="0.5rem"
                        )
                    ),
                    align="center",
                    justify="center",
                    gap="2"
                ),
                size="3",
                radius="full",
                style={
                    "background": colors["bg"],
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "boxShadow": "0 8px 32px rgba(0, 0, 0, 0.3)",
                    "transition": "all 0.3s ease",
                    "cursor": "pointer",
                    "minWidth": ["50px", "50px", "120px", "120px", "120px"],
                    "height": "44px",
                    "_hover": {
                        "background": colors["hover_bg"],
                        "transform": "translateY(-2px)",
                        "boxShadow": "0 12px 40px rgba(0, 0, 0, 0.4)"
                    }
                }
            ),
            href=url,
            target="_blank",
        )

    def _create_expertise_box(self) -> rx.Component:
        from state import State
        from portfolio.translations import get_translation
        return rx.box(
            # Header
            rx.text(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "skills_title"),
                    get_translation("en", "skills_title")
                ),
                weight="bold",
                size="5",
                text_align="center",
                color="cyan.300",
                margin_top="1rem",
                margin_bottom="1.5rem"
            ),

            # Core Skills Section
            rx.vstack(
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_skill_1"),
                        get_translation("en", "skills_skill_1")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6",
                    style={"span": {"color": "cyan.400", "fontWeight": "bold"}}
                ),
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_skill_2"),
                        get_translation("en", "skills_skill_2")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_skill_3"),
                        get_translation("en", "skills_skill_3")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_skill_4"),
                        get_translation("en", "skills_skill_4")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                spacing="3",
                align="center",
                width="100%",
                margin_bottom="2rem"
            ),

            # Divider
            rx.divider(border_color="rgba(100, 116, 139, 0.3)", margin_y="1.5rem"),

            # Additional Experience Header
            rx.text(
                rx.cond(
                    State.language == "pl",
                    get_translation("pl", "skills_additional"),
                    get_translation("en", "skills_additional")
                ),
                weight="bold",
                size="4",
                text_align="center",
                color="cyan.300",
                margin_bottom="1.5rem"
            ),

            # Additional Experience Section
            rx.vstack(
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_add_1"),
                        get_translation("en", "skills_add_1")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_add_2"),
                        get_translation("en", "skills_add_2")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_add_3"),
                        get_translation("en", "skills_add_3")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    rx.cond(
                        State.language == "pl",
                        get_translation("pl", "skills_add_4"),
                        get_translation("en", "skills_add_4")
                    ),
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                spacing="3",
                align="center",
                width="100%",
                margin_bottom="1rem"
            ),

            # Box styling
            padding_x="9",
            padding_y="12",
            border_radius="3xl",
            margin_y="6",
            width=["90%", "90%", "80%", "70%", "60%"],
            max_width="650px",
            style={
                "background": "rgba(30, 41, 59, 0.8)",
                "backdropFilter": "blur(20px)",
                "border": "1px solid rgba(100, 116, 139, 0.2)",
                "boxShadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05)",
                "margin": "0 auto"
            }
        )
