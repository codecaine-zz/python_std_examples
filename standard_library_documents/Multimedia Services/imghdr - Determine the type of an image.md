# imghdr - Determine the type of an image

The `imghdr` module in Python is used to identify the format of image files by checking their first few bytes. This can be particularly useful when dealing with images where you need to programmatically determine the file type without relying on file extensions.

Below are comprehensive code examples for each functionality available in the `imghdr` module:

### 1. `identify(filename)`

This function takes a filename as input and returns a tuple containing two elements: the image format (if recognized) and an error message if no format is recognized.

```python
import imghdr

def identify_image_format(filename):
    result = imghdr.identify(filename)
    if result:
        format, error = result
        print(f"Image format identified as: {format}")
    else:
        print("No image format found. Error:", error)

# Example usage
identify_image_format('example.jpg')
```

### 2. `what(buf)`

This function takes a bytes-like object containing the first few bytes of an image file and returns the image format if recognized, or `None` if no format is recognized.

```python
import imghdr

def identify_image_format_from_bytes(buffer):
    result = imghdr.what(buffer)
    if result:
        print(f"Image format identified as: {result}")
    else:
        print("No image format found.")

# Example usage
buffer = b'\xFFD8\xFFE0\x00\x10JFIF\x00'
identify_image_format_from_bytes(buffer)
```

### 3. `isgif(buf)`

This function checks if the provided bytes-like object contains a GIF file.

```python
import imghdr

def is_gif_file(buffer):
    result = imghdr.isgif(buffer)
    print(f"Is the buffer a GIF file? {result}")

# Example usage
buffer = b'\x47\x49\x46\x38\x39'
is_gif_file(buffer)
```

### 4. `ispng(buf)`

This function checks if the provided bytes-like object contains a PNG file.

```python
import imghdr

def is_png_file(buffer):
    result = imghdr.ispng(buffer)
    print(f"Is the buffer a PNG file? {result}")

# Example usage
buffer = b'\x89PNG\r\n\x1a\n'
is_png_file(buffer)
```

### 5. `issvg(buf)`

This function checks if the provided bytes-like object contains an SVG file.

```python
import imghdr

def is_svg_file(buffer):
    result = imghdr.issvg(buffer)
    print(f"Is the buffer an SVG file? {result}")

# Example usage
buffer = b'<?xml version="1.0" encoding="utf-8"?><svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">'
is_svg_file(buffer)
```

### 6. `istiff(buf)`

This function checks if the provided bytes-like object contains a TIFF file.

```python
import imghdr

def is_tiff_file(buffer):
    result = imghdr.istiff(buffer)
    print(f"Is the buffer a TIFF file? {result}")

# Example usage
buffer = b'II\x2a\x00\x16'
is_tiff_file(buffer)
```

### 7. `iswebp(buf)`

This function checks if the provided bytes-like object contains a WebP file.

```python
import imghdr

def is_webp_file(buffer):
    result = imghdr.iswebp(buffer)
    print(f"Is the buffer a WebP file? {result}")

# Example usage
buffer = b'\x52\x49\x46\x50\x2A\x31\x2E\x30'
is_webp_file(buffer)
```

### 8. `isspc(buf)`

This function checks if the provided bytes-like object contains a SPARK file.

```python
import imghdr

def is_spark_file(buffer):
    result = imghdr.isspc(buffer)
    print(f"Is the buffer a SPARK file? {result}")

# Example usage
buffer = b'\x53\x50\x42\x48'
is_spark_file(buffer)
```

### 9. `iseps(buf)`

This function checks if the provided bytes-like object contains an EPS (Encapsulated PostScript) file.

```python
import imghdr

def is_eps_file(buffer):
    result = imghdr.iseps(buffer)
    print(f"Is the buffer an EPS file? {result}")

# Example usage
buffer = b'\x25\x21\x43\x0D\x0A\x0A'
is_eps_file(buffer)
```

### 10. `isppm(buf)`

This function checks if the provided bytes-like object contains a PPM (Portable Pixel Map) file.

```python
import imghdr

def is_ppm_file(buffer):
    result = imghdr.isppm(buffer)
    print(f"Is the buffer a PPM file? {result}")

# Example usage
buffer = b'P3\n20 20\n150\n'
is_ppm_file(buffer)
```

### 11. `ispbm(buf)`

This function checks if the provided bytes-like object contains a PBM (Portable BitMap) file.

```python
import imghdr

def is_pbm_file(buffer):
    result = imghdr.ispbm(buffer)
    print(f"Is the buffer a PBM file? {result}")

# Example usage
buffer = b'P1\n20 20'
is_pbm_file(buffer)
```

### 12. `ispgm(buf)`

This function checks if the provided bytes-like object contains a PGM (Portable GrayMap) file.

```python
import imghdr

def is_pgm_file(buffer):
    result = imghdr.ispgm(buffer)
    print(f"Is the buffer a PGM file? {result}")

# Example usage
buffer = b'P5\n20 20\n150'
is_pgm_file(buffer)
```

### 13. `isxpm(buf)`

This function checks if the provided bytes-like object contains an XPM (X PixMap) file.

```python
import imghdr

def is_xpm_file(buffer):
    result = imghdr.isxpm(buffer)
    print(f"Is the buffer an XPM file? {result}")

# Example usage
buffer = b'/* XPM */
static char *xpm[] = {
    "16 16 2 1",
    "      c none",
    ".     c black",
    "................"
}
is_xpm_file(buffer)
```

These examples demonstrate how to use each function in the `imghdr` module to determine the format of image files. Each example includes comments explaining the purpose and usage of the function, making it easy to understand and integrate into larger projects.
