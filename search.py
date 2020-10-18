import words as ws

def wfreq(fname, searches, enc):
    '''Returns a dictionary that associates to each word in the list searches,
    its percentage frequency in the file having name fname. The file will be decoded
    using the encoding enc.'''
    wlst = ws.fwords(fname, enc)    # list of words in the file
    nw = len(wlst)    # total number of words in the file
    fd = {}           
    for w in searches:
        occ = wlst.count(w.lower())   # number of occurences
        # percentage frequency rounded to the third decimal digit
        fd[w] = round((float(occ)/nw)*100, 3)
    return fd


fname = 'alice.txt'
searches = ['alice','rabbit','turtle','king']
print 'Percentage frequency dictionary of the file "'+fname+'":'
print wfreq(fname, searches, 'utf8')


def scores(fnames, searches):
    '''Returns a dictionary that associates to each file in fnames, its score
    relative to the list of words searches. Files are decoded with the UTF-8 encoding.'''
    d = {}
    for fn in fnames:
        fd = wfreq(fn, searches, 'utf8')    # frequency dictionary
        d[fn] = round(sum(fd.values()), 3)  # score
    return d


fnames = ['alice.txt','holmes.txt','frankenstein.txt','prince.txt','mobydick.txt','treasure.txt']
searches = ['monster','horror','rabbit','crime','night']
print 'Scores with respect to:', searches
print scores(fnames, searches)


def print_table(rows):
    '''Prints a table whose rows are the elements of the list rows,
    which are assumed to be lists of equal length'''
    nc = len(rows[0])    # number of columns
    maxl = [0]*nc        # initializes a list of length equal to nc
    for r in rows:       # computes the maximum length of a column
        for i in range(nc):
            if len(str(r[i])) > maxl[i]:
                maxl[i] = len(str(r[i]))
    for r in rows:
        for i in range(nc):
            print str(r[i]).ljust(maxl[i]),  # left justification
        print

        
rows = [[''] + searches]    # the first row of the table
for fn in fnames:           # for each file, we have a row whose first element
    r = [fn]                # is the name of the file
    fd = wfreq(fn, searches, 'utf8')
    for w in searches:      # and then frequencies ordered as in the list searches
        r.append(fd[w])
    rows.append(r)  
print_table(rows)
    
        
    
