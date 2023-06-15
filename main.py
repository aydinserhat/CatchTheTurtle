import turtle
import time
import random
#screen
board = turtle.Screen()
board.bgcolor("Light Blue")
board.title("Catch The Turtle")
turtle.shape("turtle")
turtle.shapesize(2)

def atama(x,y):
    x=random.randint(0,180)
    y=random.randint(0,250)
    turtle.hideturtle()
    turtle.setpos(x,y)
    time.sleep(0.5)
    turtle.hideturtle()
    time.sleep(0.5)
    turtle.showturtle()

turtle.penup()
turtle.hideturtle()
turtle.setpos(random.randint(-250,250),random.randint(-250,250))
time.sleep(0.5)
turtle.hideturtle()
time.sleep(0.5)
turtle.showturtle()

turtle.onclick(atama, btn=1, add=True)

board.mainloop()