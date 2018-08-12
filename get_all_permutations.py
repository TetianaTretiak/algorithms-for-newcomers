# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:12:27 2018

@author: Midori

@description:
Write a Python program to create all possible permutations from a given collection of distinct numbers.

"""

def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        
        print(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
        
  return result_perms

my_nums = [1,2]
print("Original Collection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))