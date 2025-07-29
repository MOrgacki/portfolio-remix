import reflex as rx

# CSS animations and keyframes
animations_css = {
    "@keyframes float": {
        "0%": {"transform": "translateY(0px) rotate(0deg)", "opacity": "0.7"},
        "50%": {"transform": "translateY(-20px) rotate(180deg)", "opacity": "1"},
        "100%": {"transform": "translateY(0px) rotate(360deg)", "opacity": "0.7"},
    },
    "@keyframes floatReverse": {
        "0%": {"transform": "translateY(0px) rotate(0deg)", "opacity": "0.5"},
        "50%": {"transform": "translateY(20px) rotate(-180deg)", "opacity": "0.8"},
        "100%": {"transform": "translateY(0px) rotate(-360deg)", "opacity": "0.5"},
    },
    "@keyframes pulse": {
        "0%": {"transform": "scale(1)", "opacity": "0.4"},
        "50%": {"transform": "scale(1.1)", "opacity": "0.7"},
        "100%": {"transform": "scale(1)", "opacity": "0.4"},
    },
    "@keyframes drift": {
        "0%": {"transform": "translateX(0px) translateY(0px)"},
        "25%": {"transform": "translateX(30px) translateY(-30px)"},
        "50%": {"transform": "translateX(-20px) translateY(-60px)"},
        "75%": {"transform": "translateX(-40px) translateY(-30px)"},
        "100%": {"transform": "translateX(0px) translateY(0px)"},
    },
    "@keyframes glow": {
        "0%": {"boxShadow": "0 0 20px rgba(0, 212, 255, 0.3)"},
        "50%": {"boxShadow": "0 0 40px rgba(0, 212, 255, 0.6), 0 0 60px rgba(91, 115, 255, 0.4)"},
        "100%": {"boxShadow": "0 0 20px rgba(0, 212, 255, 0.3)"},
    },
    "@keyframes fadeInUp": {
        "0%": {"opacity": "0", "transform": "translateY(30px)"},
        "100%": {"opacity": "1", "transform": "translateY(0)"},
    },
    "@keyframes slideInLeft": {
        "0%": {"opacity": "0", "transform": "translateX(-30px)"},
        "100%": {"opacity": "1", "transform": "translateX(0)"},
    }
}

def animated_shape(shape_type: str, size: str, color: str, animation: str, duration: str, delay: str = "0s", position: dict = None) -> rx.Component:
    """Create an animated background shape"""
    if position is None:
        position = {"top": "50%", "left": "50%"}
    
    base_style = {
        "position": "absolute",
        "borderRadius": "50%" if shape_type == "circle" else "10px",
        "width": size,
        "height": size,
        "background": color,
        "animation": f"{animation} {duration} infinite {delay}",
        "pointerEvents": "none",
        "zIndex": "1",
        **position
    }
    
    if shape_type == "triangle":
        base_style.update({
            "width": "0",
            "height": "0",
            "borderLeft": f"{size} solid transparent",
            "borderRight": f"{size} solid transparent",
            "borderBottom": f"{size} solid {color}",
            "borderRadius": "0",
            "background": "transparent"
        })
    elif shape_type == "diamond":
        base_style.update({
            "transform": "rotate(45deg)",
            "borderRadius": "10px"
        })
    
    return rx.box(style=base_style)

def background_shapes() -> rx.Component:
    """Create animated background shapes"""
    return rx.box(
        # Floating circles
        animated_shape(
            "circle", "80px", 
            "linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(91, 115, 255, 0.1) 100%)",
            "float", "6s", "0s",
            {"top": "10%", "left": "10%"}
        ),
        animated_shape(
            "circle", "120px",
            "linear-gradient(135deg, rgba(91, 115, 255, 0.08) 0%, rgba(0, 212, 255, 0.08) 100%)",
            "floatReverse", "8s", "1s",
            {"top": "70%", "right": "15%"}
        ),
        animated_shape(
            "circle", "60px",
            "linear-gradient(135deg, rgba(0, 212, 255, 0.12) 0%, rgba(91, 115, 255, 0.12) 100%)",
            "drift", "10s", "2s",
            {"top": "30%", "right": "25%"}
        ),
        
        # Pulsing shapes
        animated_shape(
            "diamond", "40px",
            "rgba(0, 212, 255, 0.15)",
            "pulse", "4s", "1.5s",
            {"top": "20%", "right": "10%"}
        ),
        animated_shape(
            "diamond", "35px",
            "rgba(91, 115, 255, 0.12)",
            "pulse", "5s", "3s",
            {"bottom": "25%", "left": "20%"}
        ),
        
        # Glowing orbs
        animated_shape(
            "circle", "25px",
            "rgba(0, 212, 255, 0.6)",
            "glow", "3s", "0.5s",
            {"top": "15%", "left": "70%"}
        ),
        animated_shape(
            "circle", "30px",
            "rgba(91, 115, 255, 0.5)",
            "glow", "4s", "2s",
            {"bottom": "20%", "right": "30%"}
        ),
        
        # Additional floating elements
        animated_shape(
            "circle", "50px",
            "linear-gradient(135deg, rgba(0, 212, 255, 0.06) 0%, rgba(91, 115, 255, 0.06) 100%)",
            "float", "7s", "4s",
            {"bottom": "40%", "left": "5%"}
        ),
        animated_shape(
            "diamond", "45px",
            "rgba(0, 212, 255, 0.08)",
            "drift", "9s", "1s",
            {"top": "60%", "left": "40%"}
        ),
        
        position="fixed",
        top="0",
        left="0",
        width="100%",
        height="100%",
        overflow="hidden",
        z_index="0",
        pointer_events="none"
    )

def particle_field() -> rx.Component:
    """Create a subtle particle field effect"""
    particles = []
    
    # Create multiple small particles
    for i in range(12):
        particles.append(
            rx.box(
                style={
                    "position": "absolute",
                    "width": "2px",
                    "height": "2px",
                    "background": "rgba(0, 212, 255, 0.4)",
                    "borderRadius": "50%",
                    "top": f"{10 + (i * 7)}%",
                    "left": f"{5 + (i * 8)}%",
                    "animation": f"pulse {3 + (i % 3)}s infinite {i * 0.5}s",
                    "pointerEvents": "none"
                }
            )
        )
    
    return rx.box(
        *particles,
        position="fixed",
        top="0",
        left="0",
        width="100%",
        height="100%",
        z_index="0",
        pointer_events="none"
    )

def enhanced_gradient_overlay() -> rx.Component:
    """Create an enhanced gradient overlay with animation"""
    return rx.box(
        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "background": """
                radial-gradient(circle at 20% 80%, rgba(0, 212, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(91, 115, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(0, 212, 255, 0.05) 0%, transparent 50%)
            """,
            "animation": "pulse 8s infinite",
            "zIndex": "1",
            "pointerEvents": "none"
        }
    )

def animated_background() -> rx.Component:
    """Complete animated background system"""
    return rx.box(
        # Base shapes
        background_shapes(),
        
        # Particle field
        particle_field(),
        
        # Enhanced gradient overlay
        enhanced_gradient_overlay(),
        
        position="fixed",
        top="0",
        left="0",
        width="100%",
        height="100%",
        z_index="0",
        pointer_events="none"
    )