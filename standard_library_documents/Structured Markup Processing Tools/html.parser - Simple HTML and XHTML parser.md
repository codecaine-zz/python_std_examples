# html.parser - Simple HTML and XHTML parser
## Table of Contents

1. [Example 1: Basic Parsing with `HTMLParser`](#example-1-basic-parsing-with-htmlparser)
2. [Explanation:](#explanation)
3. [Example 2: Extracting Links with `BeautifulSoup`](#example-2-extracting-links-with-beautifulsoup)
4. [Explanation:](#explanation)
5. [Example 3: Parsing Attributes](#example-3-parsing-attributes)
6. [Explanation:](#explanation)



Certainly! Below are comprehensive and well-documented examples for using the `html.parser` module in Python, which is part of the standard library. This module provides a simple way to parse HTML and XHTML documents.

### Example 1: Basic Parsing with `HTMLParser`

This example demonstrates how to use the `HTMLParser` class from the `html.parser` module to extract text from an HTML document.

```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []

    def handle_data(self, data):
        # This method is called for each block of plain text in the document
        self.data.append(data)

def parse_html(html_content):
    parser = MyHTMLParser()
    parser.feed(html_content)
    return parser.data

# Example usage
html_content = """
<html>
<head>
    <title>Sample HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample paragraph.</p>
</body>
</html>
"""

parsed_data = parse_html(html_content)
print(parsed_data)
```

### Explanation:
- **`MyHTMLParser` Class**: This class inherits from `HTMLParser` and overrides the `handle_data` method to print any plain text found in the HTML.
- **`parse_html` Function**: This function creates an instance of `MyHTMLParser`, feeds it the HTML content, and then returns the extracted data.
- **Example Usage**: The HTML content is defined as a string, and the `parse_html` function is called to extract and print all text from the document.

### Example 2: Extracting Links with `BeautifulSoup`

For more complex parsing tasks, you might use `BeautifulSoup`, which provides a more powerful interface for working with HTML and XML documents.

pip install beautifulsoup4

```python
from bs4 import BeautifulSoup

def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

# Example usage
html_content = """
<html>
<head>
    <title>Sample HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample paragraph.</p>
    <a href="https://www.example.com">Visit Example</a>
    <a href="https://www.python.org">Python Website</a>
</body>
</html>
"""

links = extract_links(html_content)
print(links)
```

### Explanation:
- **`BeautifulSoup`**: This class is part of the `bs4` module and provides methods to parse HTML and XML documents.
- **`extract_links` Function**: This function uses `BeautifulSoup` to create a parsed representation of the HTML content. It then finds all `<a>` tags with an `href` attribute and extracts their href values.
- **Example Usage**: The same HTML content is used, and the function returns a list of links found in the document.

### Example 3: Parsing Attributes

You can also extract attributes from specific elements using BeautifulSoup.

```python
from bs4 import BeautifulSoup

def extract_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('title').get_text()
    return title

# Example usage
html_content = """
<html>
<head>
    <title>Sample HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample paragraph.</p>
</body>
</html>
"""

title = extract_title(html_content)
print(title)
```

### Explanation:
- **`find` Method**: This method searches for the first occurrence of an element in the parsed document.
- **`get_text` Method**: This method returns the text content of the found element, which is useful for extracting titles or other simple text data.

These examples demonstrate how to use different parsing techniques with `html.parser` and `BeautifulSoup`, covering basic extraction, more complex operations like link extraction, and attribute access.
