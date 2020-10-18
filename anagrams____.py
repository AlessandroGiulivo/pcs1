import words as w

def fwords(filename, enc):
    with open(filename, 'U') as f:
        text = f.read()
    text = text.decode(enc)
    return w.words(text)
    
def anagrams(fname, w):
    l = []
    for x in fwords(fname, 'utf8'):
        if sorted(list(w.lower())) == sorted(list(x.lower())):
            if x.lower() not in l:
                l.append(x.lower())
    return l

print anagrams('alice.txt', 'read')