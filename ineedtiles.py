# This programme calculates  how many tiles you
# need to tile a wall or floor (m2)

length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

# length = 4
# width = 2

area = length * width

needed = area * 1.05

print("You need", needed, "tiles in metres squared,")

