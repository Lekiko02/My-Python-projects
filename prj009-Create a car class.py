class Car:
    def __init__(self):
        self.gasoline = 100

    def display_tank(self):
        print(f"The car has {self.gasoline}L of gasoline in the tank.")

    def drive(self, km):
        if self.gasoline <= 0:
            print("You're out of gas, fill up the tank!")
            return

        self.gasoline -= (km * 5) / 100

        if self.gasoline < 10:
            print("You're running low on gas!")

        self.display_tank()

    def refuel(self):
        self.gasoline = 100
        print("You're ready to go!")
