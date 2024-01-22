import turtle

# Set up the window
window = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Set pen size to 3
t.pensize(3)

# Set drawing color to blue
t.pencolor("blue")

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle right by 90 degrees
t.right(90)

# Move the turtle forward by 50 units
t.forward(50)

# Turn the turtle left by 90 degrees
t.left(90)

# Lift the pen up – no drawing when moving
t.penup()

# Move the turtle to a specific location
t.goto(-50, -50)

# Put the pen down – drawing when moving
t.pendown()

# Draw a circle with radius of 25
t.circle(25)

# Draw a dot with diameter 10
t.dot(10)

# Set the turtle heading to 0 (East)
t.setheading(0)

# Change the turtle color
t.color("red")

# Draw a filled shape
t.begin_fill()
t.circle(40)
t.end_fill()

# Clear the drawing
t.clear()

# Reset the turtle's state
t.reset()

# Hide the turtle
t.hideturtle()

# Display the turtle
t.showturtle()

# Set the animation speed (0:fastest, 1:slowest, 10:normal)
t.speed(5)

# Display text
t.write("Hello, Turtle!")

# Get input with a dialog box
user_input = turtle.textinput("User Input", "Enter something:")

# Respond to user input
t.write(f"You entered: {user_input}")

# Filling a shape with color
t.begin_fill()
t.circle(80)
t.end_fill()

# Close the window on a click
window.exitonclick()