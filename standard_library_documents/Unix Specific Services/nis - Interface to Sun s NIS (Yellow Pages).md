# nis - Interface to Sun’s NIS (Yellow Pages)

**nis Module Code Generator**
================================

### Overview

The `nis` module provides an interface to Sun's NIS (Yellow Pages), which is a distributed database that stores information about hosts, networks, and services.

### Installation

To use the `nis` module, you need to have the `nis` package installed. On Ubuntu-based systems, you can install it using:

```bash
sudo apt-get install nis
```

### Importing the Module

To import the `nis` module in Python, use:

```python
import nis
```

### Setting up NIS

Before using the `nis` module, you need to set up NIS on your system. This typically involves creating `/etc/nsswitch.conf` file with the following content:

```bash
passwd: files nis
group: files nis
hosts: nis dns
```

Then, restart the system or run the following command to activate the changes:

```bash
sudo /etc/init.d/nscud restart
```

### NIS Functions

The `nis` module provides several functions that can be used to interact with the NIS database. Here are some of the most commonly used functions:

#### 1. `nis.getent_group(groupname)`

Get information about a group by its name.

```python
import nis

group_name = "wheel"
group_info = nis.getent_group(group_name)
print(group_info)
```

#### 2. `nis.getent_host(hostname)`

Get information about a host by its hostname or IP address.

```python
import nis

hostname = "example.com"
host_info = nis.getent_host(hostname)
print(host_info)
```

#### 3. `nis.getent_passwd(username)`

Get information about a user by its username.

```python
import nis

username = "root"
user_info = nis.getent_passwd(username)
print(user_info)
```

#### 4. `nis.getent_password(username, password)` (Python 3.7+)

Get the hashed password for a given username and password.

```python
import nis

username = "root"
password = "secret"
hashed_password = nis.getent_password(username, password)
print(hashed_password)
```

#### 5. `nis.getent_passwd(username)`

Get information about a user by its username, including the hashed password.

```python
import nis

username = "root"
user_info = nis.getent_passwd(username)
print(user_info)
```

### NIS Exception Handling

The `nis` module raises exceptions when errors occur while interacting with the NIS database. You can catch these exceptions using a try-except block:

```python
try:
    group_info = nis.getent_group(group_name)
except Exception as e:
    print(f"Error: {e}")
```

### Conclusion

The `nis` module provides an interface to Sun's NIS, which is useful for interacting with the NIS database in Python. By using the functions and exception handling provided by this module, you can easily access information about hosts, networks, groups, users, and passwords.

**Code Generation Output**
```python
import nis

def get_group_info(group_name):
    """Get information about a group by its name."""
    try:
        return nis.getent_group(group_name)
    except Exception as e:
        print(f"Error: {e}")

def get_host_info(hostname):
    """Get information about a host by its hostname or IP address."""
    try:
        return nis.getent_host(hostname)
    except Exception as e:
        print(f"Error: {e}")

def get_user_info(username):
    """Get information about a user by its username."""
    try:
        return nis.getent_passwd(username)
    except Exception as e:
        print(f"Error: {e}")

def get_password(hashed_password):
    """Get the hashed password for a given username and password."""
    try:
        return nis.getent_password(username, password)
    except Exception as e:
        print(f"Error: {e}")

def get_user_info_by_username(username):
    """Get information about a user by its username, including the hashed password."""
    try:
        return nis.getent_passwd(username)
    except Exception as e:
        print(f"Error: {e}")
```
Note that this code generation output includes all the functions mentioned above. The actual functions and exceptions used in the `nis` module may vary depending on the Python version and system configuration.
