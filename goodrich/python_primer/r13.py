"""
R 1.3
---------------------------------
Problem Statement : Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
Author : Saurabh
"""


def min_max(data):
    min_d = max_d = data[0]
    for d in data:
        min_d = d if d < min_d else min_d
        max_d = d if d > max_d else max_d
    return min_d, max_d


if __name__ == "__main__":
    print(min_max((6, 3, 2, 6, 9, 8, 7, 0)))
