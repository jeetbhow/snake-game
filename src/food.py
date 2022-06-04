import random
from turtle import Turtle
from typing import Tuple


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()

    def move(self) -> None:
        self.goto(10 * random.randint(0, 10), 10 * random.randint(0, 10))