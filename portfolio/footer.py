import reflex as rx
from reflex.components.radix.themes.layout.stack import HStack
css: dict = {
    "footer": {
        "align_items": "center",
        "padding": ["1rem 1rem", "1rem 1rem", "1rem 2rem", "1rem 2rem", "1rem 2rem"],
        "transition": "all 550ms ease",
        "flexShrink": "0",
        "justifyContent": "center"
    }
}


class Footer:
    def __init__(self) -> None:
        self.footer: HStack = rx.hstack(
            # Removed footer text for cleaner design
            justify="center",
            align="center",
            style=css.get("footer")
        )

    def build(self) -> HStack:
        return self.footer
