# argparse - Parser for command-line options, arguments and subcommands

The `argparse` module in Python is a powerful tool for parsing command-line arguments and providing usage information to users. It allows you to create user-friendly interfaces that are easy to use and understand, while also enabling robust error handling and help output.

Below are comprehensive code examples for various functionalities within the `argparse` module, including setting up argument parsers, defining options, handling subcommands, and displaying usage information.

### Example 1: Basic Argument Parsing

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a basic command-line parser')

# Add arguments to the parser
parser.add_argument('--name', type=str, help='Your name')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode (prints additional information)')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed arguments
print(f'Hello {args.name}')
if args.verbose:
    print('Verbose mode is enabled.')
```

### Example 2: Argument Parsing with Subcommands

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with subcommands')

# Add subparsers
subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

# Define the first subcommand
parser_add = subparsers.add_parser('add', help='Add two numbers')
parser_add.add_argument('a', type=float, help='First number to add')
parser_add.add_argument('b', type=float, help='Second number to add')

# Define the second subcommand
parser_mult = subparsers.add_parser('mult', help='Multiply two numbers')
parser_mult.add_argument('a', type=float, help='First number to multiply')
parser_mult.add_argument('b', type=float, help='Second number to multiply')

# Parse the command-line arguments
args = parser.parse_args()

# Handle the parsed subcommand and perform operations
if args.command == 'add':
    result = args.a + args.b
    print(f'The sum is {result}')
elif args.command == 'mult':
    result = args.a * args.b
    print(f'The product is {result}')
```

### Example 3: Argument Parsing with Options

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with options')

# Add options to the parser
parser.add_argument('--input', type=str, required=True, help='Input file path')
parser.add_argument('--output', type=str, default='output.txt', help='Output file path (default: output.txt)')
parser.add_argument('-f', '--force', action='store_true', help='Force overwriting the output file if it already exists')

# Parse the command-line arguments
args = parser.parse_args()

# Process the parsed options
print(f'Input File: {args.input}')
print(f'Output File: {args.output}')
if args.force:
    print('Forcing overwrite of output file.')
```

### Example 4: Argument Parsing with Custom Help Messages

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with custom help messages')

# Add arguments to the parser
parser.add_argument('--name', type=str, required=True, help='Your name (mandatory)')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode (optional)')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed arguments and custom messages
print(f'Hello {args.name}!')
if args.verbose:
    print('Verbose mode is enabled.')
else:
    print('Verbose mode is disabled.')
```

### Example 5: Argument Parsing with Default Values

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with default values')

# Add arguments to the parser with default values
parser.add_argument('--threshold', type=float, default=10.0, help='Threshold value (default: 10.0)')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed arguments and default values
print(f'Threshold Value: {args.threshold}')
if args.debug:
    print('Debug mode is enabled.')
else:
    print('Debug mode is disabled.')
```

### Example 6: Argument Parsing with Required Arguments

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with required arguments')

# Add arguments to the parser as required
parser.add_argument('--username', type=str, help='Your username (required)')
parser.add_argument('--password', type=str, help='Your password (required)')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed arguments
print(f'Username: {args.username}')
print(f'Password: {args.password}')
```

### Example 7: Argument Parsing with Error Handling

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with error handling')

# Add an argument to the parser
parser.add_argument('--count', type=int, help='Number of times to repeat (default: 1)')

# Parse the command-line arguments
args = parser.parse_args()

try:
    for _ in range(args.count):
        print('Repeat')
except TypeError as e:
    parser.error(f'Invalid count value: {e}')
```

### Example 8: Argument Parsing with Descriptive Help Output

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with descriptive help output')

# Add arguments to the parser
parser.add_argument('--input', type=str, required=True, help='Input file path (mandatory)')
parser.add_argument('--output', type=str, default='output.txt', help='Output file path (default: output.txt)')

# Display usage information
print(parser.format_help())
```

### Example 9: Argument Parsing with Subparsers and Aliases

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with subcommands and aliases')

# Add subparsers with aliases
subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

# Define the first subcommand with alias
parser_add = subparsers.add_parser('add', help='Add two numbers', aliases=['sum'])
parser_add.add_argument('a', type=float, help='First number to add')
parser_add.add_argument('b', type=float, help='Second number to add')

# Define the second subcommand with alias
parser_mult = subparsers.add_parser('mult', help='Multiply two numbers', aliases=['product'])
parser_mult.add_argument('a', type=float, help='First number to multiply')
parser_mult.add_argument('b', type=float, help='Second number to multiply')

# Parse the command-line arguments
args = parser.parse_args()

# Handle the parsed subcommand and perform operations
if args.command == 'add' or args.command == 'sum':
    result = args.a + args.b
    print(f'The sum is {result}')
elif args.command == 'mult' or args.command == 'product':
    result = args.a * args.b
    print(f'The product is {result}')
```

### Example 10: Argument Parsing with Custom Type Conversion

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with custom type conversion')

# Define a custom function for converting string to float
def convert_to_float(value):
    try:
        return float(value)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f'Invalid number: {value}. Must be a valid float.')

# Add an argument with custom type conversion
parser.add_argument('--number', type=convert_to_float, help='Number to process')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed argument after conversion
print(f'The processed number is {args.number}')
```

### Example 11: Argument Parsing with Nested Subcommands

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with nested subcommands')

# Add subparsers for the main command
main_subparsers = parser.add_subparsers(dest='main_command', help='Main command help')

# Define the first subcommand
subcmd1 = main_subparsers.add_parser('cmd1', help='Sub-command 1')
subcmd1.add_argument('--option', type=str, help='Option for sub-command 1')

# Define the second subcommand
subcmd2 = main_subparsers.add_parser('cmd2', help='Sub-command 2')
subcmd2.add_argument('--arg', type=int, help='Argument for sub-command 2')

# Parse the command-line arguments
args = parser.parse_args()

# Handle the parsed subcommands and their arguments
if args.main_command == 'cmd1':
    print(f'Option: {args.option}')
elif args.main_command == 'cmd2':
    print(f'Argument: {args.arg}')
```

### Example 12: Argument Parsing with Custom Help Formatter

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with custom help formatter')

# Add arguments to the parser
parser.add_argument('--input', type=str, required=True, help='Input file path (mandatory)')
parser.add_argument('--output', type=str, default='output.txt', help='Output file path (default: output.txt)')

# Create a custom help formatter class
class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_usage(self, usage, actions, groups, prefix=''):
        lines = self._split_lines(usage)
        # Customize the help format here
        return '\n'.join(lines)

# Set the custom help formatter
parser.formatter_class = CustomHelpFormatter

# Display usage information with custom formatting
print(parser.format_help())
```

### Example 13: Argument Parsing with Default Values and Aliases

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with default values and aliases')

# Add arguments to the parser with default values and aliases
parser.add_argument('--option', type=str, help='Option with default value (default: default_value)', default='default_value')
parser.add_argument('--alias-option', type=str, help='Alias for option', alias=['aopt'])

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed arguments
print(f'Option: {args.option}')
print(f'Alias Option: {args.alias_option}')
```

### Example 14: Argument Parsing with Mutually Exclusive Groups

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with mutually exclusive groups')

# Add subparsers for the main command
main_subparsers = parser.add_subparsers(dest='main_command', help='Main command help')

# Define the first subcommand group
group1 = main_subparsers.add_argument_group('Group 1')
group1.add_argument('--flag1', action='store_true', help='Flag 1 in Group 1')
group1.add_argument('--flag2', action='store_true', help='Flag 2 in Group 1')

# Define the second subcommand group
group2 = main_subparsers.add_argument_group('Group 2')
group2.add_argument('--flag3', action='store_true', help='Flag 3 in Group 2')
group2.add_argument('--flag4', action='store_true', help='Flag 4 in Group 2')

# Parse the command-line arguments
args = parser.parse_args()

# Handle the parsed flags from different groups
if args.main_command == 'cmd1':
    if args.flag1:
        print('Flag 1 in Group 1 is set')
    elif args.flag2:
        print('Flag 2 in Group 1 is set')
elif args.main_command == 'cmd2':
    if args.flag3:
        print('Flag 3 in Group 2 is set')
    elif args.flag4:
        print('Flag 4 in Group 2 is set')
```

### Example 15: Argument Parsing with Help Callbacks

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with help callbacks')

# Add arguments to the parser
parser.add_argument('--option', type=str, help='Option with callback function')

# Define a callback function for the help option
def on_help(args):
    print('This is a custom help message.')
    parser.print_usage()

# Set the help callback for the help option
parser.set_defaults(on_help=on_help)

# Parse the command-line arguments
args = parser.parse_args()

# Check if the help option was used and execute the callback
if hasattr(args, 'on_help'):
    args.on_help()
```

### Example 16: Argument Parsing with Default Values for Mutually Exclusive Groups

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example of a command-line parser with default values for mutually exclusive groups')

# Add subparsers for the main command
main_subparsers = parser.add_subparsers(dest='main_command', help='Main command help')

# Define the first subcommand group with default value
group1 = main_subparsers.add_argument_group('Group 1')
group1.add_argument('--flag1', action='store_true', help='Flag 1 in Group 1 (default)')
group1.add_argument('--flag2', action='store_true', help='Flag 2 in Group 1')

# Define the second subcommand group with default value
group2 = main_subparsers.add_argument_group('Group 2')
group2.add_argument('--flag3', action='store_true', help='Flag 3 in Group 2 (default)')
group2.add_argument('--flag4', action='store_true', help='Flag 4 in Group 2')

# Parse the command-line arguments
args = parser.parse_args()

# Handle the parsed flags from different groups with default values
if args.main_command == 'cmd1':
    if args.flag1:
        print('Flag 1 in Group 1 is set')
    elif args.flag2:
        print('Flag 2 in Group 1 is set')
elif args.main_command == 'cmd2':
    if args.flag3:
        print('Flag 3 in Group 2 is set (default)')
    elif args.flag4:
        print('Flag 4 in Group 2 is set')
```