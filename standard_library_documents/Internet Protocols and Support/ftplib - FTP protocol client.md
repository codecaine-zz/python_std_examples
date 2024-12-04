# ftplib - FTP protocol client

The `ftplib` module provides a way to interact with an FTP (File Transfer Protocol) server using Python. Below are comprehensive examples demonstrating various functionalities of this module, including connecting to an FTP server, uploading and downloading files, changing directories, handling basic commands, and closing the connection.

### Example 1: Connecting to an FTP Server

```python
import ftplib

# Connect to the FTP server with default port (21)
ftp = ftplib.FTP('ftp.example.com')

# Login using username and password
ftp.login(user='your_username', passwd='your_password')

# Print welcome message from the server
print(ftp.getwelcome())

# Close the connection
ftp.quit()
```

### Example 2: Uploading a File

```python
import ftplib

def upload_file():
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Specify the local file path to be uploaded
        local_file_path = 'path/to/local/file.txt'

        # Define the remote filename on the server where the file will be stored
        remote_filename = 'remote/file.txt'

        # Open the local file in binary mode and upload it to the server
        with open(local_file_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_filename}', file)

        print(f'File {local_file_path} uploaded successfully as {remote_filename}')

    except ftplib.error_perm as e:
        print(f'Upload failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to upload a file
upload_file()
```

### Example 3: Downloading a File

```python
import ftplib

def download_file():
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Specify the remote file path on the server to be downloaded
        remote_file_path = 'remote/file.txt'

        # Define the local filename where the file will be saved locally
        local_file_path = 'path/to/local/file_downloaded.txt'

        # Open a binary file in write mode and download the file from the server
        with open(local_file_path, 'wb') as file:
            ftp.retrbinary(f'RETR {remote_file_path}', file.write)

        print(f'File {remote_file_path} downloaded successfully as {local_file_path}')

    except ftplib.error_perm as e:
        print(f'Download failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to download a file
download_file()
```

### Example 4: Changing Directory

```python
import ftplib

def change_directory():
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Change to a specific directory on the server
        remote_directory = '/path/to/remote/directory'
        ftp.cwd(remote_directory)

        print(f'Changed to {remote_directory}')

    except ftplib.error_perm as e:
        print(f'Directory change failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to change directory
change_directory()
```

### Example 5: Listing Files in a Directory

```python
import ftplib

def list_files():
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Change to a specific directory on the server
        remote_directory = '/path/to/remote/directory'
        ftp.cwd(remote_directory)

        # List files in the current directory
        files_list = ftp.nlst()

        print(f'Files in {remote_directory}:')
        for file in files_list:
            print(file)

    except ftplib.error_perm as e:
        print(f'Directory listing failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to list files
list_files()
```

### Example 6: Handling FTP Errors

```python
import ftplib

def handle_ftp_errors():
    try:
        # Connect to the FTP server with default port (21)
        ftp = ftplib.FTP('ftp.example.com')

        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Specify a non-existent file path for testing error handling
        remote_file_path = 'non_existent/file.txt'

        # Attempt to retrieve the file, which should fail
        ftp.retrbinary(f'RETR {remote_file_path}', lambda data: None)

    except ftplib.error_perm as e:
        print(f'Error retrieving file: {e}')

    finally:
        # Close the connection
        if 'ftp' in locals():
            ftp.quit()

# Call the function to handle FTP errors
handle_ftp_errors()
```

### Example 7: Storing Large Files

To upload large files efficiently, consider using a context manager to handle file operations:

```python
import ftplib
import os

def store_large_file(local_file_path, remote_filename):
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Open the local file in binary mode
        with open(local_file_path, 'rb') as file:
            # Use STORbinary to upload the file in chunks
            ftp.storbinary(f'STOR {remote_filename}', file)

        print(f'Large file {local_file_path} uploaded successfully as {remote_filename}')

    except ftplib.error_perm as e:
        print(f'Large file upload failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to store a large file
store_large_file('path/to/large/file.txt', 'large_file_downloaded.txt')
```

### Example 8: Renaming or Moving Files

```python
import ftplib

def rename_or_move_files():
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Define old and new file paths on the server
        remote_old_file_path = 'remote/oldfile.txt'
        remote_new_file_path = 'remote/newfile.txt'

        # Rename or move the file
        ftp.rename(remote_old_file_path, remote_new_file_path)

        print(f'File {remote_old_file_path} renamed/moved to {remote_new_file_path}')

    except ftplib.error_perm as e:
        print(f'Rename/move failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to rename or move files
rename_or_move_files()
```

### Example 9: Deleting Files

```python
import ftplib

def delete_file():
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Define the remote file path on the server to be deleted
        remote_file_path = 'remote/file.txt'

        # Delete the file from the server
        ftp.delete(remote_file_path)

        print(f'File {remote_file_path} deleted successfully')

    except ftplib.error_perm as e:
        print(f'Delete failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to delete a file
delete_file()
```

### Example 10: Changing Permissions

FTP servers typically do not support changing permissions directly through `ftplib`. However, you can simulate this by deleting and then uploading a new file with desired permissions.

```python
import ftplib
import os

def change_permissions(local_file_path, remote_filename):
    # Connect to the FTP server with default port (21)
    ftp = ftplib.FTP('ftp.example.com')

    try:
        # Login using username and password
        ftp.login(user='your_username', passwd='your_password')

        # Define old and new file paths on the server
        remote_old_file_path = 'remote/oldfile.txt'
        remote_new_file_path = 'remote/newfile.txt'

        # Delete the old file to simulate permission change
        try:
            ftp.delete(remote_old_file_path)
        except ftplib.error_perm as e:
            print(f'Delete failed: {e}')

        # Upload a new file with desired permissions
        with open(local_file_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_new_file_path}', file)

        print(f'File {local_file_path} uploaded successfully as {remote_new_file_path}')

    except ftplib.error_perm as e:
        print(f'Upload failed: {e}')

    finally:
        # Close the connection
        ftp.quit()

# Call the function to change permissions
change_permissions('path/to/file.txt', 'file_with_desired_permissions.txt')
```

These examples cover a range of operations and error handling for FTP using Python's `ftplib` module. Adjust the paths and file names as necessary for your specific use case.
