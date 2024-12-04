# optparse — Parser for command line options

**Optparse Code Examples**
==========================

The `optparse` module provides support for parsing command-line options and arguments.

### Example 1: Basic Usage

```python
import optparse

def main():
    # Create an OptionParser object
    parser = optparse.OptionParser("Usage: python script.py [options]")

    # Add options
    parser.add_option("--foo", action="store_true", dest="foo",
                      help="Show foo")
    parser.add_option("--bar", action="store_true", dest="bar",
                      help="Show bar")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                      help="Verbose mode")

    # Parse the command-line options
    (options, args) = parser.parse_args()

    if options.foo:
        print("Option foo is set")
    if options.bar:
        print("Option bar is set")
    if options.verbose:
        print("Verbose mode is enabled")

if __name__ == "__main__":
    main()
```

### Example 2: Positional Arguments

```python
import optparse

def main():
    # Create an OptionParser object
    parser = optparse.OptionParser("Usage: python script.py [options] <filename>")

    # Add options
    parser.add_option("--foo", action="store_true", dest="foo",
                      help="Show foo")
    parser.add_option("--bar", action="store_true", dest="bar",
                      help="Show bar")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                      help="Verbose mode")

    # Parse the command-line options
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("Please provide a filename")

    filename = args[0]
    print(f"Loaded file: {filename}")

if __name__ == "__main__":
    main()
```

### Example 3: Grouping Options

```python
import optparse

def main():
    # Create an OptionParser object
    parser = optparse.OptionParser("Usage: python script.py [options]")

    # Add options grouped by section
    group = parser.add_option_group(
        "Configuration Options",
        "These are configuration-related options")
    group.add_option("--config-level", action="store", dest="config_level",
                     help="Set the config level (e.g., DEBUG, INFO, WARNING, ERROR)")
    group.add_option("--config-file", action="store", dest="config_file",
                     help="Path to the configuration file")

    # Parse the command-line options
    (options, args) = parser.parse_args()

    print(f"Config Level: {options.config_level}")
    print(f"Config File: {options.config_file}")

if __name__ == "__main__":
    main()
```

### Example 4: Default Values

```python
import optparse

def main():
    # Create an OptionParser object
    parser = optparse.OptionParser("Usage: python script.py [options]")

    # Add options with default values
    parser.add_option("--foo", action="store_true", dest="foo",
                      help="Show foo (default: False)")
    parser.add_option("--bar", action="store", type="int", dest="bar",
                      help="Show bar (default: 0)")

    # Parse the command-line options
    (options, args) = parser.parse_args()

    print(f"Option foo is set: {options.foo}")
    print(f"Option bar is set to {options.bar}")

if __name__ == "__main__":
    main()
```

### Example 5: Help Message

```python
import optparse

def main():
    # Create an OptionParser object
    parser = optparse.OptionParser("Usage: python script.py [options]")

    # Add options
    parser.add_option("--foo", action="store_true", dest="foo",
                      help="Show foo")
    parser.add_option("--bar", action="store", type="int", dest="bar",
                      help="Show bar (default: 0)")

    # Print the help message
    print("Options:")
    parser.print_help()

if __name__ == "__main__":
    main()
```
