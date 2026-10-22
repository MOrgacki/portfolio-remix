import reflex as rx
from portfolio.header import Header
from portfolio.footer import Footer
from portfolio.main import Main
from portfolio.animations import animated_background, animations_css
from portfolio.loader import page_transition_loader
from portfolio.floating_button import floating_language_button
from state import State


@rx.page(route="/contact", title="Marcin Orgacki | Contact")
def contact_page() -> rx.Component:
    """Contact page - same content as homepage"""
    header = Header()
    main = Main()
    footer = Footer()
    header_component = header.build()
    main_component = main.build_view()
    footer_component = footer.build()

    # Layout - same as index page
    layout = rx.vstack(
        header_component,
        main_component,
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
