import reflex as rx
from reflex.components.radix.themes.layout.box import Box
from reflex.components.radix.themes.layout.stack import HStack, VStack

css: dict = {
    "main": {
        "height": "100vh",
        "min_height": "100vh",
        "width": "100%",
        "padding": ["0.5rem 0.5rem 0.5rem 0.5rem",],
        "align_items": "center",
        "justify_content": "center"
    }
}

wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(25deg)"},
        "100%": {"transform": "rotate(-15deg)"},
    }
}


class Main:
    def __init__(self) -> None:
        self.box: Box = rx.box(width="100%")
        self.a, self.b, *self.rest = [
            rx.heading("Hello,",
                       font_size=["1.35rem", "1.75rem",
                                  "3rem", "4rem", "4rem"],
                       font_weight="600",
                       line_height="1",),
            rx.heading("I'm",
                       font_size=["1.35rem", "1.75rem",
                                  "3rem", "4rem", "4rem"],
                       font_weight="600",
                       line_height="1",),
            rx.heading(
                "Marcin",
                color="#3b9eff",
                font_size=["1.35rem", "1.75rem",
                           "3rem", "4rem", "4rem"],
                font_weight="600",
                line_height="1",
                background="linear-gradient(to right, #e1e1e1, #757575)",
                background_clip="text",
                text_align="center",

            ), rx.heading(
                "Orgacki",
                color="#3b9eff",
                font_size=["1.35rem", "1.75rem",
                           "3rem", "4rem", "4rem"],
                font_weight="600",
                line_height="1",
                background="linear-gradient(to right, #e1e1e1, #757575)",
                background_clip="text",
                text_align="center",),
            rx.heading("👋", font_size=["1.35rem", "1.75rem",
                                       "3rem", "4rem", "4rem"], style={
                **wave,  # Spread the keyframes here
                "animation": "wave 0.8s cubic-bezier(0.25,0.46,0.45,0.94) infinite alternate-reverse both"
            },)]

        self.badge_stack_max: rx.Component = rx.hstack(spacing="4")
        self.badge_stack_min: rx.Component = rx.vstack(
            spacing="2", align="center")
        self.name_mobile: VStack = rx.vstack(rx.hstack(self.a, self.b), *self.rest, align="center"
                                             )
        self.name_desktop: HStack = rx.hstack(self.a, self.b, *self.rest,
                                              spacing="4", line_height="1", padding=["0.5rem",],)
        titles: list = ["QA Manager",
                        "Senior QA Engineer", "Test Automation Specialist"]
        self.badge_stack_max.children = [
            self._create_badges(title) for title in titles]
        self.badge_stack_min.children = [
            self._create_badges(title) for title in titles]

        self.crumbs: rx.Component = rx.hstack(spacing="4")
        data: list = [("github", "GitHub", "https://github.com/MOrgacki"),
                      ["linkedin", "LinkedIn", "https://www.linkedin.com/in/m-orgacki/"]]
        self.crumbs.children = [
            self._create_breadcrumb_item(icon, title, url) for icon, title, url in data]

    def build_view(self):
        self.box.children = [self._build_desktop(), self._build_mobile()]
        return self.box

    def _build_desktop(self):
        return rx.tablet_and_desktop(
            rx.vstack(rx.box(self.name_desktop), self.badge_stack_min, self.crumbs, style=css.get("main")))

    def _build_mobile(self):
        return rx.mobile_only(
            rx.vstack(rx.box(self.name_mobile), self.badge_stack_min, self.crumbs,  style=css.get("main")))

    def _create_badges(self, title: str) -> rx.Component:
        return rx.badge(
            title,
            variant="solid",
            padding=["0.15rem 0.35rem", "0.15rem 0.35rem",
                     "0.15rem 1rem", "0.15rem 1rem", "0.15rem 1rem",],
            font_size=["0.65rem", "0.65rem",
                       "0.9rem", "0.9rem", "0.9rem"],
        )

    def _create_breadcrumb_item(self, icon: str, title: str, url: str | None) -> rx.Component:
        return rx.link(rx.badge(
            rx.flex(
                rx.icon(icon, size=18),
                rx.tablet_and_desktop(rx.text(
                    title,
                    size="2",
                    weight="medium",
                    padding=["0rem 0rem 0rem 0.5rem",]
                ),
                    direction="row",
                    gap="1",
                    align="center",
                )),
            size="2",
            radius="full",
            color_scheme="gray",

        ),      href=url,             target="_blank",)
