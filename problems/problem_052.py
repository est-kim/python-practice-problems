# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html

from random import randint

def generate_lottery_numbers():
    new_list = []
    while len(new_list) < 6:
        new_list.append(randint(1, 40))
        for num in new_list:
            if new_list.count(num) > 1:
                new_list.remove(num)
                new_list.append(randint(1, 40))
    return new_list


#source https://www.geeksforgeeks.org/python-count-occurrences-element-list/
#https://www.freecodecamp.org/news/python-list-remove-how-to-remove-an-item-from-a-list-in-python/#:~:text=How%20to%20Remove%20an%20Element,find%20it%20and%20remove%20it.
