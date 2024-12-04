# turtle — Turtle graphics

Here's an example of using the turtle module in Python:

```python
# Importing the turtle module
import turtle

# Creating a new turtle screen and setting its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Creating a new turtle object
my_turtle = turtle.Turtle()

# Moving the turtle forward by 20 units
my_turtle.forward(100)

# Turning the turtle left by 90 degrees
my_turtle.left(90)

# Drawing a square using the turtle's movements
for _ in range(4):
    my_turtle.forward(50)
    my_turtle.right(90)

# Writing "Hello, World!" on the screen using the turtle's pen
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()
my_turtle.write("Hello, World!", align="center", font=("Arial", 24, "bold"))

# Keeping the window open until it is closed by the user
turtle.done()
```

### Turtle Module Overview

The turtle module in Python provides a simple way to create graphics and animations. It allows you to create shapes, lines, curves, and more using basic movements such as forward, backward, left, right, and up.

Here are some key features of the turtle module:

*   **Turtle Movement:** The turtle can move forward, backward, left, or right by a specified distance.
*   **Drawing Shapes:** You can use loops to draw shapes like squares, triangles, and more.
*   **Writing Text:** You can write text on the screen using the `write` method of the turtle object.
*   **Coloring Shapes:** You can change the color of the turtle's pen by calling the `pencolor` method.

### Common Turtle Methods

Here are some common methods used with the turtle module:

*   `forward(distance)`: Moves the turtle forward by a specified distance.
*   `backward(distance)`: Moves the turtle backward by a specified distance.
*   `left(angle)`: Turns the turtle left by a specified angle.
*   `right(angle)`: Turns the turtle right by a specified angle.
*   `penup()`: Lifts the pen off the paper, allowing you to move without drawing.
*   `pendown()`: Places the pen back on the paper, starting to draw again.
*   `write(text, align=align, font=(font_size, font_type, font_style))`: Writes text on the screen using the turtle's pen.

### Turtle Module Constants

Here are some constants provided by the turtle module:

*   `speed(slow=10, fast=0)`: Sets the speed of the turtle movements.
*   `colormode(r, g, b, color)`: Changes the color mode to RGB or CMYK.

Note: The above code examples demonstrate basic usage of the turtle module. For more advanced graphics and animations, consider exploring other Python modules like NumPy, Matplotlib, or Pillow.
