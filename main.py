import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Capstone Game")
player = Player()
screen.listen()
screen.onkey(player.move, "space")

car_menager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_menager.create_car()
    car_menager.move_cars()

    for car in car_menager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        player.go_to_start()
        car_menager.level_up()
        scoreboard.increase_score()


screen.exitonclick()