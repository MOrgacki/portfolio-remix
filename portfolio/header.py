import reflex as rx
from reflex.components.radix.themes.layout.stack import HStack

mail = "marcinorgacki@gmail.com"

css: dict = {
    "header": {
        "width": "100%",
        "padding": ["0rem 1rem", "0rem 1rem", "0rem 1rem", "0rem 8rem", "0rem 8rem",],
        "transition": "all 550ms ease"
    },
}


class Header:
    def __init__(self) -> None:
        self.email: HStack = rx.hstack(
            rx.box(rx.icon(tag="mail", size=30,
                           padding=["6px 6px",]), justify="center"),
            rx.tablet_and_desktop(rx.link(rx.box(rx.text(mail)), href=f"mailto:{mail}",
                                          style={
                "textDecoration": "none",  # Remove underline
                "color": "inherit",
            },),
                align="center",
                justify="center", href=f"mailto:{mail}"))
        self.theme: rx.Component = rx.color_mode.button()

    def build(self) -> rx.Component:
        self.header: HStack = rx.hstack(
            self.email, rx.spacer(), self.theme, style=css.get("header"))
        return self.header
