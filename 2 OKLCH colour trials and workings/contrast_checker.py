from coloraide import Color

def get_contrast_ratio(color1, color2):
    """Calculate WCAG contrast ratio between two colors"""
    return color1.contrast(color2, method="wcag21")

def get_wcag_level(contrast_ratio, is_large_text=False):
    """Determine WCAG compliance level"""
    if is_large_text:
        if contrast_ratio >= 4.5:
            return "AAA"
        elif contrast_ratio >= 3.0:
            return "AA"
        else:
            return "Fail"
    else:
        if contrast_ratio >= 7.0:
            return "AAA"
        elif contrast_ratio >= 4.5:
            return "AA"
        else:
            return "Fail"

def create_lightness_scale(base_l, base_c, base_h, steps=4):
    """Create lighter and darker variations of a base color"""
    colors = []
    
    # Lighter colors
    for i in range(steps, 0, -1):
        l = base_l + (i * 0.1)
        color = Color("oklch", [l, base_c, base_h])
        
        if not color.in_gamut("srgb"):
            color = color.fit("srgb")
        
        colors.append({
            'name': f'Light +{i}',
            'color': color,
            'hex': color.to_string(hex=True),
            'oklch': f"oklch({l:.2f} {base_c:.2f} {base_h})"
        })
    
    # Base color
    base_color = Color("oklch", [base_l, base_c, base_h])
    if not base_color.in_gamut("srgb"):
        base_color = base_color.fit("srgb")
    
    colors.append({
        'name': 'Base',
        'color': base_color,
        'hex': base_color.to_string(hex=True),
        'oklch': f"oklch({base_l:.2f} {base_c:.2f} {base_h})"
    })
    
    # Darker colors
    for i in range(1, steps + 1):
        l = base_l - (i * 0.1)
        color = Color("oklch", [l, base_c, base_h])
        
        if not color.in_gamut("srgb"):
            color = color.fit("srgb")
        
        colors.append({
            'name': f'Dark -{i}',
            'color': color,
            'hex': color.to_string(hex=True),
            'oklch': f"oklch({l:.2f} {base_c:.2f} {base_h})"
        })
    
    return colors

def analyze_contrast(background_oklch, base_l=0.50, base_c=0.11, base_h=140, steps=4):
    """Analyze contrast ratios for all colors against a background"""
    
    # Parse background color
    bg_color = Color("oklch", background_oklch)
    if not bg_color.in_gamut("srgb"):
        bg_color = bg_color.fit("srgb")
    
    print("=" * 80)
    print(f"WCAG CONTRAST ANALYSIS")
    print("=" * 80)
    print(f"\nBackground: {bg_color.to_string(hex=True)} - oklch({background_oklch[0]:.2f} {background_oklch[1]:.2f} {background_oklch[2]})")
    print("\nNormal Text: AA = 4.5:1, AAA = 7:1")
    print("Large Text:  AA = 3:1,   AAA = 4.5:1")
    print("=" * 80)
    
    # Generate color scale
    colors = create_lightness_scale(base_l, base_c, base_h, steps)
    
    # Analyze each color
    print(f"\n{'Color':<12} {'Hex':<10} {'Contrast':<10} {'Normal':<8} {'Large':<8}")
    print("-" * 80)
    
    aa_normal = []
    aaa_normal = []
    aa_large = []
    aaa_large = []
    
    for item in colors:
        color = item['color']
        contrast = get_contrast_ratio(color, bg_color)
        
        normal_level = get_wcag_level(contrast, is_large_text=False)
        large_level = get_wcag_level(contrast, is_large_text=True)
        
        print(f"{item['name']:<12} {item['hex']:<10} {contrast:>6.2f}:1   {normal_level:<8} {large_level:<8}")
        
        # Categorize
        if normal_level == "AA":
            aa_normal.append(item)
        elif normal_level == "AAA":
            aaa_normal.append(item)
            aa_normal.append(item)  # AAA also meets AA
        
        if large_level == "AA":
            aa_large.append(item)
        elif large_level == "AAA":
            aaa_large.append(item)
            aa_large.append(item)  # AAA also meets AA
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nNormal Text (body copy, UI labels):")
    print(f"  AA compliant:  {len(aa_normal)} colors")
    print(f"  AAA compliant: {len(aaa_normal)} colors")
    
    print(f"\nLarge Text (18pt+, or 14pt+ bold):")
    print(f"  AA compliant:  {len(aa_large)} colors")
    print(f"  AAA compliant: {len(aaa_large)} colors")
    
    # Show recommended colors
    if aaa_normal:
        print(f"\n{'Recommended for AAA (normal text):':<40}")
        for item in aaa_normal:
            print(f"  {item['name']:<12} {item['hex']}")
    
    if aa_normal:
        print(f"\n{'Recommended for AA (normal text):':<40}")
        for item in aa_normal:
            if item not in aaa_normal:  # Don't duplicate AAA colors
                print(f"  {item['name']:<12} {item['hex']}")

# Usage example
if __name__ == "__main__":
    # Your base palette settings
    base_lightness = 0.50
    base_chroma = 0.11
    base_hue = 140
    
    # Example: Using "Dark -2" as background
    # From your palette: oklch(0.30 0.11 140) = #013900
    print("\n### Analysis with Dark -2 background ###\n")
    analyze_contrast(
        background_oklch=[0.30, 0.11, 140],
        base_l=base_lightness,
        base_c=base_chroma,
        base_h=base_hue
    )
    
    # You can test other backgrounds too
    print("\n\n### Analysis with Dark -3 background ###\n")
    analyze_contrast(
        background_oklch=[0.20, 0.11, 140],
        base_l=base_lightness,
        base_c=base_chroma,
        base_h=base_hue
    )