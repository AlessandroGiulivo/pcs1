# -*- coding: utf-8 -*-
#1. firstline(t, s) returns the first line of the string t that contains the string s; if s does not occur in t, it returns None.
def firstline(t, s):
    for e in t.splitlines():
        if s in e:
            return e
    return None
t = u'''Quant'è bella giovinezza
che si fugge tuttavia
Chi vuol esser lieto, sia:
del doman non c'è certezza.'''
print firstline(t, 'non')