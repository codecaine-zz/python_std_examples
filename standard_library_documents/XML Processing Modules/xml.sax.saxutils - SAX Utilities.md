# xml.sax.saxutils - SAX Utilities

Below are comprehensive code examples for using the `xml.sax.saxutils` module from Python's standard library, which provides utilities for XML parsing and string manipulation.

### 1. **Escape Characters in XML**

```python
from xml.sax.saxutils import escape

# Input string containing special characters
input_string = '<"&><>/'

# Escaping special characters for XML output
escaped_string = escape(input_string)

print(f"Original String: {input_string}")
print(f"Escaped String: {escaped_string}")
```

### 2. **Unescape Characters in XML**

```python
from xml.sax.saxutils import unescape

# Input string containing escaped entities
escaped_string = '&lt;"&amp;&gt;&amp;quot;&amp;apos;'  # Example of a long escape sequence

# Unescaping special characters from XML input
unescaped_string = unescape(escaped_string)

print(f"Escaped String: {escaped_string}")
print(f"Unescaped String: {unescaped_string}")
```

### 3. **Entity Encoding**

```python
from xml.sax.saxutils import entityEscape

# Input string containing special characters
input_string = 'The &quot;quick&quot; brown fox jumps over the &lt;lazy&gt; dog.'

# Entity encoding special characters for XML output
encoded_string = entityEscape(input_string)

print(f"Original String: {input_string}")
print(f"Encoded String: {encoded_string}")
```

### 4. **HTML Character Entities**

```python
from xml.sax.saxutils import htmlEntityDecode

# Input string containing HTML character entities
html_encoded_string = 'The &quot;quick&quot; brown fox jumps over the &lt;lazy&gt; dog.'

# Decoding HTML character entities to their corresponding characters
decoded_string = htmlEntityDecode(html_encoded_string)

print(f"Encoded String: {html_encoded_string}")
print(f"Decoded String: {decoded_string}")
```

### 5. **XML Character Reference Entities**

```python
from xml.sax.saxutils import xmlcharrefreplace

# Input string containing XML character reference entities
xml_entity_string = 'The &quot;quick&quot; brown fox jumps over the &lt;lazy&gt; dog.'

# Replacing XML character reference entities with their corresponding characters
replaced_string = xmlcharrefreplace(xml_entity_string)

print(f"Original String: {xml_entity_string}")
print(f"Replaced String: {replaced_string}")
```

### 6. **XML Namespace Mapping**

```python
from xml.sax.saxutils import prepare_input_source

# Input string with namespaces
input_string = """
<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <child xsi:type="typeA">Content</child>
</root>
"""

# Preparing input source for XML parsing
input_source = prepare_input_source(input_string)

print(f"Input Source: {input_source}")
```

### 7. **XML Character Reference Replacement**

```python
from xml.sax.saxutils import characterEntityResolver

# Function to resolve character entities to their corresponding characters
def custom_resolver(public_id, system_id):
    # Example mapping for HTML special characters
    if public_id == "-//W3C//DTD HTML 4.01 Transitional//EN":
        return {"&lt;": "<", "&gt;": ">", "&amp;": "&"}
    return None

# Setting up the custom character entity resolver
resolver = characterEntityResolver(custom_resolver)

print(f"Custom Resolver: {resolver}")
```

### 8. **XML Character Reference Replacement with XML Namespace**

```python
from xml.sax.saxutils import prepare_input_source, resolve_entity

# Input string with namespaces and character entities
input_string = """
<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <child xsi:type="typeA">Content &amp; more content</child>
</root>
"""

# Preparing input source for XML parsing
input_source = prepare_input_source(input_string)

# Resolving entities in the input source using the resolver
resolved_input = resolve_entity(input_source, "more content")

print(f"Original Input: {input_source}")
print(f"Resolved Input: {resolved_input}")
```

These examples demonstrate various functionalities of the `xml.sax.saxutils` module, including escaping and unescaping characters, encoding HTML entities, handling XML namespace mappings, and using custom character entity resolvers. Each example is accompanied by comments for clarity.
