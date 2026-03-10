
# Author: Ehsanullah Akbari
# Date: 2025-03-07
# exercise 2 of week-1  
# Description: Find maximam number in a list .
# Example:
# [23,40,5,6] ----> 40


def find_max(list):
    max= 0
    for x in list:
        if max< x:
            max= x
    return max        

print(find_max([30,4,5,6]))
