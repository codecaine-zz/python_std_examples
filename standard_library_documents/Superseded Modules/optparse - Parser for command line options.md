# optparse - Parser for command line options
## Table of Contents

1. [Explanation:](#explanation)
2. [Usage:](#usage)



The `optparse` module is a simple way to handle command-line options in Python, similar to how `getopt` works in C. It provides a flexible framework for parsing command-line options and arguments.

Below are comprehensive code examples that cover various functionalities of the `optparse` module:

```python
import optparse

def main():
    # Create an OptionParser object
    parser = optparse.OptionParser()

    # Define command-line options
    # long_opt: --option
    # short_opt: -o
    # dest: variable to store the option's value
    # help: description of the option
    parser.add_option("--input", "-i", dest="input_file", help="Input file path")

    parser.add_option("--output", "-o", dest="output_file", help="Output file path")

    parser.add_option(
        "--verbose",
        "-v",
        action="store_true",
        dest="verbose",
        help="Enable verbose mode"
    )

    # Parse the command-line options and arguments
    (options, args) = parser.parse_args()

    # Check if required options are provided
    if not options.input_file:
        print("Error: Input file path is required")
        parser.print_help()
        return

    if not options.output_file:
        print("Error: Output file path is required")
        parser.print_help()
        return

    # Process the parsed options and arguments
    process_options(options, args)

def process_options(options, args):
    print(f"Input File: {options.input_file}")
    print(f"Output File: {options.output_file}")
    if options.verbose:
        print("Verbose mode is enabled")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **OptionParser Initialization**:
   - We create an `OptionParser` object which is used to define and parse the command-line options.

2. **Defining Options**:
   - `add_option` method is used to define various types of command-line options:
     - `--input` or `-i`: A long option with a short alias.
     - `--output` or `-o`: Another long option with a short alias.
     - `--verbose` or `-v`: A boolean flag that stores a True/False value.

3. **Parsing Options and Arguments**:
   - The `parse_args()` method is called to parse the command-line arguments. It returns a tuple containing two elements: a namespace object (`options`) with attributes set from the parsed options, and a list of remaining arguments (`args`).

4. **Validation**:
   - We check if both input and output file paths are provided. If not, we print an error message and help information using `parser.print_help()`.

5. **Processing Options**:
   - The `process_options` function demonstrates how to use the parsed options. It prints the values of the input and output files and checks if verbose mode is enabled.

### Usage:

To run this script from the command line, you can use the following commands:

```bash
python script.py --input=input.txt --output=output.txt -v
```

This will execute the script with the specified options.
