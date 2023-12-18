"""
Write a function that accepts a string that contains all the letters of the alphabet  except 1 and returns the mssing letter.
"""
import string


test = "the quick brown box jumps over a lazy dog"


def findMissingLetter(strArray):
    hash = {}
    alphabet = list(string.ascii_lowercase)
    strArray = list(strArray.replace(" ", ""))

    # all the letters in the string
    for letter in strArray:
        if letter in hash:
            continue
        else:
            hash[letter] = True

    # remove letters in hash from string array
    for letter in hash:
        alphabet.remove(letter)

    # return missing character
    return alphabet[0]


print(findMissingLetter(test))
