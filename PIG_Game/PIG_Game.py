import random



def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("How many player Will participate (2-4)? ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            
            break
        else:
            print("Must be between (2-4): ")

    else:
        print("Invalid, print a valid number")

print(players)

max_scores = 50 
players_scores =[0 for _ in range(players)]

while max(players_scores) < max_scores :
    for i in range(players):
        print(f"Player {i + 1} turn has just started!\n")
        print(f"Your total score is {players_scores[i]}\n")

        current_score = 0

        while True:

            should_roll = input("Would like to roll(y or n? ")
            if should_roll.lower() != "y":
                break
                
            value = roll()
            if value == 1:
                print("Your rolled a 1 ,score back to zero")
                current_score = 0
                break

            else:
                current_score += value
                print(f"You rolled {value}")

            print(f"Your score is {current_score}")

        players_scores[i] += current_score
        print(f"Your total score is {players_scores[i]}")

max_scores = max(players_scores)
winning_i = players_scores.index(max_scores)
print(f"Player {winning_i + 1} have won with a score of {max_scores}")
            