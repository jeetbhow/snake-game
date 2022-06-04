from turtle import Screen, Turtle
from snake import Snake, Segment
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
snake = Snake()
screen.update()

screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_over = False
food = Food()
food.move()
while not game_over:
    screen.update()
    snake.move()
    time.sleep(0.05)

    if snake.head.distance(food) < 10.0:
        food.move()
        new_segment = Segment((snake.tail.xcor(), snake.tail.ycor()))
        snake.add_segment(new_segment)
        scoreboard.update()

    if (snake.head.xcor() > 290.0 or snake.head.xcor() < -290.0 or
            snake.head.ycor() > 295.0 or snake.head.ycor() < -295.0):
        game_over = True

scoreboard.game_over()
screen.exitonclick()
