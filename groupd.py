#groupd(lst) takes a list lst of integers as input such that the first three integers in the list represent a date,
#the second three represent a second date, the next three another date, and so on,
#modifies the list lst by grouping each triple in a string (separating the numbers with the character '/').
#We assume that the list lst has a length divisible by 3.

def groupd(lst):
    for x in range((len(lst))/3):
        lst[x:x+3] = [str(lst[x]) + '/' + str(lst[x+1]) + '/' + str(lst[x+2])]
    return lst
        
print groupd([1, 2, 2013, 3, 9, 2011, 10, 11, 2000])