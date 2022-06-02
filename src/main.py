from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')

snake_body = []
body_unit_offset = -10
for i in range(3):
    body_unit = Turtle(shape='square', visible=True)
    body_unit.shapesize(stretch_wid=0.5, stretch_len=0.5)
    body_unit.color('white')
    body_unit.penup()
    body_unit.goto(x=i * body_unit_offset, y=0)
    snake_body.append(body_unit)

screen.exitonclick()