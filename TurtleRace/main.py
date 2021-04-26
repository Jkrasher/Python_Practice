"""
Turtle Race
"""

from turtle import Turtle, Screen
import random

"""
Settings
"""
screen = Screen()
screen.setup(width=500, height=400)
colors= ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["tim", "tommy", "terry", "tonya", "tony", "tyler"]
starting_x = -235

# user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: " )
# print(user_bet)

selection = 0
print(colors[int(selection)])
startying_y = [-125, -75, -25, 50, 100, 150]
finish_line_x = 230
all_turltes = []
user_bet = True

"""
Turtle instances
"""


for turtle_i in range(6):
    new_turtle = Turtle(shape="turtle")
    print(new_turtle)
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.speed(random.randrange(1, 10))
    new_turtle.goto(x=-230, y=startying_y[turtle_i])
    all_turltes.append(new_turtle)
#     print(colors)
#     new_turtle =


bet_question = screen.textinput("Place Your Bet Below", "Who do you think will win?")
print(bet_question)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turltes:
        if turtle.xcor() > finish_line_x:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet_question:
                print(f"You've won! The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!!")



        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# tim.speed("fastest")
# tim.goto(100, 100)


# def move_forwards():
#     tim.fd(5)
#
#
# def move_back():
#     tim.bk(5)
#
# def clear_Home():
#     tim.penup()
#     tim.home()
#     tim.clear()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_back)
#
# screen.onkey(key="c", fun=clear_Home)

screen.exitonclick()


