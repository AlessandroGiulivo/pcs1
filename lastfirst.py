#lastfirst takes as imput a list lst and
#returns the first element of lst whose first character is different from the last charachter of the previous element.

def okpair(s, t):
    return s[-1] == t[0]

def lastfirst(lst):
    for i in range(len(lst) - 1):
        if not okpair(lst[i], lst[i + 1]):
            return lst[i + 1]

print lastfirst(['sun','nature','elm','game','win'])