name = input("Type your name: ")
print(f"Welcome {name}, to this adventure")

answer = input("You are come to a dirt road, it has come to an end and you can left or right. witch way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river , you can walk around it or swim across? Type walk to walk around or swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by a alligator")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game. ")

    else:
        print("Not a valid option. You loose. ")
elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them(yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they gave you Gold. You win")

        elif answer == "no":
            print("You ignore the stranger, and loose your self in the forest")

    elif answer == "back":
        print("You go back and loose")

    else:
        print("Not a valid option. You loose. ")

