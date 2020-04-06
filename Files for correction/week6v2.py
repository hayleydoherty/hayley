# Hayley Doherty

def sqrt(n):
    root = n * 0.3 # approximate of sqrt
    while True:
        root2 = (root + (n / root)) / 2 # newtons eqn
        if abs(root - root2) < 0.00001:
            return root2
        root = root2    
        
print(sqrt(14.5))