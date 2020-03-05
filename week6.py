# Hayley Doherty
# doesnt use the function

n = float(input('What number do you want to squareroot?'))
x = float(input('Estimate your answer'))
root = (x + (n / x)) / 2 

def sqrt():
    for i in range(0, 15):
        root = (root + (n / root)) / 2
        
    return root
print(root)