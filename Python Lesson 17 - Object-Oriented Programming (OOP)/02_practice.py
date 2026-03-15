# Create Game Character System

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attacks with power {self.attack_power}")

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")

# Warrior Class
class Warrior(Character):
    def special_attack(self):
        print(f"{self.name} uses SWORD SLASH ⚔️")


# Mage Class
class Mage(Character):
    def special_attack(self):
        print(f"{self.name} casts FIREBALL 🔥")


# Archer Class
class Archer(Character):
    def special_attack(self):
        print(f"{self.name} shoots ARROW 🏹")


# Creating Objects
warrior = Warrior("Thor", 150, 25)
mage = Mage("Merlin", 100, 30)
archer = Archer("Robin", 120, 20)


# Testing
warrior.show_status()
warrior.attack()
warrior.special_attack()

print("-----------")

mage.show_status()
mage.attack()
mage.special_attack()

print("-----------")

archer.show_status()
archer.attack()
archer.special_attack()


