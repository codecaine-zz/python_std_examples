# sqlite3 - DB-API 2.0 interface for SQLite databases

The `sqlite3` module is a part of Python's standard library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. This makes it particularly suitable for small applications or embedded systems where a full-fledged RDBMS might be overkill.

Below are comprehensive code examples for various functionalities in the `sqlite3` module, including connection management, cursor creation, executing queries, handling results, and closing connections. These examples follow best practices and are designed to be clear and concise.

### 1. Establishing a Connection

```python
import sqlite3

# Connect to an SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object using the connection
cursor = connection.cursor()
```

**Explanation:**
- `sqlite3.connect('example.db')` creates a new connection to an SQLite database file named 'example.db'. If the file does not exist, it will be created.
- The `cursor()` method is used to create a cursor object which is used to execute SQL commands.

### 2. Executing a Query

```python
# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john.doe@example.com'))

# Commit the changes to the database
connection.commit()
```

**Explanation:**
- `CREATE TABLE IF NOT EXISTS users (...)` creates a new table named 'users' with columns for `id`, `name`, and `email`.
- `INSERT INTO users (name, email) VALUES (?, ?)` inserts a new row into the 'users' table. The placeholders `?` are used to safely insert data from variables.
- `connection.commit()` saves the changes made by the SQL commands.

### 3. Fetching Results

```python
# Query all users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

**Explanation:**
- `SELECT * FROM users` retrieves all records from the 'users' table.
- `fetchall()` returns all remaining rows of a query result as a list of tuples. Each tuple represents a row.

### 4. Handling Exceptions

```python
try:
    # Attempt to execute a command that will fail due to missing column name
    cursor.execute("INSERT INTO users (name) VALUES (?)", ('Jane Doe',))
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
```

**Explanation:**
- `try-except` block is used to handle potential errors during database operations.
- `sqlite3.Error` is a base class for all exceptions related to the SQLite library.

### 5. Closing the Connection

```python
# Close the cursor and connection
cursor.close()
connection.close()
```

**Explanation:**
- `cursor.close()` releases the resources associated with the cursor object.
- `connection.close()` closes the database connection, freeing up system resources.

### Additional Examples

#### 6. Executing Prepared Statements (Parameterized Queries)

```python
# Prepare and execute a parameterized query
name = 'Alice Smith'
email = 'alice.smith@example.com'
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
connection.commit()

# Fetch the inserted user by name
cursor.execute("SELECT * FROM users WHERE name=?", (name,))
user = cursor.fetchone()
print(user)
```

**Explanation:**
- `INSERT INTO users (name, email) VALUES (?, ?)` uses placeholders to safely insert data.
- `fetchone()` retrieves the first row of a query result.

#### 7. Querying Multiple Rows

```python
# Execute a query that returns multiple rows
cursor.execute("SELECT * FROM users")
for user in cursor:
    print(user)
```

**Explanation:**
- The loop iterates over the results and prints each row as a tuple.

#### 8. Dropping a Table

```python
# Drop an existing table if it exists
try:
    cursor.execute("DROP TABLE IF EXISTS users")
except sqlite3.Error as e:
    print(f"An error occurred while dropping the table: {e}")
```

**Explanation:**
- `DROP TABLE IF EXISTS users` removes the 'users' table if it exists, using a try-except block to handle potential errors.

#### 9. Using Transactions

```python
# Start a transaction and insert multiple records in one shot
connection.execute("BEGIN TRANSACTION")
cursor.executemany(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    [
        ('Bob Brown', 'bob.brown@example.com'),
        ('Charlie Green', 'charlie.green@example.com')
    ]
)
connection.commit()
```

**Explanation:**
- `BEGIN TRANSACTION` starts a new transaction.
- `executemany()` is used to insert multiple records in one query, which can be more efficient than executing individual queries.

#### 10. Retrieving the Last Inserted Row ID

```python
# Get the last inserted row ID after inserting data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('David Blue', 'david.blue@example.com'))
connection.commit()

last_insert_id = cursor.lastrowid
print(f"The last inserted row ID is: {last_insert_id}")
```

**Explanation:**
- `lastrowid` provides the ID of the last row that was successfully inserted into the table.

These examples cover a range of common operations with SQLite using Python's `sqlite3` module. By following these examples, you should be able to efficiently manage and interact with SQLite databases in your Python applications.
