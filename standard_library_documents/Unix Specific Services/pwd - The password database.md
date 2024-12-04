# pwd - The password database

The `pwd` module in Python provides an interface to the system's password database, which contains user account information such as usernames, passwords, home directories, and shell programs.

Below are comprehensive code examples demonstrating various functionalities of the `pwd` module:

### 1. Getting a Password Database Entry by Username

```python
import pwd

# Example: Get the password entry for a specific username
username = 'example_user'
try:
    pwd_entry = pwd.getpwnam(username)
    print(f"User {username} found:")
    print(f"Username: {pwd_entry.pw_name}")
    print(f"Password Hash: {pwd_entry.pw_passwd}")
    print(f"UID: {pwd_entry.pw_uid}")
    print(f"GID: {pwd_entry.pw_gid}")
    print(f"Home Directory: {pwd_entry.pw_dir}")
    print(f"Shell Program: {pwd_entry.pw_shell}")
except KeyError:
    print(f"User {username} not found.")
```

### 2. Getting a Password Database Entry by UID

```python
import pwd

# Example: Get the password entry for a specific UID
uid = 1001
try:
    pwd_entry = pwd.getpwuid(uid)
    print(f"User with UID {uid} found:")
    print(f"Username: {pwd_entry.pw_name}")
    print(f"Password Hash: {pwd_entry.pw_passwd}")
    print(f"UID: {pwd_entry.pw_uid}")
    print(f"GID: {pwd_entry.pw_gid}")
    print(f"Home Directory: {pwd_entry.pw_dir}")
    print(f"Shell Program: {pwd_entry.pw_shell}")
except KeyError:
    print(f"No user found with UID {uid}.")
```

### 3. Listing All Users

```python
import pwd

# Example: List all users in the system
for user_info in pwd.getpwall():
    print(f"Username: {user_info.pw_name}, UID: {user_info.pw_uid}")
```

### 4. Retrieving Group Information for a User

```python
import grp

# Example: Get the group information for a specific username
username = 'example_user'
try:
    user_entry = pwd.getpwnam(username)
    group_id = user_entry.pw_gid
    group_info = grp.getgrgid(group_id)
    print(f"User {username} belongs to group:")
    print(f"Group Name: {group_info.gr_name}")
    print(f"Group ID: {group_info.gr_gid}")
    print(f"Group Members: {', '.join(group_info.gr_mem)}")
except KeyError:
    print(f"User {username} not found.")
```

### 5. Listing All Groups

```python
import grp

# Example: List all groups in the system
for group_info in grp.getgrall():
    print(f"Group Name: {group_info.gr_name}, Group ID: {group_info.gr_gid}")
```

### 6. Retrieving User Information Using `os` Module

```python
import os
import pwd

# Example: Get user information using os.getpwuid()
username = 'example_user'
try:
    user_id = os.getuid()
    user_entry = pwd.getpwuid(user_id)
    print(f"Current user {pwd.getlogin()} found:")
    print(f"Username: {user_entry.pw_name}")
    print(f"Password Hash: {user_entry.pw_passwd}")
    print(f"UID: {user_entry.pw_uid}")
    print(f"GID: {user_entry.pw_gid}")
    print(f"Home Directory: {user_entry.pw_dir}")
    print(f"Shell Program: {user_entry.pw_shell}")
except KeyError:
    print("No user information available.")
```

### 7. Changing the Shell of a User

```python
import pwd
import os

# Example: Change the shell for a specific user
username = 'example_user'
shell_path = '/bin/bash'
try:
    user_entry = pwd.getpwnam(username)
    # Check if the new shell exists
    if os.path.exists(shell_path):
        print(f"Changing shell for {username} to {shell_path}.")
        user_entry.pw_shell = shell_path
        pwd.setpwent()
        try:
            pwd.putpwent(user_entry)
            pwd.endpwent()
            print("Shell changed successfully.")
        except PermissionError:
            print("Permission denied to change the shell.")
    else:
        print(f"The specified shell {shell_path} does not exist.")
except KeyError:
    print(f"User {username} not found.")
```

### 8. Retrieving User and Group Information Using `getpass` Module

```python
import getpass

# Example: Retrieve user information using getpass.getuser()
print(f"The current user is: {getpass.getuser()}")

# Example: Retrieve group information for the current user
username = getpass.getuser()
try:
    user_entry = pwd.getpwnam(username)
    print(f"Current user's group is:")
    group_info = grp.getgrgid(user_entry.pw_gid)
    print(f"Group Name: {group_info.gr_name}")
    print(f"Group ID: {group_info.gr_gid}")
    print(f"Group Members: {', '.join(group_info.gr_mem)}")
except KeyError:
    print("No user information available.")
```

### 9. Listing All Users and Their Groups

```python
import pwd
import grp

# Example: List all users and their groups
for user_info in pwd.getpwall():
    username = user_info.pw_name
    try:
        group_info = grp.getgrgid(user_info.pw_gid)
        print(f"User {username} belongs to group(s):")
        for member in group_info.gr_mem:
            print(member)
    except KeyError:
        print(f"No information available for user {username}.")
```

### 10. Changing the Password of a User

```python
import pwd
import crypt
import os

# Example: Change the password for a specific user (requires superuser privileges)
username = 'example_user'
new_password = 'securepassword'

try:
    user_entry = pwd.getpwnam(username)
    # Check if the new password meets complexity requirements
    if len(new_password) >= 8 and any(char.isdigit() for char in new_password):
        print(f"Changing password for {username}.")
        
        # Hash the new password
        salt = os.urandom(2).hex()
        hashed_password = crypt.crypt(new_password, f'$6${salt}')

        user_entry.pw_passwd = hashed_password

        pwd.setpwent()
        try:
            pwd.putpwent(user_entry)
            pwd.endpwent()
            print("Password changed successfully.")
        except PermissionError:
            print("Permission denied to change the password.")
    else:
        print("The new password must be at least 8 characters long and contain at least one digit.")
except KeyError:
    print(f"User {username} not found.")
```

### Notes:
- **Superuser Privileges**: Some of these examples require superuser privileges (`sudo`) due to operations like changing passwords or modifying user information.
- **Password Hashing**: Passwords are hashed using the `crypt` module. The format `$6$<salt>$<hashed_password>` is used for bcrypt hashing, which provides strong password security.
- **Error Handling**: Proper error handling is implemented to manage cases where users or groups do not exist or permissions are denied.

These examples cover a range of functionalities available in the `pwd` module, providing clear and concise code that can be used as documentation or reference material.
