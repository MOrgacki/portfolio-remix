import reflex as rx
from reflex.components.radix.themes.layout.stack import HStack

mail = "marcinorgacki@gmail.com"

css: dict = {
    "header": {
        "width": "100vw",
        "maxWidth": "100%",
        "padding": ["1rem 1rem", "1rem 1rem", "1rem 2rem", "1rem 2rem", "1rem 2rem"],
        "transition": "all 550ms ease",
        "flexShrink": "0",
        "background": "rgba(15, 15, 35, 0.9)",
        "backdropFilter": "blur(20px)",
        "border": "1px solid rgba(100, 116, 139, 0.2)",
        "borderTop": "none",
        "borderLeft": "none",
        "borderRight": "none",
        "boxSizing": "border-box"
    },
}

def nav_item_desktop(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color="white", size=18),
            rx.text(
                text,
                size="3",
                color="white",
                weight="medium",
            ),
            align="center",
            spacing="2"
        ),
        href=href,
        underline="none",
        padding_x="1.5rem",
        padding_y="0.75rem",
        text_align="center",
        border_radius="0.25rem",
        _hover={
            "bg": "rgba(0, 212, 255, 0.1)",
            "color": "cyan.300",
            "transform": "translateY(-1px)",
            "box_shadow": "0 4px 20px rgba(0, 212, 255, 0.2)",
        },
        transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
        cursor="pointer"
    )

def nav_item_mobile(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color="white", size=20),
            rx.text(text, size="3", color="white", weight="medium"),
            align="center",
            spacing="2",
            padding_x="1rem",
            padding_y="0.5rem",
            style={
                "_hover": {
                    "bg": "rgba(0, 212, 255, 0.1)",
                    "color": "cyan.300",
                    "transform": "translateY(-1px)",
                    "boxShadow": "0 4px 20px rgba(0, 212, 255, 0.2)",
                },
                "border-radius": "0.5em",
                "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
            },
        ),
        href=href,
        underline="none",
    )

class Header:
    def __init__(self) -> None:
        pass
    
    def build(self) -> rx.Component:
        # Desktop header
        desktop_header = rx.tablet_and_desktop(
            rx.hstack(
                # Logo
                rx.link(
                    rx.image(
                        src="/logo.png",
                        width="65px",
                        height="35px"
                    ),
                    href="/",
                    underline="none"
                ),
                
                # Spacer to push navigation to the right
                rx.box(flex="1"),
                
                # Navigation menu - right aligned
                rx.hstack(
                    nav_item_desktop("Home", "home", "/"),
                    nav_item_desktop("Projects", "square-library", "/projects"),
                    nav_item_desktop("Blog", "bar-chart-4", "/blog"),
                    spacing="3",
                    align="center"
                ),
                
                align="center",
                width="100%",
                style=css.get("header")
            )
        )
        
        # Mobile header with hamburger menu
        mobile_header = rx.mobile_only(
            rx.hstack(
                # Logo
                rx.link(
                    rx.image(
                        src="/logo.png",
                        width="65px",
                        height="35px"
                    ),
                    href="/",
                    underline="none"
                ),
                
                # Hamburger menu
                rx.drawer.root(
                    rx.drawer.trigger(
                        rx.button(
                            rx.icon("menu", size=24, color="white"),
                            variant="ghost",
                            size="3"
                        )
                    ),
                    rx.drawer.overlay(z_index="15"),
                    rx.drawer.portal(
                        rx.drawer.content(
                            rx.vstack(
                                rx.box(
                                    rx.drawer.close(
                                        rx.icon("x", size=30, color="white")
                                    ),
                                    width="100%",
                                    text_align="right",
                                    margin_bottom="2rem"
                                ),
                                nav_item_mobile("Home", "home", "/"),
                                nav_item_mobile("Projects", "square-library", "/projects"),
                                nav_item_mobile("Blog", "bar-chart-4", "/blog"),
                                spacing="4",
                                width="100%",
                                align="center",
                                padding="2rem"
                            ),
                            top="0",
                            right="0",
                            height="100%",
                            width="250px",
                            z_index="20",
                            style={
                                "background": "rgba(15, 15, 35, 0.95)",
                                "backdropFilter": "blur(20px)",
                                "border": "1px solid rgba(100, 116, 139, 0.2)"
                            }
                        ),
                    ),
                    direction="right",
                ),
                
                align="center",
                justify="between",
                width="100%",
                style=css.get("header")
            )
        )
        
        return rx.box(desktop_header, mobile_header)