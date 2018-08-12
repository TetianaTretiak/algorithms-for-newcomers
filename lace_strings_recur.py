# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:55:52 2018

@author: Midori
"""

def lace_strings_recur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def help_lace_strings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return out + s1[0] + s2[0] + help_lace_strings(s1[1:], s2[1:], out)
                
    return help_lace_strings(s1, s2, '')
    
print(lace_strings_recur('abcd', 'efghi'))