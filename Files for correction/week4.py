#input positive integer
#if even divide by 2
#if odd multiply by 3 and add 1
#end when current value is 1

p = int(input("Please enter a positive integer: ")) # prompts person to enter a positive whole number

while p > 1:                # while loop created, while the number entered is greater than 1, loop will run
    if p % 2 == 0:          # if statement used to determine if number entered is even by calculating if there is a remainder when it is divided by 2 (%)
        p = p // 2
    elif p % 2 != 0:        # if the number is odd
        p = p * 3 + 1       # then it is multiplied by 3 and added to 1
    print(p, end=" ")       # numbers are printed
   