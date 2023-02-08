import turtle

# Create turtle object
my_turtle1 = turtle.Turtle()

# Set line color and turtle
my_turtle1.shape("turtle")
my_turtle1.color("green")

# These are examples showing how the turtle moves from its starting position.
# You can uncomment them separately to understand how the direction works.
# Forward:
# my_turtle1.forward(100)

# Backwards:
# my_turtle1.backward(100)

# Up
# my_turtle1.left(90)
# my_turtle1.forward(100)

# Down
# my_turtle1.right(90)
# my_turtle1.forward(100)

# Example of random movement:
my_turtle1.forward(100)
my_turtle1.left(90)
my_turtle1.forward(100)
my_turtle1.right(45)
my_turtle1.forward(100)
my_turtle1.left(135)
my_turtle1.forward(300)
my_turtle1.left(90)
my_turtle1.forward(50) 

# Keep turtle canvas open when finished drawing
turtle.exitonclick()