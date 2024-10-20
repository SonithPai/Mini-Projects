import random

choices = ["square","circle","rectangle","triangle"]

r = random.choice(choices)

import turtle

if r == "square":
    t=turtle.Pen()
    t.color("blue")
    t.begin_fill()
    
    for x in range (0,4):
        t.forward(200)
        t.left(90)
    
    t.end_fill()
    t.hideturtle()
    
    for y in range (0,50):
        t.up()
        t.down()

    turtle.bye()

    shape1 = input("Guess the shape that was just drawn!!!!\n")
    if shape1 != "square":
        print("\n\n\nHa Ha!!!!! You loser doesn't even know shapes!!!! Try Again  :)!!!!!!!!!!!!!!!\n\n\n")

    else:
        print("\n\n\nGood Job!! You're not like the losers who don't know shapes!!!\n\n\n")

elif r == "circle":
    c = turtle.Pen()
    c.color("red")
    c.begin_fill()
    c.circle(100)
    c.end_fill()
    c.hideturtle()

    for x in range (0,50):
        c.up()
        c.down()

    turtle.bye()

    shape2 = input("Guess the shape that was just drawn!!!!\n")
    if shape2 != "circle":
        print("\n\n\nHa Ha!!!!! You loser doesn't even know shapes!!!! Try Again  :)!!!!!!!!!!!!!!!\n\n\n")

    else:
        print("\n\n\nGood Job!! You're not like the losers who don't know shapes!!!\n\n\n")

elif r == "rectangle":
    r = turtle.Pen()
    r.color("green")
    r.begin_fill()

    for y in range (0,2):
        r.forward(200)
        r.left(90)
        r.forward(50)
        r.left(90)

    r.end_fill()
    r.hideturtle()

    for x in range(0,50):
        r.up()
        r.down()

    turtle.bye()

    shape3 = input("Guess the shape that was just drawn!!!!\n")
    if shape3 != "rectangle":
        print("\n\n\nHa Ha!!!!! You loser doesn't even know shapes!!!! Try Again  :)!!!!!!!!!!!!!!!\n\n\n")
   
    else:
        print("\n\n\nGood Job!! You're not like the losers who don't know shapes!!!\n\n\n")

elif r == "triangle":
    a = turtle.Pen()
    a.color("yellow")
    a.begin_fill()
    
    for x in range (0,3):
        a.forward(200)
        a.left(120)

    a.end_fill()
    a.hideturtle()

    for y in range (0,50):
        a.up()
        a.down()

    turtle.bye()

    shape4 = input("Guess the shape that was just drawn!!!!\n")
    if shape4 != "triangle":
        print("\n\n\nHa Ha!!!!! You loser doesn't even know shapes!!!! Try Again  :)!!!!!!!!!!!!!!!\n\n\n")
   
    else:
        print("\n\n\nGood Job!! You're not like the losers who don't know shapes!!!\n\n\n")

else:
    print("Booooooooooooooooooooooooooooooooooooooooooooyah!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    