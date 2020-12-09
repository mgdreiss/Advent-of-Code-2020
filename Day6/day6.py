# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:18:15 2020

@author: mdrei
"""


file_loc = ('C:\\Users\\mdrei\\Documents\\code\\advent_of_code_2020\\Advent-of-Code-2020\\Day6\\')
file_name = 'file.txt'
file = file_loc + file_name

#read in the passport file    
with open(file) as f:
    lines = f.read().splitlines()