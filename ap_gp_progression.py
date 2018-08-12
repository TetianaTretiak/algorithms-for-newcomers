# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:58:36 2018

@author: Midori

@desciption:
Write a Python program to find the type of the progression (arithmetic progression/geometric progression) 
and the next successive member of a given three successive members of a sequence.
"""

def ap_gp_sequence(arr):
  if arr[0] == arr[1] == arr[2] == 0:
    return "Wrong Numbers"
  else:
    if arr[1] - arr[0] == arr[2] - arr[1]:
      n = 2 * arr[2] - arr[1]
      return "AP sequence, " + 'Next number of the sequence: ' + str(n)
    elif arr[1] % arr[0] == arr[2] % arr[1]:
      n = arr[2] ** 2 / arr[1]
      return "GP sequence, " + 'Next number of the sequence:  ' + str(n)
    else:
        return "No progression at all"
    
    

print(ap_gp_sequence([1,2,3]))
print(ap_gp_sequence([2,6,18]))
print(ap_gp_sequence([0,0,0]))
print(ap_gp_sequence([5,5,6]))