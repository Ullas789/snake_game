from turtle import Turtle,Screen
import time

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
U=90
D=270
R=0
L=180
class Snake:
    def __init__(self) :
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)
            
            
    def add_seg(self,position):
        new_segement=Turtle("square")
        new_segement.penup()
        new_segement.color("white")
        new_segement.goto(position)
        self.segments.append(new_segement)
        
    def extend(self):
        self.add_seg(self.segments[-1].position())
        
            
    def move(self):
        for num in range(len(self.segments)-1,0,-1):
            x=self.segments[num-1].xcor()
            y=self.segments[num-1].ycor()
            self.segments[num].goto(x,y)
        self.head.forward(MOVE_FORWARD)
    
    def up(self):
        if self.head.heading()!=D:
            self.head.setheading(U)
            
        
    def down(self):
        if self.head.heading()!=U:
            self.head.setheading(D)
    
    def right(self):
        if self.head.heading()!=L:
            self.head.setheading(R)
        
        
    def left(self):
        if self.head.heading()!=R:
            self.head.setheading(L)
        
        
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    
    
