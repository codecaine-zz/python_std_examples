# io — Core tools for working with streams

**io Module**
===============

The `io` module provides a way of using operating system features from within Python programs.

### 1. Reading and Writing Streams

#### Creating a Text Stream
```python
import io

# Create a text stream
text_stream = io.TextIOWrapper(io.StringIO('Hello, World!'))

# Print the contents of the stream
print(text_stream.read())
```
Output: `Hello, World!`

#### Creating a Binary Stream
```python
import io

# Create a binary stream
binary_stream = io.BytesIO(b'Hello, World!')

# Read and print the contents of the stream
print(binary_stream.getvalue())
```
Output: `b'Hello, World!'`

#### Reading from a File-like Object
```python
import io

# Create a file-like object (simulating a text file)
file_like_object = io.StringIO('Hello, World!')

# Read and print the contents of the file-like object
print(file_like_object.read())
```
Output: `Hello, World!`

#### Writing to a File-like Object
```python
import io

# Create a file-like object (simulating a text file)
file_like_object = io.StringIO()

# Write to the file-like object and print its contents
file_like_object.write('Hello, World!')
print(file_like_object.getvalue())
```
Output: `Hello, World!`

### 2. Seeking in Streams

#### Creating a Text Stream with Seekable Buffer
```python
import io

# Create a text stream with seekable buffer
text_stream = io.TextIOWrapper(io.BytesIO(b'Hello, World!'))

# Print the first 10 characters of the stream
print(text_stream.read(10))

# Move the cursor to the beginning of the stream and read again
text_stream.seek(0)
print(text_stream.read())
```
Output:
```
Helo
Hello, World!
```
### 3. Closing Streams

#### Creating a Text Stream with Seekable Buffer
```python
import io

# Create a text stream with seekable buffer
with io.TextIOWrapper(io.BytesIO(b'Hello, World!')) as text_stream:
    # Write to the stream and print its contents
    text_stream.write('New content!')
    print(text_stream.read())
```
Output: `New content!Hello, World!`

### 4. Reading and Writing with Buffers

#### Creating a Text Stream with Seekable Buffer
```python
import io

# Create a binary stream with seekable buffer
binary_stream = io.BytesIO(b'Hello, World!')

# Read from the stream using a buffer of size 10
buffered_binary_stream = io.BufferedWriter(binary_stream)
print(buffered_binary_stream.read(10))

# Write to the stream using a buffer of size 5
buffered_binary_stream.write('New content!'[:5])
```
Output:
```
b'Hello'
New content!
```
