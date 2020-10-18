#rep takes as imput a list lst and a number k and returns a new list containing elements which are present in lst at least k times
def rep(lst, k):
    y = []
    for x in lst:
        if x not in y and lst.count(x) >= k:
            y.append(x)
    return y
print rep([1, 2, 1, 5, 3, 4, 2, 1, 3, 5, 6], 2)