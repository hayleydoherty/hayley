# Hayley Doherty

def sqrt(n):
    root = n * 0.3 # approximate of sqrt
    for i in range(0, 20):   # goes through loop 20 times to get closest approx. of sqrt
        root = (root + (n / root)) / 2 # newtons eqn
        
    return root
print(sqrt(14.5))