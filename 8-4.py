"""
Write a function that returns the first non-duplicated character in the string 
"""

test = "minimum"


def nonDuplicate(string_arg):
    hash = {}

    for index in range(len(string_arg)):
        if string_arg[index] not in hash:
            tmp = {"nOfChars": 1, "index": index}
            hash[string_arg[index]] = tmp
        else:
            hash[string_arg[index]]["nOfChars"] += 1

    index_list = []
    for item in hash:
        if hash[item]["nOfChars"] == 1:
            index_list.append(hash[item]["index"])

    lowest_nonDupicate_index = min(index_list)

    return string_arg[lowest_nonDupicate_index]


print(nonDuplicate(test))
