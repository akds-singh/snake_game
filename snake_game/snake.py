from turtle import Turtle, Screen
import time

screen = Screen()
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
COLOR_LIST = ['red', 'yellow', 'green', 'pink', 'brown']
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.counter = 0
        self.head = self.segment_list[0]

    # Create the snake of required length
    def create_snake(self):

        for index_num in range(5):
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color(COLOR_LIST[index_num])
            new_segment.goto(STARTING_POSITION[index_num])

            self.segment_list.append(new_segment)
            xc = new_segment.xcor()
            yc = new_segment.ycor()
        screen.update()

    def move(self):
        for seg_num in range(len(self.segment_list)-1, 0, -1):
            print(seg_num)
            xc = self.segment_list[seg_num - 1].xcor()
            yc = self.segment_list[seg_num - 1].ycor()

            self.segment_list[seg_num].goto(xc, yc)
            self.counter += 1

        # Move the head 20 px forward , so that rest of segment follows the head
        self.head.forward(MOVE_DISTANCE)
        print('counter: ', self.counter)

    def extension(self):
        new_segment = Turtle('square')
        new_segment.fillcolor('white')
        xc = self.segment_list[-1].xcor()
        yc = self.segment_list[-1].ycor()
        new_segment.goto(xc+20, yc+20)
        self.segment_list.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # Turtle().he

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
