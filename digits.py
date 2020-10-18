#3. digits(t) returns the list of numerical sequences contained in the string t.
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
    
def nodigit(s):
    nod = ''
    for c in s:
        if (c not in nod) and (not c.isdigit()):
            nod += c
    return nod

def digits(t):
    for c in nodigit(t):
        t = t.replace(c, ' ')
    return t.split()

t = 'via Po n.23, tel. 06 7867555 - mobile 345 675665676 (cc 34565)'
print digits(t)