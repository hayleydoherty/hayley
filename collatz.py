# Hayley Doherty
# if even divide by 2
# if odd multiply by 3 and add 1
# end when value = 1

x = int(input("Please enter a positive integer: "))

iseven = True

while x > 1:
    if x % 2 == 0:
        print(x, end="")
        x = x // 2
    elif x % 2 == 1:
        print(x, end="")
        x = x * 3 + 1