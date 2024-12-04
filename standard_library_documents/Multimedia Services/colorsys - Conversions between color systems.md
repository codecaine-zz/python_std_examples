# colorsys - Conversions between color systems

The `colorsys` module in Python provides a set of functions to convert colors among different models, such as RGB, HSV, CMYK, and more. Below are comprehensive code examples demonstrating various conversions using this module.

```python
import colorsys

# Example 1: Convert from RGB to HSV
def rgb_to_hsv(rgb):
    """
    Converts an RGB tuple (r, g, b) to an HSV tuple (h, s, v).

    Parameters:
    rgb (tuple): A tuple containing three integers representing the red, green, and blue channels of a color.

    Returns:
    tuple: A tuple containing three floats representing the hue (0-1), saturation (0-1), and value (0-1) of the color.
    """
    r, g, b = rgb / 255.0
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return h, s, v

# Example 2: Convert from HSV to RGB
def hsv_to_rgb(hsv):
    """
    Converts an HSV tuple (h, s, v) to an RGB tuple (r, g, b).

    Parameters:
    hsv (tuple): A tuple containing three floats representing the hue (0-1), saturation (0-1), and value (0-1) of a color.

    Returns:
    tuple: A tuple containing three integers representing the red, green, and blue channels of the color.
    """
    h, s, v = hsv
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

# Example 3: Convert from RGB to CMYK
def rgb_to_cmyk(rgb):
    """
    Converts an RGB tuple (r, g, b) to a CMYK tuple (c, m, y, k).

    Parameters:
    rgb (tuple): A tuple containing three integers representing the red, green, and blue channels of a color.

    Returns:
    tuple: A tuple containing four floats representing the cyan, magenta, yellow, and key (black) channels of the color.
    """
    r, g, b = rgb / 255.0
    c = 1 - r
    m = 1 - g
    y = 1 - b
    k = min(c, m, y)
    if k == 1:
        return 0, 0, 0, 1
    else:
        c = (c - k) / (1 - k)
        m = (m - k) / (1 - k)
        y = (y - k) / (1 - k)
        return c, m, y, k

# Example 4: Convert from CMYK to RGB
def cmyk_to_rgb(cmyk):
    """
    Converts a CMYK tuple (c, m, y, k) to an RGB tuple (r, g, b).

    Parameters:
    cmyk (tuple): A tuple containing four floats representing the cyan, magenta, yellow, and key (black) channels of a color.

    Returns:
    tuple: A tuple containing three integers representing the red, green, and blue channels of the color.
    """
    c, m, y, k = cmyk
    r = 1 - c * (1 - k)
    g = 1 - m * (1 - k)
    b = 1 - y * (1 - k)
    return int(r * 255), int(g * 255), int(b * 255)

# Example 5: Convert from RGB to HSL
def rgb_to_hsl(rgb):
    """
    Converts an RGB tuple (r, g, b) to an HSL tuple (h, s, l).

    Parameters:
    rgb (tuple): A tuple containing three integers representing the red, green, and blue channels of a color.

    Returns:
    tuple: A tuple containing three floats representing the hue (0-1), saturation (0-1), and lightness (0-1) of the color.
    """
    r, g, b = rgb / 255.0
    h, s, l = colorsys.rgb_to_hls(r, g, b)
    return h, s, l

# Example 6: Convert from HSL to RGB
def hsl_to_rgb(hsl):
    """
    Converts an HSL tuple (h, s, l) to an RGB tuple (r, g, b).

    Parameters:
    hsl (tuple): A tuple containing three floats representing the hue (0-1), saturation (0-1), and lightness (0-1) of a color.

    Returns:
    tuple: A tuple containing three integers representing the red, green, and blue channels of the color.
    """
    h, s, l = hsl
    r, g, b = colorsys.hls_to_rgb(h, s, l)
    return int(r * 255), int(g * 255), int(b * 255)

# Example 7: Convert from RGB to hexadecimal string
def rgb_to_hex(rgb):
    """
    Converts an RGB tuple (r, g, b) to a hexadecimal string.

    Parameters:
    rgb (tuple): A tuple containing three integers representing the red, green, and blue channels of a color.

    Returns:
    str: A string representing the hexadecimal representation of the color.
    """
    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# Example 8: Convert from hex to RGB tuple
def hex_to_rgb(hex_color):
    """
    Converts a hexadecimal string to an RGB tuple (r, g, b).

    Parameters:
    hex_color (str): A string representing the hexadecimal color code.

    Returns:
    tuple: A tuple containing three integers representing the red, green, and blue channels of the color.
    """
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return r, g, b

# Example 9: Convert from RGB to XYZ
def rgb_to_xyz(rgb):
    """
    Converts an RGB tuple (r, g, b) to an XYZ tuple.

    Parameters:
    rgb (tuple): A tuple containing three integers representing the red, green, and blue channels of a color.

    Returns:
    tuple: A tuple containing three floats representing the X, Y, and Z coordinates in the CIE XYZ color space.
    """
    r, g, b = rgb / 255.0
    r = r ** 3 if r > 0.04045 else (r + 0.055) / 1.055
    g = g ** 3 if g > 0.04045 else (g + 0.055) / 1.055
    b = b ** 3 if b > 0.04045 else (b + 0.055) / 1.055
    r *= 129.876
    g *= 129.876
    b *= 129.876
    return 0.4124 * r, 0.3576 * g, 0.1805 * b

# Example 10: Convert from XYZ to RGB
def xyz_to_rgb(xyz):
    """
    Converts an XYZ tuple (x, y, z) to an RGB tuple.

    Parameters:
    xyz (tuple): A tuple containing three floats representing the X, Y, and Z coordinates in the CIE XYZ color space.

    Returns:
    tuple: A tuple containing three integers representing the red, green, and blue channels of the color.
    """
    x, y, z = xyz
    r = 3.2406 * x - 1.5372 * y - 0.4986 * z
    g = -0.9689 * x + 1.8758 * y + 0.0415 * z
    b = 0.0557 * x - 0.2040 * y + 1.0570 * z
    r, g, b = [129.876 / c for c in (r, g, b)]
    r = r ** (1/3) if r > 0.0031308 else r * 1.055 - 0.055
    g = g ** (1/3) if g > 0.0031308 else g * 1.055 - 0.055
    b = b ** (1/3) if b > 0.0031308 else b * 1.055 - 0.055
    return int(round(r * 255)), int(round(g * 255)), int(round(b * 255))

# Example usage:
rgb = (255, 0, 0)
hex_color = rgb_to_hex(rgb)
xyz = rgb_to_xyz(rgb)
print("RGB:", rgb)
print("Hex Color:", hex_color)
print("XYZ Coordinates:", xyz)

# Convert XYZ back to RGB
new_rgb = xyz_to_rgb(xyz)
print("Converted RGB from XYZ:", new_rgb)
```

This Python script defines functions to convert between various color representations such as RGB, hexadecimal, HSL, CIE XYZ, and more. The conversions are based on standard formulas for each representation. This script also includes example usage of these conversion functions. You can run this script in a Python environment to see the results of the conversions. Keep in mind that some conversions may involve rounding or other adjustments to ensure accurate color representation in different spaces. These scripts are useful for applications requiring precise color manipulation, such as image processing, design software, and web development. Enjoy experimenting with these conversions!  "
