from turtle import Turtle

FONT = "Times New Roman"
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
         self.high_score = int(data.read())
        self.up()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Scoreboard: {self.score}  High Score: {self.high_score}", align=ALIGN, font=(FONT, 24, "bold"))

    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
   
        
        
        
        
