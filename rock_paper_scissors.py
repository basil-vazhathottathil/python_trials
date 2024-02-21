import random

set=["🪨","📄","✂️"]
user_choice=int(input("What is ur choice?\nrock is 0,\npaper is 1,\nscissors is 2\n"))
comp_choice=random.randint(0,2)

if(user_choice<3):
    print("you chose" + set[user_choice])
    print("computer chose" + set[comp_choice])
    if (user_choice== comp_choice):
        print("DRAW")
    elif(user_choice<comp_choice):
        if(user_choice==0 and comp_choice==2):
            print("You win")
        else:
            print("You lose")
    else:
        print("You lose")
else:
    print("invalid choice")