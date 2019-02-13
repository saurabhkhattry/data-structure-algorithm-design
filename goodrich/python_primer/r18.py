"""
R 1.8
---------------------------------
Problem Statement : Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?
Author : Saurabh
"""

s = 'abcdefghijk'

# For any k such that −n≤k<0, s[k] will be equal to s[j] , when j = n + k

n = len(s)
k = -11
j = n + k
print(s[k])
print(s[j])
