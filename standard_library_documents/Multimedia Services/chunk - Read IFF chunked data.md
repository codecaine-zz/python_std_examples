# chunk — Read IFF chunked data

**Chunk Module Code Generator**

### Overview
The `chunk` module provides a simple way to read IFF (Image File Format) chunked data.

### Code Examples
```python
import chunk

# Create an instance of the Chunk class
chunk_instance = chunk.Chunk()

# Initialize the chunk instance with some data
chunk_data = b"Hello, World!"
chunk_instance.load(chunk_data)

# Print the chunk contents as a string
print(chunk_instance.get_contents())

# Get the chunk size
print(f"Chunk size: {len(chunk_data)}")

# Load more chunk data and append it to the existing data
more_chunk_data = b"This is some additional data."
chunk_instance.append(more_chunk_data)

# Print the updated chunk contents as a string
print(chunk_instance.get_contents())

# Get the updated chunk size
print(f"Updated chunk size: {len(chunk_data) + len(more_chunk_data)}")

# Save the chunk instance to a file
with open("chunk.bin", "wb") as f:
    chunk_instance.save(f)

# Load a chunk instance from a file
loaded_chunk = chunk.Chunk()
loaded_chunk.load_from_file("chunk.bin")
```

### Chunk Class Methods

#### `load(data)`
Loads data into the chunk instance.

*   `data`: The data to load into the chunk instance.
*   Returns: None

```python
def load(self, data):
    """
    Loads data into the chunk instance.

    :param data: The data to load into the chunk instance.
    """
    self.data = data
```

#### `append(data)`
Appends data to the existing data in the chunk instance.

*   `data`: The data to append to the existing data.
*   Returns: None

```python
def append(self, data):
    """
    Appends data to the existing data in the chunk instance.

    :param data: The data to append to the existing data.
    """
    self.data += data
```

#### `save(file)`
Saves the chunk instance to a file.

*   `file`: The file to save the chunk instance to.
*   Returns: None

```python
def save(self, file):
    """
    Saves the chunk instance to a file.

    :param file: The file to save the chunk instance to.
    """
    with open(file, "wb") as f:
        f.write(self.data)
```

#### `load_from_file(file)`
Loads a chunk instance from a file.

*   `file`: The file to load the chunk instance from.
*   Returns: A new Chunk instance containing the loaded data.
*   Raises: FileNotFoundError if the file does not exist, ValueError if the file is empty.

```python
@staticmethod
def load_from_file(file):
    """
    Loads a chunk instance from a file.

    :param file: The file to load the chunk instance from.
    :return: A new Chunk instance containing the loaded data.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file is empty.
    """
    try:
        with open(file, "rb") as f:
            data = f.read()
            if not data:
                raise ValueError("File is empty")
            return Chunk(data)
    except FileNotFoundError:
        raise
```

#### `get_contents()`
Gets the contents of the chunk instance as a string.

*   Returns: A string containing the chunk data.
*   Raises: AttributeError if the chunk instance does not contain any data.

```python
def get_contents(self):
    """
    Gets the contents of the chunk instance as a string.

    :return: A string containing the chunk data.
    :raises AttributeError: If the chunk instance does not contain any data.
    """
    return self.data.decode("utf-8") if self.data else None
```

#### `get_size()`
Gets the size of the chunk instance in bytes.

*   Returns: An integer representing the chunk size.
*   Raises: AttributeError if the chunk instance does not contain any data.

```python
def get_size(self):
    """
    Gets the size of the chunk instance in bytes.

    :return: An integer representing the chunk size.
    :raises AttributeError: If the chunk instance does not contain any data.
    """
    return len(self.data)
```

### Chunk Class Attributes

*   `data`: The chunk data as a byte string.
