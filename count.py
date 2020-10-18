#count takes as imput a list l and an element x and returns the number of times x is present in l
def count(l, x):
    c = 0
    for y in l:
        if y == x:
           c += 1
    return c