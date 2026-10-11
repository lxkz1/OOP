class Animals():
    alive = True

class Dog(Animals):
    def speak(self):
        print("WOOF!")

class Cat(Animals):
    def speak(self):
        print("Meow!")

class Car:
    alive = False

    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
