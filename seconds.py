#seconds takes as imput a number of hours, a number of minutes and a number of seconds and returns the total number of seconds
def seconds(hh, mm, ss):
    sh = hh*3600
    sm = mm*60
    return ss + sh + sm
print seconds(2, 1, 11)

#or
def seconds(hh, mm, ss):
    return hh*3600 + mm*60 + ss
print seconds(2, 1, 11)

#or
def seconds(hh, mm, ss):
    return (hh*60 + mm)*60 + ss
print seconds(2, 1, 11)