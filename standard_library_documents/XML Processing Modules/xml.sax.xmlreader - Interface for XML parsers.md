# xml.sax.xmlreader — Interface for XML parsers

**XMLSAX Reader Module**
=========================

The `xml.sax` module provides an interface for parsing XML documents.

### Class: xml.sax.XMLReader

```python
# Importing necessary modules from xml.sax
from xml.sax import saxutils
from xml.sax.xmlreader import XMLReader

class XMLReader:
    """
    Interface for XML parsers.
    
    The XMLReader class is the main interface for parsing XML documents. It provides methods for 
    registering content handlers, setting document properties, and controlling parsing events.

    Attributes:
        _content_handlers (list): List of registered content handlers.
        _error_handler (str): Default error handler to be used when an error occurs during parsing.
    """

    def __init__(self):
        # Initialize the XMLReader with empty lists for content handlers and error handler
        self._content_handlers = []
        self._error_handler = ""

    def registerContentHandler(self, handler):
        """
        Registers a content handler to be used when an element is parsed.

        Args:
            handler (object): Content handler instance.
        """
        # Add the registered content handler to the list of handlers
        self._content_handlers.append(handler)

    def setDocumentLocator(self, locator):
        """
        Sets a document locator object that will be used to locate elements in the XML document.

        Args:
            locator (xml.sax.dialect.DTDHandler): Document locator instance.
        """
        # Set the document locator
        pass

    def startElement(self, namespace, name, attributes, event_handler):
        """
        Called when an element is parsed.

        Args:
            namespace (str): Namespace of the element.
            name (str): Name of the element.
            attributes (xml.sax.attributes Attributes): Attributes of the element.
            event_handler (object): Event handler instance.
        """
        # Call the startElement method on each registered content handler
        for handler in self._content_handlers:
            handler.startElement(namespace, name, attributes, event_handler)

    def endElement(self, namespace, name):
        """
        Called when an element is closed.

        Args:
            namespace (str): Namespace of the element.
            name (str): Name of the element.
        """
        # Call the endElement method on each registered content handler
        for handler in self._content_handlers:
            handler.endElement(namespace, name)

    def characters(self, data):
        """
        Called when character data is encountered during parsing.

        Args:
            data (str): Character data to be processed.
        """
        # Call the characters method on each registered content handler
        for handler in self._content_handlers:
            handler.characters(data)

    def error(self, exception):
        """
        Called when an error occurs during parsing.

        Args:
            exception (Exception): Error exception.
        """
        # Print or handle the error by calling the _error_handler method
        print("Error:", exception)
```

### Example Usage:

```python
from xml.sax.xmlreader import XMLReader

class MyContentHandler:
    def startElement(self, namespace, name, attributes, event_handler):
        print(f"Start element: {name}")

    def endElement(self, namespace, name):
        print(f"End element: {name}")

    def characters(self, data):
        print("Character data:", data)

def main():
    # Create an instance of XMLReader
    xml_reader = XMLReader()

    # Register a content handler
    my_handler = MyContentHandler()
    xml_reader.registerContentHandler(my_handler)

    # Parse an XML document using the XMLReader
    xml_string = """
        <root>
            <person>
                <name>John</name>
                <age>30</age>
            </person>
        </root>
    """

    # Simulate parsing an XML document
    xml_reader.startElement(None, "root", None, None)
    xml_reader.endElement(None, "root")
    xml_reader.characters("\n")
    xml_reader.startElement(None, "person", None, None)
    xml_reader.endElement(None, "person")
    xml_reader.characters("\n")
    xml_reader.startElement(None, "name", None, None)
    xml_reader.endElement(None, "name")
    xml_reader.characters("John\n")
    xml_reader.startElement(None, "age", None, None)
    xml_reader.endElement(None, "age")
    xml_reader.characters("30\n")

if __name__ == "__main__":
    main()
```

This code defines a custom content handler class `MyContentHandler` that prints the start and end elements, as well as character data. It then creates an instance of `XMLReader`, registers the `MyContentHandler` instance with it, and simulates parsing an XML document using the `xml_reader`.
