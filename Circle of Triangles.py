import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")

choose = ["yellow","red","blue","green","orange","magenta","purple",]


star = turtle.Pen()
star.speed(10)

n = input("How many times???\n")
n = int(n)

for times in range(0,n):
    r = random.choices(choose)
    star.color(r)
    star.begin_fill()
    
    for x in range (0,10):
        star.right(126)
        star.forward(200)
        star.left(360-126)
        star.forward(200)


    star.end_fill()
    star.hideturtle()
    time.sleep(2)
    star.clear()


star.hideturtle()

screen.mainloop()