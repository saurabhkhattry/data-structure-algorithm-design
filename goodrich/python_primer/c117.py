"""
C 1.17
---------------------------------
Problem Statement : Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
for val in data:
val *= factor
Explain why or why not.
Author : Saurabh
"""


"""
It will not work properly as we are not updating the elements of the list.
Instead we are updating the value of the local variable val.
"""
