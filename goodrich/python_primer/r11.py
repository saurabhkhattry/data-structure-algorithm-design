"""
R 1.1
---------------------------------
Problem Statement : Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
Author : Saurabh
"""


def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


if __name__ == "__main__":
    print(is_multiple(6, 4))
    print(is_multiple(6, 2))
