""" 
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

"""


def capital_indexes(s):
    indexes = []
    for i, char in enumerate(s):
        if char.isupper():
            indexes.append(i)
    return indexes


sam = "HelLoO"
result = capital_indexes(sam)

print(result)
