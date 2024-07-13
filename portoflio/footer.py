import reflex as rx
from reflex.components.radix.themes.layout.stack import HStack
css: dict = {
    "footer":
    {

        "align_items": "center",
        "padding": ["0rem 1rem", "0rem 1rem", "0rem 1rem", "0rem 8rem", "0rem 8rem",],
        "transition": "all 550ms ease"
    }
}


class Footer:
    def __init__(self) -> None:
        self.footer: HStack = rx.hstack(style=css.get("footer"))
        self.footer.children.append(
            rx.text("Created by Marcin Orgacki with Reflex.dev ❤️",
                    font_size="10px", font_weight="semibold", align="center")
        )

    def build(self) -> HStack:
        return self.footer
