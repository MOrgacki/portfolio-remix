import reflex as rx
from portfolio.header import Header
from portfolio.footer import Footer
from portfolio.sidebar import sidebar
from portfolio.animations import animated_background, animations_css
from portfolio.loader import page_transition_loader
from portfolio.floating_button import floating_language_button
from state import State


def project_info_box(project_title: str, project_link: str, color_scheme: dict) -> rx.Component:
    """Create a small project info box with link"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("briefcase", size=16, color=color_scheme["icon"]),
                rx.text(
                    "PROJECT",
                    font_weight="800",
                    font_size="0.65rem",
                    color=color_scheme["label"],
                    text_transform="uppercase",
                    letter_spacing="0.1em"
                ),
                spacing="1",
                align="center",
                margin_bottom="0.5rem"
            ),
            rx.text(
                project_title,
                color="gray.200",
                font_size="0.85rem",
                line_height="1.4",
                font_weight="600",
                text_align="center",
                margin_bottom="0.75rem"
            ),
            rx.link(
                rx.hstack(
                    rx.text(
                        "View Project",
                        font_size="0.75rem",
                        color=color_scheme["icon"],
                        font_weight="600"
                    ),
                    rx.icon("external-link", size=12, color=color_scheme["icon"]),
                    spacing="1",
                    align="center"
                ),
                href=project_link,
                text_decoration="none",
                style={
                    "transition": "all 0.2s ease",
                    "_hover": {
                        "transform": "translateX(2px)"
                    }
                }
            ),
            spacing="2",
            align="center",
            width="100%"
        ),
        padding="1.25rem",
        border_radius="lg",
        min_width="200px",
        max_width="220px",
        height="fit-content",
        cursor="pointer",
        style={
            "background": color_scheme["bg"],
            "border": f"2px solid {color_scheme['border']}",
            "backdropFilter": "blur(10px)",
            "transition": "all 0.3s ease",
            "_hover": {
                "background": color_scheme["hover_bg"],
                "borderColor": color_scheme["hover_border"],
                "transform": "translateY(-2px)",
                "boxShadow": f"0 8px 24px {color_scheme['shadow']}"
            }
        }
    )


def achievement_card(problem_text: str, solution_text: str, result_text: str, color_scheme: dict, project_title: str = "", project_link: str = "") -> rx.Component:
    """Create an achievement card with problem-solution-result format and optional project info"""
    return rx.hstack(
        rx.box(
            rx.vstack(
                # Problem section
                rx.vstack(
                    rx.hstack(
                        rx.icon("alert-circle", size=20, color=color_scheme["icon"]),
                        rx.text(
                            State.achievements_problem,
                            font_weight="700",
                            font_size="0.75rem",
                            color=color_scheme["label"],
                            text_transform="uppercase",
                            letter_spacing="0.05em"
                        ),
                        spacing="2",
                        align="center"
                    ),
                    rx.text(
                        problem_text,
                        color="gray.300",
                        font_size="0.95rem",
                        line_height="1.6",
                        font_weight="500"
                    ),
                    spacing="3",
                    align="start",
                    width="100%"
                ),

                # Divider
                rx.divider(border_color=color_scheme["border"], opacity="0.3"),

                # Solution section
                rx.vstack(
                    rx.hstack(
                        rx.icon("lightbulb", size=20, color=color_scheme["icon"]),
                        rx.text(
                            State.achievements_solution,
                            font_weight="700",
                            font_size="0.75rem",
                            color=color_scheme["label"],
                            text_transform="uppercase",
                            letter_spacing="0.05em"
                        ),
                        spacing="2",
                        align="center"
                    ),
                    rx.text(
                        solution_text,
                        color="gray.400",
                        font_size="0.9rem",
                        line_height="1.7"
                    ),
                    spacing="3",
                    align="start",
                    width="100%"
                ),

                # Result badge
                rx.box(
                    rx.hstack(
                        rx.icon("check-circle", size=18, color=color_scheme["icon"]),
                        rx.text(
                            State.achievements_result + ": ",
                            font_weight="700",
                            font_size="0.8rem",
                            color=color_scheme["label"],
                            text_transform="uppercase",
                            letter_spacing="0.05em"
                        ),
                        rx.text(
                            result_text,
                            font_weight="600",
                            font_size="0.9rem",
                            color=color_scheme["icon"]
                        ),
                        spacing="2",
                        align="center"
                    ),
                    padding="0.75rem 1.25rem",
                    border_radius="full",
                    width="fit-content",
                    style={
                        "background": color_scheme["result_bg"],
                        "border": f"1px solid {color_scheme['result_border']}"
                    }
                ),

                spacing="5",
                align="start",
                width="100%"
            ),
            padding="2rem",
            border_radius="xl",
            flex="1",
            style={
                "background": color_scheme["bg"],
                "border": f"1px solid {color_scheme['border']}",
                "backdropFilter": "blur(10px)",
                "transition": "all 0.3s ease",
                "_hover": {
                    "background": color_scheme["hover_bg"],
                    "borderColor": color_scheme["hover_border"],
                    "transform": "translateY(-4px)",
                    "boxShadow": f"0 12px 32px {color_scheme['shadow']}"
                }
            }
        ),
        # Project info box (conditionally rendered)
        rx.cond(
            project_title != "",
            project_info_box(project_title, project_link, color_scheme),
            rx.box()
        ),
        spacing="4",
        align="start",
        width="100%"
    )


def case_studies_page() -> rx.Component:
    """Case Studies page showcasing problem-solving approach"""
    header = Header()
    footer = Footer()
    header_component = header.build()
    footer_component = footer.build()
    # sidebar_component = sidebar()  # Removed sidebar

    # Layout
    layout = rx.vstack(
        header_component,
        rx.box(
            # Hero section
            rx.vstack(
                rx.heading(
                    State.case_studies_title,
                    size="9",
                    text_align="center",
                    margin_bottom="1rem",
                    font_weight="900",
                    line_height="1.1",
                    width="100%",
                    style={
                        "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 50%, #8b5cf6 100%)",
                        "backgroundClip": "text",
                        "WebkitBackgroundClip": "text",
                        "color": "transparent",
                        "textShadow": "0 0 40px rgba(0, 212, 255, 0.4)",
                        "letterSpacing": "-0.05em"
                    }
                ),
                rx.text(
                    State.case_studies_subtitle,
                    color="gray.300",
                    text_align="center",
                    font_size="1.3rem",
                    font_weight="700",
                    margin_bottom="1.5rem",
                    max_width="900px",
                    margin_x="auto",
                    line_height="1.3"
                ),
                rx.text(
                    State.case_studies_intro,
                    color="gray.400",
                    text_align="center",
                    font_size="1.05rem",
                    margin_bottom="3rem",
                    max_width="850px",
                    margin_x="auto",
                    line_height="1.8",
                    font_weight="400"
                ),

                # Case Studies Grid - Aligned Layout with Project Info
                rx.box(
                    # Row 1 (Card 1) - Web3 Gaming & Crypto Platform
                    rx.box(
                        achievement_card(
                            State.achievement1_problem,
                            State.achievement1_solution,
                            State.achievement1_result,
                            {
                                "icon": "cyan.300",
                                "label": "cyan.400",
                                "bg": "rgba(0, 212, 255, 0.05)",
                                "border": "rgba(0, 212, 255, 0.2)",
                                "hover_bg": "rgba(0, 212, 255, 0.08)",
                                "hover_border": "rgba(0, 212, 255, 0.4)",
                                "shadow": "rgba(0, 212, 255, 0.2)",
                                "result_bg": "rgba(0, 212, 255, 0.12)",
                                "result_border": "rgba(0, 212, 255, 0.4)"
                            },
                            "Web3 Gaming & Crypto Platform",
                            "/projects"
                        ),
                        width="100%",
                        max_width="1100px",
                        margin_x="auto",
                        margin_bottom="2rem"
                    ),

                    # Row 2 (Card 2) - Fintech Banking Platform
                    rx.box(
                        achievement_card(
                            State.achievement2_problem,
                            State.achievement2_solution,
                            State.achievement2_result,
                            {
                                "icon": "blue.300",
                                "label": "blue.400",
                                "bg": "rgba(91, 115, 255, 0.05)",
                                "border": "rgba(91, 115, 255, 0.2)",
                                "hover_bg": "rgba(91, 115, 255, 0.08)",
                                "hover_border": "rgba(91, 115, 255, 0.4)",
                                "shadow": "rgba(91, 115, 255, 0.2)",
                                "result_bg": "rgba(91, 115, 255, 0.12)",
                                "result_border": "rgba(91, 115, 255, 0.4)"
                            },
                            "Fintech Banking Platform",
                            "/projects"
                        ),
                        width="100%",
                        max_width="1100px",
                        margin_x="auto",
                        margin_bottom="2rem"
                    ),

                    # Row 3 (Card 3) - AI-Powered GPU Computing App
                    rx.box(
                        achievement_card(
                            State.achievement3_problem,
                            State.achievement3_solution,
                            State.achievement3_result,
                            {
                                "icon": "purple.300",
                                "label": "purple.400",
                                "bg": "rgba(139, 92, 246, 0.05)",
                                "border": "rgba(139, 92, 246, 0.2)",
                                "hover_bg": "rgba(139, 92, 246, 0.08)",
                                "hover_border": "rgba(139, 92, 246, 0.4)",
                                "shadow": "rgba(139, 92, 246, 0.2)",
                                "result_bg": "rgba(139, 92, 246, 0.12)",
                                "result_border": "rgba(139, 92, 246, 0.4)"
                            },
                            "AI-Powered GPU Computing App",
                            "/projects"
                        ),
                        width="100%",
                        max_width="1100px",
                        margin_x="auto",
                        margin_bottom="2rem"
                    ),

                    # Row 4 (Card 4) - Web3 Gaming Mobile App - Rewards Marketplace
                    rx.box(
                        achievement_card(
                            State.achievement4_problem,
                            State.achievement4_solution,
                            State.achievement4_result,
                            {
                                "icon": "pink.300",
                                "label": "pink.400",
                                "bg": "rgba(236, 72, 153, 0.05)",
                                "border": "rgba(236, 72, 153, 0.2)",
                                "hover_bg": "rgba(236, 72, 153, 0.08)",
                                "hover_border": "rgba(236, 72, 153, 0.4)",
                                "shadow": "rgba(236, 72, 153, 0.2)",
                                "result_bg": "rgba(236, 72, 153, 0.12)",
                                "result_border": "rgba(236, 72, 153, 0.4)"
                            },
                            "Web3 Gaming Mobile App - Rewards Marketplace",
                            "/projects"
                        ),
                        width="100%",
                        max_width="1100px",
                        margin_x="auto",
                        margin_bottom="2rem"
                    ),

                    # Row 5 (Card 5) - Web3 Gaming & Crypto Platform (700k users migration)
                    rx.box(
                        achievement_card(
                            State.achievement5_problem,
                            State.achievement5_solution,
                            State.achievement5_result,
                            {
                                "icon": "orange.300",
                                "label": "orange.400",
                                "bg": "rgba(249, 115, 22, 0.05)",
                                "border": "rgba(249, 115, 22, 0.2)",
                                "hover_bg": "rgba(249, 115, 22, 0.08)",
                                "hover_border": "rgba(249, 115, 22, 0.4)",
                                "shadow": "rgba(249, 115, 22, 0.2)",
                                "result_bg": "rgba(249, 115, 22, 0.12)",
                                "result_border": "rgba(249, 115, 22, 0.4)"
                            },
                            "Web3 Gaming & Crypto Platform",
                            "/projects"
                        ),
                        width="100%",
                        max_width="1100px",
                        margin_x="auto",
                        margin_bottom="2rem"
                    ),

                    # Row 6 (Card 6) - Vibe-coded project quality rescue
                    rx.box(
                        achievement_card(
                            State.achievement6_problem,
                            State.achievement6_solution,
                            State.achievement6_result,
                            {
                                "icon": "green.300",
                                "label": "green.400",
                                "bg": "rgba(34, 197, 94, 0.05)",
                                "border": "rgba(34, 197, 94, 0.2)",
                                "hover_bg": "rgba(34, 197, 94, 0.08)",
                                "hover_border": "rgba(34, 197, 94, 0.4)",
                                "shadow": "rgba(34, 197, 94, 0.2)",
                                "result_bg": "rgba(34, 197, 94, 0.12)",
                                "result_border": "rgba(34, 197, 94, 0.4)"
                            },
                            "AI Research Analysis Platform (RAG)",
                            "/projects",
                        ),
                        width="100%",
                        max_width="1100px",
                        margin_x="auto",
                        margin_bottom="2rem"
                    ),

                    padding="2rem",
                    margin_bottom="3rem",
                    max_width="1200px",
                    margin_x="auto",
                    width="100%"
                ),

                # CTA Section
                rx.box(
                    rx.vstack(
                        rx.text(
                            State.case_studies_cta,
                            color="gray.300",
                            text_align="center",
                            font_size="1.2rem",
                            font_weight="600",
                            margin_bottom="1.5rem"
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("mail", size=20),
                                    rx.text("Get in Touch", font_weight="600"),
                                    spacing="2",
                                    align="center"
                                ),
                                size="3",
                                style={
                                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                    "color": "white",
                                    "padding": "1rem 2rem",
                                    "borderRadius": "full",
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "transform": "translateY(-2px)",
                                        "boxShadow": "0 8px 24px rgba(0, 212, 255, 0.3)"
                                    }
                                }
                            ),
                            href="/#contact"
                        ),
                        spacing="3",
                        align="center"
                    ),
                    padding="3rem 2rem",
                    border_radius="xl",
                    max_width="800px",
                    margin_x="auto",
                    margin_bottom="3rem",
                    style={
                        "background": "rgba(15, 23, 42, 0.5)",
                        "border": "1px solid rgba(100, 116, 139, 0.2)",
                        "backdropFilter": "blur(10px)"
                    }
                ),

                width="100%",
                padding="2rem",
                align="center"
            ),

            # Content styling
            padding="2rem 0",
            flex="1"
        ),

        footer_component,
        align="stretch",
        spacing="0",
        width="100%",
        min_height="100vh",
        style={
            "display": "flex",
            "flexDirection": "column",
            "background": "linear-gradient(180deg, #0a0e1a 0%, #0f1729 50%, #0a0e1a 100%)"
        }
    )

    return rx.fragment(
        # page_transition_loader(),  # Temporarily disabled
        floating_language_button(),
        rx.box(
            animated_background(),
            layout,
            position="relative",
            width="100%"
        ),
        rx.html(f"<style>{animations_css}</style>")
    )
