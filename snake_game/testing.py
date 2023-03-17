import turtle

# create a screen object
screen = turtle.Screen()
screen.bgcolor("black")

# create a turtle object
t = turtle.Turtle()
t.color("white")
t.shape("square")
t.penup()


# define a function to move the turtle forward by 10 units
def move():
    t.forward(10)


# define a function to turn the turtle left by 90 degrees
def turn():
    t.left(90)


# define a function to draw a square and schedule the next move and turn
def draw():
    # clear the previous drawing
    # screen.reset()
    # draw a square
    for i in range(4):
        move()
        turn()
    # schedule the next draw after 1 second
    screen.ontimer(draw, 1000)


# start the drawing loop
draw()

# mainloop to keep the window open
screen.mainloop()
