import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car_speed=0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    car_manager.create_car()
    car_manager.moving()
    if player.ycor() > 280:
        player.finish_level()
        scoreboard.score_point()
        car_speed *= 0.7
    for i in car_manager.turts:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_finished()

screen.exitonclick()