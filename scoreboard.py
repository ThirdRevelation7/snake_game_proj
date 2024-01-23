from turtle import Turtle

FONT = "courier"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.goto(0, 270)
        self.color("lime")
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(arg=f"Scoreboard: {self.score}", align="center", font=(FONT, 30, "bold"))

    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(arg="Game Over", align="center", font=("Magneto", 30, "bold"))
        self.goto(0, -25)
        self.write(arg="Click screen to exit", align="center", font=("Gothic", 20))
        
        
        
        
