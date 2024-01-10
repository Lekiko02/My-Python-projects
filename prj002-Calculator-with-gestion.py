# Declare two variables
a = b = ""

# While a and b are not numbers, loop
while not (a.isdigit() and b.isdigit()):

    # Ask the user for two numbers
    a = input("Enter a first number: ")
    b = input("Enter a second number: ")

    # Display a message if the entered numbers are not valid
    if not (a.isdigit() and b.isdigit()):
        print("Please enter two valid numbers")

# Display the result of the addition
print(f"The result of adding {a} and {b} is equal to {int(a) + int(b)}")
