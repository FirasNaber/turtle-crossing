import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="w")
screen.onkeypress(fun=player.move, key="W")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        car.speed_up()
        scoreboard.next_level()

    for c in car.cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
