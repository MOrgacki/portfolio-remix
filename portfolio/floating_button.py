import reflex as rx
from state import State


def floating_language_button() -> rx.Component:
    """Floating language switcher button in bottom-right corner"""
    return rx.box(
        rx.button(
            rx.hstack(
                rx.icon("globe", size=20, color="white"),
                rx.text(
                    rx.cond(
                        State.language == "en",
                        "EN",
                        "PL"
                    ),
                    size="3",
                    color="white",
                    font_weight="bold"
                ),
                align="center",
                spacing="2"
            ),
            on_click=State.toggle_language,
            size="3",
            style={
                "background": "linear-gradient(135deg, rgba(0, 212, 255, 0.9) 0%, rgba(91, 115, 255, 0.9) 100%)",
                "backdropFilter": "blur(20px)",
                "border": "1px solid rgba(255, 255, 255, 0.2)",
                "boxShadow": "0 8px 32px rgba(0, 212, 255, 0.4)",
                "transition": "all 0.3s ease",
                "cursor": "pointer",
                "padding": "0.75rem 1rem",
                "borderRadius": "50px",
                "_hover": {
                    "transform": "translateY(-3px) scale(1.05)",
                    "boxShadow": "0 12px 40px rgba(0, 212, 255, 0.6)"
                }
            }
        ),
        position="fixed",
        bottom="2rem",
        right="2rem",
        z_index="1000",
        style={
            "animation": "fadeIn 0.5s ease-out 1s both"
        }
    )
