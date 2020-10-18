#long_str takes as imput a list lst and a number k and returns the number of elements of lst which have lenght equal or greater then k
def long_str(lst, k):
    count = 0
    for s in lst:
        if len(s) >= k:
            count += 1
    return count

print long_str(['ornd', 'bye', 'ok', 'okokok'], 5)