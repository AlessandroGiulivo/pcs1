#okpair takes as imput two strings s and t and checks wether the last character of s is the same as the first character of t
def okpair(s, t):
    return s[-1] == t[0]
    
print okpair('bubble', 'elbow')
print okpair('bubble', 'trouble')