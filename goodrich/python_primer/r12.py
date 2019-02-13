"""
R 1.2
---------------------------------
Problem Statement : Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
Author : Saurabh
"""


def is_even(k):
    a = 1
    # Using bitwise AND operator
    if k & a == 0:
        return True
    return False


if __name__ == "__main__":
    print(is_even(6))
    print(is_even(5))
