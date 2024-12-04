# urllib - URL handling modules

The `urllib` module in Python provides a variety of functions to handle URLs. Below are comprehensive, well-documented code examples covering various functionalities within this module.

### 1. **urllib.request Module**

This module contains functions to open and read from URLs, and to handle errors that may occur during the process.

#### Example 1: Using `urlopen` to Retrieve a Web Page

```python
import urllib.request

def fetch_web_page(url):
    """
    Fetches the content of a web page using urllib.request.urlopen.
    
    Args:
    url (str): The URL of the web page to retrieve.
    
    Returns:
    str: The content of the web page as a string.
    """
    try:
        # Open the URL and read its contents
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
        
        return html_content.decode('utf-8')  # Decode from bytes to string
        
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e.reason}")
        return None

# Example usage
url = 'https://www.example.com'
content = fetch_web_page(url)
if content:
    print(content[:100])  # Print the first 100 characters of the page
```

#### Example 2: Handling Redirects with `urlopen`

```python
import urllib.request

def fetch_web_page_with_redirects(url):
    """
    Fetches a web page and handles redirects using urllib.request.urlopen.
    
    Args:
    url (str): The URL of the web page to retrieve.
    
    Returns:
    str: The content of the final destination page as a string.
    """
    try:
        # Open the URL and handle redirects
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
        
        return html_content.decode('utf-8')
    
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL error occurred: {e.reason}")
        return None

# Example usage
url = 'https://www.example.com/redirect-target'
content = fetch_web_page_with_redirects(url)
if content:
    print(content[:100])
```

### 2. **urllib.parse Module**

This module provides functions to parse URLs and manage query parameters.

#### Example 3: Parsing a URL

```python
import urllib.parse

def parse_url(url):
    """
    Parses a URL using urllib.parse.urlparse.
    
    Args:
    url (str): The URL to be parsed.
    
    Returns:
    tuple: A named tuple containing the components of the URL.
    """
    # Parse the URL into its components
    parsed_url = urllib.parse.urlparse(url)
    
    return parsed_url

# Example usage
url = 'https://www.example.com/path?query=param&another=2'
parsed = parse_url(url)
print(parsed)
```

#### Example 4: Encoding Query Parameters

```python
import urllib.parse

def encode_query_params(params):
    """
    Encodes query parameters into a URL-encoded string using urllib.parse.urlencode.
    
    Args:
    params (dict): A dictionary of key-value pairs to be encoded.
    
    Returns:
    str: The URL-encoded query string.
    """
    # Encode the parameters
    encoded_params = urllib.parse.urlencode(params)
    
    return encoded_params

# Example usage
params = {'key': 'value', 'another_key': 2}
encoded = encode_query_params(params)
print(encoded)
```

### 3. **urllib.error Module**

This module provides exception classes for errors that may occur during URL operations.

#### Example 5: Handling URLError and HTTPError

```python
import urllib.request

def handle_url_errors(url):
    """
    Handles potential URLError and HTTPError exceptions using urllib.request.urlopen.
    
    Args:
    url (str): The URL to be retrieved.
    
    Returns:
    str: The content of the web page as a string if successful, None otherwise.
    """
    try:
        # Open the URL
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
        
        return html_content.decode('utf-8')
    
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL error occurred: {e.reason}")
        return None

# Example usage
url = 'https://www.example.com/nonexistent-page'
content = handle_url_errors(url)
if content:
    print(content[:100])
```

### 4. **urllib.robotparser Module**

This module provides functions to parse and understand the `robots.txt` files that specify which parts of a website can be accessed by web robots.

#### Example 6: Parsing `robots.txt`

```python
import urllib.robotparser

def parse_robots_file(url):
    """
    Parses a `robots.txt` file using urllib.robotparser.RobotFileParser.
    
    Args:
    url (str): The URL to the `robots.txt` file.
    
    Returns:
    RobotFileParser: An instance of RobotFileParser that can be queried.
    """
    # Parse the `robots.txt` file
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url)
    rp.read()
    
    return rp

# Example usage
url = 'https://www.example.com/robots.txt'
rp = parse_robots_file(url)
print(f"Allowed user agents: {rp.allowed_user_agents()}")
```

### 5. **urllib.robotparser Module - Querying Permissions**

```python
import urllib.robotparser

def check_robot_permission(rp, user_agent, path):
    """
    Checks if a specific user agent can access a given path based on the `robots.txt` file.
    
    Args:
    rp (RobotFileParser): An instance of RobotFileParser.
    user_agent (str): The user agent to query.
    path (str): The URL path to check.
    
    Returns:
    bool: True if the user agent is allowed to access the path, False otherwise.
    """
    # Check if the user agent can access the path
    return rp.can_fetch(user_agent, path)

# Example usage
rp = parse_robots_file('https://www.example.com/robots.txt')
user_agent = 'MyUserAgent'
path = '/'
if check_robot_permission(rp, user_agent, path):
    print(f"User Agent {user_agent} is allowed to access {path}")
else:
    print(f"User Agent {user_agent} is not allowed to access {path}")
```

These examples demonstrate how to use various functionalities within the `urllib` module to handle URL requests, parse URLs and query parameters, manage errors, and interact with `robots.txt` files.
