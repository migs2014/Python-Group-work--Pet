class pet:
    def __init__(self,name):
        self.name=name
        self.hunger = 5   # default value for hunger
        self.energy = 5  # default value for energy
        self.hapiness = 5  # default value for hapiness

    def eat(self):
        self.hunger = max (0, self.hunger - 3)  # Decrease hunger by 3, but not below 0
        self.happiness = min (10, self.hapiness + 1)  # Increase happiness by 1, but not above 10
        print(f"{self.name} has eaten.")
    def sleep(self):
        self.energy = min (10, self.energy + 5) # Increase energy by 45, but not above 10
        print(f"{self.name} is sleeping.")
    def play(self):
        if self.energy >= 2:  # Check if there is enough energy to play
            self.energy -= 2  # Decrease energy by 2
            self.happiness = min (10, self.hapiness + 2)  # Increase happiness by 3, but not above 10
            self.hunger = min (10, self.hunger + 1)
            print(f"{self.name} is playing.")
        else:
            print(f"{self.name} is too tired to play.")
    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.hapiness}/10")