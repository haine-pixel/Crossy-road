import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move,"Up")
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if  car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        player.reset()
        car_manager.new_stage()
        scoreboard.update_scoreboard()

screen.exitonclick()
