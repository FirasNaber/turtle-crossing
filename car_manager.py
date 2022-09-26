from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.cars = []
        self.current_moving_distance = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            starting_position = (300, randint(-260, 260))
            new_car.setposition(starting_position)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.current_moving_distance)

    def speed_up(self):
        self.current_moving_distance += MOVE_INCREMENT
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.current_moving_distance)
