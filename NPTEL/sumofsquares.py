'''
A positive integer m is a sum of squares if it can be written as k + l where k > 0, l > 0 and both k and l are perfect squares.
Write a Python function sumofsquares(m) that takes an integer m returns True if m is a sum of squares and False otherwise. (If m is not positive, your function should return False.)
Here are some examples to show how your function should work.
>>> sumofsquares(41)
True
>>> sumofsquares(30)
False
>>> sumofsquares(17)
True
'''

import math


def sumofsquares(m):
    d = range((int(math.sqrt(m / 2))), (int(math.sqrt(m - 1)) + 2))
    s = [1]
    for x in d:
        s.append(x*x)
    print(m, d, s)
    z = 0
    while z < len(s):
        for y in s[z:]:
            if y + s[z] == m:
                return True
        z += 1
    return False


print(sumofsquares(17))
