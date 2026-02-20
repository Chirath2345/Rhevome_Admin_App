# utilities/responsive_utils.py

def set_viewport(page, screen_name):
    """Set page viewport for responsiveness testing"""
    if screen_name.lower() == "pc":
        page.set_viewport_size({"width": 1920, "height": 1080})
    elif screen_name.lower() == "laptop":
        page.set_viewport_size({"width": 1366, "height": 768})
    elif screen_name.lower() == "ipad":
        page.set_viewport_size({"width": 768, "height": 1024})
    else:
        raise ValueError(f"Unknown screen size: {screen_name}")
