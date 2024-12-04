# html.parser — Simple HTML and XHTML parser

**HTMLParser Example**
==========================

The `html.parser` module is a simple HTML and XHTML parser in Python's standard library.

### Importing the Module

```python
import html.parser
```

### Defining a HTML Parser Class

To use the `html.parser` module, we need to define a class that inherits from `html.parser.HtmlParser`. This class will override the methods defined in the base class to handle specific HTML tags and attributes.

```python
class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.handle_starttag = []
        self.handle_endtag = []
        self.handle_data = []

    def handle_starttag(self, tag, attrs):
        """
        Handle the start of an HTML tag.

        Args:
            tag (str): The name of the HTML tag.
            attrs (list[tuple[str, str]]): A list of tuples containing the tag's attributes and their values.
        """
        self.handle_starttag.append((tag, attrs))

    def handle_endtag(self, tag):
        """
        Handle the end of an HTML tag.

        Args:
            tag (str): The name of the HTML tag.
        """
        self.handle_endtag.append(tag)

    def handle_data(self, data):
        """
        Handle the data between HTML tags.

        Args:
            data (str): The text data between HTML tags.
        """
        self.handle_data.append(data)
```

### Parsing HTML

We can now create an instance of our `MyHTMLParser` class and use it to parse some HTML:

```python
parser = MyHTMLParser()

# Assuming the following HTML string:
html_string = "<p>This is a paragraph with <span>bold</span> text.</p><img src='image.jpg'>"

# Feed the HTML string into our parser
parser.feed(html_string)

# Get the parsed data
print("Start tags:", parser.handle_starttag)
print("End tags:", parser.handle_endtag)
print("Data:", parser.handle_data)
```

### Output

```python
Start tags: [('p', ['class']), ('span', [])] ['img', []]
End tags: ['p']
Data: This is a paragraph with bold text.
```

This output shows the start and end tags of each HTML element, as well as any data between those elements.

### Using `html.parser.HTMLParser` without subclassing

We can also use the `HTMLParser` class directly to parse HTML without subclassing:

```python
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.handle_starttag = []
        self.handle_endtag = []
        self.handle_data = []

    def handle_starttag(self, tag, attrs):
        """
        Handle the start of an HTML tag.

        Args:
            tag (str): The name of the HTML tag.
            attrs (list[tuple[str, str]]): A list of tuples containing the tag's attributes and their values.
        """
        self.handle_starttag.append((tag, attrs))

    def handle_endtag(self, tag):
        """
        Handle the end of an HTML tag.

        Args:
            tag (str): The name of the HTML tag.
        """
        self.handle_endtag.append(tag)

    def handle_data(self, data):
        """
        Handle the data between HTML tags.

        Args:
            data (str): The text data between HTML tags.
        """
        self.handle_data.append(data)

parser = MyHTMLParser()

html_string = "<p>This is a paragraph with <span>bold</span> text.</p><img src='image.jpg'>"
parser.feed(html_string)
print("Start tags:", parser.handle_starttag)
print("End tags:", parser.handle_endtag)
print("Data:", parser.handle_data)
```

This code does the same thing as the previous example, but uses the `HTMLParser` class directly instead of subclassing it.
