# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4


def sum_fraction_sequence(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i / (i + 1)
    return sum




#resource: https://stackoverflow.com/questions/69475392/how-to-use-for-loop-to-sum-first-n-integer-fractions
