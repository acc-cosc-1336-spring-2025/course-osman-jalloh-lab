import random

class Die:
    __roll_value = 0  

    def roll(self):
        self.__roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return self.__roll_value

    def __str__(self):
        return f"The rolled value is {self.__roll_value}"
