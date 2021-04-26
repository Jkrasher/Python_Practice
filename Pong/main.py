import turtle
from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
STARTING_RT_X = 350
STARTING_RT_Y = 0
STARTING_LT_X = -350
STARTING_LT_Y = 0


screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
STARTING_RT_POSITION = (STARTING_RT_X, STARTING_RT_Y)
STARTING_LT_POSITION = (STARTING_LT_X, STARTING_LT_Y)
RANDOM_PADDLE_POS = (random.randint(-780, 780+1), random.randint(-780, 780+1) )

scoreboard = Scoreboard()
SCORE_RT = 0
SCORE_LT = 0

rt_paddle = Paddle(STARTING_RT_POSITION)
lt_paddle = Paddle(STARTING_LT_POSITION)
# random_paddle = Paddle(RANDOM_PADDLE_POS)
pong_ball = Ball()

screen.listen()
screen.onkey(rt_paddle.go_up, "Up")
screen.onkey(rt_paddle.go_down, "Down")
screen.onkey(lt_paddle.go_up, "w")
screen.onkey(lt_paddle.go_down, "s")
# SCREEN.onkey(random_paddle.go_up, "y")
# SCREEN.onkey(random_paddle.go_down, "h")

# ball_screen = Screen()
# ball_screen.tracer(10)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.move()


    #Detect collision with top and bott walls
    #Detect collision with paddle
    if pong_ball.ycor() > 285 or pong_ball.ycor() < -285:
        pong_ball.bounce()
    # if pong_ball.xcor() >= ((rt_paddle.xcor() - 10)) or pong_ball.xcor() == (lt_paddle.xcor() + 10):
    #     pong_ball.paddle_hit()

    # detect collisison with paddles
    if (pong_ball.distance(rt_paddle) < 50 and pong_ball.xcor() > 320) \
            or (pong_ball.distance(lt_paddle) < 50 and pong_ball.xcor() < -320):
        print(pong_ball.distance(rt_paddle))
        print("collision with rt paddle...")
        pong_ball.paddle_hit()

    # Detect the ball going out of bounds
    STARTING_RT_X = STARTING_RT_X
    STARTING_LT_X = STARTING_LT_X
    print((pong_ball.position()[0]))
    if (pong_ball.position()[0] > (STARTING_RT_X) + 30):
        scoreboard.l_point()
        print("Ball out of RIGHT bounds...<<>>")
        pong_ball.ball_reset()

    if (pong_ball.position()[0] < (STARTING_LT_X - 30)):
        scoreboard.r_point()
        print("Ball out of LEFT bounds...<<>>")
        pong_ball.ball_reset()

    print(f'SCORE_RT: {scoreboard.r_score}\n')
    print(f'SCORE_LT: {scoreboard.l_score}\n')




screen.exitonclick()
# raise turtle.Terminator