# ast - Abstract Syntax Trees
## Table of Contents

1. [1. Parsing Source Code](#1-parsing-source-code)
2. [2. Walking the AST](#2-walking-the-ast)
3. [3. Modifying the AST](#3-modifying-the-ast)
4. [4. Evaluating an AST](#4-evaluating-an-ast)
5. [5. Extracting Information from an AST](#5-extracting-information-from-an-ast)



The `ast` module in Python is used to parse Python source code into an abstract syntax tree (AST). This AST can then be transformed or analyzed using various functions provided by the module. Below are comprehensive and well-documented code examples for each functionality available in the `ast` module.

### 1. Parsing Source Code

```python
import ast

# Sample Python source code as a string
source_code = """
def add(a, b):
    return a + b

result = add(3, 5)
"""

# Parse the source code into an AST
tree = ast.parse(source_code)

# Print the AST in a readable format
print(ast.dump(tree))
```

**Explanation:**
- `ast.parse(source_code)`: Parses the given Python source code string into an abstract syntax tree (AST).
- `ast.dump(tree)`: Prints the AST in a human-readable format.

### 2. Walking the AST

```python
import ast

# Sample AST from the previous example
tree = ast.parse(source_code)

def traverse(node, indent=0):
    print(' ' * indent + node.__class__.__name__)
    for child in ast.iter_child_nodes(node):
        traverse(child, indent + 4)

# Traverse the AST and print each node's class name
traverse(tree)
```

**Explanation:**
- `ast.iter_child_nodes(node)`: Iterates over all child nodes of a given AST node.
- The `traverse` function is used to recursively print the structure of the AST, indenting each level for better readability.

### 3. Modifying the AST

```python
import ast

# Sample AST from the previous example
tree = ast.parse(source_code)

def modify(node):
    if isinstance(node, ast.FunctionDef) and node.name == 'add':
        # Modify the function definition to include a docstring
        node.body.insert(0, ast.Expr(value=ast.Str(s='This is a modified add function')))

# Traverse the AST and modify nodes as needed
modify(tree)

# Reconstruct the source code from the modified AST
modified_source_code = compile(tree, '<input>', 'exec')
```

**Explanation:**
- `isinstance(node, ast.FunctionDef) and node.name == 'add'`: Checks if a node is a function definition named `add`.
- `node.body.insert(0, ast.Expr(value=ast.Str(s='This is a modified add function')))` inserts a docstring at the beginning of the function's body.
- `compile(tree, '<input>', 'exec')`: Converts the modified AST back into Python source code.

### 4. Evaluating an AST

```python
import ast
import operator as op

# Sample AST from the previous example
tree = ast.parse(source_code)

def evaluate(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = evaluate(ast.walk(node)[0])
        right = evaluate(ast.walk(node)[-1])
        operators = {
            ast.Add: op.add,
            ast.Sub: op.sub,
            ast.Mult: op.mul,
            ast.Div: op.truediv,
            ast.Pow: op.pow
        }
        return operators[type(node.op)](left, right)
    else:
        raise ValueError(f"Unsupported node type: {node.__class__.__name__}")

# Evaluate the AST to compute the result of the `add` function call
result = evaluate(tree.body[0].value.args[1])
print(result)
```

**Explanation:**
- `ast.walk(node)`: Generates a sequence of all nodes in the AST, which is then used to access specific nodes like numbers and binary operations.
- `operators[type(node.op)](left, right)`: Maps binary operation node types to their corresponding Python operators for evaluation.

### 5. Extracting Information from an AST

```python
import ast

# Sample AST from the previous example
tree = ast.parse(source_code)

def extract_functions(tree):
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
    return functions

# Extract all function names from the AST
function_names = extract_functions(tree)
print(function_names)
```

**Explanation:**
- `ast.walk(tree)`: Iterates over all nodes in the AST.
- `isinstance(node, ast.FunctionDef)`: Checks if a node is a function definition.
- Collects all function names into a list and returns it.

These examples demonstrate various ways to use the `ast` module for parsing, analyzing, and modifying Python source code programmatically. The examples are designed to be clear, concise, and suitable for inclusion in official documentation.
