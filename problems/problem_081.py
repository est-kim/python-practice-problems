# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"

class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return self.__class__.__name__ + " has " + str(self.number_of_legs) + " legs and is primarily " + self.primary_color

class Dog(Animal):
    def __init__(self, number_of_legs, primary_color):
        super().__init__(number_of_legs, primary_color)

    def speak(self):
        return "Bark!"

class Cat(Animal):
    def __init__(self, number_of_legs, primary_color):
        super().__init__(number_of_legs, primary_color)

    def speak(self):
        return "Miao!"

class Snake(Animal):
    def __init__(self, number_of_legs, primary_color):
        super().__init__(number_of_legs, primary_color)

    def speak(self):
        return "Sssssss!"

#resoureces:
#https://www.geeksforgeeks.org/python-super/
