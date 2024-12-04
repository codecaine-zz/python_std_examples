# urllib.request — Extensible library for opening URLs

**Urllib Request Example**
=====================================

The `urllib.request` module provides an extensible framework for working with URLs.

**Example Usage:**

```python
import urllib.request

# Open a URL and print the response
def open_url(url):
    try:
        # Open the URL using urlopen
        with urllib.request.urlopen(url) as response:
            # Print the status code of the response
            print(f"Status Code: {response.status}")
            
            # Read the content of the response
            content = response.read().decode('utf-8')
            print("Content:")
            print(content)
    except Exception as e:
        print(f"Error occurred: {e}")

# Open a URL and save it to a file
def save_url_to_file(url, filename):
    try:
        # Open the URL using urlopen
        with urllib.request.urlopen(url) as response:
            # Read the content of the response
            content = response.read().decode('utf-8')
            
            # Save the content to a file
            with open(filename, 'w') as file:
                file.write(content)
    except Exception as e:
        print(f"Error occurred: {e}")

# Open a URL and send a GET request
def send_get_request(url):
    try:
        # Open the URL using urlopen
        with urllib.request.urlopen(url) as response:
            # Read the content of the response
            content = response.read().decode('utf-8')
            
            # Print the content
            print("Content:")
            print(content)
    except Exception as e:
        print(f"Error occurred: {e}")

# Main function
def main():
    url1 = "http://example.com"
    url2 = "http://www.google.com"
    
    open_url(url1)
    save_url_to_file(url2, "google_content.txt")
    send_get_request("http://www.python.org")

if __name__ == "__main__":
    main()
```

**Methods:**

### `urllib.request.urlopen(url)`

*   Opens the specified URL and returns a response object.
*   Returns a `Response` object containing the result of an HTTP request.

### `urllib.request.Request(url, data=None, method='GET')`

*   Creates a new Request object for the given URL.
*   Args:
    *   url: The URL to send the request to.
    *   data: Data to be sent with the request. Defaults to None.
    *   method: HTTP method (e.g., 'GET', 'POST'). Defaults to 'GET'.

### `urllib.request.urlopen(url, timeout=None)`

*   Opens the specified URL and returns a response object.
*   Args:
    *   url: The URL to send the request to.
    *   timeout: The timeout in seconds. If None, the default is used.

**Properties:**

### `Response.geturl()`

*   Returns the URL of the response.

### `Response.info()`

*   Returns a dictionary containing information about the response.

### `Response.read(size=-1)`

*   Reads the entire content of the response.
*   Args:
    *   size: The maximum amount of data to read. If -1, read the entire content.

### `Response.readline()`

*   Reads the next line from the response body.

### `Response.readlines()`

*   Returns a list of lines in the response body.

### `Response.close()`

*   Closes the connection to the server.

**Examples:**

```python
import urllib.request

# Open the URL using urlopen
with urllib.request.urlopen("http://example.com") as response:
    # Print the status code of the response
    print(f"Status Code: {response.status}")
    
    # Read the content of the response
    content = response.read().decode('utf-8')
    print(content)

# Open the URL using Request
request = urllib.request.Request("http://www.google.com", data="Hello, World!")
with urllib.request.urlopen(request) as response:
    print(response.info())

# Open a local file and read its contents
with open("example.txt", "r") as file:
    # Read the content of the file
    content = file.read()
    print(content)
```
