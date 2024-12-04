# colorsys — Conversions between color systems

**Colorsys Module Documentation**
=====================================

The `colorsys` module provides functions to convert between different color spaces.

**Functions**
--------------

### 1. HSB to RGB Conversion

```python
import colorsys

def hsb_to_rgb(h, s, v):
    """
    Convert HSV (Hue-Saturation-Value) color to RGB (Red-Green-Blue).

    Parameters:
        h (float): Hue value in the range [0, 1].
        s (float): Saturation value in the range [0, 1].
        v (float): Value (brightness) value in the range [0, 1].

    Returns:
        tuple: RGB values as a tuple of three floats in the range [0, 1].
    """
    # Convert HSV to RGB using colorsys.hsv_to_rgb function
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (r, g, b)

# Example usage:
h, s, v = 0.5, 0.7, 0.9
rgb_values = hsb_to_rgb(h, s, v)
print("RGB Values:", rgb_values)
```

### 2. RGB to HSV Conversion

```python
import colorsys

def rgb_to_hsv(r, g, b):
    """
    Convert RGB (Red-Green-Blue) color to HSV (Hue-Saturation-Value).

    Parameters:
        r (float): Red component value in the range [0, 1].
        g (float): Green component value in the range [0, 1].
        b (float): Blue component value in the range [0, 1].

    Returns:
        tuple: HSV values as a tuple of three floats in the range [0, 1].
    """
    # Convert RGB to HSV using colorsys.rgb_to_hsv function
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return (h, s, v)

# Example usage:
r, g, b = 0.2, 0.4, 0.6
hsv_values = rgb_to_hsv(r, g, b)
print("HSV Values:", hsv_values)
```

### 3. RGB to YUV Conversion

```python
import colorsys

def rgb_to_yuv(r, g, b):
    """
    Convert RGB (Red-Green-Blue) color to YUV (Luminance-Chrominance).

    Parameters:
        r (float): Red component value in the range [0, 1].
        g (float): Green component value in the range [0, 1].
        b (float): Blue component value in the range [0, 1].

    Returns:
        tuple: YUV values as a tuple of three floats in the range [-128, 127].
    """
    # Convert RGB to YUV using colorsys.rgb_to_yuv function
    y, u, v = colorsys.rgb_to_yuv(r, g, b)
    return (y, u, v)

# Example usage:
r, g, b = 0.1, 0.3, 0.5
yuv_values = rgb_to_yuv(r, g, b)
print("YUV Values:", yuv_values)
```

### 4. YUV to RGB Conversion

```python
import colorsys

def yuv_to_rgb(y, u, v):
    """
    Convert YUV (Luminance-Chrominance) color to RGB (Red-Green-Blue).

    Parameters:
        y (float): Luminance component value in the range [-128, 127].
        u (float): Chrominance (blue) component value in the range [-128, 127].
        v (float): Chrominance (red) component value in the range [-128, 127].

    Returns:
        tuple: RGB values as a tuple of three floats in the range [0, 1].
    """
    # Convert YUV to RGB using colorsys.yuv_to_rgb function
    r, g, b = colorsys.yuv_to_rgb(y, u, v)
    return (r, g, b)

# Example usage:
y, u, v = 100, -50, 75
rgb_values = yuv_to_rgb(y, u, v)
print("RGB Values:", rgb_values)
```

### 5. HSL to RGB Conversion

```python
import colorsys

def hsl_to_rgb(h, s, l):
    """
    Convert HSL (Hue-Saturation-Lightness) color to RGB (Red-Green-Blue).

    Parameters:
        h (float): Hue value in the range [0, 1].
        s (float): Saturation value in the range [0, 1].
        l (float): Lightness value in the range [0, 1].

    Returns:
        tuple: RGB values as a tuple of three floats in the range [0, 1].
    """
    # Convert HSL to RGB using colorsys.hsl_to_rgb function
    r, g, b = colorsys.hsl_to_rgb(h, s, l)
    return (r, g, b)

# Example usage:
h, s, l = 0.6, 0.8, 0.9
rgb_values = hsl_to_rgb(h, s, l)
print("RGB Values:", rgb_values)
```

### 6. RGB to HSL Conversion

```python
import colorsys

def rgb_to_hsl(r, g, b):
    """
    Convert RGB (Red-Green-Blue) color to HSL (Hue-Saturation-Lightness).

    Parameters:
        r (float): Red component value in the range [0, 1].
        g (float): Green component value in the range [0, 1].
        b (float): Blue component value in the range [0, 1].

    Returns:
        tuple: HSL values as a tuple of three floats in the range [0, 1].
    """
    # Convert RGB to HSL using colorsys.rgb_to_hsl function
    h, s, l = colorsys.rgb_to_hsl(r, g, b)
    return (h, s, l)

# Example usage:
r, g, b = 0.2, 0.4, 0.6
hsl_values = rgb_to_hsl(r, g, b)
print("HSL Values:", hsl_values)
```

### 7. YUV to HSL Conversion

```python
import colorsys

def yuv_to_hsl(y, u, v):
    """
    Convert YUV (Luminance-Chrominance) color to HSL (Hue-Saturation-Lightness).

    Parameters:
        y (float): Luminance component value in the range [-128, 127].
        u (float): Chrominance (blue) component value in the range [-128, 127].
        v (float): Chrominance (red) component value in the range [-128, 127].

    Returns:
        tuple: HSL values as a tuple of three floats in the range [0, 1].
    """
    # Convert YUV to HSL using colorsys.yuv_to_hsl function
    h, s, l = colorsys.yuv_to_hsl(y, u, v)
    return (h, s, l)

# Example usage:
y, u, v = 100, -50, 75
hsl_values = yuv_to_hsl(y, u, v)
print("HSL Values:", hsl_values)
```

### 8. HSL to YUV Conversion

```python
import colorsys

def hsl_to_yuv(h, s, l):
    """
    Convert HSL (Hue-Saturation-Lightness) color to YUV (Luminance-Chrominance).

    Parameters:
        h (float): Hue value in the range [0, 1].
        s (float): Saturation value in the range [0, 1].
        l (float): Lightness value in the range [0, 1].

    Returns:
        tuple: YUV values as a tuple of three floats in the range [-128, 127].
    """
    # Convert HSL to YUV using colorsys.hsl_to_yuv function
    y, u, v = colorsys.hsl_to_yuv(h, s, l)
    return (y, u, v)

# Example usage:
h, s, l = 0.7, 0.9, 1.0
yuv_values = hsl_to_yuv(h, s, l)
print("YUV Values:", yuv_values)
```
