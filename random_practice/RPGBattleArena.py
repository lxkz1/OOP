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
            return "The Character has been killed"

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
        reduced = self.health - (max(0, amount - self.shield))
        super().take_damage(reduced)


class Mage(Characters):

    mana = 100

    def fireball(self):
        if self.mana > 50:
            return "Pass"
        else:
            return "False"

    def take_damage(self, amount):
        if self.fireball() == "Pass":
            amount = 0
            if amount < self.health:
                self.health -= amount
            else:
                return "The Character has been killed"
        else:
            if amount < self.health:
                self.health -= amount
            else:
                return "The Character has been killed"


class Archer(Characters):

    def critical_chance(self):
        randomnumber = random.randint(1, 100)
        if randomnumber < 75:
            return "Pass"
        return "Fail"

    def attacks(self, target):
        if self.critical_chance() == "Pass":
            target_health = target.health() - (self.attack_power * 2)
            return target_health
        else:
            target_health = target.health() - self.attack_power
            return target_health

def main():
    characters = []
    for i in range(1,3):
        character_type = type_of_character()
        charname = input(f"please input your {character_type} number {i}'s name: ")
        charhealth = input(f"please input your {character_type} number {i}'s health: ")
        charattack = input(f"please input your {character_type} attack {i}'s power: ")
        if type_of_character == "archer":
            char = Archer(charname,charhealth,charattack)
        elif type_of_character == "mage":
            char = Mage(charname,charhealth,charattack)
        elif type_of_character == "warrior":
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


def battle(char1, char2):
    while True:
        char1.attacks(char2)



if __name__ == "__main__":
    main()