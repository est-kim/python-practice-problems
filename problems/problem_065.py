# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function


def biggest_gap(numbers):
    new_list = []
    for num in range(len(numbers)-1):
        diff_left = numbers[num+1] - numbers[num]
        new_list.append(diff_left)
        diff_right = numbers[num] - numbers[num+1]
        new_list.append(diff_right)
    new_list.sort()
    biggest_diff = new_list[-1]
    return biggest_diff


#resources:
#https://www.tutorialspoint.com/largest-gap-in-python
#https://www.pythontutorial.net/python-basics/python-sort-list/
