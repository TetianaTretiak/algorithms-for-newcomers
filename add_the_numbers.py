# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:56:44 2018

@author: Midori

@description: Write a program to add all the digits of a given positive integer until the result has a single digit.
"""

def add_the_numbers(num):
    
    while num >= 10:
        new_num = 0
        str_num = str(num)
        for i in str_num:
            new_num += int(i)
                
        num = new_num
    return num

print(add_the_numbers(165954))

        

