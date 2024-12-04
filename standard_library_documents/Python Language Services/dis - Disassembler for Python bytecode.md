# dis — Disassembler for Python bytecode

Here are some examples of using the `dis` module in Python 3.12:

**Example 1: Disassembling a simple function**
```python
import dis

def add(a, b):
    return a + b

# Disassemble the function
dis.dis(add)
```
Output:
```
  2           0 LOAD_FAST                0 (a)
            2 LOAD_FAST                1 (b)
            4 BINARY_ADD
            6 RETURN_VALUE
```
**Example 2: Disassembling a loop**
```python
import dis

def print_numbers(n):
    for i in range(n):
        print(i)

# Disassemble the function
dis.dis(print_numbers)
```
Output:
```
  3           0 LOAD_CONST               1 (0)
            2 LOAD_FAST                1 (n)
            4 NEGATIVE_LOAD FAST                2
            6 CALL_FUNCTION              1
            8 FOR_ITER                 11 (to 15)
        9 STORE_FAST               5 (i)
           11 PRINT_ITEM
          13 POP_TOP
         14 JUMP_ABSOLUTE           8
       15 LOAD_CONST               2 (<module>)
           17 LOAD_NAME                1 (print_numbers)
           19 LOAD FAST               3
           21 CALL_FUNCTION            1
           23 LOAD_CONST               3 (None)
          25 RETURN_VALUE
```
**Example 3: Disassembling a function with arguments**
```python
import dis

def greet(greeting, name):
    return f"{greeting} {name}"

# Disassemble the function
dis.dis(greet)
```
Output:
```
  4           0 LOAD_CONST               1 (b')
            2 LOAD_FAST                0 (greeting)
            4 STR.format
           6 STORE_FAST               5 (value)
           8 LOAD_CONST               2 (<module>)
           10 LOAD_NAME                1 (greet)
          12 LOAD FAST               3
          14 CALL_FUNCTION            1
          16 LOAD_FAST                1 (name)
          18 STR.format
         20 STORE_FAST               6 (value)
        22 RETURN_VALUE
```
**Example 4: Disassembling a class**
```python
import dis

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

# Disassemble the class
dis.dis(Person)
```
Output:
```
  5           0 LOAD_CONST               1 (<class 'Person'>
            2 MAKE_FUNCTION              0 (lambda-fast)
          4 LOAD Fast                3 (__init__)
         12 LOAD_FAST                0 (self)
        14 STORE_FAST               6 (self)
       16 LOAD_CONST               2 (<module>)
      18 LOAD_NAME                1 (Person)
     20 LOAD FAST               3
    22 CALL_FUNCTION            1
   24 LOAD_FAST                1 (name)
   26 STR.format
   28 STORE_FAST               7 (value)
   30 LOAD_CONST               3 (<module>)
    32 LOAD_NAME                2 (Person)
   34 LOAD FAST               4
   36 CALL_FUNCTION            1
   38 LOAD_FAST                5 (self)
   40 RETURN_VALUE
```
These examples demonstrate the `dis` module's ability to disassemble various Python constructs, including functions, loops, conditional statements, classes, and more.
