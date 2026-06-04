from turtle import Turtle, Screen
import time
from player import Player
from car_manager import Carmanager
from scoreboard import Scoreboard


screen = Screen()

screen.setup(600, 600)
screen.tracer(0)

player = Player()
carmanager = Carmanager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()
    
    #detection of collision

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
            
    #Detection successful crossing
    if player.finish():
        player.restart()
        carmanager.level_up()
        scoreboard.increase_level()

screen.exitonclick()