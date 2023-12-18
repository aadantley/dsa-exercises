"""
Write a function that accepts an array of strings and retuns the first duplicate value it finds.

Note, assume there's only one pair of duplicates.
"""

test = ["a", "v", "c", "d", "v", "e", "f"]

def findDuplicate(arr):
    hash = {}
    for val in arr:
        if val in hash:
            hash[val] = 1
        else: 
            hash[val] = 0
            
    duplicates = []
    for key in hash:
        if hash[key] == 1:
            duplicates.append(key)

    return duplicates

print(findDuplicate(test))