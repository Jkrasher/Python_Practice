
import colorgram
import turtle as t
from turtle import Screen
import random


print(dir(colorgram))


colors = colorgram.extract("/Users/joniman/Desktop/100DaysofCode/Hirst-Painting/image3.jpg", 30)

rgb_colors = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    # rgb_colors.append(color.rgb)

print(rgb_colors)

pencolors = ["red", "violet", "blue", "grey", "black", "orange",
             "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
             "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
print(tim.position())
tim.goto(-400,-400)
dot_count = 15
row = -400
col = -400

for step in range(1, (dot_count ** 2) + 1):
    # tim.color(random.choice(rgb_colors)
    tim.dot(20, (random.choice(pencolors)))
    tim.fd(50)

    if step % dot_count == 0:
        col += 50
        tim.goto(row, col)




screen = Screen()

screen.exitonclick()
