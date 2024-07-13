import reflex as rx
from portfolio.header import Header
from portfolio.main import Main
from portfolio.footer import Footer

dots_animation = {
    "@keyframes dots": {
        "0%": {"backgroundPosition": "0 0"},
        "100%": {"backgroundPosition": "40px 40px"},
    }
}


@rx.page(route="/")
def index() -> rx.Component:
    header = Header()
    main = Main()
    footer = Footer()
    header_component = header.build()
    main_component = main.build_view()
    footer_component = footer.build()
    return rx.vstack(
        header_component,
        main_component,
        footer_component,
        align="center",
        background="radial-gradient(circle, rgba(12,3,255,0.49) 1.2px,transparent 1.2px)",
        background_size="25px 25px",
        style={
            "boxSizing": "border-box",  # Include padding and border in sizing
            "width": "100%",
            "height": "100vh",
            "margin": "0",
            "padding": "0",
            "overflow": "hidden",  # Hide any overflow content
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",  # Distribute space to push footer to bottom
            **dots_animation,  # Spread the keyframes here
            "animation": "dots 4s linear infinite alternate-reverse both",
        },
        width="100%",  # Ensure full width of the viewport
        height="100vh",  # Ensure full height of the viewport


    )
    # header_component = header.build()
    # main_component = main.build_desktop()
    # footer_component = footer.build()
    # return rx.vstack(
    #     header_component,
    #     main_component,
    #     footer_component,
    #     align="center",
    #     background="radial-gradient(circle, rgba(2,3,255,0.49) 1.2px,transparent 1px)",
    #     background_size="25px 25px",
    #     style={
    #         **dots_animation,  # Spread the keyframes here
    #         "animation": "dots 4s linear infinite alternate-reverse both"
    #     },

    # ),


app = rx.App(
    theme=rx.theme(
        has_background=True,
        color_mode="dark",
        accent_color="blue",
    ), style={
        "overflow": "hidden",  # Hide any overflow content
        "width": "100%",
        "height": "100vh",
        "margin": "0",
        "padding": "0",
    }
)

# app.add_page(header.build, "/")
# app.add_page(main.build, "/")

app.add_page(index)
