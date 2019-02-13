"""
C 1.14
---------------------------------
Problem Statement : Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
Author : Saurabh
"""


def product_odd(tup_seq):
    first = second = None
    for elm in tup_seq:
        if elm % 2 == 1:
            if first is None:
                first = elm
            else:
                second = elm
                break
    if second is not None:
        return first, second
    else:
        return "Does not have a valid pair !"
    

if __name__ == "__main__":
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    b = (2, 4, 6, 8)
    print(product_odd(a))
    print(product_odd(b))
