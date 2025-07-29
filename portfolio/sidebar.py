import reflex as rx

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color="white"),
            rx.text(text, size="4", color="white"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": "rgba(0, 212, 255, 0.1)",
                    "color": "cyan.300",
                    "transform": "translateX(4px) scale(1.02)",
                    "boxShadow": "0 4px 20px rgba(0, 212, 255, 0.2)",
                },
                "border-radius": "0.5em",
                "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                "animation": "slideInLeft 0.6s ease-out",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "home", "/"),
        sidebar_item("Projects", "square-library", "/projects"),
        sidebar_item("Blog", "bar-chart-4", "/#"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.image(
                    src="/logo.jpg",
                    width="80px",
                    height="80px",
                    border_radius="50%",
                    margin_bottom="1.5em",
                    object_fit="cover",
                ),
                sidebar_items(),
                spacing="3",
                padding_x="1em",
                padding_y="1.5em",
                align="center",
                height="100vh",
                width="200px",
                style={
                    "position": "sticky",
                    "top": "0",
                    "flexShrink": "0",
                    "background": "rgba(15, 15, 35, 0.9)",
                    "backdropFilter": "blur(20px)",
                    "border": "1px solid rgba(100, 116, 139, 0.2)",
                    "borderLeft": "none",
                    "borderTop": "none",
                    "borderBottom": "none"
                }
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=36),
                    style={
                        "position": "fixed",
                        "top": "1rem",
                        "left": "1rem",
                        "zIndex": "10",
                        "background": "rgba(30, 41, 59, 0.9)",
                        "backdropFilter": "blur(20px)",
                        "padding": "0.5rem",
                        "borderRadius": "0.5rem",
                        "cursor": "pointer",
                        "border": "1px solid rgba(100, 116, 139, 0.2)",
                        "color": "cyan.300"
                    }
                ),
                rx.drawer.overlay(z_index="15"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                                text_align="right",
                                margin_bottom="1rem"
                            ),
                            rx.image(
                                src="/logo.jpg",
                                width="80px",
                                height="80px",
                                border_radius="50%",
                                margin_bottom="1.5em",
                                object_fit="cover",
                            ),
                            sidebar_items(),
                            spacing="3",
                            width="100%",
                            align="center"
                        ),
                        top="0",
                        left="0",
                        height="100%",
                        width="250px",
                        padding="1.5em",
                        z_index="20",
                        style={
                            "background": "rgba(15, 15, 35, 0.95)",
                            "backdropFilter": "blur(20px)",
                            "border": "1px solid rgba(100, 116, 139, 0.2)"
                        }
                    ),
                ),
                direction="left",
            ),
        ),
    )


