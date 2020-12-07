# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:06:30 2020

@author: mdrei
"""

import pandas as pd
import math
from functools import reduce

file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Day3\\')
file_name = 'day3_file.txt'
file = file_loc + file_name

# read first line of the file and get the length of the row
with open(file) as f:
    row_len = len(f.readline().strip())
    
# use the length of the rows and read_fwf to read each character in the string
# into separate columns
base_df = pd.read_fwf(file, widths=[1 for i in range(row_len)], header=None)


# repeat the pattern to the right many times n is the number of times to repeat
# since the patter to search the forest is right 3 down 1 then the number
# of times needed to repeat is (the number of downward steps needed) x (the 
# number of steps taken to the right for each downward step(3)) / (row length) 
# rounded up
down_steps = base_df.shape[0] - 1
n = math.ceil((down_steps * 3) / row_len)

df = pd.concat([base_df for i in range(n)], axis=1)

#rename the columns from 0 to the number of columns
num_cols = df.shape[1]
cols = list(range(num_cols))
df.columns = cols

#Use the right 3 down 1 method to step through the pattern
#Create a list of index postions to check using this pattern
#Since the checking method only steps down 1 each time, then total number of
# spots to check will be the number of rows minus 1
num_to_check = df.shape[0] - 1
pos_to_check = [(i+1, 3*(i+1)) for i in range(num_to_check)]

#iterate over the positions to check and see if there is a tree ('#')
tree_counter = 0
for pos in pos_to_check:
    if df.loc[pos[0], pos[1]]=='#':
        tree_counter += 1

print('Part1 Answer')
print(tree_counter)

####### Part2
# create a function to search the pattern for general right X down Y search pattern
# in general the number of positions needed to check is (the number of rows-1) / 
# (the down step) rounded up
# down_steps is also the num of positions to check

def tree_searcher(right_step, down_step, base_df):
    row_len = base_df.shape[1]
    down_steps = math.ceil((base_df.shape[0] - 1) / down_step)
    num_time_to_repeat_pattern = math.ceil((down_steps * right_step) / row_len)
    df = pd.concat([base_df for i in range(num_time_to_repeat_pattern)], axis=1)
    cols = list(range(df.shape[1]))
    df.columns = cols
    pos_to_check = [((i+1)*down_step, (i+1)*right_step) for i in range(down_steps)]
    tree_counter = 0  
    for pos in pos_to_check:
        if df.loc[pos[0], pos[1]]=='#':
            tree_counter += 1
    return tree_counter

#create list of the travel patterns to check and iterate 
# (right_step, down_step)
patterns = [(1,1), (3,1), (5,1), (7,1), (1,2)]

ans_list = []
for pat in patterns:
    ans_list.append(tree_searcher(pat[0], pat[1], base_df))

ans2 = reduce(lambda x, y: x*y, ans_list)

print('Part2 Answer')
print(ans2)







