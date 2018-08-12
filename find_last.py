# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:58:40 2018

The task is to find the position of the last entry of the substring in a string

@author: Midori
"""

def find_last(search, target):
    index = -1
    temp_index = search.find(target)
    while temp_index != -1:
        index = temp_index
        temp_index = search.find(target, index + 1)
    else:
        return index
        

print(find_last('aaaa', 'a'))
#>>> 3

print(find_last('aaaaa', 'aa'))
#>>> 3

print(find_last('aaaa', 'b'))
#>>> -1

print(find_last("111111111", "1"))
#>>> 8

print(find_last("222222222", ""))
#>>> 9

print(find_last("", "3"))
#>>> -1

print(find_last("", ""))