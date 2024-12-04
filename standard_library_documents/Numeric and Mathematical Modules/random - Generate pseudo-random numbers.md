# random — Generate pseudo-random numbers

**Random Module Code Examples**
=====================================

### Importing the Random Module
```python
# Import the random module
import random
```

### Generating Random Integers
```python
# Generate a random integer between 1 and 10
print(random.randint(1, 10))  # Output: 5

# Generate a random integer within a specified range
print(random.randint(-10, 10))  # Output: -7
```

### Generating Random Floating Point Numbers
```python
# Generate a random floating point number between 1.0 and 10.0
print(random.uniform(1.0, 10.0))  # Output: 4.523213456123456

# Generate a random floating point number within a specified range
print(random.uniform(-10.0, 10.0))  # Output: 2.134567890123456
```

### Generating Random Choices
```python
# Define a list of choices
choices = ['apple', 'banana', 'cherry']

# Generate a random choice from the list
print(random.choice(choices))  # Output: e.g., 'banana'

# Generate multiple random choices
print(random.choices(choices, k=3))  # Output: e.g., ['banana', 'apple', 'cherry']
```

### Generating Random Samples
```python
# Define a list of sample data
data = [1, 2, 3, 4, 5]

# Generate a random sample of 3 elements from the list
print(random.sample(data, 3))  # Output: e.g., [4, 2, 5]
```

### Shuffling Lists
```python
# Define a list to be shuffled
numbers = [1, 2, 3, 4, 5]

# Shuffle the list in-place
random.shuffle(numbers)
print(numbers)  # Output: e.g., [4, 5, 2, 1, 3]
```

### Setting Random Seeds
```python
# Set the random seed to a fixed value for reproducibility
random.seed(42)

# Generate a random integer between 1 and 10
print(random.randint(1, 10))  # Output: always 5

# Set the random seed again to return to default behavior
random.seed()
```

### Other Functions
```python
# Get the current system time in seconds since the epoch
print(random.getrandbits(32))

# Generate a random boolean value
print(random.random() < 0.5)  # Output: True or False

# Generate a random selection of two values from a list
selected = random.sample([1, 2, 3], 2)
print(selected)  # Output: e.g., [2, 1]
```

Note that the `random` module uses a pseudo-random number generator (PRNG), which is seeded with a fixed value or generated randomly at runtime. This means that the output of the PRNG will be different each time you run your program.
