import random

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        i = 0
        k = 10
        while i != k:
            print(random.randint(1, self.sides))
            i +=1

kub = Die()
kub.roll_die()