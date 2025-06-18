# parser - Access Python parse trees
## Table of Contents

1. [Notes:](#notes)
2. [Example for Parsing HTML with `html.parser`:](#example-for-parsing-html-with-htmlparser)
3. [Example for Parsing XML with `xml.etree.ElementTree`:](#example-for-parsing-xml-with-xmletreeelementtree)



The `parser` module in Python is not a standard module, but it can be used to parse text files using regular expressions or simple parsing techniques. However, if you are referring to parsing HTML or XML documents, there are more suitable modules like `html.parser` and `xml.etree.ElementTree`.

For those interested in parsing text with regular expressions or other basic parsing techniques, I can provide examples of how to use the `re` module for pattern matching:

```python
import re

# Example 1: Simple pattern matching using re.match()
pattern = r'hello'
text = 'hello world!'
match = re.match(pattern, text)

if match:
    print('Pattern found:', match.group())
else:
    print('Pattern not found.')

# Example 2: Finding all occurrences of a pattern
pattern = r'\bword\b'
text = 'This is a word and another word.'
matches = re.findall(pattern, text)
print('Found words:', matches)

# Example 3: Using regular expressions for simple parsing
def parse_phone_number(text):
    pattern = r'(\+\d{1,2}\s?)?(\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return 'No phone number found.'

text = "Contact: 123-456-7890 or +1 (401) 555-1234"
print('Parsed phone number:', parse_phone_number(text))
```

### Notes:
- **`re.match()`**: This function checks for a match only at the beginning of the string.
- **`re.findall()`**: This function returns all non-overlapping matches of pattern in string, as a list of strings. It is similar to `finditer()` but returns a list of strings instead of iterator objects.
- **Regular Expressions**: The examples use basic regular expressions to match and parse patterns like words, phone numbers, etc.

If you are looking to parse HTML or XML documents, consider using the `html.parser` or `xml.etree.ElementTree` modules:

### Example for Parsing HTML with `html.parser`:
```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start tag:', tag)
        for attr in attrs:
            print('Attribute:', attr)

    def handle_endtag(self, tag):
        print('End tag  :', tag)

    def handle_data(self, data):
        print('Data     :', data)

html = """
<html>
<head><title>Test</title></head>
<body>
<p>This is a <a href="https://example.com">link</a>.</p>
</body>
</html>
"""

parser = MyHTMLParser()
parser.feed(html)
```

### Example for Parsing XML with `xml.etree.ElementTree`:
```python
import xml.etree.ElementTree as ET

xml_data = """
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>36.99</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J.K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
</bookstore>
"""

root = ET.fromstring(xml_data)

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    price = book.find('price').text
    print(f"Title: {title}, Author: {author}, Year: {year}, Price: {price}")
```

These examples demonstrate how to parse simple text patterns and XML documents using Python's standard libraries. For parsing HTML, `html.parser` is sufficient for basic tasks; for more complex scenarios, consider using libraries like BeautifulSoup or lxml.
