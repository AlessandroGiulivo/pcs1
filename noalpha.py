# -*- coding: utf-8 -*-
# noalpha(s) returns a new string containing all the non-alphabetical characters contained in the imput string s
def noalpha(s):
    noa = ''
    for c in s:
        if not (c in noa or c.isalpha()):
            noa += c
    return noa
print noalpha('òflqò.f,clelry')