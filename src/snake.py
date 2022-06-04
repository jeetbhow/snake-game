from turtle import Turtle
from typing import List

INITIAL_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]


class Segment(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.goto(position)


class Snake:
    """Class that models the snake in the snake game. Contains methods that add
    segments to the snake as well as move it forward and change its direction. A
    snake is initialized with a body of 3 segments.

    Attributes:
        segments: a list of Segment objects that store data for each unit of the snake.
        head: the first segment of the snake that controls its direction.
    """

    def __init__(self) -> None:
        self.segments: List[Segment] = []

        for i in range(3):
            self.add_segment(Segment(INITIAL_POSITIONS[i]))

        self.head: Turtle = self.segments[0]
        self.tail: Turtle = self.segments[-1]

    def add_segment(self, s: Segment) -> None:
        """Takes a segment s as input and appends it to the body of the snake."""
        if s is not None:
            self.segments.append(s)
        else:
            return

    def move(self) -> None:
        """Move the entire snake forward by 10 units in the current direction."""
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(10)

    def up(self) -> None:
        """Change the direction of the snake so that it faces up if it's not currently
        moving along the vertical axis.
        """
        if self.head.heading() != 270.0:
            self.head.setheading(90.0)

    def down(self) -> None:
        """Change the direction of the snake so that it faces down if it's not
        currently moving along the vertical axis.
        """
        if self.head.heading() != 90.0:
            self.head.setheading(270.0)

    def left(self) -> None:
        """Changes the direction of the snake so that it faces left if it's
        not current moving along the horizontal axis."""
        if self.head.heading() != 0.0:
            self.head.setheading(180.0)

    def right(self) -> None:
        """Changes the direction of the snake so that it faces right if it's
        not current moving along the horizontal axis."""
        if self.head.heading() != 180.0:
            self.head.setheading(0.0)
