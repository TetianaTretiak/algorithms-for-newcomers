# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 19:05:40 2018

@author: Midori
@description: Write a program which finds the second max element in a list.
"""

def get_second_max(arr):
    
    max_element = max(arr)
    
    max_new = 0
    
    for i in arr:
        if i != max_element and i > max_new:
            max_new = i        
    
    return max_new


print(get_second_max([2, 5, 7, 7]))
    
