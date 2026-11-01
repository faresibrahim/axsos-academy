

"""
Zoo Game - practice for the 4 OOP pillars

1. Abstraction   -> Animal is an abstract class. You cannot create a plain "Animal".
2. Encapsulation -> Animal hides its hunger level (__hunger) behind methods.
3. Inheritance   -> Lion, Monkey, Penguin and Elephant reuse code from Animal.
4. Polymorphism  -> Every animal answers make_sound() in its own way.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# PARENT CLASS (Abstraction + Encapsulation)
# ---------------------------------------------------------------
class Animal(ABC):  # ABC makes this an "abstract" class
    def __init__(self, name, age):
        self.name = name      # public: can be read or changed from outside
        self.age = age
        self.__hunger = 50    # private (double underscore): 0 = full, 100 = starving

    # A property lets us READ hunger like a normal attribute: animal.hunger
    # There is no setter, so outside code cannot set it directly.
    @property
    def hunger(self):
        return self.__hunger

    def feed(self, amount=20):
        # max() keeps hunger from going below 0
        self.__hunger = max(0, self.__hunger - amount)
        return f"{self.name} ate and is less hungry (hunger: {self.__hunger})."

    def get_hungrier(self, amount=15):
        # min() keeps hunger from going above 100
        self.__hunger = min(100, self.__hunger + amount)

    def is_hungry(self):
        return self.__hunger >= 70

    def describe(self):
        # self.__class__.__name__ gives the class name, e.g. "Lion"
        return (f"{self.name} the {self.__class__.__name__} "
                f"(age {self.age}, hunger {self.__hunger})")

    # Abstract methods: every child class MUST write its own version.
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def perform_trick(self):
        pass


# ---------------------------------------------------------------
# CHILD CLASSES (Inheritance)
# ---------------------------------------------------------------
class Lion(Animal):
    def __init__(self, name, age, mane_size="big"):
        super().__init__(name, age)  # let Animal set up name, age and hunger
        self.mane_size = mane_size   # extra attribute only lions have

    def make_sound(self):
        return f"{self.name} says: ROAAAR!"

    def hunt(self):  # a method only Lion has
        return f"{self.name} sneaks through the grass and pounces!"

    def perform_trick(self):
        return self.hunt()


class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} says: Ooh ooh aah aah!"

    def climb(self):  # a method only Monkey has
        return f"{self.name} swings from branch to branch."

    def perform_trick(self):
        return self.climb()


class Penguin(Animal):
    def make_sound(self):
        return f"{self.name} says: Honk honk!"

    def swim(self):  # a method only Penguin has
        return f"{self.name} dives into the pool and zooms underwater."

    def perform_trick(self):
        return self.swim()


class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} says: Prrrrrrr!"

    def spray_water(self):  # a method only Elephant has
        return f"{self.name} sprays water with its trunk. Splash!"

    def perform_trick(self):
        return self.spray_water()

    # Overriding: Elephants eat a lot, so we change how feed() works.
    def feed(self, amount=20):
        # super().feed() reuses the parent's code, so we only change the amount
        return super().feed(amount * 2)


# ---------------------------------------------------------------
# ZOO CLASS (holds many animals)
# ---------------------------------------------------------------
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []  # a list that will hold Animal objects

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for number, animal in enumerate(self.animals, start=1):
            print(f"  {number}. {animal.describe()}")

    def all_sounds(self):
        # POLYMORPHISM: we call the same method on every animal,
        # and each animal answers in its own way.
        for animal in self.animals:
            print(f"  {animal.make_sound()}")

    def next_day(self):
        for animal in self.animals:
            animal.get_hungrier()
            if animal.is_hungry():
                print(f"  Warning: {animal.name} is very hungry!")


# ---------------------------------------------------------------
# GAME CODE
# ---------------------------------------------------------------
def choose_animal(zoo):
    """Show the animals and return the one the player picks (or None)."""
    zoo.show_animals()
    choice = input("Pick an animal number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(zoo.animals):
        return zoo.animals[int(choice) - 1]
    print("That is not a valid number.")
    return None


def main():
    zoo = Zoo("Sunny Zoo")
    zoo.add_animal(Lion("Leo", 5))
    zoo.add_animal(Monkey("Momo", 3))
    zoo.add_animal(Penguin("Pingu", 2))
    zoo.add_animal(Elephant("Ella", 10))

    # Uncomment the next line to see abstraction in action. It raises a TypeError:
    # Animal("Mystery", 1)

    print(f"Welcome to {zoo.name}!")

    while True:
        print("\n1. See all animals")
        print("2. Feed an animal")
        print("3. Hear all animal sounds")
        print("4. Ask an animal to do its trick")
        print("5. Next day (animals get hungry)")
        print("6. Quit")
        choice = input("What do you want to do? ")

        if choice == "1":
            zoo.show_animals()
        elif choice == "2":
            animal = choose_animal(zoo)
            if animal:
                print(animal.feed())  # Elephant's feed() runs for Ella
        elif choice == "3":
            zoo.all_sounds()
        elif choice == "4":
            animal = choose_animal(zoo)
            if animal:
                print(animal.perform_trick())  # polymorphism again
        elif choice == "5":
            zoo.next_day()
        elif choice == "6":
            print("Thanks for visiting the zoo. Goodbye!")
            break
        else:
            print("Please type a number from 1 to 6.")


# This line runs main() only when you run this file directly
if __name__ == "__main__":
    main()


