"""
C 1.15
---------------------------------
Problem Statement : Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
Author : Saurabh
"""


def distinct_num(tup_seq):
    dist_flag = 'Y'
    for elm in tup_seq:
        count = 0
        for other_elm in tup_seq:
            if other_elm == elm:
                count += 1
                if count > 1:
                    dist_flag = 'N'
                    break
        if dist_flag == 'N':
            break
    if dist_flag == 'N':
        return "Not Distinct !"
    else:
        return "Distinct !"


if __name__ == "__main__":
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    b = (2, 4, 6, 8, 8)
    print(distinct_num(a))
    print(distinct_num(b))
