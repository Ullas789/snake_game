from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",15,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        #which saves the high score in your data file
        with open("snake_game/data.txt") as data:
            self.high_score=int(data.read())
            
        
        self.hideturtle()
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High score :{self.high_score}",align=ALIGNMENT,font=FONT)
        
   
    def reset_score(self):
        if self.high_score < self.score:
            self.high_score=self.score
            with open("snake_game/data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()
        
    def increment(self):
        self.score+=1
        self.update()
    
    
        
        
        
        
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)
        
