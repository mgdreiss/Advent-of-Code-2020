# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:18:15 2020

@author: mdrei
"""


file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Advent-of-Code-2020\\Day6\\')
#file_name = 'trial_file.txt'
file_name = 'file.txt'
file = file_loc + file_name

#read in the passport file    
with open(file) as f:
    lines = f.read().splitlines() 
    
    
#combine strings from multiple lines together
#then convert string to a set which does not allow duplicate characters
answers = ''
count = 0
for i in range(len(lines)):
    if i == (len(lines) - 1):
        answers += lines[i].strip()
        count += len(set(answers))

    if lines[i] != '':
        answers += lines[i].strip()
    else:
        count += len(set(answers))
        answers = ''
        
print('Part1 Answer')
print(count)


################## PART2
# modify part1 to create a list of answers then look for characters that have 
# the same count as number of people in group
# answer list will contain a tuple that keeps track of the 3 things:
# (all_the_answers, number_of_people, unique_characters)

ans_list = []
num_people = 0
answers = ''
for i in range(len(lines)):
    if i == (len(lines) - 1):
        answers += lines[i].strip()
        num_people += 1
        ans_list.append((answers, num_people, set(answers)))

    if lines[i] != '':
        answers += lines[i].strip()
        num_people += 1
    else:
        ans_list.append((answers, num_people, set(answers)))
        answers = ''
        num_people = 0

count = 0        
for answer in ans_list:
    for char in answer[2]:
        if answer[0].count(char) == answer[1]:
            count += 1
                
print('Part2 Answer')
print(count)
        
