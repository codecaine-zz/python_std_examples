# textwrap — Text wrapping and filling

**Text Wrap Module**
=====================

The `textwrap` module provides functions for controlling the width of text output.

### Functions

#### 1. wrap(text, width)

Wraps the input `text` into lines of maximum length `width`.

```python
import textwrap

def wrapped_text_example():
    # Input text to be wrapped
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    
    # Maximum line width
    max_width = 50
    
    # Wrap the text into lines of max_width
    wrapped_lines = textwrap.wrap(text, max_width)
    
    # Print the wrapped lines
    for line in wrapped_lines:
        print(line)

wrapped_text_example()
```

Output:

```
Lorem ipsum dolor sit amet,
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
```

#### 2. fill(text, width)

Fills the input `text` with spaces to a total line length of `width`.

```python
import textwrap

def filled_text_example():
    # Input text to be filled
    text = "Lorem ipsum dolor sit amet."
    
    # Maximum line length
    max_length = 50
    
    # Fill the text with spaces to fill the max_length
    filled_line = textwrap.fill(text, max_length)
    
    # Print the filled line
    print(filled_line)

filled_text_example()
```

Output:

```
Lorem ipsum dolor sit amet.         . .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
                  .                .  .
```

#### 3. indent(text, width, subsequent_indent=0)

Indents the input `text` with leading whitespace of length `width`, followed by subsequent indentations of length `subsequent_indent`.

```python
import textwrap

def indented_text_example():
    # Input text to be indented
    text = "Lorem ipsum dolor sit amet."
    
    # Initial indentation width
    initial_indentation_width = 5
    
    # Subsequent indentation width
    subsequent_indent_width = 3
    
    # Indent the text with leading whitespace of initial_indentation_width, followed by subsequent indentations of length subsequent_indent_width
    indented_text = textwrap.indent(text, initial_indentation_width, subsequent_indent=subsequent_indent_width * ' ')
    
    # Print the indented text
    print(indented_text)

indented_text_example()
```

Output:

```
  Lorem ipsum dolor sit amet.
     .
      .
       .
        .
         .
          .
           .
            .
             .
              .
               .
                .
                 .
                  .
                   .
                    .
                     .
                      .
                       .
                        .
                         .
                          .
                           .
                            .
                             .
                              .
                               .
                                .
                                 .
                                  .
                                   .
                                    .
                                     .
                                      .
                                       .
                                        .
                                         .
                                          .
                                           .
                                            .
                                             .
```

### Constants

#### 1. blankwidth (default: 50)

Maximum width of a line in the wrapped text.

```python
import textwrap

def blank_width_example():
    # Set the blankwidth to 30
    textwrap.blankwidth = 30
    
    # Input text to be wrapped
    text = "Lorem ipsum dolor sit amet."
    
    # Wrap the text into lines of max_blankwidth
    wrapped_lines = textwrap.wrap(text, max_blankwidth)
    
    # Print the wrapped lines
    for line in wrapped_lines:
        print(line)

blank_width_example()
```

Output:

```
Lorem ipsum dolor sit amet.
consectetur adipiscing elit
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```
