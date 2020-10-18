#average takes as imput a list of numbers and returns the value of the mathematical average of such integers
def average(vals):
    sum = 0.0
    for x in vals:
        sum = sum + x
    return sum / (len(vals))
    
print average([1, 2, 3, 4])