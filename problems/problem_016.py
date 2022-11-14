# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return True
    else:
        return False
