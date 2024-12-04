# html - HyperText Markup Language support

The `html` module in Python provides tools to parse HTML documents and render them as formatted text, including basic formatting features like bold, italic, lists, links, and images. Below are comprehensive and well-documented code examples for various functionalities provided by the `html` module.

### Example 1: Parsing an HTML Document

This example demonstrates how to parse an HTML document using the `BeautifulSoup` library from the `bs4` package, which is a popular choice for parsing HTML in Python.

```python
from bs4 import BeautifulSoup
import requests

# Fetch an HTML page
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all links from the parsed document
links = soup.find_all('a')
for link in links:
    print(f"Link: {link.get('href')}, Text: {link.text}")
```

### Example 2: Rendering HTML as a String

This example shows how to render an HTML document into a formatted string using the `html` module.

```python
from html import escape

# Define some text with HTML tags
text = "<strong>Hello, <em>world!</em></strong>"

# Escape any special characters and render as HTML
formatted_text = escape(text)
print(formatted_text)  # Output: &lt;strong&gt;Hello, &lt;em&gt;world!&lt;/em&gt;&lt;/strong&gt;
```

### Example 3: Rendering HTML to a File

This example demonstrates how to write an HTML document to a file.

```python
from html import escape

# Define some text with HTML tags
text = "<h1>Welcome to Python</h1><p>This is a sample paragraph.</p>"

# Escape any special characters and render as HTML
formatted_text = escape(text)

# Write the formatted text to a file
with open('output.html', 'w') as file:
    file.write(formatted_text)
```

### Example 4: Creating an HTML Page from Python

This example shows how to create a simple HTML page programmatically using the `html` module.

```python
from html import escape

# Define some content for the HTML page
title = "My Custom Webpage"
content = "<h1>Welcome to My Website</h1><p>This is my custom webpage.</p>"

# Escape any special characters and render as HTML
formatted_title = escape(title)
formatted_content = escape(content)

# Create the HTML structure
html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{formatted_title}</title>
</head>
<body>
    {formatted_content}
</body>
</html>"""

# Write the HTML page to a file
with open('custom_page.html', 'w') as file:
    file.write(html_page)
```

### Example 5: Modifying an HTML Document

This example demonstrates how to modify an existing HTML document by adding or removing elements.

```python
from bs4 import BeautifulSoup
import requests

# Fetch an HTML page
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Add a new paragraph to the body
new_paragraph = soup.new_tag("p")
new_paragraph.string = "This is a newly added paragraph."
soup.body.append(new_paragraph)

# Remove an existing element
existing_element = soup.find('a')
if existing_element:
    existing_element.decompose()

# Print the modified HTML content
print(soup.prettify())
```

### Example 6: Escaping Special Characters

This example shows how to use the `html` module's `escape` function to safely render text containing HTML tags.

```python
from html import escape

# Define some text with special characters and HTML tags
text = "<>&'\""

# Escape any special characters
escaped_text = escape(text)
print(escaped_text)  # Output: &lt;&gt;&#38;&#39;&quot;
```

### Example 7: Encoding HTML Entities

This example demonstrates how to use the `html` module's `unescape` function to decode HTML entities.

```python
from html import unescape

# Define some text with HTML entities
escaped_text = "&lt;>&#38;&#39;&quot;"

# Decode the HTML entities
decoded_text = unescape(escaped_text)
print(decoded_text)  # Output: <>&'"
```

### Example 8: Parsing HTML from a String

This example shows how to parse an HTML string using the `BeautifulSoup` library.

```python
from bs4 import BeautifulSoup

# Define an HTML string
html_string = "<h1>Hello, World!</h1><p>This is a paragraph.</p>"

# Parse the HTML string
soup = BeautifulSoup(html_string, 'html.parser')

# Extract all paragraphs from the parsed document
paragraphs = soup.find_all('p')
for para in paragraphs:
    print(para.text)
```

### Example 9: Rendering HTML with Custom Styling

This example demonstrates how to render an HTML document with custom CSS styles.

```python
from html import escape

# Define some text with HTML tags and a simple CSS style
text = "<h1>Welcome to Python</h1><p style='color: blue; font-size: 20px;'>This is my custom webpage.</p>"

# Escape any special characters and render as HTML
formatted_text = escape(text)
print(formatted_text)  # Output: &lt;h1&gt;Welcome to Python&lt;/h1&gt;&lt;p style='color: blue; font-size: 20px;'&gt;This is my custom webpage.&lt;/p&gt;
```

### Example 10: Handling HTML Entities in a String

This example shows how to handle and decode HTML entities within a string.

```python
from html import unescape

# Define a string containing HTML entities
html_entities = "&amp;&lt;&gt;"

# Decode the HTML entities
decoded_string = unescape(html_entities)
print(decoded_string)  # Output: & < >
```

These examples cover various aspects of working with HTML in Python using the `html` module. Each example is well-documented, includes comments explaining each step, and follows best practices for clarity and maintainability.
