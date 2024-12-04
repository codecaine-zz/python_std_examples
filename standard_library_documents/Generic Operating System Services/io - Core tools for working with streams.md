# io - Core tools for working with streams

The `io` module in Python is a core module that provides support for file-like objects, including handling different types of streams such as binary files and text files. Below are comprehensive and well-documented code examples for various functionalities within the `io` module.

### 1. Basic File Handling

#### Reading from a File
This example demonstrates how to read data from a file using the built-in `open()` function.

```python
# Importing the io module for file handling
import io

def read_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_file('example.txt')
```

### 2. Writing to a File

#### Writing Text to a File
This example shows how to write text to a file using the `write()` method of a file object.

```python
# Importing the io module for file handling
import io

def write_to_file(filename, content):
    try:
        # Open the file in write mode (overwrites existing content)
        with open(filename, 'w') as file:
            # Write content to the file
            file.write(content)
        print("Content written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
write_to_file('example.txt', "Hello, World!\nThis is a test file.")
```

#### Writing Binary Data to a File
This example demonstrates how to write binary data to a file using the `write()` method.

```python
# Importing the io module for file handling
import io

def write_binary_data(filename, binary_data):
    try:
        # Open the file in binary write mode (overwrites existing content)
        with open(filename, 'wb') as file:
            # Write binary data to the file
            file.write(binary_data)
        print("Binary data written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
binary_data = b'\x48\x65\x6c\x6c\x6f'  # ASCII representation of 'Hello'
write_binary_data('example.bin', binary_data)
```

### 3. Appending to a File

#### Appending Text to a File
This example shows how to append text to an existing file using the `write()` method.

```python
# Importing the io module for file handling
import io

def append_to_file(filename, content):
    try:
        # Open the file in append mode (adds new content at the end)
        with open(filename, 'a') as file:
            # Append content to the file
            file.write(content)
        print("Content appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
append_to_file('example.txt', "\nThis is additional text.")
```

#### Appending Binary Data to a File
This example demonstrates how to append binary data to an existing file using the `write()` method.

```python
# Importing the io module for file handling
import io

def append_binary_data(filename, binary_data):
    try:
        # Open the file in binary append mode (adds new data at the end)
        with open(filename, 'ab') as file:
            # Append binary data to the file
            file.write(binary_data)
        print("Binary data appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
binary_data = b'\x57\x6f\x72\x6c\x64'  # ASCII representation of 'World'
append_binary_data('example.bin', binary_data)
```

### 4. Text Stream Handling

#### Reading Lines from a File
This example shows how to read lines from a file using the `readlines()` method.

```python
# Importing the io module for file handling
import io

def read_lines_from_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            print("Lines in the file:")
            for line in lines:
                print(line.strip())  # Remove newline characters
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_lines_from_file('example.txt')
```

#### Writing Lines to a File
This example shows how to write lines to a file using the `writelines()` method.

```python
# Importing the io module for file handling
import io

def write_lines_to_file(filename, lines):
    try:
        # Open the file in write mode (overwrites existing content)
        with open(filename, 'w') as file:
            # Write a list of lines to the file
            file.writelines(lines)
        print("Lines written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
lines = ["Line 1\n", "Line 2\n", "Line 3"]
write_lines_to_file('example.txt', lines)
```

### 5. Buffering

#### Using Buffered I/O with `io.StringIO`
This example demonstrates how to use a buffered string stream for in-memory file operations.

```python
# Importing the io module for file handling
import io

def buffer_string_io():
    try:
        # Create a StringIO object
        buffer = io.StringIO()
        
        # Write content to the buffer
        buffer.write("This is a buffered string.\n")
        buffer.write("Another line.")
        
        # Get the current position in the buffer
        print(f"Current position: {buffer.tell()}")
        
        # Seek to a specific position
        buffer.seek(0)
        
        # Read content from the buffer
        content = buffer.read()
        print("Content of the buffer:")
        print(content.strip())
        
        # Flush the buffer and close it
        buffer.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
buffer_string_io()
```

### 6. BytesIO for Binary Data

#### Using Buffered I/O with `io.BytesIO`
This example demonstrates how to use a buffered binary stream for in-memory file operations.

```python
# Importing the io module for file handling
import io

def buffer_bytes_io():
    try:
        # Create a BytesIO object
        buffer = io.BytesIO()
        
        # Write binary data to the buffer
        buffer.write(b'This is buffered binary.\n')
        buffer.write(b'Another line.')
        
        # Get the current position in the buffer
        print(f"Current position: {buffer.tell()}")
        
        # Seek to a specific position
        buffer.seek(0)
        
        # Read binary data from the buffer
        content = buffer.read()
        print("Content of the buffer:")
        print(content.decode('utf-8'))  # Decode bytes to string
        
        # Flush the buffer and close it
        buffer.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
buffer_bytes_io()
```

These examples cover various aspects of file handling, including reading and writing text and binary data, appending to files, handling different types of streams (text and binary), and using buffered I/O with `StringIO` and `BytesIO`.
