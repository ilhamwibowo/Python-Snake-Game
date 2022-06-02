from turtle import Turtle

style = ('Arial', 8, 'normal')
alg = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_text()

    def create_text(self):
        self.color('white')
        self.penup()
        self.goto(0,250)
        self.write("Score : " + str(self.score), font=style, align=alg)
        self.hideturtle()

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=style, align=alg)

    def update_text(self):
        self.clear()
        self.write("Score : " + str(self.score), font=style, align=alg)


    