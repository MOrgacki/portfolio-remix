import reflex as rx
from portfolio.header import Header
from portfolio.footer import Footer
from portfolio.animations import animated_background, animations_css

@rx.page(route="/blog", title="Marcin Orgacki | Blog")
def blog_page() -> rx.Component:
    """Blog page component - placeholder"""
    header = Header()
    footer = Footer()
    header_component = header.build()
    footer_component = footer.build()
    
    # Main content
    main_content = rx.box(
        rx.vstack(
            # Title section
            rx.box(
                rx.heading(
                    "Blog",
                    size="8",
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
                    "Coming Soon - Insights and thoughts on QA, testing, and software development",
                    color="gray.400",
                    text_align="center",
                    font_size="1.1rem",
                    margin_bottom="3rem",
                    max_width="600px",
                    margin_x="auto",
                    line_height="1.6",
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.2s both",
                        "position": "relative",
                        "zIndex": "10"
                    }
                ),
                margin_bottom="4rem"
            ),
            
            # Placeholder content
            rx.box(
                rx.vstack(
                    rx.box(
                        rx.icon("pen-line", size=80, color="cyan.300", margin_bottom="2rem"),
                        text_align="center"
                    ),
                    rx.heading(
                        "Blog Coming Soon!",
                        size="6",
                        color="white",
                        text_align="center",
                        margin_bottom="1rem",
                        font_weight="700"
                    ),
                    rx.text(
                        "I'm working on creating valuable content about:",
                        color="gray.300",
                        text_align="center",
                        font_size="1rem",
                        margin_bottom="2rem",
                        line_height="1.6"
                    ),
                    
                    # Topics list
                    rx.vstack(
                        rx.hstack(
                            rx.icon("check", size=20, color="cyan.300"),
                            rx.text("QA strategies and best practices", color="gray.300", font_size="0.95rem"),
                            spacing="3",
                            align="center"
                        ),
                        rx.hstack(
                            rx.icon("check", size=20, color="cyan.300"),
                            rx.text("Test automation frameworks and tools", color="gray.300", font_size="0.95rem"),
                            spacing="3",
                            align="center"
                        ),
                        rx.hstack(
                            rx.icon("check", size=20, color="cyan.300"),
                            rx.text("Industry insights and case studies", color="gray.300", font_size="0.95rem"),
                            spacing="3",
                            align="center"
                        ),
                        rx.hstack(
                            rx.icon("check", size=20, color="cyan.300"),
                            rx.text("Software development trends", color="gray.300", font_size="0.95rem"),
                            spacing="3",
                            align="center"
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="3rem"
                    ),
                    
                    # Contact for suggestions
                    rx.text(
                        "Have a topic you'd like me to write about? Feel free to reach out!",
                        color="gray.400",
                        text_align="center",
                        font_size="0.9rem",
                        font_style="italic",
                        margin_bottom="2rem"
                    ),
                    
                    # Back to home button
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("home", size=20),
                                rx.text("Home", font_size="1rem", font_weight="500"),
                                spacing="2",
                                align="center"
                            ),
                            size="3",
                            style={
                                "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                "color": "white",
                                "border": "none",
                                "padding": "0.75rem 1.5rem",
                                "borderRadius": "0.75rem",
                                "transition": "all 0.3s ease",
                                "_hover": {
                                    "transform": "translateY(-2px)",
                                    "boxShadow": "0 8px 25px rgba(0, 212, 255, 0.4)"
                                }
                            }
                        ),
                        href="/",
                        underline="none"
                    ),
                    
                    spacing="4",
                    align="center",
                    padding="3rem",
                    max_width="600px",
                    margin="0 auto"
                ),
                
                # Placeholder box styling
                border_radius="2xl",
                style={
                    "background": "linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.9))",
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(148, 163, 184, 0.1)",
                    "boxShadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
                    "animation": "slideInUp 0.8s ease-out 0.4s both",
                    "position": "relative",
                    "zIndex": "10"
                },
                margin="0 auto",
                max_width="800px"
            ),
            
            spacing="4",
            align="center",
            width="100%",
            padding="2rem",
            min_height="60vh",
            justify="center"
        ),
        flex="1"
    )
    
    # Layout structure
    layout = rx.vstack(
        header_component,
        main_content,
        footer_component,
        align="stretch",
        spacing="0",
        width="100%",
        min_height="100vh",
        style={
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between"
        }
    )

    return rx.box(
        # Animated background
        animated_background(),
        
        # Main content
        layout,
        
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
        min_height="100vh"
    )