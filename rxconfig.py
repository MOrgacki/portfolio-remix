import reflex as rx

config = rx.Config(
    app_name="portfolio",
    watch_dirs=["."],
    ignore_dirs=["__pycache__", ".git", "node_modules", ".venv"],
)
