# spwd - The shadow password database
## Table of Contents

1. [Example 1: Retrieve a Shadow Password Entry](#example-1-retrieve-a-shadow-password-entry)
2. [Example 2: Modify a Shadow Password Entry](#example-2-modify-a-shadow-password-entry)
3. [Example 3: List All Shadow Password Entries](#example-3-list-all-shadow-password-entries)
4. [Note:](#note)



The `spwd` module in the Python standard library provides access to the Unix-style shadow password database, which is used to store encrypted passwords for user accounts. This module allows you to manage and query shadow password entries without accessing the underlying system's files directly.

Below are comprehensive examples of how to use the `spwd` module for various operations:

### Example 1: Retrieve a Shadow Password Entry

```python
import spwd

def get_shadow_entry(username):
    """
    Retrieves the shadow password entry for a given username.

    Args:
        username (str): The username for which to retrieve the shadow password entry.

    Returns:
        dict: A dictionary containing the shadow password information.
    """
    try:
        # Retrieve the shadow password entry
        pwd_entry = spwd.getspnam(username)
        
        # Extract and return relevant information from the shadow password entry
        shadow_info = {
            'user': pwd_entry.sp_nam,  # Username
            'password': pwd_entry.sp_pwd,  # Encrypted Password
            'flags': pwd_entry.sp_flags,  # Flags (e.g., account expiration)
            'last_change': pwd_entry.sp_lastchg,  # Last password change timestamp
            'min': pwd_entry.sp_min,      # Minimum number of days between password changes
            'max': pwd_entry.sp_max,      # Maximum number of days a password can be used
            'warn': pwd_entry.sp_warn,    # Number of days before expiration to warn user
            'inactive': pwd_entry.sp_inact,  # Inactivity period after password expiration
            'expire': pwd_entry.sp_expire,   # Account expiration timestamp
            'reserved': pwd_entry.sp_atime,   # Last authentication time
        }
        
        return shadow_info
    except KeyError:
        print(f"No shadow entry found for user: {username}")
        return None

# Example usage
username = "exampleuser"
shadow_info = get_shadow_entry(username)
if shadow_info:
    print(shadow_info)
```

### Example 2: Modify a Shadow Password Entry

```python
import spwd
import crypt

def modify_shadow_entry(username, new_password):
    """
    Modifies the encrypted password for a given username.

    Args:
        username (str): The username whose shadow password needs to be modified.
        new_password (str): The new plain text password to encrypt and update.

    Returns:
        bool: True if the modification is successful, False otherwise.
    """
    try:
        # Retrieve the current shadow password entry
        pwd_entry = spwd.getspnam(username)
        
        # Encrypt the new password using crypt.CRYPT_METHOD_SHA512
        encrypted_password = crypt.crypt(new_password, crypt.METHOD_SHA512)
        
        # Update the shadow password in memory
        pwd_entry.sp_pwd = encrypted_password
        
        # Write the updated entry back to the system
        spwd.setspnam(username, pwd_entry)
        
        print(f"Shadow password for {username} has been successfully modified.")
        return True
    except (KeyError, crypt.CryptError) as e:
        print(f"Failed to modify shadow password for user {username}: {e}")
        return False

# Example usage
username = "exampleuser"
new_password = "new_secure_password123"
success = modify_shadow_entry(username, new_password)
```

### Example 3: List All Shadow Password Entries

```python
import spwd

def list_shadow_entries():
    """
    Lists all shadow password entries in the system.

    Returns:
        list: A list of dictionaries, each containing information about a shadow password entry.
    """
    shadow_entries = []
    
    # Iterate over all shadow password entries
    try:
        for pwd_entry in spwd.getspall():
            shadow_info = {
                'user': pwd_entry.sp_nam,
                'password': pwd_entry.sp_pwd,
                'flags': pwd_entry.sp_flags,
                'last_change': pwd_entry.sp_lastchg,
                'min': pwd_entry.sp_min,
                'max': pwd_entry.sp_max,
                'warn': pwd_entry.sp_warn,
                'inactive': pwd_entry.sp_inact,
                'expire': pwd_entry.sp_expire,
                'reserved': pwd_entry.sp_atime,
            }
            shadow_entries.append(shadow_info)
    except PermissionError:
        print("Permission denied to access shadow password database.")
    except Exception as e:
        print(f"An error occurred while listing shadow password entries: {e}")
    
    return shadow_entries

# Example usage
shadow_list = list_shadow_entries()
for entry in shadow_list:
    print(entry)
```

### Note:
- The `spwd` module is only available on Unix-like systems and may not be available on Windows.
- The encryption method used for passwords can vary based on system configuration. For example, on most systems, `crypt.METHOD_SHA512` is used, which is a strong cryptographic hash function.
- Ensure that you have the necessary permissions to modify shadow password entries on your system.

These examples provide a basic framework for interacting with the shadow password database using Python's `spwd` module. Adjustments may be needed based on specific system configurations and requirements.
