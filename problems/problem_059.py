# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random

def specific_random():
    div_num = []
    for num in range(10, 500):
        if num % 5 == 0 and num % 7 == 0:
            div_num.append(num)
    return random.choice(div_num)


#resources:
#https://www.geeksforgeeks.org/random-choices-method-in-python/
