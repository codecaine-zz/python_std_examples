# ftplib — FTP protocol client

Here's an example of how you can use the `ftplib` module to connect to an FTP server, upload and download files, and list the directory contents:

```python
# Import the ftplib module
from ftplib import FTP, FTPException

def ftp_example():
    # Define the FTP host, username, and password
    host = 'ftp.example.com'
    username = 'username'
    password = 'password'

    try:
        # Create an FTP connection to the server
        with FTP(host) as ftp:
            # Login to the FTP server using the provided credentials
            ftp.login(user=username, passwd=password)

            print("Connected to the FTP server.")

            # List the directory contents
            print("Directory Contents:")
            for filename in ftp.nlst():
                print(filename)

            # Download a file from the FTP server
            print("\nDownloading 'example.txt'...")
            with open('example.txt', 'wb') as local_file:
                ftp.retrbinary('RETR example.txt', local_file.write)
            print("Download completed.")

            # Upload a file to the FTP server
            print("\nUploading 'local_example.txt'...")
            with open('local_example.txt', 'rb') as remote_file:
                ftp.storbinary('STOR example.txt', remote_file)
            print("Upload completed.")

    except FTPException as e:
        print(f"FTP Exception: {e}")
    except FileNotFoundError:
        print("File not found.")
    except ConnectionError:
        print("Connection error.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to test the example
ftp_example()
```

Here are some more examples of what you can do with `ftplib`:

*   **Login and logout**:

    ```python
ftp.login(user=username, passwd=password)
ftp.quit()
```
*   **Change directory**:

    ```python
ftp.cwd('/path/to/directory')
```
*   **Delete file**:

    ```python
ftp.dele(filename)
```
*   **Renamed a file**:

    ```python
ftp.rename('old_name', 'new_name')
```

Here's the full documentation for the `ftplib` module:

https://docs.python.org/3/library/ftplib.html

The official Python documentation covers all aspects of the FTP protocol client.
