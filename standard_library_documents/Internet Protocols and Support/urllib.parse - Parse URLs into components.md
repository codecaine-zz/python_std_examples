# urllib.parse - Parse URLs into components

Here are comprehensive examples of how to use the `urllib.parse` module in Python, including how to parse URLs into components:

```python
import urllib.parse

# Example 1: Parsing a simple URL
url = "http://example.com/path?query=param"
parsed_url = urllib.parse.urlparse(url)

print("Scheme:", parsed_url.scheme)      # Output: http
print("Netloc:", parsed_url.netloc)    # Output: example.com
print("Path:", parsed_url.path)        # Output: /path
print("Params:", parsed_url.params)     # Output: ''
print("Query:", parsed_url.query)       # Output: query=param
print("Fragment:", parsed_url.fragment)   # Output: ''

# Example 2: Parsing a URL with IPv6
url_ipv6 = "http://[2001:db8::1]/path?query=param"
parsed_ipv6_url = urllib.parse.urlparse(url_ipv6)

print("Scheme:", parsed_ipv6_url.scheme)   # Output: http
print("Netloc:", parsed_ipv6_url.netloc)  # Output: [2001:db8::1]
print("Path:", parsed_ipv6_url.path)     # Output: /path
print("Params:", parsed_ipv6_url.params)    # Output: ''
print("Query:", parsed_ipv6_url.query)   # Output: query=param
print("Fragment:", parsed_ipv6_url.fragment)# Output: ''

# Example 3: Parsing a URL with username and password
url_user_pass = "http://user:password@example.com/path?query=param"
parsed_user_pass_url = urllib.parse.urlparse(url_user_pass)

print("Scheme:", parsed_user_pass_url.scheme) # Output: http
print("Netloc:", parsed_user_pass_url.netloc)  # Output: user:password@example.com
print("Path:", parsed_user_pass_url.path)     # Output: /path
print("Params:", parsed_user_pass_url.params)    # Output: ''
print("Query:", parsed_user_pass_url.query)   # Output: query=param
print("Fragment:", parsed_user_pass_url.fragment)# Output: ''

# Example 4: Parsing a URL with multiple query parameters
url_params = "http://example.com/path?query1=value1&query2=value2"
parsed_params_url = urllib.parse.urlparse(url_params)

print("Scheme:", parsed_params_url.scheme) # Output: http
print("Netloc:", parsed_params_url.netloc)  # Output: example.com
print("Path:", parsed_params_url.path)     # Output: /path
print("Params:", parsed_params_url.params)    # Output: ''
print("Query:", parsed_params_url.query)   # Output: query1=value1&query2=value2
print("Fragment:", parsed_params_url.fragment)# Output: ''

# Example 5: Parsing a URL with fragment identifier
url_fragment = "http://example.com/path?query=param#fragment"
parsed_fragment_url = urllib.parse.urlparse(url_fragment)

print("Scheme:", parsed_fragment_url.scheme)   # Output: http
print("Netloc:", parsed_fragment_url.netloc)  # Output: example.com
print("Path:", parsed_fragment_url.path)     # Output: /path
print("Params:", parsed_fragment_url.params)    # Output: ''
print("Query:", parsed_fragment_url.query)   # Output: query=param
print("Fragment:", parsed_fragment_url.fragment)# Output: fragment

# Example 6: Parsing a URL with port number
url_port = "http://example.com:8080/path?query=param"
parsed_port_url = urllib.parse.urlparse(url_port)

print("Scheme:", parsed_port_url.scheme)   # Output: http
print("Netloc:", parsed_port_url.netloc)  # Output: example.com:8080
print("Path:", parsed_port_url.path)     # Output: /path
print("Params:", parsed_port_url.params)    # Output: ''
print("Query:", parsed_port_url.query)   # Output: query=param
print("Fragment:", parsed_port_url.fragment)# Output: ''

# Example 7: Parsing a URL with username and password using the urlunparse function
parsed_url = urllib.parse.urlparse(url)
url_unparsed = urllib.parse.urlunparse(parsed_url)

print("Original URL:", url)          # Output: http://example.com/path?query=param
print("Unparsed URL:", url_unparsed)# Output: http://example.com/path?query=param

# Example 8: Parsing a URL with multiple query parameters using the urlencode function
query_dict = {'key1': 'value1', 'key2': 'value2'}
encoded_query = urllib.parse.urlencode(query_dict)

print("Encoded Query:", encoded_query) # Output: key1=value1&key2=value2

# Example 9: Parsing a URL with fragment identifier using the urljoin function
base_url = "http://example.com/path"
fragment_url = "#fragment"
joined_url = urllib.parse.urljoin(base_url, fragment_url)

print("Joined URL:", joined_url)   # Output: http://example.com/path#fragment

# Example 10: Parsing a URL with IPv6 using the quote function
ipv6_url = "http://[2001:db8::1]/path?query=param"
quoted_ipv6_url = urllib.parse.quote(ipv6_url)

print("Quoted IPv6 URL:", quoted_ipv6_url) # Output: http%3A%2F%255B2001%3Ab8%3A0000%3A0000%3A0000%3A0000%3A0000%3A0001%5D%2Fpath%3Fquery%3Dparam
```

These examples demonstrate various ways to parse URLs using the `urllib.parse` module, including handling different components of a URL such as scheme, netloc, path, query parameters, and fragment identifiers. The code also includes examples for parsing URLs with IPv6 addresses, port numbers, and username/password credentials. Additionally, it shows how to encode and join URLs using the provided functions.
