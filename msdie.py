#class definition for an n-sided die

#import packages

import random

class MSdie:

    value = 0

  #constructor here

    def __init__(self,numOfSides):
        self.numOfSides = numOfSides

  #define classmethod 'roll' to roll the MSdie
    def roll(self):

        if self.value != 0:
            return self.value

        else:
            self.value = random.randint(1, self.numOfSides)
            return self.value

    def getValue(self):
        return self.value


    def setValue(self, value):
        self.value = value
