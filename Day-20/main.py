from turtle import Turtle, Screen
import time
from snake import Snake, play

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()

play(snake)

screen.exitonclick()