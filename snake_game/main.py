
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# colors= ["red", "orange", "yellow", "green", "blue", "purple"]
# starting_pos = [(0, 0), (-20, 0), (-40, 0)]
# starting_number = 3
# snake_body = []
#
# segments = []
#
# for position in starting_pos:
#     new_section = Turtle(shape="square")
#     new_section.penup()
#     print(new_section)
#     for color in range(starting_number+1):
#         new_section.color(colors[color])
#         print(new_section.fillcolor())
#     new_section.goto(position)
#     segments.append(new_section)


"""
Using the screen tracer method in turtle docs, we will move the snake with a while loop -
"""

snake = Snake()
food = Food()
score = Score()


# score.start_over(self)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #score.write()
    # Detect Movements.
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Detect Collision with Food.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        score.refresh_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


    # if head collides with any segment of the tail:
        #traigger game over








    # for seg in segments:
    #     seg.fd(20)






    # snake_head_x = new_section.xcor()
    # snake_head_y = new_section.ycor()
    # section_counter = 0
    #
    #
    # new_section.penup()
    # print(snake_head_x)
    # print(snake_head_y)
    #
    # if turtle > 0 and section_counter < 2:
    #     section2 = new_section.goto(x=(snake_head_x-20), y=(snake_head_y))
    #     section_counter += 1
    #     print(new_section.pos())
    # elif turtle > 1 and section_counter > 1:
    #     section_counter += 1
    #     section3 = new_section.goto(x=(snake_head_x-(turtle*section_counter)), y=(snake_head_y))
    #     print(new_section.pos())



screen.exitonclick()