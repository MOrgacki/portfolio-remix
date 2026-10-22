import reflex as rx
from state import State

# Animations for loaders
loader_animations = {
    "@keyframes spin": {
        "0%": {"transform": "rotate(0deg)"},
        "100%": {"transform": "rotate(360deg)"}
    },
    "@keyframes pulse": {
        "0%, 100%": {"opacity": "1"},
        "50%": {"opacity": "0.5"}
    },
    "@keyframes fadeIn": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"}
    },
    "@keyframes fadeOut": {
        "0%": {"opacity": "1"},
        "100%": {"opacity": "0"}
    },
    "@keyframes scaleIn": {
        "0%": {"transform": "scale(0.8)", "opacity": "0"},
        "100%": {"transform": "scale(1)", "opacity": "1"}
    },
    "@keyframes loaderEnter": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"}
    }
}


def initial_loader() -> rx.Component:
    """Initial app loading screen"""
    return rx.box(
        rx.vstack(
            # Animated logo/spinner
            rx.box(
                rx.box(
                    width="80px",
                    height="80px",
                    border_radius="50%",
                    border="4px solid rgba(0, 212, 255, 0.1)",
                    border_top="4px solid #00d4ff",
                    style={
                        **loader_animations,
                        "animation": "spin 1s linear infinite"
                    }
                ),
                margin_bottom="2rem"
            ),

            # Loading text
            rx.heading(
                State.loader_loading,
                size="6",
                color="cyan.300",
                font_weight="600",
                style={
                    **loader_animations,
                    "animation": "pulse 1.5s ease-in-out infinite"
                }
            ),

            rx.text(
                State.loader_please_wait,
                color="gray.400",
                font_size="0.9rem",
                margin_top="0.5rem"
            ),

            align="center",
            justify="center",
            spacing="4"
        ),

        # Full screen overlay
        position="fixed",
        top="0",
        left="0",
        right="0",
        bottom="0",
        display="flex",
        align_items="center",
        justify_content="center",
        z_index="9999",
        style={
            **loader_animations,
            "background": "linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%)",
            "backdropFilter": "blur(10px)",
            "animation": "loaderEnter 0.4s ease-out forwards",
            "transition": "opacity 0.5s ease-out"
        }
    )


def page_transition_loader() -> rx.Component:
    """Loader for page transitions"""
    return rx.box(
        rx.vstack(
            # Smaller spinner for transitions
            rx.box(
                rx.box(
                    width="50px",
                    height="50px",
                    border_radius="50%",
                    border="3px solid rgba(0, 212, 255, 0.1)",
                    border_top="3px solid #00d4ff",
                    style={
                        **loader_animations,
                        "animation": "spin 0.8s linear infinite"
                    }
                ),
                margin_bottom="1rem"
            ),

            rx.text(
                State.loader_loading_page,
                color="cyan.300",
                font_size="0.9rem",
                font_weight="500",
                style={
                    **loader_animations,
                    "animation": "pulse 1.2s ease-in-out infinite"
                }
            ),

            align="center",
            justify="center",
            spacing="3"
        ),

        # Full screen overlay with transparency
        position="fixed",
        top="0",
        left="0",
        right="0",
        bottom="0",
        display="flex",
        align_items="center",
        justify_content="center",
        z_index="9998",
        style={
            **loader_animations,
            "background": "rgba(15, 15, 35, 0.95)",
            "backdropFilter": "blur(20px)",
            "animation": "fadeIn 0.2s ease-out"
        }
    )


def inline_loader() -> rx.Component:
    """Small inline loader for sections"""
    return rx.hstack(
        rx.box(
            width="20px",
            height="20px",
            border_radius="50%",
            border="2px solid rgba(0, 212, 255, 0.1)",
            border_top="2px solid #00d4ff",
            style={
                **loader_animations,
                "animation": "spin 0.6s linear infinite"
            }
        ),
        rx.text(
            "Loading...",
            color="cyan.300",
            font_size="0.85rem",
            margin_left="0.5rem"
        ),
        align="center",
        spacing="2"
    )
