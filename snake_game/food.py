import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.shape("circle")
        self.shapesize(.5,0.5,1)
        self.refresh()

    def refresh(self):
        rand_xc = random.randint(-295, 295)
        rand_yc = random.randint(-295, 295)
        self.goto(rand_xc, rand_yc)
        print(rand_xc, rand_yc)
