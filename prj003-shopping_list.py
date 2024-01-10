import sys

LIST = []

MENU = """Choose from the following 5 options:
1: Add an item to the list
2: Remove an item from the list
3: Display the list
4: Clear the list
5: Quit
? Your choice: """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Please choose a valid option...")
        continue

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
    elif user_choice == "5":  # Quit
        print("Goodbye!")
        sys.exit()

    print("-" * 50)
