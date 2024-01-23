from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("deep pink")
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        """spawns food in new random location"""
        x_axis = random.randint(-270, 270)
        y_axis = random.randint(-270, 265)
        self.goto(x_axis, y_axis)


