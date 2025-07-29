# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website built with Reflex (Python-based web framework). The application showcases Marcin Orgacki's QA/testing expertise and professional background.

## Architecture

The application follows a component-based architecture with these main modules:

- **portfolio/main.py**: Central landing page content with skills, experience, and contact information
- **portfolio/header.py**: Top navigation with email contact and theme toggle
- **portfolio/footer.py**: Simple footer with attribution
- **portfolio/sidebar.py**: Navigation sidebar with responsive drawer for mobile
- **portfolio/portfolio.py**: Main application entry point and page routing
- **state.py**: Global application state management
- **rxconfig.py**: Reflex framework configuration

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
reflex run

# Build for production
reflex export

# Initialize/reset database (if needed)
reflex init
```

## Key Framework Details

- **Framework**: Reflex 0.8.1 (Python-based reactive web framework)
- **Styling**: CSS-in-Python with responsive breakpoints
- **Components**: Class-based component architecture
- **State Management**: Reflex State classes for reactive updates
- **Responsive Design**: Built-in breakpoint system (mobile_only, tablet_and_desktop, etc.)

## Component Structure

Each UI component follows this pattern:
1. CSS styles defined as dictionaries
2. Component class with `__init__` method for setup
3. `build()` or `build_view()` method returning Reflex components
4. Responsive layouts using Reflex's breakpoint utilities

## Styling Approach

- Gradient backgrounds and modern UI design
- Responsive typography with breakpoint-specific font sizes
- CSS animations (wave effect, hover transitions)
- Brand-specific colors for social links
- Theme support (light/dark mode toggle)

## Asset Management

Static assets are stored in `/assets/` directory:
- `logo.jpg`: Profile image used in sidebar
- `favicon.ico`: Browser tab icon

Assets are referenced with relative paths (e.g., `src="/logo.jpg"`)