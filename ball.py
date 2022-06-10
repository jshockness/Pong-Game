from turtle import Turtle
import random

rand_num = random.randint(-10, 10)

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.goto(0, 0)

  def move(self):
    new_x = self.xcor() + rand_num  
    new_y = self.ycor() + rand_num
    self.goto(new_x, new_y)