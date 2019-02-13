"""
R 1.4
---------------------------------
Problem Statement : Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
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
