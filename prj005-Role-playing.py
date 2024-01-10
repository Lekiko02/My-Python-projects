import random

ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

while True:
    # Player's turn
    if SKIP_TURN:
        print("You skip your turn...")
        SKIP_TURN = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Do you want to attack (1) or use a potion (2)? ")

        if user_choice == "1":  # Attack
            your_attack = random.randint(5, 10)
            ENEMY_HEALTH -= your_attack
            print(f"You dealt {your_attack} points of damage to the enemy ⚔️")
        elif user_choice == "2" and NUMBER_OF_POTIONS > 0:  # Potion
            potion_health = random.randint(15, 50)
            PLAYER_HEALTH += potion_health
            NUMBER_OF_POTIONS -= 1
            SKIP_TURN = True
            print(f"You recover {potion_health} health ❤️ ({NUMBER_OF_POTIONS} left)")
        else:
            print("You have no more potions...")
            continue

    if ENEMY_HEALTH <= 0:
        print("You won!")
        break

    # Enemy's attack
    enemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= enemy_attack
    print(f"The enemy dealt {enemy_attack} points of damage ⚔️")

    if PLAYER_HEALTH <= 0:
        print("You lost!")
        break

    # Stats
    print(f"You have {PLAYER_HEALTH} health points remaining.")
    print(f"The enemy has {ENEMY_HEALTH} health points remaining.")
    print("-" * 50)

print("Game over.")
