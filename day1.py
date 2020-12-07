# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 07:29:27 2020

@author: mdrei
"""

import pandas as pd
import numpy as np
from functools import reduce

file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\')

#read exense report from txt file
with open(file_loc + 'day1_expense_report.txt') as f:
    lines = f.readlines()

# value to search for
target = 2020

#create pandas series from list
exp = pd.Series(lines).str.strip().astype(int)

#### PART1
# create a square matrix using the series
exp_matrix = pd.DataFrame(np.resize(exp.values, (exp.size, exp.size)))

#add the original series to each column in the matrix and 
# find the location where the sum is 2020
exp_summed = exp_matrix.add(exp, axis='index')
exp_2020 = exp_summed.isin([target]).any()

#use the index to filter original series and get the two values
ans = exp.loc[exp_2020[exp_2020 == True].index]

#print the answer
print('Part1 Answer')
print(ans.iloc[0] * ans.iloc[1])

##############################
# part 2 (use brute force method)

#use the same method as before but loop over all the values and add them to
#the matrix from part1
#this method replicates the answer three times
ans_list = []
for i in range(exp.size):
    df = exp[i] + exp_summed
    df_targ = df.isin([target]).any()
    if df_targ.sum() > 0:
        x = exp[i]
        y = exp.loc[df_targ[df_targ == True].index].iloc[0]
        z = exp.loc[df_targ[df_targ == True].index].iloc[1]
        ans_list.append((x, y, z))

#multiple the elements of one the lists in the answer list together
print('Part2 Answer')
print(reduce(lambda x, y: x*y, ans_list[0]))

