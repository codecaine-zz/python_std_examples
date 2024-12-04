# pwd — The password database

**Password Database Module: pwd**
=====================================

The `pwd` module provides access to Unix password management functionality.

### Importing the Module
```python
import pwd
```
This line imports the `pwd` module, which can be used to retrieve information about user accounts on a Unix system.

### Getting User Information
```python
# Get information about a specific user
try:
    user_info = pwd.getpwnam('username')
    print(f"Username: {user_info.pw_name}")
    print(f"Password: {user_info.pw_password}")
except KeyError as e:
    print(f"Error: User '{e}' not found")
```
This code retrieves information about a specific user using the `getpwnam` function. If the user is found, it prints their username and password (in hashed form). If the user is not found, it raises a `KeyError`.

### Getting All Users
```python
# Get a list of all users in the system
try:
    all_users = pwd.getpwent()
    while all_users:
        print(f"Username: {all_users.pw_name}")
        print(f"UID: {all_users.pw_uid}")
        print(f"GID: {all_users.pw_gid}")
        print(f"Password: {all_users.pw_password}")
        all_users = pwd.getpwent()
except Exception as e:
    print(f"Error: {e}")
```
This code retrieves a list of all users in the system using the `getpwent` function. It prints each user's information, including their username, UID (user ID), GID (group ID), and hashed password.

### Setting User Password
```python
import pwd

# Get a handle to the user account
try:
    user_handle = pwd.getpwnam('username')
except KeyError as e:
    print(f"Error: User '{e}' not found")
    exit(1)

# Set the new password for the user
new_password = input("Enter new password: ")
user_handle.pw_password = new_password.encode()
try:
    # Use the `chpass` system call to set the new password
    import os
    os.system(f"chpass {user_handle.pw_name}")
except Exception as e:
    print(f"Error setting password: {e}")
```
This code sets a new password for a user. It prompts the user to enter a new password, and then uses the `chpass` system call to set the new password.

### Getting Group Information
```python
import pwd

# Get a list of all groups in the system
try:
    group_info = pwd.getgrall()
    for group in group_info:
        print(f"GroupName: {group.gr_name}")
        print(f"GID: {group.gr_gid}")
except Exception as e:
    print(f"Error: {e}")
```
This code retrieves a list of all groups in the system using the `getgrall` function. It prints each group's information, including their name and GID.

### Getting Group Information for a Specific User
```python
import pwd

# Get the ID of the user
try:
    user_id = pwd.getpwnam('username').pw_uid
except KeyError as e:
    print(f"Error: User '{e}' not found")
    exit(1)

# Get information about the group with that ID
try:
    group_info = pwd.getgrgid(user_id)
    print(f"GroupName: {group_info.gr_name}")
    print(f"GID: {group_info.gr_gid}")
except KeyError as e:
    print(f"Error: Group '{e}' not found")
```
This code retrieves the ID of a user, and then uses that ID to get information about their primary group using the `getgrgid` function. It prints the group's name and GID.

### Adding a New User
```python
import pwd

# Create a new user account
try:
    # Get a handle to the user account
    user_handle = pwd.getpwnam('username')
except KeyError as e:
    print(f"Error: User '{e}' not found")
    exit(1)

# Set the user's UID, GID, and other information
user_handle.pw_uid = 1000
user_handle.pw_gid = 1000
user_handle.pw_gecos = "John Doe <john@example.com>"
user_handle.pw_dir = "/home/john"
try:
    # Use the `chown` system call to set the user's directory ownership
    import os
    os.system(f"chown {user_handle.pw_name} /home/{user_handle.pw_name}")
except Exception as e:
    print(f"Error: {e}")
```
This code creates a new user account and sets their UID, GID, and other information using the `getpwnam` function. It then uses the `chown` system call to set the user's directory ownership.

### Changing Group Ownership
```python
import pwd

# Get a list of all users in the system
try:
    all_users = pwd.getpwent()
    while all_users:
        print(f"Username: {all_users.pw_name}")
        print(f"UID: {all_users.pw_uid}")
        print(f"GID: {all_users.pw_gid}")
        print(f"Password: {all_users.pw_password}")
        all_users = pwd.getpwent()
except Exception as e:
    print(f"Error: {e}")

# Get the ID of a user
try:
    user_id = 1000
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Get the ID of a group
try:
    group_id = 1000
except Exception as e:
    print(f"Error: {e}")
    exit(1)

try:
    # Use the `chown` system call to change the group ownership of a file
    import os
    os.system(f"chown {user_id}:{group_id} /path/to/file")
except Exception as e:
    print(f"Error changing ownership: {e}")
```
This code changes the group ownership of a file using the `chown` system call.

Note that this is not an exhaustive list of all possible functions and methods provided by the `pwd` module. For more information, please refer to the [Python documentation](https://docs.python.org/3/library/pwd.html).
