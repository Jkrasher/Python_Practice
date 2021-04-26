
from turtle import Turtle, Screen

STARTING_POSITIONS = starting_pos = [(0, 0), (-20, 0), (-40, 0)]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_NUMBER = 3
MOVE_DISTANCE = 20
HEADING = [0,90,180, 270]
UP = HEADING[1]
DOWN = HEADING[3]
LEFT = HEADING[2]
RIGHT = HEADING[0]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_section = Turtle(shape="square")
        new_section.penup()
        #print(new_section)
        for color in range(STARTING_NUMBER + 1):
            new_section.color(COLORS[color])
            #print(new_section.fillcolor())
        new_section.goto(position)
        self.segments.append(new_section)


    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

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
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



