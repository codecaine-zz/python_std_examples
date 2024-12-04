# nis — Interface to Sun’s NIS (Yellow Pages)

**nis Module Code Generation**
=====================================

The `nis` module provides an interface to Sun's NIS (Yellow Pages), also known as the Network Information Service.

### Table of Contents

1. [Importing the nis module](#importing-the-nis-module)
2. [Loading a NIS database](#loading-a-nis-database)
3. [Searching for entries in a NIS database](#searching-for-entries-in-a-nis-database)
4. [Creating a NIS database](#creating-a-nis-database)
5. [Deleting a NIS database](#deleting-a-nis-database)

### Code Examples

#### Importing the nis module
```python
import nis

# Create an instance of the nis class
nis_db = nis.NIS()
```

#### Loading a NIS database
```python
# Load a existing NIS database from the default location ( /var/nis )
nis_db.load('sun4c')

# Load a specific NIS database with name 'my_nis'
nis_db.load('my_nis')
```

#### Searching for entries in a NIS database
```python
# Search for all entries in the current database
entries = nis_db.getnames()

# Get a specific entry from the current database by name
entry = nis_db.getname('MY_SERVICE')

print(entries)
print(entry)
```

#### Creating a NIS database
```python
# Create a new NIS database with default configuration
nis_db.create_database()

# Create a new NIS database with custom configuration
nis_db.create_database(
    # Specify the name of the database
    name='my_nis',
    # Specify the password for the database
    passwd='my_password',
)
```

#### Deleting a NIS database
```python
# Delete the current NIS database
nis_db.delete_database()

# Delete a specific NIS database with name 'my_nis'
nis_db.delete_database('my_nis')
```

### Full Code Example

```python
import nis

def main():
    # Create an instance of the nis class
    nis_db = nis.NIS()
    
    # Load a existing NIS database from the default location ( /var/nis )
    nis_db.load('sun4c')
    
    # Search for all entries in the current database
    entries = nis_db.getnames()
    
    print("Entries:")
    print(entries)
    
    # Get a specific entry from the current database by name
    entry = nis_db.getname('MY_SERVICE')
    
    print("\nEntry:")
    print(entry)
    
    # Create a new NIS database with default configuration
    nis_db.create_database()
    
    # Search for all entries in the newly created database
    entries_new = nis_db.getnames()
    
    print("New Entries:")
    print(entries_new)
    
if __name__ == "__main__":
    main()

```

Note: This code examples are just a starting point, you should consider implementing proper error handling and security measures when working with NIS databases.
