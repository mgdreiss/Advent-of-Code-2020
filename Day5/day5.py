# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:31:02 2020

@author: mdrei
"""

import math
import statistics as stats


file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Advent-of-Code-2020\\Day5\\')
file_name = 'file.txt'
file = file_loc + file_name

#read in the passport file    
with open(file) as f:
    lines = f.read().splitlines()

# recursive function to perform the binary partitioning
def binary_partitioner(min_row, max_row, string):
    #print(min_row, max_row, string)
    # ensure string is long enought for recursive function to finish
    # this assumes min_row starts at zero
    if (max_row - min_row) >= 2 ** len(string):
        return None
    med = stats.median([min_row, max_row])
    if max_row == min_row:
        return max_row
    if string[0] in ['F', 'L']:
        return binary_partitioner(min_row, math.floor(med), string[1:])
    if string[0] in ['B', 'R']:
        return binary_partitioner(math.ceil(med), max_row, string[1:])
    
#apply the recursive function to the row and column strings separately
#then apply seat id equation: seat_id = row_num * 8 + column_num

seat_ids = []    
for line in lines:
    row_num = binary_partitioner(0, 127, line[0:7])
    col_num = binary_partitioner(0, 7, line[7:])
    seat_id = row_num * 8 + col_num
    seat_ids.append(seat_id)


print('Part1 Answer')
print(max(seat_ids))  


##################### Part2

# the missing seat will be the number missing from seat_ids when compared to
# the full list of possible seat_ids
poss_seats = list(range(min(seat_ids), max(seat_ids)+1))

#use set methods to find the missing number
missing_seats = list(set(poss_seats).difference(set(seat_ids)))

print('Part1 Answer')
print(missing_seats[0])  











