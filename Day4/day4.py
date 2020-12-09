# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:15:05 2020

@author: mdrei
"""

import re

file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Advent-of-Code-2020\\Day4\\')
file_name = 'file.txt'
file = file_loc + file_name

#read in the passport file    
with open(file) as f:
    lines = f.readlines()

# append and empty string to the end of lines to ensure that the last entry
# is not skipped
lines.append('')

# iterate through the lines of the file and identify the non_empty lines
# and keep track of the indices
non_empty_indices = []
one_passport_indices = []
for i in range(len(lines)):
    if len(lines[i].strip()) > 1:
        one_passport_indices.append(i)
    else:
        non_empty_indices.append(one_passport_indices)
        one_passport_indices = []


# use the selected indices to combine the lines together 
# after combining the lines, convert to dictionary
pass_list = []
for lst in non_empty_indices:
    string = ''
    for index in lst:
        string = string + lines[index].strip() + ' '
    data_list = (re.split(':| ', string.strip()))
    d = dict(zip(data_list[::2], data_list[1::2]))
    pass_list.append(d)

# fields to search for in the passport dictionaries. Do not need to search for
# cid since it is not a requirement
req_fields = ['ecl', 'byr', 'iyr', 'pid', 'hgt', 'eyr', 'hcl']

#search for the required fields in the dictionaries and keep track of
# valid passports for part2
all_field_passports = []
for d in pass_list:
    in_dict = []
    for field in req_fields:
        in_dict.append(field in d.keys())
    if all(in_dict):
        all_field_passports.append(d)
        
print('Part1 Answer')
print(len(all_field_passports))

########################## Part2

# check value for each key in the valid dictionaries to see if the value
# meets the formatting requirments
valid_passports = []
#eye color requirements
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#pattern to match for hair color
hcl_pat = re.compile('[\d|a-f]{6,6}')

for d in all_field_passports:
    reqs = []
    
    byr = int(d['byr'])
    if (byr >= 1920) & (byr <= 2002):
        reqs.append(True)
    else:
        reqs.append(False)
    
    iyr = int(d['iyr'])
    if (iyr >= 2010) & (iyr <= 2020):
        reqs.append(True)
    else:
        reqs.append(False)

    eyr = int(d['eyr'])
    if (eyr >= 2020) & (eyr <= 2030):
        reqs.append(True)
    else:
        reqs.append(False)        
    
    hgt_str = d['hgt']
    if hgt_str[-2:] == 'in':
        hgt = int(hgt_str[:-2])
        if (hgt >= 59) & (hgt <= 76):
            reqs.append(True)
        else:
            reqs.append(False)
    elif hgt_str[-2:] == 'cm':
        hgt = int(hgt_str[:-2])
        if (hgt >= 150) & (hgt <= 193):
            reqs.append(True)
        else:
            reqs.append(False)
    else:
        reqs.append(False)

    hcl = d['hcl']
    if bool(hcl_pat.match(hcl[1:])) & (hcl[0] == '#') & (len(hcl) == 7):
        reqs.append(True)
    else:
        reqs.append(False)        
    
    ecl = d['ecl']
    if ecl in eye_colors:
        reqs.append(True)
    else:
        reqs.append(False)    

    pid = d['pid']        
    if (pid.isnumeric()) & (len(pid) == 9):
        reqs.append(True)
    else:
        reqs.append(False)    
    
    if all(reqs):
        valid_passports.append(d)
    

    
print('Part2 Answer')
print(len(valid_passports))  


