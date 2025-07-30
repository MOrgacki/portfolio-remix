import reflex as rx
from typing import List, Dict, Any, Optional
from portfolio.header import Header
from portfolio.footer import Footer
from portfolio.sidebar import sidebar
from portfolio.animations import animated_background, animations_css

# Sample project data structure
PROJECT_FIELDS = ["id", "title", "description", "technologies", "domain", "github", "demo", "image", "status"]

# Static filter data
TECHNOLOGIES = ["All", "Python", "Selenium", "Pytest", "Docker", "React", "FastAPI", "PostgreSQL", "TypeScript", "Node.js", "Jest", "OpenAPI", "Go", "InfluxDB", "Grafana", "Java", "Spring Boot", "MySQL", "Redis", "Appium", "AWS Device Farm", "Jenkins"]
DOMAINS = ["All", "Testing", "Analytics", "Performance", "Data Management", "Mobile Testing"]

PROJECTS_DATA = [
    {
        "id": 1,
        "title": "Automated Testing Framework",
        "description": "Comprehensive testing automation framework for web applications with CI/CD integration and parallel execution capabilities.",
        "technologies": ["Python", "Selenium", "Pytest", "Docker"],
        "domain": "Testing",
        "github": "https://github.com/MOrgacki/test-framework",
        "demo": "",
        "image": "/project1.jpg",
        "status": "Completed"
    },
    {
        "id": 2,
        "title": "QA Dashboard Analytics",
        "description": "Real-time dashboard for tracking QA metrics, test coverage, and defect analysis with interactive visualizations.",
        "technologies": ["React", "Python", "FastAPI", "PostgreSQL"],
        "domain": "Analytics",
        "github": "https://github.com/MOrgacki/qa-dashboard",
        "demo": "https://qa-dashboard-demo.com",
        "image": "/project2.jpg",
        "status": "In Progress"
    },
    {
        "id": 3,
        "title": "API Test Suite Generator",
        "description": "Tool that automatically generates comprehensive API test suites from OpenAPI specifications.",
        "technologies": ["TypeScript", "Node.js", "Jest", "OpenAPI"],
        "domain": "Testing",
        "github": "https://github.com/MOrgacki/api-test-gen",
        "demo": "",
        "image": "/project3.jpg",
        "status": "Completed"
    },
    {
        "id": 4,
        "title": "Performance Monitor",
        "description": "Lightweight performance monitoring tool for web applications with real-time alerts and reporting.",
        "technologies": ["Go", "InfluxDB", "Grafana", "Docker"],
        "domain": "Performance",
        "github": "https://github.com/MOrgacki/perf-monitor",
        "demo": "https://perf-monitor-demo.com",
        "image": "/project4.jpg",
        "status": "Completed"
    },
    {
        "id": 5,
        "title": "Test Data Management",
        "description": "Centralized test data management system with data masking and synthetic data generation capabilities.",
        "technologies": ["Java", "Spring Boot", "MySQL", "Redis"],
        "domain": "Data Management",
        "github": "https://github.com/MOrgacki/test-data-mgmt",
        "demo": "",
        "image": "/project5.jpg",
        "status": "In Progress"
    },
    {
        "id": 6,
        "title": "Mobile App Testing Suite",
        "description": "Cross-platform mobile testing framework supporting iOS and Android with cloud device integration.",
        "technologies": ["Appium", "Python", "AWS Device Farm", "Jenkins"],
        "domain": "Mobile Testing",
        "github": "https://github.com/MOrgacki/mobile-test-suite",
        "demo": "",
        "image": "/project6.jpg",
        "status": "Completed"
    }
]

class ProjectsState(rx.State):
    selected_technologies: List[str] = ["All"]
    selected_domain: str = "All"
    projects: List[Dict[str, Any]] = PROJECTS_DATA
    
    def get_technologies(self) -> List[str]:
        techs = set()
        for project in PROJECTS_DATA:
            techs.update(project["technologies"])
        return sorted(list(techs))
    
    def get_domains(self) -> List[str]:
        domains = set(project["domain"] for project in PROJECTS_DATA)
        return ["All"] + sorted(list(domains))
    
    def filter_projects(self):
        filtered = PROJECTS_DATA
        
        # Only filter by technologies if there are selections and "All" is not selected
        if self.selected_technologies and "All" not in self.selected_technologies:
            filtered = [p for p in filtered if any(tech in p["technologies"] for tech in self.selected_technologies)]
        
        if self.selected_domain != "All":
            filtered = [p for p in filtered if p["domain"] == self.selected_domain]
            
        self.projects = filtered
    
    def toggle_technology_filter(self, tech: str):
        if tech == "All":
            # If "All" is clicked, clear all selections or select only "All"
            if "All" in self.selected_technologies:
                self.selected_technologies = []
            else:
                self.selected_technologies = ["All"]
        else:
            # If any specific technology is clicked
            if tech in self.selected_technologies:
                self.selected_technologies.remove(tech)
            else:
                # Remove "All" if it was selected, then add the specific technology
                if "All" in self.selected_technologies:
                    self.selected_technologies.remove("All")
                self.selected_technologies.append(tech)
        self.filter_projects()
    
    def set_domain_filter(self, domain: str):
        self.selected_domain = domain
        self.filter_projects()
        
    def clear_all_filters(self):
        self.selected_technologies = ["All"]
        self.selected_domain = "All"
        self.filter_projects()

def project_card(project) -> rx.Component:
    """Create a project card component"""
    return rx.box(
        # Project image with modern gradient
        rx.box(
            rx.text(
                "🚀",
                font_size="4rem",
                text_align="center"
            ),
            height="180px",
            width="100%",
            display="flex",
            align_items="center",
            justify_content="center",
            background="linear-gradient(135deg, rgba(0, 212, 255, 0.05) 0%, rgba(91, 115, 255, 0.05) 50%, rgba(139, 92, 246, 0.05) 100%)",
            border_radius="xl",
            margin_bottom="1.5rem",
            position="relative",
            overflow="hidden",
            style={
                "_before": {
                    "content": "''",
                    "position": "absolute",
                    "top": "-50%",
                    "left": "-50%",
                    "width": "200%",
                    "height": "200%",
                    "background": "radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%)",
                    "opacity": "0",
                    "transition": "opacity 0.3s ease"
                },
                "_hover:before": {
                    "opacity": "1"
                }
            }
        ),
        
        # Project title with modern styling
        rx.heading(
            project["title"],
            size="5",
            margin_bottom="1rem",
            line_height="1.2",
            font_weight="800",
            text_align="center",
            style={
                "background": "linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%)",
                "backgroundClip": "text",
                "WebkitBackgroundClip": "text",
                "color": "transparent",
                "textShadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                "letterSpacing": "-0.025em",
                "transition": "all 0.3s ease"
            }
        ),
        
        # Project description
        rx.text(
            project["description"],
            color="gray.400",
            line_height="1.7",
            margin_bottom="1.5rem",
            min_height="5rem",
            font_size="0.9rem",
            padding_x="0.5rem",
            text_align="center"
        ),
        
        # Technology info - static for now
        rx.box(
            rx.text(
                "Technologies: Python, Selenium, React, etc.",
                color="cyan.300",
                font_size="0.8rem",
                text_align="center",
                margin_bottom="1rem"
            ),
            margin_bottom="1.5rem",
            padding_x="0.5rem"
        ),
        
        # Domain badge only
        rx.box(
            rx.badge(
                project["domain"],
                style={
                    "background": "rgba(91, 115, 255, 0.15)",
                    "color": "blue.300",
                    "border": "1px solid rgba(91, 115, 255, 0.3)",
                    "padding": "0.4rem 1rem",
                    "borderRadius": "1.5rem",
                    "fontSize": "0.8rem",
                    "fontWeight": "600",
                    "textTransform": "uppercase",
                    "letterSpacing": "0.05em"
                }
            ),
            text_align="center",
            margin_bottom="1.5rem"
        ),
        
        # Action buttons
        rx.hstack(
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("github", size=16),
                        rx.text("Code", font_size="0.85rem", font_weight="500"),
                        spacing="2",
                        align="center"
                    ),
                    size="2",
                    variant="outline",
                    style={
                        "background": "rgba(36, 41, 47, 0.8)",
                        "color": "white",
                        "border": "1px solid rgba(255, 255, 255, 0.15)",
                        "padding": "0.6rem 1.2rem",
                        "borderRadius": "0.75rem",
                        "transition": "all 0.2s ease",
                        "_hover": {
                            "background": "rgba(36, 41, 47, 1)",
                            "transform": "translateY(-1px)",
                            "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)"
                        }
                    }
                ),
                href=project["github"],
                target="_blank"
            ),
            rx.cond(
                project["demo"] != "",
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("external-link", size=16),
                            rx.text("Demo", font_size="0.85rem", font_weight="500"),
                            spacing="2",
                            align="center"
                        ),
                        size="2",
                        style={
                            "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                            "color": "white",
                            "border": "none",
                            "padding": "0.6rem 1.2rem",
                            "borderRadius": "0.75rem",
                            "transition": "all 0.2s ease",
                            "_hover": {
                                "transform": "translateY(-1px)",
                                "boxShadow": "0 8px 25px rgba(0, 212, 255, 0.4)"
                            }
                        }
                    ),
                    href=project["demo"],
                    target="_blank"
                )
            ),
            spacing="3",
            justify="center",
            padding="0.5rem",
            margin_top="auto"
        ),
        
        # Modern card styling
        padding="8",
        border_radius="2xl",
        style={
            "background": "linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.9))",
            "backdropFilter": "blur(20px)",
            "border": "1px solid rgba(148, 163, 184, 0.1)",
            "boxShadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
            "position": "relative",
            "overflow": "hidden",
            "_before": {
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "height": "1px",
                "background": "linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.4), transparent)",
                "opacity": "0",
                "transition": "opacity 0.3s ease"
            },
            "_hover": {
                "transform": "translateY(-4px)",
                "boxShadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 30px rgba(0, 212, 255, 0.1)",
                "borderColor": "rgba(0, 212, 255, 0.2)"
            },
            "_hover:before": {
                "opacity": "1"
            }
        },
        width="100%"
    )

def filter_section() -> rx.Component:
    """Create the filter section"""
    return rx.vstack(
        rx.box(
            rx.heading(
                "Projects",
                size="8",
                text_align="center",
                margin_bottom="0.5rem",
                font_weight="900",
                line_height="1.2",
                padding_y="0.5rem",
                style={
                    "background": "linear-gradient(135deg, #00d4ff 0%, #5b73ff 50%, #8b5cf6 100%)",
                    "backgroundClip": "text",
                    "WebkitBackgroundClip": "text",
                    "color": "transparent",
                    "textShadow": "0 0 30px rgba(0, 212, 255, 0.3)",
                    "letterSpacing": "-0.05em",
                    "animation": "slideInUp 0.8s ease-out",
                    "position": "relative",
                    "zIndex": "10",
                    "overflow": "visible"
                }
            ),
            rx.text(
                "With over 7 years of experience, I've successfully delivered 34+ projects across software houses, banking institutions, and product companies. From test automation frameworks to quality assurance solutions that drive business success.",
                color="gray.400",
                text_align="center",
                font_size="1.1rem",
                margin_bottom="3rem",
                max_width="700px",
                margin_x="auto",
                line_height="1.6",
                style={
                    "animation": "slideInUp 0.8s ease-out 0.2s both",
                    "position": "relative",
                    "zIndex": "10"
                }
            ),
            margin_bottom="2rem"
        ),
        
        # Filter section with responsive layout
        rx.box(
            # Desktop layout (horizontal)
            rx.tablet_and_desktop(
                rx.hstack(
                    # Technologies (multi-select)
                    rx.vstack(
                        rx.text("Technologies", color="gray.300", font_weight="bold", font_size="0.9rem", margin_bottom="0.5rem"),
                        rx.flex(
                            rx.foreach(
                                TECHNOLOGIES[:8],  # Show first 8 technologies
                                lambda tech: rx.badge(
                                    tech,
                                    variant="outline",
                                    cursor="pointer",
                                    on_click=ProjectsState.toggle_technology_filter(tech),
                                    style={
                                        "background": rx.cond(
                                            ProjectsState.selected_technologies.contains(tech),
                                            "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                            "rgba(30, 41, 59, 0.4)"
                                        ),
                                        "color": rx.cond(
                                            ProjectsState.selected_technologies.contains(tech),
                                            "white",
                                            "gray.400"
                                        ),
                                        "border": rx.cond(
                                            ProjectsState.selected_technologies.contains(tech),
                                            "1px solid rgba(0, 212, 255, 0.6)",
                                            "1px solid rgba(100, 116, 139, 0.2)"
                                        ),
                                        "padding": "0.3rem 0.7rem",
                                        "borderRadius": "1rem",
                                        "fontSize": "0.75rem",
                                        "fontWeight": "500",
                                        "transition": "all 0.2s ease",
                                        "_hover": {
                                            "transform": "translateY(-1px)",
                                            "boxShadow": "0 2px 8px rgba(0, 212, 255, 0.15)"
                                        }
                                    }
                                )
                            ),
                            gap="8",
                            wrap="wrap",
                            max_width="400px"
                        ),
                        align="start",
                        flex="1"
                    ),
                    
                    # Divider
                    rx.divider(orientation="vertical", height="80px", color="rgba(100, 116, 139, 0.2)"),
                    
                    # Domains (single select)
                    rx.vstack(
                        rx.text("Domain", color="gray.300", font_weight="bold", font_size="0.9rem", margin_bottom="0.5rem"),
                        rx.flex(
                            rx.foreach(
                                DOMAINS,
                                lambda domain: rx.badge(
                                    domain,
                                    variant="outline",
                                    cursor="pointer",
                                    on_click=ProjectsState.set_domain_filter(domain),
                                    style={
                                        "background": rx.cond(
                                            ProjectsState.selected_domain == domain,
                                            "linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)",
                                            "rgba(30, 41, 59, 0.4)"
                                        ),
                                        "color": rx.cond(
                                            ProjectsState.selected_domain == domain,
                                            "white",
                                            "gray.400"
                                        ),
                                        "border": rx.cond(
                                            ProjectsState.selected_domain == domain,
                                            "1px solid rgba(139, 92, 246, 0.6)",
                                            "1px solid rgba(100, 116, 139, 0.2)"
                                        ),
                                        "padding": "0.3rem 0.7rem",
                                        "borderRadius": "1rem",
                                        "fontSize": "0.75rem",
                                        "fontWeight": "500",
                                        "transition": "all 0.2s ease",
                                        "_hover": {
                                            "transform": "translateY(-1px)",
                                            "boxShadow": "0 2px 8px rgba(139, 92, 246, 0.15)"
                                        }
                                    }
                                )
                            ),
                            gap="8", 
                            wrap="wrap",
                            max_width="300px"
                        ),
                        align="start",
                        flex="1"
                    ),
                    
                    # Clear filters button
                    rx.button(
                        "Clear All",
                        on_click=ProjectsState.clear_all_filters,
                        size="2",
                        variant="outline",
                        style={
                            "background": "rgba(239, 68, 68, 0.1)",
                            "color": "red.300",
                            "border": "1px solid rgba(239, 68, 68, 0.3)",
                            "padding": "0.5rem 1rem",
                            "borderRadius": "0.75rem",
                            "fontSize": "0.8rem",
                            "fontWeight": "500",
                            "_hover": {
                                "background": "rgba(239, 68, 68, 0.2)",
                                "transform": "translateY(-1px)"
                            }
                        }
                    ),
                    
                    spacing="6",
                    align="start",
                    justify="center",
                    width="100%",
                    max_width="1000px",
                    margin="0 auto"
                )
            ),
            
            # Mobile layout (vertical)
            rx.mobile_only(
                rx.vstack(
                    # Technologies (multi-select)
                    rx.vstack(
                        rx.text("Technologies", color="gray.300", font_weight="bold", font_size="0.9rem", margin_bottom="0.5rem", text_align="center"),
                        rx.flex(
                            rx.foreach(
                                TECHNOLOGIES[:6],  # Show fewer on mobile
                                lambda tech: rx.badge(
                                    tech,
                                    variant="outline",
                                    cursor="pointer",
                                    on_click=ProjectsState.toggle_technology_filter(tech),
                                    style={
                                        "background": rx.cond(
                                            ProjectsState.selected_technologies.contains(tech),
                                            "linear-gradient(135deg, #00d4ff 0%, #5b73ff 100%)",
                                            "rgba(30, 41, 59, 0.4)"
                                        ),
                                        "color": rx.cond(
                                            ProjectsState.selected_technologies.contains(tech),
                                            "white",
                                            "gray.400"
                                        ),
                                        "border": rx.cond(
                                            ProjectsState.selected_technologies.contains(tech),
                                            "1px solid rgba(0, 212, 255, 0.6)",
                                            "1px solid rgba(100, 116, 139, 0.2)"
                                        ),
                                        "padding": "0.3rem 0.7rem",
                                        "borderRadius": "1rem",
                                        "fontSize": "0.7rem",
                                        "fontWeight": "500",
                                        "transition": "all 0.2s ease",
                                        "_hover": {
                                            "transform": "translateY(-1px)",
                                            "boxShadow": "0 2px 8px rgba(0, 212, 255, 0.15)"
                                        }
                                    }
                                )
                            ),
                            gap="6",
                            wrap="wrap",
                            justify="center",
                            width="100%"
                        ),
                        align="center",
                        width="100%",
                        margin_bottom="1.5rem"
                    ),
                    
                    # Horizontal divider for mobile
                    rx.divider(color="rgba(100, 116, 139, 0.2)", margin_y="1rem"),
                    
                    # Domains (single select)
                    rx.vstack(
                        rx.text("Domain", color="gray.300", font_weight="bold", font_size="0.9rem", margin_bottom="0.5rem", text_align="center"),
                        rx.flex(
                            rx.foreach(
                                DOMAINS,
                                lambda domain: rx.badge(
                                    domain,
                                    variant="outline",
                                    cursor="pointer",
                                    on_click=ProjectsState.set_domain_filter(domain),
                                    style={
                                        "background": rx.cond(
                                            ProjectsState.selected_domain == domain,
                                            "linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)",
                                            "rgba(30, 41, 59, 0.4)"
                                        ),
                                        "color": rx.cond(
                                            ProjectsState.selected_domain == domain,
                                            "white",
                                            "gray.400"
                                        ),
                                        "border": rx.cond(
                                            ProjectsState.selected_domain == domain,
                                            "1px solid rgba(139, 92, 246, 0.6)",
                                            "1px solid rgba(100, 116, 139, 0.2)"
                                        ),
                                        "padding": "0.3rem 0.7rem",
                                        "borderRadius": "1rem",  
                                        "fontSize": "0.7rem",
                                        "fontWeight": "500",
                                        "transition": "all 0.2s ease",
                                        "_hover": {
                                            "transform": "translateY(-1px)",
                                            "boxShadow": "0 2px 8px rgba(139, 92, 246, 0.15)"
                                        }
                                    }
                                )
                            ),
                            gap="6",
                            wrap="wrap",
                            justify="center",
                            width="100%"
                        ),
                        align="center",
                        width="100%",
                        margin_bottom="1.5rem"
                    ),
                    
                    # Clear filters button (mobile)
                    rx.button(
                        "Clear All",
                        on_click=ProjectsState.clear_all_filters,
                        size="2",
                        variant="outline",
                        style={
                            "background": "rgba(239, 68, 68, 0.1)",
                            "color": "red.300",
                            "border": "1px solid rgba(239, 68, 68, 0.3)",
                            "padding": "0.5rem 1rem",
                            "borderRadius": "0.75rem",
                            "fontSize": "0.8rem",
                            "fontWeight": "500",
                            "_hover": {
                                "background": "rgba(239, 68, 68, 0.2)",
                                "transform": "translateY(-1px)"
                            }
                        }
                    ),
                    
                    spacing="4",
                    align="center",
                    width="100%",
                    padding="1rem"
                )
            ),
            
            # Filter status indicator
            rx.cond(
                (ProjectsState.selected_technologies.length() > 0) | (ProjectsState.selected_domain != "All"),
                rx.text(
                    rx.cond(
                        ProjectsState.selected_technologies.length() > 0,
                        rx.cond(
                            ProjectsState.selected_technologies.contains("All"),
                            "Filtered by all technologies",
                            f"Filtered by {ProjectsState.selected_technologies.length()} technologies"
                        ),
                        ""
                    ) + rx.cond(
                        ProjectsState.selected_domain != "All",
                        f" and {ProjectsState.selected_domain} domain",
                        ""
                    ),
                    color="cyan.300",
                    font_size="0.8rem",
                    text_align="center",
                    margin_top="1rem",
                    font_style="italic"
                )
            ),
            
            padding="2rem",
            background="rgba(15, 23, 42, 0.6)",
            border_radius="xl",
            border="1px solid rgba(100, 116, 139, 0.1)",
            margin_bottom="3rem",
            style={
                "animation": "slideInUp 0.8s ease-out 0.3s both",
                "position": "relative",
                "zIndex": "10"
            }
        ),
        
        align="center",
        width="100%"
    )

@rx.page(route="/projects", title="Marcin Orgacki | Projects")
def projects_page() -> rx.Component:
    """Projects page component"""
    header = Header()
    footer = Footer()
    header_component = header.build()
    footer_component = footer.build()
    sidebar_component = sidebar()
    
    # Layout without sidebar - same as main page
    layout = rx.vstack(
        header_component,
        rx.box(
            # Header section with filters
            filter_section(),
            
            # Projects grid - modern multi-column layout
            rx.box(
                rx.grid(
                    rx.foreach(
                        ProjectsState.projects,
                        project_card
                    ),
                    columns={"base": "1", "sm": "1", "md": "2", "lg": "3", "xl": "3"},
                    spacing="8",
                    width="100%"
                ),
                width="100%",
                max_width="1400px",
                margin="0 auto",
                padding="2rem"
            ),
            
            # Content styling
            padding="2rem 0",
            flex="1"
        ),
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