from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
    
    
game=True

while game:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        
        food.refresh()
        scoreboard.increment()
        snake.extend()
        
    if snake.head.xcor() >280 or snake.head.ycor() >280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset()
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset_score()
            snake.reset()
            






screen.exitonclick()