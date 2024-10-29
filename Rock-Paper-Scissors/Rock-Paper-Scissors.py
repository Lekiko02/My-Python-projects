import random

user_points = 0
computer_points = 0
options = ["rock","paper","scissors"]
while True:
    user_choices = input("Choose between:Rock,Paper,Scissors or Q to quit the game :) ").lower()
    if user_choices == "q":
        break

    if user_choices  not in options:
        
        continue

    comp_choices = random.choice(options)
    print(f"Computer choose ,{comp_choices}.")

    if user_choices == "Rock" and comp_choices == "Paper":
        print("You won!")
        user_points += 1
    elif user_choices == "Scissors" and comp_choices == "Paper":
        user_points += 1
    elif user_choices == "rock" and comp_choices == "scissors":
        user_points += 1

    elif user_choices == comp_choices:
        user_points += 0 
        print("Nobody want to loose ahah ;)")

    else:
        print("You lost!")
        computer_points += 1

print(f"You Won {user_points} times against computer")
print(f"Computer Won {computer_points} times against You")


    