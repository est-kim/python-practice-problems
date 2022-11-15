# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

spec_char = "~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/"


def check_password(password):
    check_lower = False
    check_upper = False
    check_digit = False
    check_spec = False
    check_length = False

    for pw in password:
        if pw.islower():
            check_lower = True
        if pw.isupper():
            check_upper = True
        if pw.isdigit():
            check_digit = True
        for char in spec_char:
            if char == pw:
                check_spec = True
        if len(password) in range(6, 12):
            check_length = True
    return check_lower and check_upper and check_digit and check_spec and check_length
