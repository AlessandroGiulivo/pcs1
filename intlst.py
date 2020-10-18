# -*- coding: utf-8 -*-
#l2d(lst) takes as input a list lst containing numbers from 0 to 9 expressed in alphabetical form ('zero','one', …,'nine'),
#returns a new list whose elements are the corresponding number in lst in int form.
def intlst(lst):
    string_l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    l = []
    for x in lst:
        for j in range(len(string_l)):
            if string_l[j] == x:
                l = l + [j]
    return l
    
print intlst(['nine','two','two','three', 'seven'])