import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.next_level()

    for c in car.cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
