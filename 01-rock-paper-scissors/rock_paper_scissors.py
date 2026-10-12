import random

# MAPPING OF THE CHOICES 
choice = {"Rock":-1,"Paper":0,"Scissor":1}
reverse_choice = {-1:"Rock",0:"Paper",1:"Scissor"}

# GETS INPUT FROM USER
you_str = input("Enter your choice: ").capitalize()

if you_str not in choice:
    print("Something went wrong")
else:
    computer = random.choice([-1,0,1])
    you = choice[you_str]

    print(f"Your choice is {you_str}\nComputer's choice is {reverse_choice[computer]}")

# IT'S THE LOGIC PART : DECIDING WIN OR LOSE
    if computer == you :
       print("It's a draw")
    else :
        if computer == 1 and you == 0:
            print("You lost the game")
        elif computer ==1 and you == -1:
            print("You win the game")
        elif computer == -1 and you == 1:
            print("You lost the game")
        elif computer == -1 and you == 0:
            print("You win the game")
        elif computer == 0 and you == -1:
            print("You lost the game")
        elif computer == 0 and you == 1:
            print("You win the game")
        
        
