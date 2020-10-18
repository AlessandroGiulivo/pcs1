import words

def wset(fname):
    return set(words.fwords(fname, 'utf8'))
    
print wset('alice.txt')
print len(wset('alice.txt'))