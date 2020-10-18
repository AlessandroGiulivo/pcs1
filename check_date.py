#check date takes as imput a string month and a number day which represent a date, and check wether the date is correct
def check_date(month, day):
    if day % 1.0 != 0:
        return False
    if day < 1:
        return False
    if month == 'feb':
        return day <= 28
    elif month in ['apr', 'jun', 'sep', 'nov']:
        return day <= 30
    elif month in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
        return day <= 31
    else: return False

    
print check_date('jan', 31)
print check_date('mar', 1.5)
print check_date('feb', 30)
print check_date('nov', 30)
print check_date('dec', 32)