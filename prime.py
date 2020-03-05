# Hayley 
# Check if a number is prime

p = 13 * 17
m = 2

while m < p:
    if p % m == 0:
        print(m , "divides", p, "and therefore", p, "is not prime.")
    m = m + 1