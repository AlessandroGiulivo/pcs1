#crossing_over takes as imput two lists m and f and
#returns a new list where each element of m is followed by the element of f in its same position
def crossing_over(m, f):
    x = []
    for i in range(len(m)):
        x = x + [m[i], f[i]]
    return x
print crossing_over([1, 3, 5], [2, 4, 6])