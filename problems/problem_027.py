# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    max = values[0]
    for value in values:
        if value > max:
            max = value
    return max
