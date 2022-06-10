from turtle import Turtle
import random

rand_num = random.randint(-10, 10)

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x_move = rand_num
    self.y_move = rand_num

  def move(self):
    new_x = self.xcor() + self.x_move  
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce(self):
    self.y_move *= -1

  def hit(self):
    self.x_move *= -1
    