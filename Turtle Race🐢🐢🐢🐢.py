import turtle

def welcome_message():
    print("\n\nHello, and welcome to my game!!!")
    print("This game is about you answering questions to move the pen forward!!!")
    print("You can check how far you've reached by going to the window \"Python Turtle Graphics\" :)")
    print("\nLet's Get Started  :)\n")

def start_game():
    playing = input("Now to actually play this game... I need you to type \"Turtle\" (with the capital \"T\").\n")
    if playing != "Turtle":
        print("\nToo scared for my program, loser!!!!!!!!!!\n")
        return False
    return True

def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("light blue")
    
    t = turtle.Pen()
    t.up()
    t.left(180)
    t.forward(700)
    t.left(180)
    t.down()
    t.color("black")

    end = turtle.Pen()
    end.up()
    end.forward(700)
    end.down()
    end.begin_fill()
    
    for x in range (0,4):
        end.forward(10)
        end.left(90)

    end.end_fill()
    end.hideturtle()
    
    return t

def ask_question(t):
    points = 0
    
    
    # Question 1
    Q1 = input("\n\nQuestion \nWhat covers a turtle's body?\n")
    if Q1 == "shell":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")
    
    
    
    # Question 2
    Q2 = input("\n\nQuestion 2 \nWhat type of blood do turtles have? Cold-blooded or Warm-blooded??(Write \"blooded\" and not\"blood\")\n")
    if Q2 == "cold-blooded":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 3 
    Q3 = input("\n\nQuestion 3 \nAre turtles omnivores??\n")
    if Q3 == "yes":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 4
    Q4 = input("\n\nQuestion 4 \nAre turtles reptiles or amphibians?\n")
    if Q4 == "reptiles":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 5 
    Q5 = input("\n\nQuestion 5 \nWhat season do most turtles lay eggs?\n")
    if Q5 == "summer":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 6
    Q6 = input("\n\nQuestion 6 \nWhere do sea turtles lay their eggs?\n")
    if Q6 == "beach":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 7
    Q7 = input("\n\nQuestion 7 \nCan turtles swim?\n")
    if Q7 == "yes":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 8
    Q8 = input("\n\nQuestion 8 \nDo turtles have teeth?\n")
    if Q8 == "no":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 9
    Q9 = input("\n\nQuestion 9 \nHow many species of turtles are there?\n")
    if Q9 == "356":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

   
   
    # Question 10
    Q10 = input("\n\nQuestion 10 \nWith what do turtles protect themselves?\n")
    if Q10 == "shell":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 11
    Q11 = input("\n\nQuestion 11 \nWhat is the largest species of turtle?\n")
    if Q11 == "leatherback":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 12
    Q12 = input("\n\nQuestion 12 \nWhat do turtles use to swim?\n")
    if Q12 == "flippers":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 13
    Q13 = input("\n\nQuestion 13 \nWhat do turtles do in cold weather?\n")
    if Q13 == "hibernate":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    
    
    # Question 14
    Q14 = input("\n\nQuestion 14 \nWhat sense is strongest in turtles?\n")
    if Q14 == "smell":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")
    


    # Question 15
    Q15 = input("\n\nQuestion 15 \nDo turtles have ears?\n")
    if Q15 == "yes":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")

    

    # Question 16
    Q16 = input("\n\nQuestion 16 \nWhat color are most turtle shells?\n")
    if Q16 == "brown":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 17
    Q17 = input("\n\nQuestion 17 \nWhat is the primary threat to sea turtles?\n")
    if Q17 == "pollution":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 18
    Q18 = input("\n\nQuestion 18 \nWhat body part allows turtles to retract their head to?\n")
    if Q18 == "neck":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 19
    Q19 = input("\n\nQuestion 19 \nWhat do tortoises eat?\n")
    if Q19 == "plants":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 20
    Q20 = input("\n\nQuestion 20 \nWhat are baby turtles called?\n")
    if Q20 == "hatchlings":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 21
    Q21 = input("\n\nQuestion 21 \nWhat do baby turtles do after hatching?\n")
    if Q21 == "crawl":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 22
    Q22 = input("\n\nQuestion 22 \nWhat is the top part of a turtle's shell called?\n")
    if Q22 == "carapace":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 23
    Q23 = input("\n\nQuestion 23 \nWhat is the bottom part of a turtle's shell called?\n")
    if Q23 == "plastron":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 24
    Q24 = input("\n\nQuestion 24 \nHow do turtles navigate during migration?\n")
    if Q24 == "magnetism":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 25
    Q25 = input("\n\nQuestion 25 \nWhat is the lifespan of a turtle?\n")
    if Q25 == "100 years":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 26 
    Q26 = input("\n\nQuestion 26 \nCan turtles see in color?\n")
    if Q26 == "yes":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 27
    Q27 = input("\n\nQuestion 27 \nWhat time of day do sea turtles usually hatch?\n")
    if Q27 == "night":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")



    # Question 28
    Q28 = input("\n\nQuestion 28 \nDo turtles have a backbone?\n")
    if Q28 == "yes":
        print("\nCorrect Answer. You are rewarded with 1 point.")
        points += 1
        t.forward(50)
    else:
        print("\nIncorrect Answer!!")
    
    




    # Final score
    print(f"\nCongratulations! Your total score is {points}/28.")
    return points

    if points == 28:
        print("\n\nDamn bro!!! You might be the only person to get full points!!😮👊\n\n")

    elif points >= 19:
        print("\n\nSo close!! Try Again!!!\n\n")

    elif points >= 10:
        print("\n\nVery Good!! This Quiz was hard, don't worry!!\n\n")

    elif points >=0:
        print("\n\nLooks like it was very hard, eh??\n\n")



welcome_message()

if start_game():
    t = setup_turtle()
    points = ask_question(t)
    
turtle.done()
