# spwd — The shadow password database

**Spwd Module Code Generation**
=====================================

The `spwd` module provides an interface to the `/etc/shadow` file, which stores the encrypted passwords for system users.

### spwd Module Contents

```python
# Importing the necessary modules
import os

class SpwdException(Exception):
    """Raised when there's an error interacting with the shadow password database."""
    pass

def getspnam(name):
    """
    Returns the user name corresponding to the specified password entry.

    Args:
        name (str): The password to search for.

    Returns:
        str: The matching user name.
    """
    # Convert the password name to lowercase and encode it
    encoded_name = name.lower().encode('utf-8')
    
    # Search for the matching entry in the shadow password database
    with open('/etc/shadow', 'rb') as f:
        for line in f:
            if encoded_name == line.decode('utf-8').encode(':'):
                return line.split()[0]
    
    # If no match is found, raise an exception
    raise SpwdException("No matching user name found")

def getpwent():
    """
    Returns the next password entry from the shadow password database.

    Returns:
        str: The username of the next password entry.
    """
    with open('/etc/shadow', 'rb') as f:
        line = next((line for line in f if line.startswith('#')), None)
        
        # If no more entries are available, return None
        if line is None:
            return None
        
        # Extract and decode the username from the first field of the line
        encoded_name = line.decode('utf-8').split(':')[0].encode(':')
        return encoded_name.decode()

def setpw(name, pw):
    """
    Sets or updates a user's password.

    Args:
        name (str): The username to update.
        pw (str): The new password to set.

    Raises:
        SpwdException: If there's an error updating the password.
    """
    # Encode the password and username
    encoded_pw = pw.encode('utf-8')
    encoded_name = name.lower().encode(':')

    # Open the shadow password database for writing
    with open('/etc/shadow', 'ab') as f:
        # Write a new line to the file, including the timestamp and password entry
        f.write(f'!{getpwent()}\x01\x00\x00\x00{encoded_name}{ encoded_pw }\n')
```

### Example Use Cases

```python
# Get the user name corresponding to a specific password entry
try:
    username = getspnam('my_password')
    print(username)
except SpwdException as e:
    print(e)

# Get the next password entry from the shadow password database
entry = getpwent()
if entry is not None:
    print(entry.decode())
else:
    print("No more entries available")

# Set or update a user's password
try:
    setpw('my_username', 'new_password')
except SpwdException as e:
    print(e)
```

Note that the `getspnam` function only searches for exact matches, and does not perform any checks to ensure the entered name is a valid username.
