# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:11:49 2018

@author: Midori

@description: 
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

"""

a = raw_input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a, a))
n3 = int( "%s%s%s" % (a, a, a))
n4 = int( "%s%s%s%s" % (a, a, a, a))
print(n1 + n2 + n3 + n4)
