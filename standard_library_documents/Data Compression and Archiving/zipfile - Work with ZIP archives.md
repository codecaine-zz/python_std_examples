# zipfile — Work with ZIP archives

**ZIP Archive Operations using `zipfile`**
=====================================================

The `zipfile` module provides support for reading and writing ZIP archives.

### Installing the `zipfile` Module

The `zipfile` module is part of Python's standard library, so you don't need to install it separately. You can import it directly in your Python code:

```python
import zipfile
```

### Reading a ZIP Archive

To read a ZIP archive, use the `zipfile.ZipFile()` class.

```python
# Open a ZIP file for reading
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Iterate over the files in the ZIP archive
    for file in zip_ref.namelist():
        print(file)
        
    # Extract a single file from the ZIP archive
    with zip_ref.open(file) as f:
        print(f.read())
```

### Writing a ZIP Archive

To write a ZIP archive, use the `zipfile.ZipFile()` class with the `'w'` mode.

```python
# Create a new ZIP file for writing
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Add files to the ZIP archive
    zip_ref.write('file1.txt')
    zip_ref.write('file2.txt', 'file2.txt')
```

### Reading and Writing a ZIP Archive with Compression

To read or write a ZIP archive with compression, use the `zipfile.ZipFile()` class with the `'r'` or `'w'` mode, respectively.

```python
# Open a ZIP file for reading with compression
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Iterate over the files in the ZIP archive
    for file in zip_ref.namelist():
        print(file)
        
        # Extract a single file from the ZIP archive
        with zip_ref.open(file) as f:
            print(f.read())
            
# Create a new ZIP file for writing with compression
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Add files to the ZIP archive
    zip_ref.write('file1.txt')
    zip_ref.write('file2.txt', 'file2.txt')

    # Compress the ZIP archive
    zip_ref.close()
```

### Creating a ZIP Archive with Multiple Files

To create a ZIP archive with multiple files, use the `zipfile.ZipFile()` class and add files to it using the `write()` method.

```python
import zipfile

# Create a new ZIP file for writing
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Add files to the ZIP archive
    zip_ref.write('file1.txt')
    zip_ref.write('file2.txt', 'file2.txt')
    
    # Add another file to the ZIP archive
    with open('file3.txt', 'rb') as f:
        zip_ref.writestr('file3.txt', f.read())
```

### Creating a ZIP Archive with a Single File

To create a ZIP archive with a single file, use the `zipfile.ZipFile()` class and add a file to it using the `writestr()` method.

```python
import zipfile

# Create a new ZIP file for writing
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Add files to the ZIP archive
    zip_ref.writestr('file.txt', 'Hello, World!')
```

### Extracting Files from a ZIP Archive

To extract a file from a ZIP archive using the `zipfile` module, use the `ZipFile()` class and the `open()` method.

```python
import zipfile

# Open a ZIP file for reading
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Extract a single file from the ZIP archive
    with zip_ref.open('file.txt') as f:
        print(f.read())
```

### Deleting a File from a ZIP Archive

To delete a file from a ZIP archive using the `zipfile` module, use the `ZipFile()` class and the `remove()` method.

```python
import zipfile

# Open a ZIP file for reading
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Delete a file from the ZIP archive
    if 'file.txt' in zip_ref.namelist():
        zip_ref.remove('file.txt')
```

### Listing Files in a ZIP Archive

To list files in a ZIP archive using the `zipfile` module, use the `ZipFile()` class and the `namelist()` method.

```python
import zipfile

# Open a ZIP file for reading
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # List files in the ZIP archive
    print(zip_ref.namelist())
```

### Checking if a File Exists in a ZIP Archive

To check if a file exists in a ZIP archive using the `zipfile` module, use the `ZipFile()` class and the `namelist()` method.

```python
import zipfile

# Open a ZIP file for reading
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Check if a file exists in the ZIP archive
    print('file.txt' in zip_ref.namelist())
```

### Writing to a ZIP Archive

To write data to a ZIP archive using the `zipfile` module, use the `ZipFile()` class and the `writestr()` method.

```python
import zipfile

# Create a new ZIP file for writing
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Write data to the ZIP archive
    zip_ref.writestr('file.txt', 'Hello, World!')
```

### Reading from a ZIP Archive

To read data from a ZIP archive using the `zipfile` module, use the `ZipFile()` class and the `open()` method.

```python
import zipfile

# Open a ZIP file for reading
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Read data from the ZIP archive
    with zip_ref.open('file.txt') as f:
        print(f.read().decode())
```

### Creating a ZIP Archive with Encryption

To create a ZIP archive with encryption using the `zipfile` module, use the `'w'` mode and specify the encryption method.

```python
import zipfile
from Crypto.Cipher import AES

# Create a new ZIP file for writing with encryption
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Add files to the ZIP archive
    zip_ref.write('file1.txt')
    zip_ref.write('file2.txt', 'file2.txt')

    # Encrypt the ZIP archive
    cipher = AES.new(b'secret_key', AES.MODE_CTR)
    with open('example.zip', 'rb') as f_in:
        data = f_in.read()
    encrypted_data = cipher.encrypt(data)

    with open('encrypted_example.zip', 'wb') as f_out:
        f_out.write(encrypted_data)
```

### Decrypting a ZIP Archive

To decrypt a ZIP archive using the `zipfile` module, use the `'r'` mode and specify the encryption method.

```python
import zipfile
from Crypto.Cipher import AES

# Open a ZIP file for reading with decryption
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Decrypt the ZIP archive
    cipher = AES.new(b'secret_key', AES.MODE_CTR)
    data = cipher.decrypt(zip_ref.read(1024))
```

### Checking ZIP File Integrity

To check ZIP file integrity using the `zipfile` module, use the `'r'` mode and specify a checksum algorithm.

```python
import zipfile
from hashlib import sha256

# Open a ZIP file for reading with checksum verification
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Check the checksum of the ZIP archive
    checksum = sha256(zip_ref.read(1024)).hexdigest()
```

### Creating a ZIP Archive with Multiple Files and Compression

To create a ZIP archive with multiple files and compression using the `zipfile` module, use the `'w'` mode and specify the compression level.

```python
import zipfile

# Create a new ZIP file for writing
with zipfile.ZipFile('example.zip', 'w') as zip_ref:
    # Add files to the ZIP archive
    zip_ref.write('file1.txt')
    zip_ref.write('file2.txt', 'file2.txt')

    # Compress the ZIP archive with level 9
    zip_ref.close()
```

### Checking ZIP File Integrity using CRC-32

To check ZIP file integrity using CRC-32 using the `zipfile` module, use the `'r'` mode and specify the checksum algorithm.

```python
import zipfile
from crccheck import Checksum as _Checksum

# Open a ZIP file for reading with CRC-32 verification
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    # Calculate the CRC-32 checksum of the ZIP archive
    crc = _Checksum(0x104c11db)
    data = zip_ref.read()
    crc.update(data)
```
