# random - Generate Pseudo-Random Numbers

The `random` module in Python provides various functions to generate pseudo-random numbers, which are useful for simulations, cryptography, and more. Below are comprehensive examples of how to use this module to generate different types of random numbers.

## 1. Basic Random Number Generation

To generate a random integer within a specified range, you can use the `randint()` function:

```python
import random

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print("Random Integer:", random_integer)

# Generate a random integer between -5 and 5 (inclusive)
random_integer_negative = random.randint(-5, 5)
print("Random Integer (negative range):", random_integer_negative)
```

### 2. Random Floating-Point Numbers

To generate a floating-point number within a specified range, you can use the `uniform()` function:

```python
import random

# Generate a random floating-point number between 0 and 1
random_float = random.uniform(0, 1)
print("Random Float:", random_float)

# Generate a random floating-point number between 3.5 and 7.8
random_float_custom_range = random.uniform(3.5, 7.8)
print("Random Float (custom range):", random_float_custom_range)
```

### 3. Random Choice from a List

To select a random element from a list, you can use the `choice()` function:

```python
import random

fruits = ['apple', 'banana', 'cherry', 'date']
random_fruit = random.choice(fruits)
print("Random Fruit:", random_fruit)

# Selecting multiple random elements without replacement
random_fruits_multiple = random.sample(fruits, 3)
print("Random Fruits (multiple selection without replacement):", random_fruits_multiple)
```

### 4. Random Selection with Replacement

To select a random element from a list and allow replacement (i.e., selecting the same element multiple times), you can use the `choices()` function:

```python
import random

fruits = ['apple', 'banana', 'cherry', 'date']
random_fruits_with_replacement = random.choices(fruits, k=3)
print("Random Fruits (with replacement):", random_fruits_with_replacement)
```

### 5. Random Shuffle a List

To shuffle the elements of a list in place, you can use the `shuffle()` function:

```python
import random

fruits = ['apple', 'banana', 'cherry', 'date']
random.shuffle(fruits)
print("Shuffled Fruits:", fruits)

# Note: The original list is modified in place
```

### 6. Random Seed for Reproducibility

To ensure that your random number generation is reproducible, you can set a seed using the `seed()` function:

```python
import random

random.seed(42)
print("Random Number with Seed:", random.randint(1, 10))

# Using the same seed will produce the same random numbers
random.seed(42)
print("Another Random Number with Same Seed:", random.randint(1, 10))
```

### 7. Random Normal Distribution

To generate random numbers from a normal distribution, you can use the `normalvariate()` function:

```python
import random

# Generate a random number from a normal distribution with mean 0 and standard deviation 1
random_normal = random.normalvariate(0, 1)
print("Random Normal Number:", random_normal)

# Generate multiple numbers from a normal distribution
random_normals = [random.normalvariate(0, 1) for _ in range(5)]
print("Random Normals:", random_normals)
```

### 8. Random Binomial Distribution

To generate random numbers from a binomial distribution, you can use the `binomial()` function:

pip install numpy

```python
import numpy as np

# Generate a random number from a binomial distribution with parameters n=10 and p=0.5
random_binomial = np.random.binomial(10, 0.5)
print("Random Binomial Number:", random_binomial)

# Generate multiple numbers from a binomial distribution
random_bins = [np.random.binomial(10, 0.5) for _ in range(5)]
print("Random Bins:", random_bins)
```

### 9. Random Exponential Distribution

To generate random numbers from an exponential distribution, you can use the `expovariate()` function:

```python
import random

# Generate a random number from an exponential distribution with rate parameter λ=1
random_exponential = random.expovariate(1)
print("Random Exponential Number:", random_exponential)

# Generate multiple numbers from an exponential distribution
random_expenses = [random.expovariate(0.5) for _ in range(5)]
print("Random Expenses:", random_expenses)
```

### 10. Random Choices with Weights

To generate a list of random choices based on weights, you can use the `choices()` function:

```python
import random

fruits = ['apple', 'banana', 'cherry', 'date']
weights = [2, 3, 1, 4]  # Corresponding to the frequency of each fruit

random_fruits_weighted = random.choices(fruits, weights=weights, k=5)
print("Random Fruits with Weights:", random_fruits_weighted)
```

### Conclusion

The `random` module in Python provides a wide range of functions to generate various types of pseudo-random numbers. These examples cover basic operations like generating integers and floats, selecting elements from lists, shuffling lists, and generating numbers from different distributions. By using these functions, you can effectively incorporate randomness into your applications for simulations, games, and more.
