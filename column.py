#column(table, k) returns a list containing the values in the kth column of the table table.
def column(table, k):
    l = []
    for e in table.splitlines():
        e = e.split(';')
        l.append(e[k])
    return l
table = '''Milan;12;23
Rome;16;25
Naples;15;27
Florence;11;20'''
print column(table, 1)