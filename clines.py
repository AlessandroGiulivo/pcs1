#clines(fname, s) returns the number of lines in the file fname whih contain the query string s
def clines(fname, s):
    c = 0
    s = s.lower()
    with open(fname, 'r') as f:
        for l in f:
            if s in l.lower():
                c += 1
    return c
    
print clines('alice.txt', 'shrink')