"""
R 1.5
---------------------------------
Problem Statement : Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
Author : Saurabh
"""


def sum_of_squares(n):
    total = 0
    for d in range(n+1):
        total = total + d*d
    return total


if __name__ == "__main__":
    print(sum_of_squares(2))
    print(sum_of_squares(7))
    # One liner :
    x = 7
    print(sum([d*d for d in range(x + 1)]))
