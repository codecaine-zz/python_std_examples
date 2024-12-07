# textwrap - Text wrapping and filling

Below is a comprehensive set of code examples that demonstrate various functionalities provided by the `textwrap` module in Python's standard library. The `textwrap` module provides utilities to format text in a variety of ways, such as filling and wrapping text.

```python
# Importing the textwrap module
import textwrap

# 1. Basic Text Wrapping

# Example: Simple text wrapping


def simple_text_wrapping():
    """
    This example demonstrates basic text wrapping.
    The input string is wrapped to fit a specified width.
    """
    input_text = "This is an example of how the textwrap module can be used to wrap text."
    print("Original Text:")
    print(input_text)

    # Wrapping the text to 40 characters per line
    wrapped_text = textwrap.wrap(input_text, width=40)
    print("\nWrapped Text:")
    for line in wrapped_text:
        print(line)


simple_text_wrapping()

# 2. Filling Text

# Example: Filling with fill()


def fill_example():
    """
    This example demonstrates using the `fill()` function to wrap and fill text.
    The `fill()` method wraps the input text into a paragraph that fits within the specified width,
    while also indenting each line of the output by a specified number of spaces.
    """
    input_text = "This is an example of how the textwrap module can be used to wrap text."
    print("Original Text:")
    print(input_text)

    # Wrapping and filling the text with 40 characters per line, indented by 2 spaces
    filled_text = textwrap.fill(
        input_text, width=40, initial_indent="  ", subsequent_indent="  ")
    print("\nFilled Text:")
    print(filled_text)


fill_example()

# 3. Indentation

# Example: Indenting text


def indent_example():
    """
    This example demonstrates the use of `indent()` to add leading whitespace to each line of a paragraph.
    The `fill()` method is used first to wrap and fill the input text, then `indent()` is applied to add indentation.
    """
    input_text = "This is an example of how the textwrap module can be used to wrap text."
    print("Original Text:")
    print(input_text)

    # Wrapping and filling the text with 40 characters per line
    filled_text = textwrap.fill(input_text, width=40)

    # Adding 2 spaces of indentation to each line
    indented_text = textwrap.indent(filled_text, "  ")
    print("\nIndented Text:")
    print(indented_text)


indent_example()

# 4. Dedenting Text

# Example: Removing leading whitespace from text


def dedent_example():
    """
    This example demonstrates the use of `dedent()` to remove any common leading whitespace from each line.
    The input text should have consistent leading whitespace on all lines for this function to work correctly.
    """
    input_text = """  This is an example of how the textwrap module can be used to wrap text.
                    Notice that there are two spaces at the beginning of each line."""

    print("Original Text:")
    print(input_text)

    # Dedenting the text
    dedented_text = textwrap.dedent(input_text)
    print("\nDedented Text:")
    print(dedented_text)


dedent_example()

# 5. Processing Unicode Characters

# Example: Handling non-ASCII characters


def unicode_example():
    """
    This example demonstrates handling text containing non-ASCII characters.
    The `fill()` function is used to wrap and fill the input text, which includes emojis and other Unicode characters.
    """
    input_text = "This is an example of how the textwrap module can be used with text containing non-ASCII characters 😊."
    print("Original Text:")
    print(input_text)

    # Wrapping and filling the text with 40 characters per line
    filled_text = textwrap.fill(input_text, width=40)
    print("\nFilled Text:")
    print(filled_text)


unicode_example()

```

### Explanation:
1. **Simple Text Wrapping**: Demonstrates how to wrap a given string to fit within a specified width.
2. **Filling Text**: Uses `fill()` for wrapping and filling text, optionally indenting each line of the output.
3. **Indentation**: Shows how to use `indent()` to add leading whitespace to a paragraph that has been wrapped and filled.
4. **Dedenting Text**: Illustrates removing common leading whitespace using `dedent()`.
5. **Processing Unicode Characters**: Demonstrates handling text containing non-ASCII characters.

These examples provide a comprehensive overview of the functionalities available in the `textwrap` module, including handling different types of input and formatting options.
