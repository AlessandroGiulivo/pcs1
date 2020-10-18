#product takes as imput a list of numbers and returns the value of their product
def product(vals):
    prod = 1
    for x in vals:
        prod = prod * x
    return prod
    
print product([2, 3, 6])