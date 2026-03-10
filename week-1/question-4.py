
# Author: Ehsanullah Akbari
# Date: 2025-03-07
# exercise 4 of week-1  
# Description: Read CSV file using Python .

# import csv

# with open('file.csv', mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(row)



# Author: Ehsanullah Akbari
# Date: 2026-03-08
# exercise 5 of week-1  
# Description: swap two vareibles .


# def swapTwoVar(a,b):
#       [a,b] = [b,a]
#       print(f"a:{a} b:{b}")

# swapTwoVar(30,40)      


# Author: Ehsanullah Akbari
# Date: 2026-03-08
# exercise 6 of week-2 finding the smallest and largest number 
# example
# input : a=4 b=5 c=10
# output: a=10 b=4



def find_small_and_largest_number(a,b,c):
      if a>b and a>c:
            return a
      elif b>a and b>c:
            return b
      elif c>a and c>b:
            return c
      
print(find_small_and_largest_number(10,50,3))         





       