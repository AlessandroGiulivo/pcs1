#row(table, k) returns a list containing the values in the kth row of the table table.
def row(table, k):
    return table.splitlines()[k]

table = '''Milan;12;23
Rome;16;25
Naples;15;27
Florence;11;20'''

print row(table, 2)