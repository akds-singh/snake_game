from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title(titlestring='Snake-Game')
screen.tracer(0)
food = Food()
score_board = ScoreBoard()

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

is_game_on: bool = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.score += 1
        score_board.clear()
        score_board.score_count()
        snake.extension()
        print(snake.head.xcor())
    if snake.head.ycor() > 298 or snake.head.ycor() < -298 or snake.head.xcor() > 298 or snake.head.xcor() < -298:
        is_game_on = False

    for index in range(len(snake.segment_list) - 1, 2, -1):
        if snake.head.distance(snake.segment_list[index]) < 10:
            is_game_on = False

score_board.goto((0, 0))
score_board.game_over()
screen.exitonclick()
