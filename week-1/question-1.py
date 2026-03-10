
# Author: Ehsanullah Akbari
# Date: 2025-03-07
# exercise 1 of week-1  
# Description:Reverse a list .
# Example:
# [23,4,5,6] ----> [6,5,4,23]

def reverseList(list):
    reverse= []
    for x in list[::-1]:
        reverse.append(x)
    return reverse

print(reverseList([2,3,4,5]))     