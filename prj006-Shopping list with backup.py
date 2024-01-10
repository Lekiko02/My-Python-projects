import os
import sys
import json

CUR_DIR = os.path.dirname(__file__)
LIST_PATH = os.path.join(CUR_DIR, "list.json")

MENU = """Choose from the following 5 options:
1: Add an item to the list
2: Remove an item from the list
3: Display the list
4: Clear the list
5: Save and Quit
? Your choice: """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

if os.path.exists(LIST_PATH):
    with open(LIST_PATH, "r") as f:
        LIST = json.load(f)
else:
    LIST = []

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Please choose a valid option...")

    if user_choice == "1":  # Add an item
        item = input("Enter the name of an item to add to the shopping list: ")
        LIST.append(item)
        print(f"The item {item} has been successfully added to the list.")
    elif user_choice == "2":  # Remove an item
        item = input("Enter the name of an item to remove from the shopping list: ")
        if item in LIST:
            LIST.remove(item)
            print(f"The item {item} has been successfully removed from the list.")
        else:
            print(f"The item {item} is not in the list.")
    elif user_choice == "3":  # Display the list
        if LIST:
            print("Here is the content of your list:")
            for i, item in enumerate(LIST, 1):
                print(f"{i}. {item}")
        else:
            print("Your list does not contain any items.")
    elif user_choice == "4":  # Clear the list
        LIST.clear()
        print("The list has been cleared of its content.")
    elif user_choice == "5":  # Save and Quit
        with open(LIST_PATH, "w") as f:
            json.dump(LIST, f, indent=4)
        print("Goodbye!")
        sys.exit()

    print("-" * 50)
