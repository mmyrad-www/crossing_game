COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle
new_x=300



class CarManager():
    def __init__(self):
        self.turts=[]

    def create_car(self):
        random_chance=random.randint(0,5)
        if random_chance==2:
            car=Turtle("square")
            car.color(COLORS[random.randint(0, 5)])
            car.penup()
            car.shapesize(1, 2)
            random_y = random.randint(-40, 50) * 5
            car.goto(new_x,random_y)
            self.turts.append(car)

    def moving(self):
        for i in self.turts:
            i.backward(STARTING_MOVE_DISTANCE)


