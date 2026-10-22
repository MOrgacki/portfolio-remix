import reflex as rx
from portfolio.header import Header
from portfolio.footer import Footer
from portfolio.sidebar import sidebar
from portfolio.animations import animated_background, animations_css
from portfolio.loader import page_transition_loader
from portfolio.floating_button import floating_language_button
from portfolio.main import contact_section
from state import State


@rx.page(route="/experience", title="Marcin Orgacki | Experience")
def experience_page() -> rx.Component:
    """Experience page component with tech stack and expertise"""
    header = Header()
    footer = Footer()
    header_component = header.build()
    footer_component = footer.build()
    sidebar_component = sidebar()

    # Layout without sidebar - same as main page
    layout = rx.vstack(
        header_component,
        rx.box(
            # Main heading
            rx.vstack(
                rx.heading(
                    State.exp_title,
                    size="9",
                    text_align="center",
                    margin_bottom="0.5rem",
                    font_weight="900",
                    line_height="1.2",
                    padding_y="0.5rem",
                    style={
                        "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 50%, #8b5cf6 100%)",
                        "backgroundClip": "text",
                        "WebkitBackgroundClip": "text",
                        "color": "transparent",
                        "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                        "letterSpacing": "-0.05em",
                        "animation": "slideInUp 0.8s ease-out",
                        "position": "relative",
                        "zIndex": "10",
                        "overflow": "visible"
                    }
                ),
                rx.text(
                    State.exp_subtitle,
                    color="gray.300",
                    text_align="center",
                    font_size="1.2rem",
                    font_weight="600",
                    margin_bottom="1rem",
                    max_width="800px",
                    margin_x="auto",
                    line_height="1.4"
                ),
                rx.text(
                    State.exp_description,
                    color="gray.400",
                    text_align="center",
                    font_size="1rem",
                    margin_bottom="2rem",
                    max_width="750px",
                    margin_x="auto",
                    line_height="1.7"
                ),

                # Services section
                rx.box(
                    rx.vstack(
                        rx.heading(
                            State.services_title,
                            size="7",
                            text_align="center",
                            margin_bottom="2rem",
                            font_weight="800",
                            line_height="1.2",
                            style={
                                "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 50%, #8b5cf6 100%)",
                                "backgroundClip": "text",
                                "WebkitBackgroundClip": "text",
                                "color": "transparent",
                                "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                                "letterSpacing": "-0.05em"
                            }
                        ),

                        rx.flex(
                            # Manual & Automated Testing
                            rx.box(
                                rx.vstack(
                                    rx.icon("bug", size=32, color="cyan.300", margin_bottom="0.5rem"),
                                    rx.heading(State.service_testing_title, size="3", color="white", text_align="center", margin_bottom="0.5rem", min_height="3rem"),
                                    rx.text(
                                        State.service_testing_desc,
                                        color="gray.400",
                                        font_size="0.85rem",
                                        text_align="center",
                                        line_height="1.6"
                                    ),
                                    spacing="2",
                                    align="center"
                                ),
                                padding="1.5rem",
                                border_radius="lg",
                                flex="1 1 calc(33.333% - 1rem)",
                                min_width="280px",
                                max_width="400px",
                                style={
                                    "background": "rgba(0, 212, 255, 0.05)",
                                    "border": "1px solid rgba(0, 212, 255, 0.2)",
                                    "backdropFilter": "blur(10px)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(0, 212, 255, 0.08)",
                                        "borderColor": "rgba(0, 212, 255, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            ),

                            # Business Process Automation
                            rx.box(
                                rx.vstack(
                                    rx.icon("workflow", size=32, color="blue.300", margin_bottom="0.5rem"),
                                    rx.heading(State.service_automation_title, size="3", color="white", text_align="center", margin_bottom="0.5rem", min_height="3rem"),
                                    rx.text(
                                        State.service_automation_desc,
                                        color="gray.400",
                                        font_size="0.85rem",
                                        text_align="center",
                                        line_height="1.6"
                                    ),
                                    spacing="2",
                                    align="center"
                                ),
                                padding="1.5rem",
                                border_radius="lg",
                                flex="1 1 calc(33.333% - 1rem)",
                                min_width="280px",
                                max_width="400px",
                                style={
                                    "background": "rgba(91, 115, 255, 0.05)",
                                    "border": "1px solid rgba(91, 115, 255, 0.2)",
                                    "backdropFilter": "blur(10px)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(91, 115, 255, 0.08)",
                                        "borderColor": "rgba(91, 115, 255, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            ),

                            # Custom AI Agents
                            rx.box(
                                rx.vstack(
                                    rx.icon("bot", size=32, color="purple.300", margin_bottom="0.5rem"),
                                    rx.heading(State.service_ai_title, size="3", color="white", text_align="center", margin_bottom="0.5rem", min_height="3rem"),
                                    rx.text(
                                        State.service_ai_desc,
                                        color="gray.400",
                                        font_size="0.85rem",
                                        text_align="center",
                                        line_height="1.6"
                                    ),
                                    spacing="2",
                                    align="center"
                                ),
                                padding="1.5rem",
                                border_radius="lg",
                                flex="1 1 calc(33.333% - 1rem)",
                                min_width="280px",
                                max_width="400px",
                                style={
                                    "background": "rgba(139, 92, 246, 0.05)",
                                    "border": "1px solid rgba(139, 92, 246, 0.2)",
                                    "backdropFilter": "blur(10px)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(139, 92, 246, 0.08)",
                                        "borderColor": "rgba(139, 92, 246, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            ),

                            # Testing Strategy & QA Management
                            rx.box(
                                rx.vstack(
                                    rx.icon("clipboard-list", size=32, color="pink.300", margin_bottom="0.5rem"),
                                    rx.heading(State.service_strategy_title, size="3", color="white", text_align="center", margin_bottom="0.5rem", min_height="3rem"),
                                    rx.text(
                                        State.service_strategy_desc,
                                        color="gray.400",
                                        font_size="0.85rem",
                                        text_align="center",
                                        line_height="1.6"
                                    ),
                                    spacing="2",
                                    align="center"
                                ),
                                padding="1.5rem",
                                border_radius="lg",
                                flex="1 1 calc(33.333% - 1rem)",
                                min_width="280px",
                                max_width="400px",
                                style={
                                    "background": "rgba(236, 72, 153, 0.05)",
                                    "border": "1px solid rgba(236, 72, 153, 0.2)",
                                    "backdropFilter": "blur(10px)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(236, 72, 153, 0.08)",
                                        "borderColor": "rgba(236, 72, 153, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            ),

                            # Business Relations & Stakeholder Management
                            rx.box(
                                rx.vstack(
                                    rx.icon("users", size=32, color="orange.300", margin_bottom="0.5rem"),
                                    rx.heading(State.service_relations_title, size="3", color="white", text_align="center", margin_bottom="0.5rem", min_height="3rem"),
                                    rx.text(
                                        State.service_relations_desc,
                                        color="gray.400",
                                        font_size="0.85rem",
                                        text_align="center",
                                        line_height="1.6"
                                    ),
                                    spacing="2",
                                    align="center"
                                ),
                                padding="1.5rem",
                                border_radius="lg",
                                flex="1 1 calc(33.333% - 1rem)",
                                min_width="280px",
                                max_width="400px",
                                style={
                                    "background": "rgba(249, 115, 22, 0.05)",
                                    "border": "1px solid rgba(249, 115, 22, 0.2)",
                                    "backdropFilter": "blur(10px)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(249, 115, 22, 0.08)",
                                        "borderColor": "rgba(249, 115, 22, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            ),

                            # Security, Infrastructure & Performance Testing
                            rx.box(
                                rx.vstack(
                                    rx.icon("shield", size=32, color="green.300", margin_bottom="0.5rem"),
                                    rx.heading(State.service_security_title, size="3", color="white", text_align="center", margin_bottom="0.5rem", min_height="3rem"),
                                    rx.text(
                                        State.service_security_desc,
                                        color="gray.400",
                                        font_size="0.85rem",
                                        text_align="center",
                                        line_height="1.6"
                                    ),
                                    spacing="2",
                                    align="center"
                                ),
                                padding="1.5rem",
                                border_radius="lg",
                                flex="1 1 calc(33.333% - 1rem)",
                                min_width="280px",
                                max_width="400px",
                                style={
                                    "background": "rgba(34, 197, 94, 0.05)",
                                    "border": "1px solid rgba(34, 197, 94, 0.2)",
                                    "backdropFilter": "blur(10px)",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "rgba(34, 197, 94, 0.08)",
                                        "borderColor": "rgba(34, 197, 94, 0.4)",
                                        "transform": "translateX(4px)"
                                    }
                                }
                            ),

                            gap="1.5rem",
                            wrap="wrap",
                            justify="center",
                            width="100%"
                        ),

                        spacing="3",
                        align="center",
                        width="100%"
                    ),
                    padding="2rem",
                    border_radius="xl",
                    margin_bottom="3rem",
                    max_width="1400px",
                    margin_x="auto",
                    style={
                        "background": "rgba(15, 23, 42, 0.5)",
                        "border": "1px solid rgba(100, 116, 139, 0.2)",
                        "backdropFilter": "blur(10px)"
                    }
                ),

                # Tech Stack & Languages section (side by side)
                rx.flex(
                    # Tech stack (left side)
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                State.exp_tech_stack,
                                size="6",
                                text_align="center",
                                margin_bottom="1.5rem",
                                font_weight="800",
                                line_height="1.2",
                                style={
                                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                    "backgroundClip": "text",
                                    "WebkitBackgroundClip": "text",
                                    "color": "transparent",
                                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                                    "letterSpacing": "-0.05em"
                                }
                            ),

                        # Programming Languages
                        rx.vstack(
                            rx.text(
                                "Programming Languages",
                                color="gray.300",
                                font_weight="600",
                                font_size="0.9rem",
                                text_align="center"
                            ),
                            rx.flex(
                                *[rx.badge(tech, style={
                                    "background": "rgba(0, 212, 255, 0.1)",
                                    "color": "cyan.300",
                                    "border": "1px solid rgba(0, 212, 255, 0.3)",
                                    "padding": "0.4rem 0.8rem",
                                    "fontSize": "0.8rem",
                                    "fontWeight": "500"
                                }) for tech in ["JavaScript", "Python", "Bash"]],
                                gap="10px",
                                wrap="wrap",
                                justify="start",
                                width="100%"
                            ),
                            spacing="2",
                            margin_bottom="1.5rem",
                            width="100%"
                        ),

                        # Testing Tools
                        rx.vstack(
                            rx.text(
                                "Testing Tools",
                                color="gray.300",
                                font_weight="600",
                                font_size="0.9rem",
                                text_align="center"
                            ),
                            rx.flex(
                                *[rx.badge(tech, style={
                                    "background": "rgba(91, 115, 255, 0.1)",
                                    "color": "blue.300",
                                    "border": "1px solid rgba(91, 115, 255, 0.3)",
                                    "padding": "0.4rem 0.8rem",
                                    "fontSize": "0.8rem",
                                    "fontWeight": "500"
                                }) for tech in ["Cypress", "Playwright", "Postman", "TestRail", "Swagger", "Fiddler", "OWASP ZAP", "Selenium", "Device Emulators", "LambdaTest", "DevTools", "Mockoon", "VMs", "Locust", "WireShark"]],
                                gap="10px",
                                wrap="wrap",
                                justify="start",
                                width="100%"
                            ),
                            spacing="2",
                            margin_bottom="1.5rem",
                            width="100%"
                        ),

                        # Databases
                        rx.vstack(
                            rx.text(
                                "Databases",
                                color="gray.300",
                                font_weight="600",
                                font_size="0.9rem",
                                text_align="center"
                            ),
                            rx.flex(
                                *[rx.badge(tech, style={
                                    "background": "rgba(139, 92, 246, 0.1)",
                                    "color": "purple.300",
                                    "border": "1px solid rgba(139, 92, 246, 0.3)",
                                    "padding": "0.4rem 0.8rem",
                                    "fontSize": "0.8rem",
                                    "fontWeight": "500"
                                }) for tech in ["SQL", "NoSQL", "PostgreSQL", "MongoDB", "TimescaleDB", "MariaDB", "Redis", "MySQL"]],
                                gap="10px",
                                wrap="wrap",
                                justify="start",
                                width="100%"
                            ),
                            spacing="2",
                            margin_bottom="1.5rem",
                            width="100%"
                        ),

                        # Technologies
                        rx.vstack(
                            rx.text(
                                "Technologies",
                                color="gray.300",
                                font_weight="600",
                                font_size="0.9rem",
                                text_align="center"
                            ),
                            rx.flex(
                                *[rx.badge(tech, style={
                                    "background": "rgba(236, 72, 153, 0.1)",
                                    "color": "pink.300",
                                    "border": "1px solid rgba(236, 72, 153, 0.3)",
                                    "padding": "0.4rem 0.8rem",
                                    "fontSize": "0.8rem",
                                    "fontWeight": "500"
                                }) for tech in ["Node.js", "Laravel", "Symfony", ".NET Core", "Angular", "Vue.js", "React", "Jenkins", "AWS", "GitHub", "Flutter", "Soketi", "Django", "Flask", "GitLab", "React Native", "iOS", "Android"]],
                                gap="10px",
                                wrap="wrap",
                                justify="start",
                                width="100%"
                            ),
                            spacing="2",
                            margin_bottom="1.5rem",
                            width="100%"
                        ),

                        # Others
                        rx.vstack(
                            rx.text(
                                "Others",
                                color="gray.300",
                                font_weight="600",
                                font_size="0.9rem",
                                text_align="center"
                            ),
                            rx.flex(
                                *[rx.badge(tech, style={
                                    "background": "rgba(251, 191, 36, 0.1)",
                                    "color": "orange.300",
                                    "border": "1px solid rgba(251, 191, 36, 0.3)",
                                    "padding": "0.4rem 0.8rem",
                                    "fontSize": "0.8rem",
                                    "fontWeight": "500"
                                }) for tech in ["CI/CD", "Docker", "Jira", "ElasticSearch", "Linux", "GIT", "Agile", "Sentry", "Windows", "macOS"]],
                                gap="10px",
                                wrap="wrap",
                                justify="start",
                                width="100%"
                            ),
                            spacing="2",
                            width="100%"
                        ),

                            spacing="3",
                            align="center",
                            width="100%"
                        ),
                        padding="2rem",
                        border_radius="xl",
                        flex="1",
                        style={
                            "background": "rgba(15, 23, 42, 0.5)",
                            "border": "1px solid rgba(100, 116, 139, 0.2)",
                            "backdropFilter": "blur(10px)"
                        }
                    ),

                    # Languages (right side)
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                State.exp_languages,
                                size="6",
                                text_align="center",
                                margin_bottom="1.5rem",
                                font_weight="800",
                                line_height="1.2",
                                style={
                                    "background": "linear-gradient(135deg, #22c55e 0%, #10b981 50%, #14b8a6 100%)",
                                    "backgroundClip": "text",
                                    "WebkitBackgroundClip": "text",
                                    "color": "transparent",
                                    "textShadow": "0 0 30px rgba(34, 197, 94, 0.3)",
                                    "letterSpacing": "-0.05em"
                                }
                            ),

                            rx.vstack(
                                # English
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("en", font_size="1.5rem", font_weight="700", color="gray.500", text_transform="lowercase"),
                                        rx.text(
                                            State.lang_english,
                                            color="white",
                                            font_weight="600",
                                            font_size="1rem",
                                            flex="1"
                                        ),
                                        rx.text(
                                            rx.cond(
                                                State.language == "en",
                                                f"{State.lang_level_upper_intermediate} (B2+)",
                                                f"{State.lang_level_upper_intermediate} (B2+)"
                                            ),
                                            color="cyan.300",
                                            font_weight="600",
                                            font_size="0.9rem"
                                        ),
                                        width="100%",
                                        align="center",
                                        spacing="3",
                                        margin_bottom="0.75rem"
                                    ),
                                    rx.box(
                                        rx.box(
                                            width="75%",
                                            height="100%",
                                            style={
                                                "background": "linear-gradient(90deg, rgba(0, 212, 255, 0.8), rgba(91, 115, 255, 0.6))",
                                                "borderRadius": "8px",
                                                "transition": "width 1s ease-out"
                                            }
                                        ),
                                        width="100%",
                                        height="12px",
                                        border_radius="8px",
                                        style={
                                            "background": "rgba(30, 41, 59, 0.6)",
                                            "overflow": "hidden"
                                        }
                                    ),
                                    width="100%",
                                    spacing="2"
                                ),

                                # Polish
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("pl", font_size="1.5rem", font_weight="700", color="gray.500", text_transform="lowercase"),
                                        rx.text(
                                            State.lang_polish,
                                            color="white",
                                            font_weight="600",
                                            font_size="1rem",
                                            flex="1"
                                        ),
                                        rx.text(
                                            rx.cond(
                                                State.language == "en",
                                                f"{State.lang_level_native} (C2)",
                                                f"{State.lang_level_native} (C2)"
                                            ),
                                            color="green.300",
                                            font_weight="600",
                                            font_size="0.9rem"
                                        ),
                                        width="100%",
                                        align="center",
                                        spacing="3",
                                        margin_bottom="0.75rem"
                                    ),
                                    rx.box(
                                        rx.box(
                                            width="100%",
                                            height="100%",
                                            style={
                                                "background": "linear-gradient(90deg, rgba(34, 197, 94, 0.8), rgba(0, 212, 255, 0.6))",
                                                "borderRadius": "8px",
                                                "transition": "width 1s ease-out"
                                            }
                                        ),
                                        width="100%",
                                        height="12px",
                                        border_radius="8px",
                                        style={
                                            "background": "rgba(30, 41, 59, 0.6)",
                                            "overflow": "hidden"
                                        }
                                    ),
                                    width="100%",
                                    spacing="2"
                                ),

                                # German
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("de", font_size="1.5rem", font_weight="700", color="gray.500", text_transform="lowercase"),
                                        rx.text(
                                            State.lang_german,
                                            color="white",
                                            font_weight="600",
                                            font_size="1rem",
                                            flex="1"
                                        ),
                                        rx.text(
                                            rx.cond(
                                                State.language == "en",
                                                f"{State.lang_level_beginner} (A1)",
                                                f"{State.lang_level_beginner} (A1)"
                                            ),
                                            color="orange.300",
                                            font_weight="600",
                                            font_size="0.9rem"
                                        ),
                                        width="100%",
                                        align="center",
                                        spacing="3",
                                        margin_bottom="0.75rem"
                                    ),
                                    rx.box(
                                        rx.box(
                                            width="15%",
                                            height="100%",
                                            style={
                                                "background": "linear-gradient(90deg, rgba(249, 115, 22, 0.8), rgba(251, 191, 36, 0.6))",
                                                "borderRadius": "8px",
                                                "transition": "width 1s ease-out"
                                            }
                                        ),
                                        width="100%",
                                        height="12px",
                                        border_radius="8px",
                                        style={
                                            "background": "rgba(30, 41, 59, 0.6)",
                                            "overflow": "hidden"
                                        }
                                    ),
                                    width="100%",
                                    spacing="2"
                                ),

                                spacing="6",
                                width="100%"
                            ),

                            # Divider
                            rx.divider(border_color="rgba(100, 116, 139, 0.3)", margin_y="2rem"),

                            # Certificates section
                            rx.vstack(
                                rx.heading(
                                    State.exp_certificates,
                                    size="5",
                                    text_align="center",
                                    margin_bottom="1.5rem",
                                    font_weight="700",
                                    line_height="1.2",
                                    style={
                                        "background": "linear-gradient(135deg, #8b5cf6 0%, #a855f7 50%, #c026d3 100%)",
                                        "backgroundClip": "text",
                                        "WebkitBackgroundClip": "text",
                                        "color": "transparent",
                                        "textShadow": "0 0 30px rgba(139, 92, 246, 0.3)",
                                        "letterSpacing": "-0.05em"
                                    }
                                ),

                                rx.vstack(
                                    # Certificate 1
                                    rx.hstack(
                                        rx.box(
                                            rx.icon("award", size=20, color="purple.300"),
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            width="40px",
                                            height="40px",
                                            border_radius="50%",
                                            style={
                                                "background": "rgba(139, 92, 246, 0.1)",
                                                "border": "2px solid rgba(139, 92, 246, 0.3)"
                                            }
                                        ),
                                        rx.text(
                                            "ISTQB® Foundation Level",
                                            color="gray.300",
                                            font_size="0.9rem",
                                            font_weight="500",
                                            flex="1"
                                        ),
                                        align="center",
                                        spacing="3",
                                        width="100%",
                                        padding="0.75rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(139, 92, 246, 0.05)",
                                            "border": "1px solid rgba(139, 92, 246, 0.15)",
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": "rgba(139, 92, 246, 0.08)",
                                                "borderColor": "rgba(139, 92, 246, 0.3)"
                                            }
                                        }
                                    ),

                                    # Certificate 2
                                    rx.hstack(
                                        rx.box(
                                            rx.icon("award", size=20, color="blue.300"),
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            width="40px",
                                            height="40px",
                                            border_radius="50%",
                                            style={
                                                "background": "rgba(91, 115, 255, 0.1)",
                                                "border": "2px solid rgba(91, 115, 255, 0.3)"
                                            }
                                        ),
                                        rx.text(
                                            "EF SET English Certificate 67/100 (C1)",
                                            color="gray.300",
                                            font_size="0.9rem",
                                            font_weight="500",
                                            flex="1"
                                        ),
                                        align="center",
                                        spacing="3",
                                        width="100%",
                                        padding="0.75rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(91, 115, 255, 0.05)",
                                            "border": "1px solid rgba(91, 115, 255, 0.15)",
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": "rgba(91, 115, 255, 0.08)",
                                                "borderColor": "rgba(91, 115, 255, 0.3)"
                                            }
                                        }
                                    ),

                                    # Certificate 3
                                    rx.hstack(
                                        rx.box(
                                            rx.icon("award", size=20, color="cyan.300"),
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            width="40px",
                                            height="40px",
                                            border_radius="50%",
                                            style={
                                                "background": "rgba(0, 212, 255, 0.1)",
                                                "border": "2px solid rgba(0, 212, 255, 0.3)"
                                            }
                                        ),
                                        rx.text(
                                            "CCNA Discovery: Small Businesses",
                                            color="gray.300",
                                            font_size="0.9rem",
                                            font_weight="500",
                                            flex="1"
                                        ),
                                        align="center",
                                        spacing="3",
                                        width="100%",
                                        padding="0.75rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(0, 212, 255, 0.05)",
                                            "border": "1px solid rgba(0, 212, 255, 0.15)",
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": "rgba(0, 212, 255, 0.08)",
                                                "borderColor": "rgba(0, 212, 255, 0.3)"
                                            }
                                        }
                                    ),

                                    # Certificate 4
                                    rx.hstack(
                                        rx.box(
                                            rx.icon("award", size=20, color="pink.300"),
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            width="40px",
                                            height="40px",
                                            border_radius="50%",
                                            style={
                                                "background": "rgba(236, 72, 153, 0.1)",
                                                "border": "2px solid rgba(236, 72, 153, 0.3)"
                                            }
                                        ),
                                        rx.text(
                                            "AgilePM® Foundation",
                                            color="gray.300",
                                            font_size="0.9rem",
                                            font_weight="500",
                                            flex="1"
                                        ),
                                        align="center",
                                        spacing="3",
                                        width="100%",
                                        padding="0.75rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(236, 72, 153, 0.05)",
                                            "border": "1px solid rgba(236, 72, 153, 0.15)",
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": "rgba(236, 72, 153, 0.08)",
                                                "borderColor": "rgba(236, 72, 153, 0.3)"
                                            }
                                        }
                                    ),

                                    spacing="3",
                                    width="100%"
                                ),

                                spacing="2",
                                width="100%"
                            ),

                            spacing="3",
                            align="center",
                            width="100%"
                        ),
                        padding="2rem",
                        border_radius="xl",
                        flex="1",
                        style={
                            "background": "rgba(15, 23, 42, 0.5)",
                            "border": "1px solid rgba(100, 116, 139, 0.2)",
                            "backdropFilter": "blur(10px)"
                        }
                    ),

                    gap="2rem",
                    wrap="wrap",
                    justify="center",
                    width="100%",
                    max_width="1400px",
                    margin_x="auto",
                    margin_bottom="3rem"
                ),

                # Timeline section
                rx.box(
                    rx.vstack(
                        rx.heading(
                            State.timeline_title,
                            size="7",
                            text_align="center",
                            margin_bottom="3rem",
                            font_weight="800",
                            line_height="1.2",
                            style={
                                "background": "linear-gradient(135deg, #ec4899 0%, #f43f5e 50%, #fb923c 100%)",
                                "backgroundClip": "text",
                                "WebkitBackgroundClip": "text",
                                "color": "transparent",
                                "textShadow": "0 0 30px rgba(236, 72, 153, 0.3)",
                                "letterSpacing": "-0.05em"
                            }
                        ),

                        # Horizontal timeline - Desktop
                        rx.tablet_and_desktop(
                            rx.box(
                                # Timeline container
                                rx.hstack(
                                    # Step 1
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("school", size=36, color="cyan.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1.5rem",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            style={
                                                "background": "rgba(0, 212, 255, 0.15)",
                                                "border": "3px solid rgba(0, 212, 255, 0.5)",
                                                "boxShadow": "0 0 25px rgba(0, 212, 255, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step1, font_weight="600", color="white", text_align="center", margin_top="1rem"),
                                        rx.text(State.timeline_step1_desc, font_size="0.85rem", color="gray.400", text_align="center", max_width="150px"),
                                        align="center",
                                        spacing="2",
                                        flex="1"
                                    ),

                                    # Connector line
                                    rx.box(height="3px", flex="1", background="linear-gradient(90deg, rgba(0, 212, 255, 0.4), rgba(91, 115, 255, 0.4))", margin_x="1rem"),

                                    # Step 2
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("code", size=36, color="blue.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1.5rem",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            style={
                                                "background": "rgba(91, 115, 255, 0.15)",
                                                "border": "3px solid rgba(91, 115, 255, 0.5)",
                                                "boxShadow": "0 0 25px rgba(91, 115, 255, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step2, font_weight="600", color="white", text_align="center", margin_top="1rem"),
                                        rx.text(State.timeline_step2_desc, font_size="0.85rem", color="gray.400", text_align="center", max_width="150px"),
                                        align="center",
                                        spacing="2",
                                        flex="1"
                                    ),

                                    # Connector line
                                    rx.box(height="3px", flex="1", background="linear-gradient(90deg, rgba(91, 115, 255, 0.4), rgba(139, 92, 246, 0.4))", margin_x="1rem"),

                                    # Step 3
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("lightbulb", size=36, color="purple.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1.5rem",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            style={
                                                "background": "rgba(139, 92, 246, 0.15)",
                                                "border": "3px solid rgba(139, 92, 246, 0.5)",
                                                "boxShadow": "0 0 25px rgba(139, 92, 246, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step3, font_weight="600", color="white", text_align="center", margin_top="1rem"),
                                        rx.text(State.timeline_step3_desc, font_size="0.85rem", color="gray.400", text_align="center", max_width="150px"),
                                        align="center",
                                        spacing="2",
                                        flex="1"
                                    ),

                                    # Connector line
                                    rx.box(height="3px", flex="1", background="linear-gradient(90deg, rgba(139, 92, 246, 0.4), rgba(236, 72, 153, 0.4))", margin_x="1rem"),

                                    # Step 4
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("briefcase-business", size=36, color="pink.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1.5rem",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            style={
                                                "background": "rgba(236, 72, 153, 0.15)",
                                                "border": "3px solid rgba(236, 72, 153, 0.5)",
                                                "boxShadow": "0 0 25px rgba(236, 72, 153, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step4, font_weight="600", color="white", text_align="center", margin_top="1rem"),
                                        rx.text(State.timeline_step4_desc, font_size="0.85rem", color="gray.400", text_align="center", max_width="150px"),
                                        align="center",
                                        spacing="2",
                                        flex="1"
                                    ),

                                    # Connector line
                                    rx.box(height="3px", flex="1", background="linear-gradient(90deg, rgba(236, 72, 153, 0.4), rgba(249, 115, 22, 0.4))", margin_x="1rem"),

                                    # Step 5
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("trophy", size=36, color="orange.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1.5rem",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            style={
                                                "background": "rgba(249, 115, 22, 0.15)",
                                                "border": "3px solid rgba(249, 115, 22, 0.5)",
                                                "boxShadow": "0 0 25px rgba(249, 115, 22, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step5, font_weight="600", color="white", text_align="center", margin_top="1rem"),
                                        rx.text(State.timeline_step5_desc, font_size="0.85rem", color="gray.400", text_align="center", max_width="150px"),
                                        align="center",
                                        spacing="2",
                                        flex="1"
                                    ),

                                    # Connector line
                                    rx.box(height="3px", flex="1", background="linear-gradient(90deg, rgba(249, 115, 22, 0.4), rgba(34, 197, 94, 0.4))", margin_x="1rem"),

                                    # Step 6
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("sparkles", size=36, color="green.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1.5rem",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            style={
                                                "background": "rgba(34, 197, 94, 0.15)",
                                                "border": "3px solid rgba(34, 197, 94, 0.5)",
                                                "boxShadow": "0 0 25px rgba(34, 197, 94, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step6, font_weight="600", color="white", text_align="center", margin_top="1rem"),
                                        rx.text(State.timeline_step6_desc, font_size="0.85rem", color="gray.400", text_align="center", max_width="150px"),
                                        align="center",
                                        spacing="2",
                                        flex="1"
                                    ),

                                    align="center",
                                    width="100%",
                                    justify="between"
                                ),
                                width="100%",
                                max_width="1400px",
                                margin_x="auto",
                                padding="2rem"
                            )
                        ),

                        # Horizontal scrollable timeline - Mobile
                        rx.mobile_only(
                            rx.box(
                                rx.hstack(
                                    # Step 1
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("school", size=28, color="cyan.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1rem",
                                            min_width="60px",
                                            min_height="60px",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            margin_bottom="1rem",
                                            style={
                                                "background": "rgba(0, 212, 255, 0.15)",
                                                "border": "2px solid rgba(0, 212, 255, 0.5)",
                                                "boxShadow": "0 0 25px rgba(0, 212, 255, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step1, font_weight="700", color="white", font_size="0.9rem", text_align="center"),
                                        rx.text(State.timeline_step1_desc, font_size="0.75rem", color="gray.400", line_height="1.4", text_align="center"),
                                        align="center",
                                        spacing="2",
                                        min_width="220px",
                                        max_width="220px",
                                        padding="1rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(15, 23, 42, 0.4)",
                                            "border": "1px solid rgba(0, 212, 255, 0.2)"
                                        }
                                    ),

                                    # Horizontal connector
                                    rx.box(
                                        width="40px",
                                        height="2px",
                                        background="linear-gradient(90deg, rgba(0, 212, 255, 0.4), rgba(91, 115, 255, 0.4))",
                                        flex_shrink="0"
                                    ),

                                    # Step 2
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("code", size=28, color="blue.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1rem",
                                            min_width="60px",
                                            min_height="60px",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            margin_bottom="1rem",
                                            style={
                                                "background": "rgba(91, 115, 255, 0.15)",
                                                "border": "2px solid rgba(91, 115, 255, 0.5)",
                                                "boxShadow": "0 0 25px rgba(91, 115, 255, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step2, font_weight="700", color="white", font_size="0.9rem", text_align="center"),
                                        rx.text(State.timeline_step2_desc, font_size="0.75rem", color="gray.400", line_height="1.4", text_align="center"),
                                        align="center",
                                        spacing="2",
                                        min_width="220px",
                                        max_width="220px",
                                        padding="1rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(15, 23, 42, 0.4)",
                                            "border": "1px solid rgba(91, 115, 255, 0.2)"
                                        }
                                    ),

                                    # Horizontal connector
                                    rx.box(
                                        width="40px",
                                        height="2px",
                                        background="linear-gradient(90deg, rgba(91, 115, 255, 0.4), rgba(139, 92, 246, 0.4))",
                                        flex_shrink="0"
                                    ),

                                    # Step 3
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("lightbulb", size=28, color="purple.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1rem",
                                            min_width="60px",
                                            min_height="60px",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            margin_bottom="1rem",
                                            style={
                                                "background": "rgba(139, 92, 246, 0.15)",
                                                "border": "2px solid rgba(139, 92, 246, 0.5)",
                                                "boxShadow": "0 0 25px rgba(139, 92, 246, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step3, font_weight="700", color="white", font_size="0.9rem", text_align="center"),
                                        rx.text(State.timeline_step3_desc, font_size="0.75rem", color="gray.400", line_height="1.4", text_align="center"),
                                        align="center",
                                        spacing="2",
                                        min_width="220px",
                                        max_width="220px",
                                        padding="1rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(15, 23, 42, 0.4)",
                                            "border": "1px solid rgba(139, 92, 246, 0.2)"
                                        }
                                    ),

                                    # Horizontal connector
                                    rx.box(
                                        width="40px",
                                        height="2px",
                                        background="linear-gradient(90deg, rgba(139, 92, 246, 0.4), rgba(236, 72, 153, 0.4))",
                                        flex_shrink="0"
                                    ),

                                    # Step 4
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("briefcase-business", size=28, color="pink.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1rem",
                                            min_width="60px",
                                            min_height="60px",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            margin_bottom="1rem",
                                            style={
                                                "background": "rgba(236, 72, 153, 0.15)",
                                                "border": "2px solid rgba(236, 72, 153, 0.5)",
                                                "boxShadow": "0 0 25px rgba(236, 72, 153, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step4, font_weight="700", color="white", font_size="0.9rem", text_align="center"),
                                        rx.text(State.timeline_step4_desc, font_size="0.75rem", color="gray.400", line_height="1.4", text_align="center"),
                                        align="center",
                                        spacing="2",
                                        min_width="220px",
                                        max_width="220px",
                                        padding="1rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(15, 23, 42, 0.4)",
                                            "border": "1px solid rgba(236, 72, 153, 0.2)"
                                        }
                                    ),

                                    # Horizontal connector
                                    rx.box(
                                        width="40px",
                                        height="2px",
                                        background="linear-gradient(90deg, rgba(236, 72, 153, 0.4), rgba(249, 115, 22, 0.4))",
                                        flex_shrink="0"
                                    ),

                                    # Step 5
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("trophy", size=28, color="orange.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1rem",
                                            min_width="60px",
                                            min_height="60px",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            margin_bottom="1rem",
                                            style={
                                                "background": "rgba(249, 115, 22, 0.15)",
                                                "border": "2px solid rgba(249, 115, 22, 0.5)",
                                                "boxShadow": "0 0 25px rgba(249, 115, 22, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step5, font_weight="700", color="white", font_size="0.9rem", text_align="center"),
                                        rx.text(State.timeline_step5_desc, font_size="0.75rem", color="gray.400", line_height="1.4", text_align="center"),
                                        align="center",
                                        spacing="2",
                                        min_width="220px",
                                        max_width="220px",
                                        padding="1rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(15, 23, 42, 0.4)",
                                            "border": "1px solid rgba(249, 115, 22, 0.2)"
                                        }
                                    ),

                                    # Horizontal connector
                                    rx.box(
                                        width="40px",
                                        height="2px",
                                        background="linear-gradient(90deg, rgba(249, 115, 22, 0.4), rgba(34, 197, 94, 0.4))",
                                        flex_shrink="0"
                                    ),

                                    # Step 6
                                    rx.vstack(
                                        rx.box(
                                            rx.icon("sparkles", size=28, color="green.300", stroke_width=2),
                                            border_radius="50%",
                                            padding="1rem",
                                            min_width="60px",
                                            min_height="60px",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            margin_bottom="1rem",
                                            style={
                                                "background": "rgba(34, 197, 94, 0.15)",
                                                "border": "2px solid rgba(34, 197, 94, 0.5)",
                                                "boxShadow": "0 0 25px rgba(34, 197, 94, 0.4)"
                                            }
                                        ),
                                        rx.text(State.timeline_step6, font_weight="700", color="white", font_size="0.9rem", text_align="center"),
                                        rx.text(State.timeline_step6_desc, font_size="0.75rem", color="gray.400", line_height="1.4", text_align="center"),
                                        align="center",
                                        spacing="2",
                                        min_width="220px",
                                        max_width="220px",
                                        padding="1rem",
                                        border_radius="lg",
                                        style={
                                            "background": "rgba(15, 23, 42, 0.4)",
                                            "border": "1px solid rgba(34, 197, 94, 0.2)"
                                        }
                                    ),

                                    align="center",
                                    spacing="0",
                                    padding="1.5rem 1rem"
                                ),
                                overflow_x="auto",
                                overflow_y="hidden",
                                width="100%",
                                style={
                                    "WebkitOverflowScrolling": "touch",
                                    "scrollbarWidth": "thin",
                                    "scrollbarColor": "rgba(0, 212, 255, 0.3) transparent",
                                    "::-webkit-scrollbar": {
                                        "height": "6px"
                                    },
                                    "::-webkit-scrollbar-track": {
                                        "background": "rgba(15, 23, 42, 0.3)"
                                    },
                                    "::-webkit-scrollbar-thumb": {
                                        "background": "rgba(0, 212, 255, 0.3)",
                                        "borderRadius": "3px"
                                    },
                                    "::-webkit-scrollbar-thumb:hover": {
                                        "background": "rgba(0, 212, 255, 0.5)"
                                    }
                                }
                            )
                        ),

                        spacing="4",
                        align="center",
                        width="100%"
                    ),
                    padding="3rem 2rem",
                    border_radius="xl",
                    margin_bottom="3rem",
                    max_width="1400px",
                    margin_x="auto",
                    style={
                        "background": "rgba(15, 23, 42, 0.5)",
                        "border": "1px solid rgba(100, 116, 139, 0.2)",
                        "backdropFilter": "blur(10px)"
                    }
                ),

                style={
                    "animation": "slideInUp 0.8s ease-out 0.2s both",
                    "position": "relative",
                    "zIndex": "10"
                },
                spacing="4",
                align="center",
                width="100%",
                padding="2rem"
            ),

            # Content styling
            padding="2rem 0",
            flex="1"
        ),

        # Contact section
        contact_section(),

        footer_component,
        align="stretch",
        spacing="0",
        width="100%",
        min_height="100vh",
        style={
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",
        }
    )

    return rx.fragment(
        # Page transition loader
        rx.cond(
            State.is_page_loading,
            page_transition_loader()
        ),

        # Main content
        rx.box(
            # Animated background
            animated_background(),

            # Main content
            layout,

            # Floating language button
            floating_language_button(),

            background="linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%)",
            style={
                **animations_css,
                "boxSizing": "border-box",
                "width": "100%",
                "minHeight": "100vh",
                "margin": "0",
                "padding": "0",
                "position": "relative",
                "overflow": "hidden"
            },
            width="100%",
            min_height="100vh",
            on_mount=State.finish_page_transition
        )
    )
