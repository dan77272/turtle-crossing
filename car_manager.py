from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.left(180)
        self.setposition(random.randrange(320, 10000, 50), random.randrange(-280, 280, 30))
        self.playerspeed = 5

    def move(self):
        self.forward(self.playerspeed)

    def reset_position(self):
        self.setposition(random.randrange(320, 10000, 50), random.randrange(-280, 280, 30))

    def increase_speed(self):
        self.playerspeed += 10
        self.forward(self.playerspeed)
