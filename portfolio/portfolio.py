import reflex as rx
from portfolio.header import Header
from portfolio.main import Main
from portfolio.footer import Footer
from portfolio.sidebar import sidebar
from portfolio.projects import projects_page
from portfolio.blog import blog_page
from portfolio.animations import animated_background, animations_css

dots_animation = {
    "@keyframes dots": {
        "0%": {"backgroundPosition": "0 0"},
        "100%": {"backgroundPosition": "40px 40px"},
    }
}


@rx.page(route="/", title="Marcin Orgacki")
def index() -> rx.Component:
    header = Header()
    main = Main()
    footer = Footer()
    header_component = header.build()
    main_component = main.build_view()
    footer_component = footer.build()
    sidebar_component = sidebar()

    # Layout without sidebar
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
        min_height="100vh",
    )


app = rx.App(
    theme=rx.theme(
        has_background=True,
        appearance="dark",
        accent_color="cyan",
        gray_color="slate",
        radius="large",
        scaling="100%"
    ), style={
        "width": "100%",
        "minHeight": "100vh",
        "margin": "0",
        "padding": "0",
        "backgroundColor": "#0f0f23"
    }
)

# app.add_page(header.build, "/")
# app.add_page(main.build, "/")

app.add_page(index)
app.add_page(projects_page)
app.add_page(blog_page)
