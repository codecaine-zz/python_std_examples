# argparse — Parser for command-line options, arguments and subcommands

**Argparse Module Code Generation**
=====================================

### Overview

The `argparse` module provides support for parsing command-line options and arguments in Python.

### Importing Argparse

```python
import argparse
```

### Creating an Argument Parser

To create an argument parser, you can use the `argparse.ArgumentParser()` function:

```python
# Create a new argument parser
parser = argparse.ArgumentParser(description='My Script')
```

### Adding Arguments

You can add arguments to your parser using the `add_argument()` method:

```python
# Add a string argument
parser.add_argument('-n', '--name', help='Your name')

# Add an integer argument
parser.add_argument('-a', '--age', type=int, help='Your age')
```

### Adding Subcommands

You can add subcommands to your parser using the `add_subparsers()` method:

```python
# Create a new subparser for 'hello' command
subparser = parser.add_subparsers(dest='command')

# Add an action for 'hello' command
action_hello = subparser.add_parser('hello')
action_hello.set_defaults(func=lambda args: print(f"Hello, {args.name}!"))

# Add an action for 'world' command
action_world = subparser.add_parser('world')
action_world.set_defaults(func=lambda args: print(f"How are you, {args.age}?"))
```

### Parsing Arguments

To parse the arguments and execute the subcommand, you can use the `parse_args()` method:

```python
# Parse the arguments
args = parser.parse_args()

if args.command == 'hello':
    # Call the function associated with 'hello' command
    args.func(args)
elif args.command == 'world':
    # Call the function associated with 'world' command
    args.func(args)
else:
    # Print an error message if the subcommand is not found
    parser.print_help()
```

### Full Example

Here's a full example that demonstrates how to use `argparse`:

```python
import argparse

def hello(args):
    """Prints out a greeting message"""
    print(f"Hello, {args.name}!")

def world(args):
    """Prints out a question message"""
    print(f"How are you, {args.age}?")

if __name__ == '__main__':
    # Create a new argument parser
    parser = argparse.ArgumentParser(description='My Script')

    # Add string argument
    parser.add_argument('-n', '--name', help='Your name')

    # Add integer argument
    parser.add_argument('-a', '--age', type=int, help='Your age')

    # Create subparser for 'hello' command
    subparser = parser.add_subparsers(dest='command')

    # Add action for 'hello' command
    action_hello = subparser.add_parser('hello')
    action_hello.set_defaults(func=hello)

    # Add action for 'world' command
    action_world = subparser.add_parser('world')
    action_world.set_defaults(func=world)

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'hello':
        # Call the function associated with 'hello' command
        args.func(args)
    elif args.command == 'world':
        # Call the function associated with 'world' command
        args.func(args)
    else:
        # Print an error message if the subcommand is not found
        parser.print_help()
```

### Running the Script

To run the script, save it to a file named `script.py` and execute it using Python:

```bash
python script.py -n John -a 30
```

This will print out a greeting message: "Hello, John!".
