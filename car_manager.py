COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.speed_increase_counter = 1
        self.spawn_rate = 1
        self.hideturtle()
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance <= self.spawn_rate:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-240, 240))
            self.all_cars.append(new_car)

    def new_stage(self):
        self.car_speed += MOVE_INCREMENT
        self.speed_increase_counter += 1
        if self.speed_increase_counter % 2 == 0:
            self.spawn_rate += 1
