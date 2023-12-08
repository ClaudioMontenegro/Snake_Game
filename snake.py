import time
from turtle import Turtle
X = -20
Y = 0
START_POSITION = [(0, Y), (X, Y), (X*2, Y)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.snake_maker()
        self.head = self.snakes[0]

    def snake_maker(self):
        for position in START_POSITION:
            self.snake_increase(position)

    def snake_increase(self, position):
        self.snake = Turtle("circle")
        self.snake.color("white")
        self.snake.shapesize(1)
        self.snake.penup()
        self.snake.goto(position)
        self.snakes.append(self.snake)

    def snake_extend(self):
        self.snake_increase(self.snakes[-1].position())
    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

