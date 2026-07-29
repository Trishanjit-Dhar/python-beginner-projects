import random

# MAPPING OF THE CHOICES 
choice = {"Rock":-1,"Paper":0,"Scissor":1}
reversechoice = {-1:"Rock",0:"Paper",1:"Scissor"}

# GETS INPUT FROM USER
youstr = input("Enter your choice: ").capitalize()

if youstr not in choice:
    print("Something went wrong")
else:
    computer = random.choice([-1,0,1])
    you = choice[youstr]

    print(f"Your choice is {youstr}\nComputer's choice is {reversechoice[computer]}")

# IT'S THE LOGIC PART : DECIDING WIN OR LOSE
    if computer == you :
       print("It's a draw")
    else :
        if computer == 1 and you == 0:
            print("You lose")
        elif computer ==1 and you == -1:
            print("You win")
        elif computer == -1 and you == 1:
            print("You lose")
        elif computer == -1 and you == 0:
            print("You win")
        elif computer == 0 and you == -1:
            print("You lose")
        elif computer == 0 and you == 1:
            print("You win")
        
        
