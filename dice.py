import random

class Dice:
    """Class to define a dice object with 'n' number of sides"""
    def __init__(self, number_of_sides=6):
        self.sides = number_of_sides

    def throw_dice(self):
        return random.randrange(1, self.sides + 1)