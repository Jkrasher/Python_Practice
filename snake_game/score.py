
from turtle import Turtle
from snake import Snake

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
GAME_OVER_FONT = ("Courier", 22 , "underline")
text_move = False

class Score(Turtle):
    def __init__(self):

        super().__init__()
        self.score_value = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score_value}", move=text_move, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=text_move, align=ALIGNMENT, font=GAME_OVER_FONT)

    # def start(self):
    #     snake= Snake()
    #     snake.move()

    def start_over(self):
        self.write("To Start Over, Press << SPACEBAR >>", move=text_move, align=ALIGNMENT, font=GAME_OVER_FONT)


    def refresh_score(self):
        self.clear()
        self.score_value += 10
        self.update_score()
