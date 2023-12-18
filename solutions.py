"""
Chapter 8 solutions written in python

"""

# exercise 1
def getIntersection(arr1, arr2):
    intersection = []
    hash = {}

    for i in range(len(arr1)):
        hash[arr1[i]] = True

    for j in range(len(arr2)):
        if hash[arr2[j]]:
            intersection.append(arr2[j])

    return intersection 

# exercise 2 
def findDuplicate(arr):
    hash = {}

    for i in range(len(arr)):
        if hash[arr[i]]:
            return arr[i]
        else:
            hash[arr[i]] = True
    

# exercise 3
def findMissingLetter(string):
    hash = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(string)):
        hash[string[i]] = True

        for i in range(len(alphabet)):
            if not hash[alphabet[i]]:
                return alphabet[i]
    

# exercise 4
def firstNonDuplicate(string):
    hash = {}

    for i in range(len(string)):
        if hash[string[i]]:
            hash[string[i]] += 1
        else:
            hash[string[i]] = 1

    for j in range(len(string)):
        if hash[string[j]] == 1:
            return string[j]