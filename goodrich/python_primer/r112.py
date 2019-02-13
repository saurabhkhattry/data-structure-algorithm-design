"""
R 1.12
---------------------------------
Problem Statement : Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
Author : Saurabh
"""

import random


def choice(seq):
    return seq[len(seq) % random.randrange(1, 10)]


if __name__ == "__main__":
    a = (2, 3, 10, 5, 6, 7, 8, 18, 9, 12, 23, 4, 8, 1)
    print(choice(a))

