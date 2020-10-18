#all_char(fname, enc) returns a unicode string that contains all the characters,
#with no repetition and in the order they appear, of the file fname decoded by the encoding enc
def all_char(fname, enc):
    with open(fname, 'r') as f:
        t = f.read().decode(enc)
        s = u''
        for c in t:
            if c not in s:
               s += c
    return sorted(list(s))
    
print all_char('alice.txt', 'utf8')