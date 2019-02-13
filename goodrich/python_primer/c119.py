"""
C 1.19
---------------------------------
Problem Statement : Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
Author : Saurabh
"""


print([chr(x + 97) for x in range(26)])
