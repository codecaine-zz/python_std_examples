# sqlite3 - DB-API 2.0 interface for SQLite databases

Here are comprehensive code examples for using the `sqlite3` module in Python, which provides an interface to the SQLite database engine:
1. Connecting to a SQLite database:
```python
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')
```
2. Creating a cursor object to execute SQL commands:
```python
cursor = conn.cursor()
```
3. Executing an SQL command to create a table:
```python
cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT NOT NULL)''')
```
4. Inserting data into the table using parameterized queries:
```python
cursor.execute("INSERT INTO users (name) VALUES (?)", ('John',))
conn.commit()
```
5. Executing a SQL query to retrieve data from the table:
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
6. Closing the database connection and cursor:
```python
cursor.close()
conn.close()
```
7. Handling exceptions using try-except blocks:
```python
import sqlite3

try:
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT NOT NULL)''')
    cursor.execute("INSERT INTO users (name) VALUES (?)", ('John',))
    conn.commit()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
finally:
    cursor.close()
    conn.close()
```
8. Creating a connection using a context manager:
```python
import sqlite3

with sqlite3.connect('my_database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT NOT NULL)''')
    cursor.execute("INSERT INTO users (name) VALUES (?)", ('John',))
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```
9. Executing an SQL command using a parameterized query with named placeholders:
```python
cursor.execute("INSERT INTO users (name) VALUES (:name)", {'name': 'John'})
conn.commit()
```
10. Executing an SQL command to update data in the table:
```python
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ('Jane', 1))
conn.commit()
```
11. Executing an SQL command to delete data from the table:
```python
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
conn.commit()
```
12. Executing an SQL command using a parameterized query with positional placeholders:
```python
cursor.execute("INSERT INTO users (name) VALUES (?, ?)", ('John', 'Doe'))
conn.commit()
```
13. Executing an SQL command to select distinct values from a table:
```python
cursor.execute("SELECT DISTINCT name FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
14. Executing an SQL command to count the number of rows in a table:
```python
cursor.execute("SELECT COUNT(*) FROM users")
row = cursor.fetchone()
print(row[0])
```
15. Executing an SQL command to order the results by a column:
```python
cursor.execute("SELECT * FROM users ORDER BY name DESC")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
16. Executing an SQL command to join two tables:
```python
cursor.execute("SELECT u.name, t.value FROM users u JOIN table2 t ON u.id = t.user_id")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
17. Executing an SQL command to perform a group by operation:
```python
cursor.execute("SELECT name, COUNT(*) FROM users GROUP BY name")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
18. Executing an SQL command to calculate the average of a column:
```python
cursor.execute("SELECT AVG(age) FROM users")
row = cursor.fetchone()
print(row[0])
```
19. Executing an SQL command to calculate the sum of a column:
```python
cursor.execute("SELECT SUM(salary) FROM employees")
row = cursor.fetchone()
print(row[0])
```
20. Executing an SQL command to calculate the maximum value of a column:
```python
cursor.execute("SELECT MAX(height) FROM people")
row = cursor.fetchone()
print(row[0])
```
21. Executing an SQL command to calculate the minimum value of a column:
```python
cursor.execute("SELECT MIN(weight) FROM people")
row = cursor.fetchone()
print(row[0])
```
22. Executing an SQL command to select data from multiple tables using subqueries:
```python
cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > 30) AS u JOIN table2 t ON u.id = t.user_id")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
23. Executing an SQL command to select data from multiple tables using joins and conditions:
```python
cursor.execute("SELECT u.name, t.value FROM users u JOIN table2 t ON u.id = t.user_id WHERE u.age > 30")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
24. Executing an SQL command to select data from multiple tables using subqueries and conditions:
```python
cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > 30) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > 100")
rows = cursor.fetchall()
for row in rows:
    print(row)
```
25. Executing an SQL command to select data from multiple tables using joins and conditions with parameters:
```python
cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > :age) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > :value", {'age': 30, 'value': 100})
rows = cursor.fetchall()
for row in rows:
    print(row)
```
26. Executing an SQL command to select data from multiple tables using joins and conditions with parameters and placeholders:
```python
cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > :age) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > ?", (100,))
rows = cursor.fetchall()
for row in rows:
    print(row)
```
27. Executing an SQL command to select data from multiple tables using joins and conditions with parameters and placeholders, and handling exceptions:
```python
import sqlite3

try:
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > :age) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > ?", (100,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("An error occurred:", e)
finally:
    cursor.close()
    conn.close()
```
28. Executing an SQL command to select data from multiple tables using joins and conditions with parameters, placeholders, and handling exceptions and logging:
```python
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

try:
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > :age) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > ?", (100,))
    rows = cursor.fetchall()
    for row in rows:
        logging.info(row)
except sqlite3.Error as e:
    logging.error("An error occurred:", e)
finally:
    cursor.close()
    conn.close()
```
29. Executing an SQL command to select data from multiple tables using joins and conditions with parameters, placeholders, and handling exceptions and logging, and using context managers:
```python
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

try:
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > :age) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > ?", (100,))
        rows = cursor.fetchall()
        for row in rows:
            logging.info(row)
except sqlite3.Error as e:
    logging.error("An error occurred:", e)
```
30. Executing an SQL command to select data from multiple tables using joins and conditions with parameters, placeholders, and handling exceptions and logging, and using context managers and exception handling:
```python
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

try:
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM (SELECT id, name FROM users WHERE age > :age) AS u JOIN table2 t ON u.id = t.user_id WHERE t.value > ?", (100,))
        rows = cursor.fetchall()
except sqlite3.Error as e:
    logging.error("An error occurred:", e)
else:
    for row in rows:
        logging.info(row)
finally:
    cursor.close()
    conn.close()
```



