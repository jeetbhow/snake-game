from turtle import Screen
from snake import Snake, Segment
from food import Food
from scoreboard import Scoreboard
import time

game_over = False

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Game objects
scoreboard = Scoreboard()
snake = Snake()
screen.update()
food = Food()
food.move()


def game_loop():
    global game_over
    while not game_over:
        screen.update()
        snake.move()
        time.sleep(0.05)

        # Food collision detection
        if snake.head.distance(food) < 10.0:
            food.move()
            new_segment = Segment((snake.tail.xcor(), snake.tail.ycor()))
            snake.add_segment(new_segment)
            scoreboard.update()

        # Wall collision detection
        if (snake.head.xcor() > 290.0 or snake.head.xcor() < -290.0 or
                snake.head.ycor() > 295.0 or snake.head.ycor() < -295.0):
            game_over = True

        # Tail collision detection
        for segment in snake.segments[1:]:
            if segment.distance(snake.head) < 5:
                game_over = True
    scoreboard.game_over()


def restart():
    global game_over
    if game_over:
        game_over = False
        scoreboard.reset()
        snake.reset()
        game_loop()


# Keypress detection.
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=restart, key='space')

game_loop()
screen.exitonclick()
