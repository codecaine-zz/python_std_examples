# xml.sax.handler - Base classes for SAX handlers

The `xml.sax.handler` module is part of the Python Standard Library's XML parsing capabilities, providing a foundation for writing event-driven parsers using the Simple API for XML (SAX). This module includes several base classes and interfaces that allow you to define custom behavior when parsing an XML document. Below are comprehensive code examples demonstrating various functionalities in this module.

### Example 1: Implementing a Basic SAX Handler

```python
import xml.sax.handler as sax_handler

class SimpleContentHandler(sax_handler.ContentHandler):
    def __init__(self):
        self.text = []

    def characters(self, data):
        # This method is called for each chunk of text found in the XML document.
        self.text.append(data)

    def startElement(self, name, attrs):
        # This method is called when an element starts.
        print(f"Start Element: {name}, Attributes: {attrs}")

    def endElement(self, name):
        # This method is called when an element ends.
        print(f"End Element: {name}")
        # Join the collected text and print it
        if self.text:
            print("Text:", ''.join(self.text))
            self.text = []

# Example usage
if __name__ == "__main__":
    xml_data = """
    <book>
        <title>Python Programming</title>
        <author>Sue Snellings</author>
        <year>2021</year>
    </book>
    """

    handler = SimpleContentHandler()
    sax_handler.parseString(xml_data, handler)
```

### Example 2: Handling Namespace Events

```python
import xml.sax.handler as sax_handler

class NamespacedHandler(sax_handler.ContentHandler):
    def __init__(self):
        self.namespaces = {}

    def startElementNS(self, name, qname, attrs):
        # This method is called when an element starts, including namespace information.
        prefix, local_name = name
        print(f"Start Element with Namespace: {prefix}:{local_name}, Attributes: {attrs}")
        if prefix:
            self.namespaces[local_name] = f"{prefix}:{qname}"

    def endElementNS(self, name, qname):
        # This method is called when an element ends.
        prefix, local_name = name
        print(f"End Element with Namespace: {prefix}:{local_name}")

# Example usage
if __name__ == "__main__":
    xml_data = """
    <book xmlns:bk="http://example.com/book">
        <bk:title>Python Programming</bk:title>
        <bk:author>Sue Snellings</bk:author>
    </book>
    """

    handler = NamespacedHandler()
    sax_handler.parseString(xml_data, handler)
```

### Example 3: Implementing an ErrorHandler

```python
import xml.sax.handler as sax_handler

class BasicErrorHandler(sax_handler.ErrorHandler):
    def error(self, exception):
        # This method is called for each parsing error.
        print(f"Error: {exception}")

    def fatalError(self, exception):
        # This method is called for each fatal parsing error.
        print(f"Fatal Error: {exception}")
        # Exit the program
        import sys
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    xml_data = """
    <book>
        <title>Python Programming</title>
        <author>Sue Snellings</author>
        </book>
    """

    handler = BasicErrorHandler()
    sax_handler.parseString(xml_data, handler)
```

### Example 4: Handling XML Processing Instructions

```python
import xml.sax.handler as sax_handler

class PIHandler(sax_handler.ContentHandler):
    def processingInstruction(self, target, data):
        # This method is called for each XML processing instruction found in the document.
        print(f"Processing Instruction: Target={target}, Data={data}")

# Example usage
if __name__ == "__main__":
    xml_data = """
    <?xml version="1.0"?>
    <book>
        <title>Python Programming</title>
        <!-- This is a comment -->
        <?xml-stylesheet type="text/xsl" href="style.xsl"?>
        </book>
    """

    handler = PIHandler()
    sax_handler.parseString(xml_data, handler)
```

### Example 5: Using NamespaceResolver

```python
import xml.sax.handler as sax_handler

class CustomNamespaceResolver(sax_handler.NamespaceResolver):
    def getPrefix(self, uri):
        # This method is called to resolve a namespace URI.
        if uri == 'http://example.com/book':
            return 'bk'
        else:
            return None

# Example usage
if __name__ == "__main__":
    xml_data = """
    <book xmlns:bk="http://example.com/book">
        <bk:title>Python Programming</bk:title>
        <bk:author>Sue Snellings</bk:author>
    </book>
    """

    resolver = CustomNamespaceResolver()
    handler = sax_handler.ContentHandler()
    handler.setNamespaceResolver(resolver)
    sax_handler.parseString(xml_data, handler)
```

These examples demonstrate how to implement various handlers using the `xml.sax.handler` module. Each example covers a specific functionality and provides clear instructions on how to use it effectively.
