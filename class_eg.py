# How you defined a class =  class + space + Name of the class (Capital letter for the first letter) + :
# You can use __init__ with classes, init automatically executes de function and the lines of codes run 
# Always in __init__ you need the (self) parameter
# Classes are a collection of functions

class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Biel", "Pug", "cream")
neighbors_dog = Dog("Bee", "Pug", "black")


# Fetching the attributes of the class using objects
print(my_dog.name)

print(my_dog.bark())
print(neighbors_dog.bark())
