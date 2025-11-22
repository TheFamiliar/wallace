# Calculate tints, shades and hues from a base colour
# ./venv/bin/python colour_calcs.py

from coloraide import Color

def create_lightness_scale(base_l, base_c, base_h, steps=4):
    """Create lighter and darker variations of a base color"""
    colors = []
    
    # Lighter colors
    for i in range(steps, 0, -1):
        l = base_l + (i * 0.1)  # Adjust increment as needed
        color = Color("oklch", [l, base_c, base_h])
        
        # Check gamut
        if not color.in_gamut("srgb"):
            print(f"Warning: Lightness {l:.2f} is outside sRGB gamut")
            color = color.fit("srgb")
        
        colors.append({
            'oklch': f"oklch({l:.2f} {base_c:.2f} {base_h})",
            'hex': color.to_string(hex=True)
        })
    
    # Base color
    base_color = Color("oklch", [base_l, base_c, base_h])
    if not base_color.in_gamut("srgb"):
        print(f"Warning: Base color is outside sRGB gamut")
        base_color = base_color.fit("srgb")
    
    colors.append({
        'oklch': f"oklch({base_l:.2f} {base_c:.2f} {base_h})",
        'hex': base_color.to_string(hex=True)
    })
    
    # Darker colors
    for i in range(1, steps + 1):
        l = base_l - (i * 0.1)
        color = Color("oklch", [l, base_c, base_h])
        
        if not color.in_gamut("srgb"):
            print(f"Warning: Lightness {l:.2f} is outside sRGB gamut")
            color = color.fit("srgb")
        
        colors.append({
            'oklch': f"oklch({l:.2f} {base_c:.2f} {base_h})",
            'hex': color.to_string(hex=True)
        })
    
    return colors

def create_hue_palette(base_l, base_c, hue_step=30):
    """Create chromatic palette by rotating hue"""
    colors = []
    
    for h in range(0, 360, hue_step):
        color = Color("oklch", [base_l, base_c, h])
        
        if not color.in_gamut("srgb"):
            print(f"Warning: Hue {h}° is outside sRGB gamut")
            color = color.fit("srgb")
        
        colors.append({
            'hue': h,
            'oklch': f"oklch({base_l:.2f} {base_c:.2f} {h})",
            'hex': color.to_string(hex=True)
        })
    
    return colors

# Usage
if __name__ == "__main__":
    # Your forest green base
    base_lightness = 0.5
    base_chroma = 0.11  # Adjust based on your forest green
    base_hue = 140      # Approximate hue for forest green
    
    # Generate lightness scale
    print("=== Lightness Scale ===")
    lightness_scale = create_lightness_scale(base_lightness, base_chroma, base_hue)
    for i, color in enumerate(lightness_scale):
        print(f"{i}: {color['hex']} - {color['oklch']}")
    
    print("\n=== Chromatic Palette (30° intervals) ===")
    chromatic_palette = create_hue_palette(base_lightness, base_chroma)
    for color in chromatic_palette:
        print(f"{color['hue']:3d}°: {color['hex']} - {color['oklch']}")