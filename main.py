import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
car = CarManager()
for _ in range(300):
    car = CarManager()
    cars.append(car)

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkeypress(fun=player.move, key="Up")
    for car in cars:
        random.choice(cars).move()

    if player.ycor() == 280:
        player.goto(0, -280)
        for car in cars:
            car.reset_position()
        for car in cars:
            car.increase_speed()
        scoreboard.update_score()
    for car in cars:
        if player.distance(car.xcor(), car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
