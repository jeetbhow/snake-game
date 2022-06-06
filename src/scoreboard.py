from turtle import Turtle


class Scoreboard(Turtle):
    """Models a scoreboard that keeps track of how many pieces of fruit have been
    consumed by the snake."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.render()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.goto(0, 280)
        self.render()

    def render(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("SF Mono", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("SF Mono", 12, "normal"))

    def update(self) -> None:
        """Increments the score by 1."""
        self.score += 1
        self.render()

