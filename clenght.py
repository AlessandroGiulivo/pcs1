#clenght(fname, s) returns the total lenght of the lines of the file pointed to by fname that contain the query string s (disresgarding case)
def clenght(fname, s):
    c = 0
    s = s.lower()
    with open(fname, 'r') as f:
         for l in f:
             if s in l.lower():
                 c += len(l)
    return c
    
print clenght('test.txt', 'on errors')