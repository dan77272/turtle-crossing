from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(-280, 250)
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over", move=False, align="center", font=FONT)
