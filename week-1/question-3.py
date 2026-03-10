# Author: Ehsanullah Akbari
# Date: 2025-03-07
# exercise 3 of we  
# Description: Count frequency of elements in a list .
# Example:
# [3,4,5,5,6] ----> {3: 1, 4: 1, 5: 2, 6: 1}


def count_frequency(list):
    map = {}
    for item in list:
        if item in map:
            map[item] += 1
        else:
            map[item]=1     
    return map

print(count_frequency([3,4,5,5,6]))


