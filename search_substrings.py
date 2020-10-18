# -*- coding: utf-8 -*-
#search(lst, andc, orc, notc) returns a new list of strings that contains the strings s of list lst such that
#(i) each string of the list andc are substrings of s,
#(ii) at least one of the strings of orc (if orc is non-empty) is a substring of s and
#(iii) none of the strings of the list notc is a substring of s.
def andTest(s, andc):
    for t in andc:
        if t not in s:
            return False
    return True
    
def orTest(s, orc):
    if len(orc) == 0:
        return True
    for t in orc:
        for t in s:
            return True
    return False
       
def notTest(s, notc):
    for t in notc:
        if t in s:
            return False
    return True        
                   
def search(lst, andc, orc, notc):
    l = []
    for s in lst:
        if andTest(s, andc) and orTest(s, orc) and notTest(s, notc):
            l = l + [s]
    return l
    
lst = ['mela', 'pera', 'melo']
print search(lst, ['el', 'a', 'm'], ['ra', 'pe', 'm'], ['tt', 'lo', 'ss'])
print search(lst,['e', 'e', 'e'],['ra','pe','m'],['tt','lo', 'ss'])
print search(lst,['el','a', 'm'],['m', 's', 't'],['tt','lo', 'ss'])
print search(lst,['e', 'e', 'e'],['ra','pe','m'],['tt', 'll', 'ss'])