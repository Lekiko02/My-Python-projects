import random

top_of_range = input("Type a umber: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

guess= random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == guess :
        print("Good Job")
        break
    elif user_guess < guess:
            print("The number that you have to guess is greather ")
    elif user_guess > guess:
        print("The number that you have to guess is smaller ")


print(f"You got it in, {guesses} guesses ")

    


    

