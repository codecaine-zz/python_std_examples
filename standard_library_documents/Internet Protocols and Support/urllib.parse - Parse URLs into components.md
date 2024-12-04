# urllib.parse — Parse URLs into components

**URL Parsing with `urllib.parse`**
=====================================

The `urllib.parse` module provides functions for parsing and manipulating URLs.

### Module Contents

*   `parseurl()`: Breaks a URL into its components.
*   `unquote()`: Unescapes characters in a URL path, query string, or fragment.
*   `urljoin()`: Joins two relative paths with a base URL.
*   `urlsplit()`: Splits a URL into its scheme, netloc, path, params, query, and fragment components.
*   `urlencode()`: Escapes special characters in a query string or form data.

### Code Examples
```python
import urllib.parse

# 1. parseurl()
def example_parseurl(url):
    """
    Breaks a URL into its components.
    
    Args:
        url (str): The URL to break down
    
    Returns:
        dict: A dictionary containing the scheme, netloc, path, params, query, and fragment of the URL.
    """
    parsed_url = urllib.parse.urlparse(url)
    return {
        "scheme": parsed_url.scheme,
        "netloc": parsed_url.netloc,
        "path": parsed_url.path,
        "params": parsed_url.params,
        "query": parsed_url.query,
        "fragment": parsed_url.fragment
    }

# 2. unquote()
def example_unquote(path):
    """
    Unescapes characters in a URL path.
    
    Args:
        path (str): The URL path to unescape
    
    Returns:
        str: The unescaped URL path.
    """
    return urllib.parse.unquote(path)

# 3. urljoin()
def example_urljoin(base_url, rel_path):
    """
    Joins two relative paths with a base URL.
    
    Args:
        base_url (str): The base URL.
        rel_path (str): The relative path to join
    
    Returns:
        str: The joined URL.
    """
    return urllib.parse.urljoin(base_url, rel_path)

# 4. urlsplit()
def example_urlsplit(url):
    """
    Splits a URL into its scheme, netloc, path, params, query, and fragment components.
    
    Args:
        url (str): The URL to split
    
    Returns:
        tuple: A tuple containing the scheme, netloc, path, params, query, and fragment of the URL.
    """
    return urllib.parse.urlparse(url)

# 5. urlencode()
def example_urlencode(data):
    """
    Escapes special characters in a query string or form data.
    
    Args:
        data (dict): A dictionary containing key-value pairs to encode
    
    Returns:
        str: The encoded query string or form data.
    """
    return urllib.parse.urlencode(data)

# Example usage
if __name__ == "__main__":
    url = "https://example.com/path?param=value"
    
    print("Parsed URL:")
    parsed_url = example_parseurl(url)
    print(parsed_url)
    
    print("\nUnescaped path:")
    unescaped_path = example_unquote(parsed_url["path"])
    print(unescaped_path)
    
    print("\nJoined URL:")
    joined_url = example_urljoin("https://example.com", "/path/rel/path")
    print(joined_url)
    
    print("\nSplit URL components:")
    split_components = example_urlsplit(url)
    print(split_components)
    
    print("\nEncoded query string:")
    encoded_data = {"key": "value"}
    encoded_query = example_urlencode(encoded_data)
    print(encoded_query)
```

### Explanation

*   The `parseurl()` function breaks a URL into its components using the `urllib.parse.urlparse()` function.
*   The `unquote()` function unescapes characters in a URL path using the `urllib.parse.unquote()` function.
*   The `urljoin()` function joins two relative paths with a base URL using the `urllib.parse.urljoin()` function.
*   The `urlsplit()` function splits a URL into its scheme, netloc, path, params, query, and fragment components using the `urllib.parse.urlparse()` function.
*   The `urlencode()` function escapes special characters in a query string or form data using the `urllib.parse.urlencode()` function.

### Advice

*   Use `parseurl()` to break down URLs into their components for analysis or manipulation.
*   Use `unquote()` to unescape characters in URL paths for safe usage.
*   Use `urljoin()` to join relative paths with a base URL for creating new URLs.
*   Use `urlsplit()` to split URLs into their components for further processing.
*   Use `urlencode()` to escape special characters in query strings or form data for safe transmission.
