# turtle - Turtle graphics

The `turtle` module is a versatile tool in Python that provides a simple way to create visual graphics using turtles, which are animated line segments on the screen. Here are comprehensive and well-documented code examples for various functionalities of the `turtle` module:

### Basic Usage Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle left by 90 degrees
t.left(90)

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Drawing Shapes Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw an equilateral triangle
side_length = 100
for _ in range(3):
    t.forward(side_length)
    t.left(120)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Drawing a Circle Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a circle with radius 50
radius = 50
t.circle(radius)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Customizing Turtle Appearance Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the color of the turtle to blue
t.color("blue")

# Set the shape of the turtle to square
t.shape("square")

# Draw a square with side length 100
for _ in range(4):
    t.forward(100)
    t.right(90)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Using Pen Up and Down Commands Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle forward by 100 units
t.forward(100)

# Lift up the pen, so the turtle won't draw while moving
t.penup()

# Move the turtle backward by 50 units
t.backward(50)

# Put down the pen again to start drawing
t.pendown()

# Draw a line of length 100 from the current position
t.forward(100)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Drawing Multiple Shapes Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square and then a circle
side_length = 100
circle_radius = 50

# Draw an equilateral triangle
for _ in range(3):
    t.forward(side_length)
    t.left(120)

# Move to the position above the square
t.penup()
t.goto(-side_length // 2, side_length // 4)
t.pendown()

# Draw a circle
t.circle(circle_radius)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Using Functions Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

def draw_square(t, side_length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

# Draw a square and then a circle
side_length = 100
circle_radius = 50

draw_square(t, side_length)
t.penup()
t.goto(-side_length // 2, side_length // 4)
t.pendown()

draw_circle(t, circle_radius)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Using Event Handling Example

```python
import turtle

# Create a turtle object
t = turtle.Turtle()

def draw_square(event):
    """Draws a square in response to mouse click."""
    t.penup()
    x, y = event.x, event.y
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(50)
        t.right(90)

# Bind the draw_square function to the left button of the mouse
turtle.onscreenclick(draw_square)

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

### Using Screen Properties Example

```python
import turtle

# Create a screen object with a specific background color
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle object
t = turtle.Turtle()

# Draw a square and then change the background color to yellow
side_length = 100
circle_radius = 50

draw_square(t, side_length)
t.penup()
t.goto(-side_length // 2, side_length // 4)
t.pendown()

draw_circle(t, circle_radius)

# Change the background color of the screen
screen.bgcolor("yellow")

# Hide the turtle and exit on click
t.hideturtle()
turtle.done()
```

These examples cover a range of functionalities available in the `turtle` module, from basic drawing commands to more advanced features like event handling and screen properties. They are designed to be clear, concise, and suitable for inclusion in official documentation or educational materials.
