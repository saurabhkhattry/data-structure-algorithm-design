"""
The Fractional Knapsack Algorithm
---------------------------------
Problem Statement : Given weights and values of n items,
 we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Author : Saurabh
"""

input_dict = {}
fraction_dict = {}
output_dict = {}
profit = 0


def load_data(l):
    global no_of_items
    no_of_items += 1
    print("Item no :{0}".format(no_of_items))
    price = int(l.split(',')[0])
    weight = int(l.split(',')[1])
    input_dict[no_of_items] = (price, weight)
    fraction_dict[no_of_items] = (price / weight)
    print("Price :{0}, weight :{1}".format(price, weight))


def sort_and_fill(total_capacity):
    global profit
    for item in sorted(fraction_dict, key=fraction_dict.get, reverse=True):
        if total_capacity >= int(input_dict.get(item)[1]):
            total_capacity = total_capacity - int(input_dict.get(item)[1])
            output_dict[item] = int(input_dict.get(item)[1])
            profit = profit + int(input_dict.get(item)[0])
        else:
            output_dict[item] = total_capacity
            profit = profit + input_dict.get(item)[0] * (total_capacity / int(input_dict.get(item)[1]))


def print_output():
    print("#########################")
    print("Choosen items are :")
    for key in output_dict:
        print("Item {0}, {1} units.".format(key, output_dict[key]))
    print("Total profit :{0}".format(profit))
    print("#########################")


if __name__ == "__main__":
    print("Fractional Knapsack")
    no_of_items = 0
    print("Enter the total capacity of the bag :")
    # Enter total capacity of bag as 40
    tc = int(input())
    print("Total capacity of the bag is {0} units.".format(tc))

    try:
        f = open("input.txt", mode='r', encoding='utf-8')
        for line in f:
            load_data(line)
    finally:
        f.close()

    sort_and_fill(tc)
    print_output()
