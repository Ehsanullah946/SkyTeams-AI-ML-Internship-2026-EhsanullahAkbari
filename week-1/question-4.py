
# Author: Ehsanullah Akbari
# Date: 2025-03-07
# exercise 4 of week-1  
# Description: Read CSV file using Python .

import csv

with open('file.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
