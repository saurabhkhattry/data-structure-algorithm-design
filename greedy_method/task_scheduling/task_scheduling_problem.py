"""
The Task Scheduling Algorithm
---------------------------------
Problem Statement : A teacher assign homework at the beginning of the first day of class.
Each  problem carries 1 mark + bonus if submitted within specified number of days.
The deadline for submitting bonus and bonus marks are different for each problem.
Each problem takes exactly one day to complete. Maximum bonus one can obtain is 15.
Your task is to find a schedule to complete all homework problems so as to maximize bonus marks.
Author : Saurabh
"""


input_dict = {}
output_dict = {}
bonus_dict = {}
total_bonus = 0


def load_data(l):
    prob_no = int(l.split(',')[0])
    deadline = int(l.split(',')[1])
    bonus = int(l.split(',')[2])
    input_dict[prob_no] = (deadline, bonus)
    bonus_dict[prob_no] = bonus
    print("Problem no :{0}".format(prob_no))
    print("Deadline :{0}, Bonus :{1}".format(deadline, bonus))


def sort_and_fill():
    global total_bonus
    for item in sorted(bonus_dict, key=bonus_dict.get, reverse=True):
        index = int(input_dict.get(item)[0])
        while index > 0:
            if index in output_dict:
                index = index - 1
            else:
                output_dict[index] = item
                total_bonus = total_bonus + int(input_dict.get(item)[1])
                break
        if index == 0:
            index2 = len(input_dict)
            while index2 > 0:
                if index2 in output_dict:
                    index2 = index2 - 1
                else:
                    output_dict[index2] = item
                    break


def print_output():
    print("#########################")
    print("Schedule to maximize bonus marks is :")
    for key in sorted(output_dict):
        print("Day {0} : Problem number {1}.".format(key, output_dict[key]))
    print("Bonus :{0}".format(total_bonus))
    print("#########################")


if __name__ == "__main__":

    try:
        f = open("input.txt", mode='r', encoding='utf-8')
        for line in f:
            load_data(line)
    finally:
        f.close()

    sort_and_fill()
    print_output()
