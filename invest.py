#invest that takes as inputs an amount of money C, an annual interest rate i and a number of years n and
#returns the total amount of money obtained after having invested C for n years at an annual interest rate of i
def invest(C, i, n):
    return C*(1+i/100.00)**n 
    
print invest(1000, 10, 2)