# -*- coding: utf-8 -*-
#countw(t, w) returns the number of occurrences of the word w in the string t.

def noalpha(s):
    noa = ''
    for c in s:
        if not (c in noa or c.isalpha()):
            noa += c
    return noa
    
def words(s):
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.split()
        
def countw(t, w):
    return words(t.lower()).count(w.lower())

t = 'today is the day after yesterday'
print countw(t, 'day')