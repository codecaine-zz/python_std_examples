# cmd - Support for line-oriented command interpreters

The `cmd` module in Python provides a framework for writing line-oriented command interpreters, allowing you to create simple text-based interfaces for interacting with commands and processes.

Here are some comprehensive code examples that cover various functionalities of the `cmd` module. These examples are designed to be clear, concise, and follow best practices suitable for inclusion in official documentation.

### Example 1: Basic Command Interpreter

```python
import cmd

class SimpleInterpreter(cmd.Cmd):
    prompt = '(simple) '

    def do_hello(self, arg):
        """Print a greeting."""
        print("Hello!")

    def do_exit(self, arg):
        """Exit the interpreter."""
        return True

if __name__ == '__main__':
    SimpleInterpreter().cmdloop()
```

### Example 2: Command with Arguments

```python
import cmd

class Calculator(cmd.Cmd):
    prompt = '(calc) '

    def do_add(self, arg):
        """Add two numbers."""
        try:
            num1, num2 = map(float, arg.split())
            result = num1 + num2
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == '__main__':
    Calculator().cmdloop()
```

### Example 3: Command with Flags

```python
import cmd

class FileManipulator(cmd.Cmd):
    prompt = '(file) '

    def do_open(self, arg):
        """Open a file and print its contents."""
        try:
            filename = arg.strip()
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("File not found.")

if __name__ == '__main__':
    FileManipulator().cmdloop()
```

### Example 4: Command History

```python
import cmd

class HistoryInterpreter(cmd.Cmd):
    prompt = '(history) '
    historyfile = None

    def postcmd(self, stop, line):
        """Store the last command in history."""
        if not stop:
            self.historyfile.append(line)
        return True

if __name__ == '__main__':
    HistoryInterpreter().cmdloop()
```

### Example 5: Subclassing `Cmd` for Custom Commands

```python
import cmd

class MyCommand(cmd.Cmd):
    prompt = '(mycommand) '

    def do_create(self, arg):
        """Create a new file."""
        try:
            filename = arg.strip()
            with open(filename, 'w') as file:
                print(f"File {filename} created.")
        except IOError:
            print("Error creating the file.")

if __name__ == '__main__':
    MyCommand().cmdloop()
```

### Example 6: Using `cmd.Cmd` in a Web Application

```python
import cmd
from http.server import HTTPServer, BaseHTTPRequestHandler

class CommandHTTPHandler(BaseHTTPRequestHandler):
    prompt = '(command) '

    def do_hello(self, arg):
        """Print a greeting over HTTP."""
        self.send_response(200)
        self.wfile.write(b"Hello!\n")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CommandHTTPHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
```

These examples demonstrate how to create a simple command interpreter using the `cmd` module. Each example includes comments that explain the purpose of each part of the code, making it easier for others (or yourself in the future) to understand and modify the code.

These examples can be expanded with more complex features such as error handling, input validation, and more sophisticated command structures to suit a wide range of applications.
