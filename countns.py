#countn(t, ns) returns the number of occurrences of the numerical sequence ns in the string t

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


def countn(t, ns):
    countn = 0
    t = digits(t)
    countn += t.count(ns)
    return countn
    
t = '34 34 hhfyf34 34 ..34 34)) 548634'
print countn(t, '34')