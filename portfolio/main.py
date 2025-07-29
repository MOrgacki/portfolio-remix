import reflex as rx
from reflex.components.radix.themes.layout.box import Box
from reflex.components.radix.themes.layout.stack import HStack, VStack

css: dict = {
    "main": {
        "width": "100%",
        "padding": ["1rem", "1rem", "2rem", "2rem", "2rem"],
        "align_items": "center",
        "justify_content": "center",
        "flex": "1",
        "display": "flex",
        "flexDirection": "column"
    }
}

wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(25deg)"},
        "100%": {"transform": "rotate(-15deg)"},
    },
    "@keyframes slideInUp": {
        "0%": {"opacity": "0", "transform": "translateY(30px)"},
        "100%": {"opacity": "1", "transform": "translateY(0)"}
    },
    "@keyframes slideInLeft": {
        "0%": {"opacity": "0", "transform": "translateX(-30px)"},
        "100%": {"opacity": "1", "transform": "translateX(0)"}
    },
    "@keyframes slideInRight": {
        "0%": {"opacity": "0", "transform": "translateX(30px)"},
        "100%": {"opacity": "1", "transform": "translateX(0)"}
    },
    "@keyframes fadeIn": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"}
    }
}



class State(rx.State):
    theme: str = "light"  # or "dark"


class Main:
    def __init__(self) -> None:
        self.box: Box = rx.box(width="100%")
        self.a, self.b, *self.rest = [
            rx.heading("Hello,",
                       font_size=["1.35rem", "1.75rem",
                                  "3rem", "4rem", "4rem"],
                       font_weight="600",
                       line_height="1.2",
                       color="gray.100"),
            rx.heading("I'm",
                       font_size=["1.35rem", "1.75rem",
                                  "3rem", "4rem", "4rem"],
                       font_weight="600",
                       line_height="1.2",
                       color="gray.100"),
            rx.heading(
                "Marcin",
                font_size=["2.5rem", "2.5rem",
                           "3rem", "4rem", "4rem"],
                font_weight="700",
                line_height="1.2",
                text_align="center",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                    "paddingBottom": "0.1rem"
                }

            ), rx.heading(
                "Orgacki",
                font_size=["2.5rem", "2.5rem",
                           "3rem", "4rem", "4rem"],
                font_weight="700",
                line_height="1.2",
                text_align="center",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                    "paddingBottom": "0.1rem"
                }),
            rx.heading("👋", font_size=["1.35rem", "1.75rem",
                                       "3rem", "4rem", "4rem"], style={
                **wave,  # Spread the keyframes here
                "animation": "wave 0.8s cubic-bezier(0.25,0.46,0.45,0.94) infinite alternate-reverse both"
            },)]

        self.badge_stack_max: rx.Component = rx.hstack(spacing="4")
        self.badge_stack_min: rx.Component = rx.hstack(
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
                      ("linkedin", "LinkedIn", "https://www.linkedin.com/in/m-orgacki/"),
                      ("mail", "Email", "mailto:marcinorgacki@gmail.com")]
        self.crumbs.children = [
            self._create_breadcrumb_item(icon, title, url) for icon, title, url in data]

        # Expertise box
        self.expertise_box = self._create_expertise_box(State.theme)

    def build_view(self):
        self.box.children = [self._build_desktop(), self._build_mobile()]
        return self.box

    def _contact_button(self):
        return rx.link(
            rx.button(
                rx.flex(
                    rx.icon("mail", size=20, color="white"),
                    rx.text(
                        "Contact Me",
                        size="3",
                        weight="bold",
                        color="white",
                        margin_left="0.5rem"
                    ),
                    align="center",
                    justify="center",
                    gap="2"
                ),
                size="3",
                radius="full",
                margin_y="4",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "boxShadow": "0 8px 32px rgba(0, 212, 255, 0.3)",
                    "transition": "all 0.3s ease",
                    "cursor": "pointer",
                    "minWidth": "120px",
                    "height": "44px",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "boxShadow": "0 12px 40px rgba(0, 212, 255, 0.4)"
                    }
                }
            ),
            href="mailto:marcinorgacki@gmail.com",
            target="_blank"
        )

    def _build_desktop(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                rx.box(
                    self.name_desktop, 
                    margin_bottom="4",
                    style={
                        **wave,
                        "animation": "slideInUp 0.8s ease-out",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    self.badge_stack_min,
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.2s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    rx.hstack(self.crumbs, justify="center", wrap="wrap", spacing="4"),
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.4s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                spacing="4",
                align="center",
                style=css.get("main")
            )
        )

    def _build_mobile(self):
        return rx.mobile_only(
            rx.vstack(
                rx.box(
                    self.name_mobile, 
                    margin_bottom="4",
                    style={
                        **wave,
                        "animation": "slideInUp 0.8s ease-out",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    self.badge_stack_min,
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.2s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(self.crumbs, justify="center", wrap="wrap", spacing="2"),
                        spacing="3", 
                        align="center"
                    ),
                    style={
                        "animation": "slideInUp 0.8s ease-out 0.4s both",
                        "zIndex": "10",
                        "position": "relative"
                    }
                ),
                spacing="4",
                align="center",
                style=css.get("main")
            )
        )

    def _create_badges(self, title: str) -> rx.Component:
        return rx.badge(
            title,
            variant="solid",
            padding=["0.10rem 0.25rem", "0.10rem 0.25rem",
                     "0.10rem 0.7rem", "0.10rem 0.7rem", "0.10rem 0.7rem",],
            font_size=["0.55rem", "0.55rem",
                       "0.75rem", "0.75rem", "0.75rem"],
            style={
                "background": "rgba(0, 212, 255, 0.1)",
                "color": "cyan.300",
                "border": "1px solid rgba(0, 212, 255, 0.2)",
                "backdropFilter": "blur(10px)"
            }
        )

    def _create_breadcrumb_item(self, icon: str, title: str, url: str | None) -> rx.Component:
        # Brand colors for dark theme
        brand_colors = {
            "GitHub": {"bg": "rgba(36, 41, 47, 0.8)", "hover_bg": "rgba(36, 41, 47, 1)", "icon_color": "white"},
            "LinkedIn": {"bg": "rgba(0, 119, 181, 0.8)", "hover_bg": "rgba(0, 119, 181, 1)", "icon_color": "white"},
            "Email": {"bg": "rgba(0, 212, 255, 0.8)", "hover_bg": "rgba(0, 212, 255, 1)", "icon_color": "white"},
        }
        colors = brand_colors.get(title, {"bg": "rgba(100, 116, 139, 0.8)", "hover_bg": "rgba(100, 116, 139, 1)", "icon_color": "gray.300"})
        
        return rx.link(
            rx.button(
                rx.flex(
                    rx.icon(icon, size=20, color=colors["icon_color"]),
                    rx.tablet_and_desktop(
                        rx.text(
                            title,
                            size="3",
                            weight="bold",
                            color="white",
                            margin_left="0.5rem"
                        )
                    ),
                    align="center",
                    justify="center",
                    gap="2"
                ),
                size="3",
                radius="full",
                style={
                    "background": colors["bg"],
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "boxShadow": "0 8px 32px rgba(0, 0, 0, 0.3)",
                    "transition": "all 0.3s ease",
                    "cursor": "pointer",
                    "minWidth": ["50px", "50px", "120px", "120px", "120px"],
                    "height": "44px",
                    "_hover": {
                        "background": colors["hover_bg"],
                        "transform": "translateY(-2px)",
                        "boxShadow": "0 12px 40px rgba(0, 0, 0, 0.4)"
                    }
                }
            ),
            href=url,
            target="_blank",
        )

    def _create_expertise_box(self, theme="light") -> rx.Component:
        return rx.box(
            # Header
            rx.text(
                "⭐ Core Skills & Highlights ⭐", 
                weight="bold", 
                size="5", 
                text_align="center", 
                color="cyan.300",
                margin_top="1rem",
                margin_bottom="1.5rem"
            ),
            
            # Core Skills Section
            rx.vstack(
                rx.text(
                    "🔹 Designing test strategies and improving SDLC/STLC processes",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6",
                    style={"span": {"color": "cyan.400", "fontWeight": "bold"}}
                ),
                rx.text(
                    "🔹 Manual & automated testing (frontend, backend, database)",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    "🔹 Leading QA teams, estimations, and daily operations",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    "🔹 Optimizing QA efforts to improve quality and reduce time-to-market",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                spacing="3",
                align="center",
                width="100%",
                margin_bottom="2rem"
            ),
            
            # Divider
            rx.divider(border_color="rgba(100, 116, 139, 0.3)", margin_y="1.5rem"),
            
            # Additional Experience Header
            rx.text(
                "🎯 Additional Experience", 
                weight="bold", 
                size="4", 
                text_align="center", 
                color="cyan.300",
                margin_bottom="1.5rem"
            ),
            
            # Additional Experience Section
            rx.vstack(
                rx.text(
                    "🔸 Release coordination & data migration",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    "🔸 Legacy platform upgrades & data warehouse projects",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    "🔸 Test strategy setup for startups",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                rx.text(
                    "🔸 Interest in AI testing, DevOps, data science, web3 & finance",
                    color="gray.300",
                    text_align="center",
                    line_height="1.6"
                ),
                spacing="3",
                align="center",
                width="100%",
                margin_bottom="1rem"
            ),
            
            # Box styling
            padding_x="9",
            padding_y="12",
            border_radius="3xl",
            margin_y="6",
            width=["90%", "90%", "80%", "70%", "60%"],
            max_width="650px",
            style={
                "background": "rgba(30, 41, 59, 0.8)",
                "backdropFilter": "blur(20px)",
                "border": "1px solid rgba(100, 116, 139, 0.2)",
                "boxShadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05)",
                "margin": "0 auto"
            }
        )
