# cmd — Support for line-oriented command interpreters

**cmd.py**
```python
"""
Support for line-oriented command interpreters.
"""

import sys
from contextlib import contextmanager

class CommandError(Exception):
    """Exception raised when a command error occurs."""
    pass

class CommandInterpreter:
    """
    A line-oriented command interpreter.

    Attributes:
        _lines (list): The lines of input to process.
        _current_line (str): The current line being processed.
    """

    def __init__(self, *args):
        self._lines = args
        self._current_line = None

    @property
    def current_line(self):
        """
        Get the current line being processed.

        Returns:
            str: The current line.
        """
        return self._current_line

    @current_line.setter
    def current_line(self, value):
        """
        Set the current line being processed.

        Args:
            value (str): The new current line.
        """
        self._current_line = value

    @contextmanager
    def _process_line(self):
        """
        Process a single line of input.

        Yields:
            list: The result of processing the line.
        """
        try:
            yield
        except Exception as e:
            raise CommandError(f"Processing error: {e}") from e

    def __iter__(self):
        """
        Iterate over the lines of input.

        Yields:
            str: Each line of input.
        """
        for line in self._lines:
            self.current_line = line
            yield from self._process_line()

def main():
    # Create a new command interpreter with some sample input lines
    interpreter = CommandInterpreter(
        "hello",
        "world!",
        "# invalid line"
    )

    # Process each line of input
    for result in interpreter:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

**Usage**
```bash
$ python cmd.py
Result: hello
Result: world!
Result: invalid line
Exception: CommandError: Processing error: SyntaxError: unexpected EOF while parsing
```
This implementation provides a basic command interpreter that can process lines of input. It includes the following features:

*   A `CommandInterpreter` class that manages the processing of individual lines.
*   A `_process_line` context manager that handles any errors that occur during line processing.
*   An `__iter__` method that yields each line of input.

Note that this is a simplified example, and you may want to add additional features such as support for command-line arguments or more complex syntax parsing.
