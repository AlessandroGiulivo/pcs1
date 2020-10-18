#distinct(lst) returns a new list that contains the same elements of lst, but with no repetitions.
def distinct(lst):
    distinct = []
    for x in lst:
        if x not in distinct:
            distinct = distinct + [x]
    return distinct
    
print distinct([3, 1, 3, 2, 6, 6, 7, 7, 7, 7, 2, 8,7, 9])
print distinct(['a', 'ab', 'a', 'ab'])