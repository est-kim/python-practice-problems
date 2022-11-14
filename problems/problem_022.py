# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    list = []
    if is_workday is True and is_sunny is False:
        list.append("umbrella")
        list.append("laptop")
    elif is_workday is True:
        list.append("laptop")
    elif is_workday is False:
        list.append("surfboard")
    return list
