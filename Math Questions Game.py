import random

points = 0

n1 = [i for i in range(1,13)]
n2 = n1.copy()

for x in range(0,10):
    r1 = random.choices(n1)[0]
    r2 = random.choices(n2)[0]
    
    ans = r1 * r2
    
    q = int(input(f"{r1}x{r2}=?\n"))
    
    if q == r1*r2:
        points += 0+1
        print(f"\nCorrect answer!! You get 1 point!! You have {points} points!!\n")

    else:
        print(f"\nIncorrect answer!! You have {points} points!!\n")

print(f"Congrats!!! You have {points} points!!")
