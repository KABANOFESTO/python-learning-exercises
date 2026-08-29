class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.alive = False

    def speak(self):
        return "Meow!"


animals = [Dog(), Cat()]


for animal in animals:
    print(
        f"{animal.__class__.__name__} says: {animal.speak()} status: {'Alive' if animal.alive else 'Dead'}"
    )
