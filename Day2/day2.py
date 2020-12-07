# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:07:27 2020

@author: mdrei
"""

import pandas as pd


file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Day2\\')
file_name = 'day2_file.txt'
file = file_loc + file_name


# read the file into a pandas dataframe and format for analysis
# char is the target character to search for in the password (pw)
# min is the minimum number of times it must appear
# max is the maximum number of times it can appear

df = pd.read_table(file, sep=' ', header=None)
df.loc[:,0].str.split('-').str[0]
df['min'] = df.loc[:,0].str.split('-').str[0].astype(int)
df['max'] = df.loc[:,0].str.split('-').str[1].astype(int)
df['char'] = df.loc[:,1].str.replace(':', '').str.strip()
df['pw'] = df.loc[:,2].str.strip()
df = df.drop([0,1,2], axis=1)

#######Part1

# apply function to create count of target character in the password
df['char_count'] = df.apply(lambda x: x['pw'].count(x['char']), axis=1)


#check if the count is within the min and max and sum to get count
ans1 = ((df['char_count'] >= df['min']) & (df['char_count'] <= df['max'])).sum()

print('Part1 Answer')
print(ans1)


################Part2
# new requirement where the min and max column give index values in the string
# to check for the character
# rename the columns to reflect this
df = df.rename(columns={'min':'pos1', 'max':'pos2'})

#apply functions to check if target character is in the specified location
#position1
df['pos1_check'] = df.apply(lambda x: x['char']==x['pw'][x['pos1'] - 1], axis=1)
#position2
df['pos2_check'] = df.apply(lambda x: x['char']==x['pw'][x['pos2'] - 1], axis=1)


#use XOR to check for the password requirements
ans2 = (df['pos1_check'] ^ df['pos2_check']).sum()

print('Part2 Answer')
print(ans2)










