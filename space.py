#space takes as imput a string s and a number k and
#returns a new string where each character of s is separated by a number k of spaces from the other
def space(s, k):
    t = ''
    for i in range(len(s) - 1):
        t = t + s[i] + ' ' * k
    return t + s[len(s) - 1]
    
print space('abc', 2)