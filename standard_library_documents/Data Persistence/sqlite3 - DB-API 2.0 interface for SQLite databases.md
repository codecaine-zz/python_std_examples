# sqlite3 — DB-API 2.0 interface for SQLite databases

Here's an example of how you can use the `sqlite3` module in Python:

```python
# Importing sqlite3 module
import sqlite3

# Create a connection object
def create_connection(db_name):
    """
    Creates a connection to the SQLite database.

    Args:
        db_name (str): The name of the database file.

    Returns:
        sqlite3.Connection: A connection object.
    """
    try:
        # Attempt to connect to the database
        conn = sqlite3.connect(db_name)
        print(f"Connected to {db_name}")
        return conn
    except sqlite3.Error as e:
        # Handle any errors that occur during connection
        print(e)

# Create a cursor object
def create_cursor(conn):
    """
    Creates a cursor object from the connection.

    Args:
        conn (sqlite3.Connection): The connection object.

    Returns:
        sqlite3.Cursor: A cursor object.
    """
    try:
        # Attempt to create a cursor
        cur = conn.cursor()
        print("Cursor created")
        return cur
    except sqlite3.Error as e:
        # Handle any errors that occur during cursor creation
        print(e)

# Create table
def create_table(conn, table_name):
    """
    Creates a new table in the database.

    Args:
        conn (sqlite3.Connection): The connection object.
        table_name (str): The name of the table to create.
    """
    try:
        # SQL query to create table
        cur = conn.cursor()
        sql_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        """
        # Execute the SQL query
        cur.execute(sql_query)
        conn.commit()
        print(f"Table {table_name} created")
    except sqlite3.Error as e:
        # Handle any errors that occur during table creation
        print(e)

# Insert data into table
def insert_data(conn, table_name, data):
    """
    Inserts data into the specified table.

    Args:
        conn (sqlite3.Connection): The connection object.
        table_name (str): The name of the table to insert data into.
        data (dict): A dictionary containing the data to be inserted.
    """
    try:
        # SQL query to insert data
        cur = conn.cursor()
        sql_query = f"""
            INSERT INTO {table_name} (name, age)
            VALUES (?, ?)
        """
        # Execute the SQL query with parameters
        cur.execute(sql_query, tuple(data.values()))
        conn.commit()
        print(f"Data inserted into table {table_name}")
    except sqlite3.Error as e:
        # Handle any errors that occur during data insertion
        print(e)

# Select data from table
def select_data(conn, table_name):
    """
    Retrieves data from the specified table.

    Args:
        conn (sqlite3.Connection): The connection object.
        table_name (str): The name of the table to retrieve data from.

    Returns:
        list: A list of rows retrieved from the database.
    """
    try:
        # SQL query to select data
        cur = conn.cursor()
        sql_query = f"""
            SELECT * FROM {table_name}
        """
        # Execute the SQL query
        cur.execute(sql_query)
        rows = cur.fetchall()
        print(f"Data retrieved from table {table_name}")
        return rows
    except sqlite3.Error as e:
        # Handle any errors that occur during data selection
        print(e)

# Update data in table
def update_data(conn, table_name, where_clause, data):
    """
    Updates the specified data in the table.

    Args:
        conn (sqlite3.Connection): The connection object.
        table_name (str): The name of the table to update data in.
        where_clause (str): The WHERE clause for the UPDATE query.
        data (dict): A dictionary containing the new data values.
    """
    try:
        # SQL query to update data
        cur = conn.cursor()
        sql_query = f"""
            UPDATE {table_name} SET name = ?, age = ?
            WHERE {where_clause}
        """
        # Execute the SQL query with parameters
        cur.execute(sql_query, tuple(data.values()))
        conn.commit()
        print(f"Data updated in table {table_name}")
    except sqlite3.Error as e:
        # Handle any errors that occur during data update
        print(e)

# Delete data from table
def delete_data(conn, table_name, where_clause):
    """
    Deletes the specified data from the table.

    Args:
        conn (sqlite3.Connection): The connection object.
        table_name (str): The name of the table to delete data from.
        where_clause (str): The WHERE clause for the DELETE query.
    """
    try:
        # SQL query to delete data
        cur = conn.cursor()
        sql_query = f"""
            DELETE FROM {table_name}
            WHERE {where_clause}
        """
        # Execute the SQL query
        cur.execute(sql_query)
        conn.commit()
        print(f"Data deleted from table {table_name}")
    except sqlite3.Error as e:
        # Handle any errors that occur during data deletion
        print(e)

# Main function
def main():
    # Create a connection to the database
    db_name = "test.db"
    conn = create_connection(db_name)
    
    # Create a cursor object
    cur = create_cursor(conn)

    # Create table
    table_name = "users"
    create_table(conn, table_name)

    # Insert data into table
    data = {"name": "John", "age": 30}
    insert_data(conn, table_name, data)

    # Select data from table
    rows = select_data(conn, table_name)
    for row in rows:
        print(row)

    # Update data in table
    where_clause = "id = 1"
    update_data(conn, table_name, where_clause, {"name": "Jane", "age": 31})

    # Delete data from table
    delete_where_clause = "id = 2"
    delete_data(conn, table_name, delete_where_clause)

if __name__ == "__main__":
    main()
```

This code covers the following topics:

1. Connecting to a SQLite database using `sqlite3.connect()`.
2. Creating a cursor object using `conn.cursor()`.
3. Executing SQL queries using the `execute()` method.
4. Committing changes using the `commit()` method.
5. Retrieving data from the database using the `fetchall()` method.
6. Updating data in the database using the `update()` method.
7. Deleting data from the database using the `delete()` method.

The example code demonstrates how to perform these tasks and provides a basic structure for working with SQLite databases using Python's `sqlite3` module.
