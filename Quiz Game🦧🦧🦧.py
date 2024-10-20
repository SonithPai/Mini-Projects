print("Welcome to my computer quiz!!")

playing = input("Do you want to play my game?? Yes or no??\n").lower()

if playing != "yes":
    print("\nToo scared for my program loser!!!!!!!!!!\n\n\n\n")
    quit()

print("\nOkay! Let's get started :)\n")

topic = input("Now, what would you like your topic to be?\nMath / Science / Computer?\n").lower()





#Math
if topic == "math":
    pointsm = 0  
    print("\n\nExcellent choice!!!")
    print("\nPlease Note: you should use '*' for multiplication and '/' for division.\n")

    # Question 1
    MQ1 = input("Question 1 \nPrime numbers are numbers that are divisible by the number 1 and the number itself. True of False??\n").lower()
    if MQ1 == "true":
        print("Correct answer! You get 1 point!!")
        pointsm += 1  
    else:
        print("Incorrect answer! You get 0 points.")

    # Question 2
    MQ2 = input("\n\nQuestion 2 \nSolve: 7 + 7 + 7 + 7 + 7 - 35 = ?\n")
    if MQ2 == "0":
        print("Correct answer! You get 1 point!!")
        pointsm += 1  
    else:
        print("Incorrect answer! You get 0 points.")

    # Question 3
    MQ3 = input("\n\nQuestion 3 \nThe number 3,124,009 is in the International Number System. Change it into Hindu-Arabic Number System. (Use commas in appropriate places.)\n")
    if MQ3 == "31,24,009":
        print("Correct answer! You get 1 point!!")
        pointsm += 1  
    else:
        print("Incorrect answer! You get 0 points.")

    # Question 4
    MQ4 = input("\n\nQuestion 4 \nWhat does BODMAS stand for?\n").lower()
    if MQ4 == "brackets of division multiplication addition subtraction":
        print("Correct answer! You get 1 point!!")
        pointsm += 1  
    else:
        print("Incorrect answer! You get 0 points.")

    # Question 5
    MQ5 = input("\n\nQuestion 5 \nWhich decimal is larger: 7.543 or 7.54?\n")
    if MQ5 == "7.543":
        print("Correct answer! You get 1 point!!")
        pointsm += 1  
    else:
        print("Incorrect answer! You get 0 points.")

    # Final score
    print(f"\nCongratulations! Your total score is {pointsm}/5.")





#Science
elif topic == "science":
    pointss = 0  
    print("\n\nExcellent choice!!!") 
    print("\nPlease Note: There will be 2 questions from Biology, 2 questions from Physics, and 1 question from Chemistry.\n")

    #Question 1
    SQ1 = input("\n\nQuestion 1 \nThe process by which the embryo in the seed becomes active in the presence of water, air and suitable temperature, and grows into a young plant is called what?\n")
    if SQ1 == "germination":
        print("Correct answer! You get 1 point!!")
        pointss += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 2
    SQ2 = input("\n\nQuestion 2 \nGlucose and Oxygen are the two end products of photosynthesis. True or False?\n")
    if SQ2 == "true":
        print("Correct answer! You get 1 point!!")
        pointss += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 3
    SQ3 = input("\n\nQuestion 3 \nIs the force of friction a contact force or a non-contact force?\n")
    if SQ3 == "contact":
        print("Correct answer! You get 1 point!!")
        pointss += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 4
    SQ4 = input("\n\nQuestion 4 \nDoes force of friction promote motion?\n")
    if SQ4 == "no":
        print("Correct answer! You get 1 point!!")
        pointss += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 5
    SQ5 = input("\n\nQuestion 5 \nThe symbol of Sodium is S. True or False?\n")
    if SQ5 == "false":
        print("Correct answer! You get 1 point!!")
        pointss += 1
    else:
        print("Incorrect answer! You get 0 points.")

    # Final score
    print(f"\nCongratulations! Your total score is {pointss}/5.")





elif topic == "computer":
    pointsc = 0  
    print("\n\nExcellent choice!!!") 

    #Question 1
    CQ1 = input("\n\nQuestion 1 \nA laptop is neither exclusively an input device nor an output device; it is a combination of both. True or False?\n")
    if CQ1 == "true":
        print("Correct answer! You get 1 point!!")
        pointsc += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 2
    CQ2 = input("\n\nQuestion 2 \nWhat is the short form for : Hypertext Markup Language?\n")
    if CQ2 == "html":
        print("Correct answer! You get 1 point!!")
        pointsc += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 3 
    CQ3 = input("\n\nQuestion 3 \nIs Scratch a software or a programming language??\n")
    if CQ3 == "programming language":
        print("Correct answer! You get 1 point!!")
        pointsc += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 4 
    CQ4 = input("\n\nQuestion 4 \nIs Google an AI or a software??\n")
    if CQ4 == "both":
        print("Correct answer! You get 1 point!!")
        pointsc += 1
    else:
        print("Incorrect answer! You get 0 points.")

    #Question 5
    CQ5 = input("\n\nQuestion 5 \nWhat do you use to move the arrow on a computer screen?\n")
    if CQ5 == "mouse":
        print("Correct answer! You get 1 point!!")
        pointsc += 1
    else:
        print("Incorrect answer! You get 0 points.")

    # Final score
    print(f"\nCongratulations! Your total score is {pointsc}/5.")



else:
    print("Sorry, that topic is not available right now.")