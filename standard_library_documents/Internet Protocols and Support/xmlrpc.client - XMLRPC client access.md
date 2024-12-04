# xmlrpc.client — XMLRPC client access

**XMLRPC Client Access**
==========================

The `xmlrpc.client` module provides an interface to remote procedure calls (RPC) using the XML-RPC protocol.

### Importing the Module
```python
import xmlrpc.client
```

### Creating an XMLRPC Client
```python
# Create a new XMLRPC client object with the specified URL
client = xmlrpc.client.ServerProxy('http://localhost:8080')
```
Replace `'http://localhost:8080'` with the actual URL of the server you want to connect to.

### Calling a Procedure on the Server
```python
# Call the 'add' procedure on the server with arguments 2 and 3
result = client.add(2, 3)
print(result)  # Output: 5

# Call the 'subtract' procedure on the server with arguments 4 and 1
result = client.subtract(4, 1)
print(result)  # Output: 3
```
### Example Use Case: Calculating the Sum of Two Numbers
```python
def calculate_sum(num1, num2):
    """
    Calculates the sum of two numbers using an XMLRPC client.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    
    Returns:
        int: The sum of num1 and num2.
    """
    # Create a new XMLRPC client object with the specified URL
    client = xmlrpc.client.ServerProxy('http://localhost:8080')
    
    try:
        # Call the 'add' procedure on the server with arguments num1 and num2
        result = client.add(num1, num2)
        return result
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function with two numbers
result = calculate_sum(5, 7)
print(result)  # Output: 12
```
### Error Handling

XMLRPC clients can raise exceptions when errors occur on the server. You can catch these exceptions and handle them accordingly.
```python
try:
    result = client.call('add', (2, 3))
except xmlrpc.client Fault as e:
    print(f"Error: {e}")
```
### Additional Example Use Cases

*   **Getting Server Information**

```python
# Get the server version information from the server
version_info = client.system.version()
print(version_info)
```

*   **Querying Data on a Database**

```python
import xmlrpc.client

class DatabaseClient:
    def __init__(self, url):
        """
        Initializes a new database client object with the specified URL.
        
        Args:
            url (str): The URL of the server.
        """
        self.url = url
        self.client = xmlrpc.client.ServerProxy(url)

    def get_data(self):
        """
        Retrieves data from the server's database.
        
        Returns:
            list: A list of retrieved data.
        """
        # Call the 'get_data' procedure on the server with no arguments
        return self.client.get_data()

# Create a new database client object
db_client = DatabaseClient('http://localhost:8080')

# Get data from the server's database
data = db_client.get_data()
print(data)
```
This is a basic overview of how to use the `xmlrpc.client` module in Python. Please note that this is not an exhaustive list, and you should always refer to the official documentation for more information on using XMLRPC clients in your projects.
