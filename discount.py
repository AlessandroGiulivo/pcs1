#discount takes as imput an initial price and a discount percentage and returns the discounted price
def discount(price, discount_percentage):
    discounted_price = price - (price*discount_percentage/100.0)
    return discounted_price   
print discount(1000, 20)

print discount(50, 17)