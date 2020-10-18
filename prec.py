#prec(d1, m1, y1, d2, m2, y2) checks wether the date d1, m1, y1 (day, month, year) precedes, or is equal to, the date d2, m2, y2
def prec(h1, d1, m1, y1, h2, d2, m2, y2):
    return [y1, m1, d1, h1] <= [y2, m2, d2, h2]
    
print prec(3, 5, 5, 2006, 5, 5, 5, 2005)
print prec(13, 11, 2012, 2, 3, 2013)
print prec(13, 11, 2012, 27, 12, 2011)
print prec(1, 10, 2013, 1, 10, 2013)