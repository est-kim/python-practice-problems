# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(word):
    new_str = ""
    new_list = []
    for letter in word:
        new_list.append(ord(letter))
    for num in new_list:
        new_str += chr(num + 1)
        for r in (("{", "a"), ("[", "A")):
            new_str = new_str.replace(*r)
    return new_str

#resources:
#https://stackoverflow.com/questions/16060899/alphabet-range-in-python (importing list of alphabets)
#https://stackoverflow.com/questions/50826831/python-append-to-an-empty-string
#https://www.geeksforgeeks.org/ord-function-python/
#https://www.geeksforgeeks.org/chr-in-python/
#https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
