import turtle
import time
import random
#screen
board = turtle.Screen()
board.bgcolor("Light Blue")
board.title("Catch The Turtle")
turtle.shape("turtle")
turtle.shapesize(2)
score = turtle.Turtle()
sayı=0
def count():
    score.hideturtle()
    score.penup()
    score.setposition(0,300)
    score.write(sayı, move=False, align='center',font=('Arial',13,'normal'))


def atama(x,y):

    x=random.randint(-250,300)
    y=random.randint(-250,250)
    turtle.hideturtle()
    turtle.setpos(x,y)
    time.sleep(0.5)
    turtle.hideturtle()
    time.sleep(0.5)
    turtle.showturtle()
    global sayı
    sayı +=1
    score.clear()
    count()


turtle.penup()
turtle.hideturtle()
turtle.setpos(random.randint(-250,250),random.randint(-250,250))
time.sleep(0.5)
turtle.hideturtle()
time.sleep(0.5)
turtle.showturtle()

turtle.onclick(atama, btn=1, add=False)

board.mainloop()