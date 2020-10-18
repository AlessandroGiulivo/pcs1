#occ takes as imout a list lst and an element v and returns a new list containing the positions where v is found in lst
def occ(lst, v):
    y = []
    for i in range(len(lst)):
        if lst[i] == v:
            y.append(i)
    return y
    
lst = ['red', 'blue', 'red', 'gray', 'yellow', 'red']
print occ(lst, 'red')