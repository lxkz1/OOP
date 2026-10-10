import random


class Characters:

    characters_created = 0

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack
        Characters.characters_created += 1

    def attacks(self, target):
        target.take_damage(self.attack_power)

    def take_damage(self, amount):
        if amount < self.health:
            self.health -= amount
        else:
            self.health = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def describe(self):
        if self.is_alive():
            print(f"{self.name} has {self.health}hp")
        else:
            print(f"{self.name} is dead")


class Warrior(Characters):
    shield = 5

    def take_damage(self, amount):
        if self.shield > 0:
            reduced = amount - self.shield
            super().take_damage(reduced)
        else:
            super().take_damage(amount)


class Mage(Characters):

    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.mana = 100

    def attacks(self, target):
        if self.mana >= 30:
            self.mana -=30
            damage = self.attack_power * 3
            target.take_damage(damage)
        else:
            super().attacks(target)

class Archer(Characters):

    def critical_chance(self):
        randomnumber = random.randint(1, 100)
        if randomnumber < 75:
            return "Pass"
        return "Fail"

    def attacks(self, target):
        if self.critical_chance() == "Pass":
            target.take_damage(self.attack_power*2)
        else:
            super().attacks(target)

def main():
    characters = []
    for i in range(1,3):
        character_type = type_of_character()
        charname = input(f"please input your {character_type} number {i}'s name: ")
        charhealth = int(input(f"please input your {character_type} number {i}'s health: "))
        charattack = int(input(f"please input your {character_type} attack {i}'s power: "))
        if character_type == "archer":
            char = Archer(charname,charhealth,charattack)
        elif character_type == "mage":
            char = Mage(charname,charhealth,charattack)
        elif character_type == "warrior":
            char = Warrior(charname,charhealth,charattack)
        else:
            char = Characters(charname,charhealth,charattack)
        characters.append(char)
    char1 , char2 = characters
    battle(char1,char2)
        
        



def type_of_character():
    characters = ["normal","warrior","archer","mage"]
    print("Please choose a character between ( normal , warrior , archer , mage)")
    while True:
        userschoice = input("Your character choise: ").strip().lower()
        if userschoice in characters:
            return userschoice
        else:
            print("Please Choose between the available characters")
            continue 


def battle(char1 : Characters, char2: Characters):
    while char1.is_alive() and char2.is_alive():
        char1.attacks(char2)
        if char2.is_alive():
            char2.attacks(char1)
        else:
            break
    if char1.is_alive():
        print(f"{char1.name} has eliminated {char2.name}")
    else:
        print(f"{char2.name} has eliminated {char1.name}")
    


if __name__ == "__main__":
    main()