"""
Find the intersection of the two arrays below using a hash table
"""

arr1 = [1,2,3,4,5]
arr2 = [0,2,3,4,6,8]

print(arr1, arr2)

hash = {}

if len(arr1) > len(arr2):
    largeArr = arr1
    smallArr = arr2
else: 
    largeArr = arr2
    smallArr = arr1 


for value in largeArr:
    hash[value] = False

for value in smallArr:
    if hash.get(value) == False:
        hash[value] = True 

intersection = []
for key in hash:
    if hash[key] == True:
        intersection.append(key)

print(intersection)