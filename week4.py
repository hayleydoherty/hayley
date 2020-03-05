#input positive integer
#if even divide by 2
#if odd multiply by 3 and add 1
#end when current value is 1

p = int(input("Please enter a positive integer: "))

while p > 1:
    if p % 2 == 0:
        print(p, end=" ")
        p = p // 2
    elif p % 2 != 0:
        print(p, end=" ")
        p = p * 3 + 1