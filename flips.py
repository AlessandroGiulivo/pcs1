#flips(s), given a list s, returns a new list having the same lenght of s, but elements in the opposite order.
def flips(s):
    t = []
    for x in range(len(s)):
        t = t + [s[-x - 1]]
    return t
    
print flips([1, 2, 3])
print flips(['a', 'b', 'c'])