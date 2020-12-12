# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:13:26 2020

@author: mdrei
"""

file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Advent-of-Code-2020\\Day7\\')
#file_name = 'trial_file.txt'
file_name = 'file.txt'
file = file_loc + file_name

#read in the passport file    
# while reading lines split the bag requirements into a dictionary
# the key will be the outer bag and the value will be the requirement

reqs = {}
with open(file) as f:
    line = f.readline()
    while line:
        line = line.replace('bags', '').replace('bag', '')
        line = line.partition('contain')
        reqs[line[0].strip()] = line[2].strip()
        line = f.readline()
        
        
# recursive function to find the possible bags that our target bag could be in
# the first argument must be an empty list
# the second argument is initially a list of size 1 containing our target
# the third argument is the requirement dictionary
# the search will stop when there are no new bags to check

def bag_search(full_list, new_targets, req_dict):
    if len(new_targets) == 0:
        return full_list
    
    bag_list = []
    for target in new_targets:
        for key in req_dict:
            if (target in req_dict[key]) & (key not in full_list):
                bag_list.append(key)
                full_list.append(key)
    return bag_search(full_list, bag_list, req_dict)


target = ['shiny gold']
possible_bags = []
possible_bags = bag_search(possible_bags, target, reqs)
ans = len(possible_bags)


print('Part1 Answer')
print(ans)



################### Part2
# use recursion again
# this time need to keep track of what we are searching for and how many


def num_bags_required(targets, req_dict, num_bags=0):
    new_targets = []
    for target in targets:
        req = req_dict[target[0]].split()
        for i in range(len(req)):
            if req[i].isdigit():
                num_needed = (int(req[i]) * target[1])
                num_bags += num_needed
                new_target = req[i+1] + ' ' + req[i+2]
                new_targets.append((new_target, num_needed))
    if len(new_targets) == 0:
        return num_bags
    else:
        return num_bags_required(new_targets, req_dict, num_bags)

target = [('shiny gold', 1)]
ans = num_bags_required(target, reqs)

print('Part2 Answer')
print(ans)


