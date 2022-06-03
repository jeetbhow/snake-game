from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.update()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")


game_over = False
while not game_over:
    snake.move()
    time.sleep(0.05)
    screen.update()

screen.exitonclick()
