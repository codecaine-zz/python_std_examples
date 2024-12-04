# imghdr — Determine the type of an image

**Image Header Module**
======================

The `imghdr` module is used to determine the type of an image.

### Code Examples

#### 1. Checking the Image Type
```python
import imghdr

# Open an image file
with open('image.jpg', 'rb') as f:
    # Read the first 4 bytes of the file (header)
    header = f.read(4)

# Check if the image is a JPEG
if imghdr.what(header):
    print("Image type: JPEG")
else:
    print("Unknown image type")
```

#### 2. Checking Other Image Types
```python
import imghdr

image_types = {
    'JPEG': imghdr.JPEG,
    'GIF': imghdr.GIF,
    'PNG': imghdr.PNG,
}

# Check the type of an image file
for extension, type in image_types.items():
    if imghdr.what(open('image.' + extension, 'rb').read(4)) == type:
        print(f"Image type: {extension}")
```

#### 3. Handling Unknown Image Types
```python
import imghdr

try:
    # Open an image file
    with open('unknown.png', 'rb') as f:
        # Read the first 4 bytes of the file (header)
        header = f.read(4)

    # Check if the image type is unknown
    image_type = imghdr.what(header)
    if image_type == imghdr.UNKNOWN:
        print("Unknown image type")
except FileNotFoundError:
    print("File not found")
```

#### 4. Using `img HDR` for Multiple Image Files
```python
import imghdr

image_files = ['image1.jpg', 'image2.png', 'unknown.png']

for file in image_files:
    try:
        # Open an image file
        with open(file, 'rb') as f:
            # Read the first 4 bytes of the file (header)
            header = f.read(4)

        # Check if the image type is known
        image_type = imghdr.what(header)
        print(f"Image type: {image_type}")
    except FileNotFoundError:
        print("File not found")
```

### Explanation

*   The `imghdr` module uses the first 4 bytes of an image file to determine its type.
*   The `what()` function returns an integer representing the image type, which can be one of:
    *   `JPEG` (for JPEG images)
    *   `GIF` (for GIF images)
    *   `PNG` (for PNG images)
    *   `UNKNOWN` (for unknown or unsupported image types)
*   By checking the first 4 bytes of an image file, you can determine its type without needing to read or parse the entire file.

**Note:** The above examples are for illustration purposes only. In real-world applications, consider using established libraries and frameworks for handling images, such as Pillow (PIL) or OpenCV, which provide more comprehensive functionality and better performance than the `imghdr` module alone.
