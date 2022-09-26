from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.setposition(x=-280, y=260)
        self.color("black")
        self.next_level()

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=FONT)
