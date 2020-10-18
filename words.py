def fwords(filename, enc):
    with open(filename, 'U') as f:
        text = f.read()
    text = text.decode(enc).lower()
    return words(text)

def noalpha(s):
    '''Returns a string containing all the non-alphabetical characters of s,
    with no repetition.'''
    noa = ''
    for c in s:
        if not (c in noa or c.isalpha()):
            noa += c
    return noa
        
def words(s):
    '''Returns the list of the words in the string s'''
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.split()
    
            
if __name__ == '__main__':
    def test_noalpha(s):
        print s
        print 'Non-alphebetical:', '"'+noalpha(s)+'"'
        print
            
    test_noalpha("Sentence (with [],{}, symbols %&#@), numbers 0987 and .!")
    test_noalpha("SentenceWithAlphabeticalCharactersOnly")
    
    def test_words(s):
        print s
        print 'words:', words(s)
        print
        
    s = """def words(s):
        '''Returns the list of the words in the string s'''
        noa = noalpha(s)
        for c in noa:
            s = s.replace(c, ' ')
        return s.split()"""
    test_words(s)
