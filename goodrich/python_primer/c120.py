"""
C 1.20
---------------------------------
Problem Statement : Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
Author : Saurabh
"""


import random


def shuffle(list_data):
    for i in range(len(list_data)):
        swap_index = random.randint(0, len(list_data)-1)
        list_data[i], list_data[swap_index] = list_data[swap_index], list_data[i]


if __name__ == "__main__":
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    shuffle(list_a)
    print(list_a)
