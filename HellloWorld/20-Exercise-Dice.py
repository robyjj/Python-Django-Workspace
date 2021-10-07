"""
class Dice
    - roll() - returns a tuple of 2 random values
"""
import random


class Dice:
    def roll(self):
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        return num1,num2


d = Dice();
a, b = d.roll()
print(f'The numbers are {a} and {b}')
