from turtle import Turtle, Screen


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.shape(name='circle')
        self.shapesize(0.01, 0.01, 0.01)
        self.color('white', 'black')
        self.goto(0, 280)
        self.write(arg=f"Score: {self.score} ", move=False, align='center', font=('Arial', 10, 'normal'))

    def score_count(self):
        # self.score += 1
        self.write(arg=f"Score: {self.score} ", move=False, align='center', font=('Arial', 10, 'normal'))

