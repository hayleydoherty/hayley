# Hayley Doherty
# this programme is used to calculate a persons BMI

weight = float(input("Enter weight in kg: ")) # Person inputs their weight, float used as it may not be a whole number
height = float(input("Enter height in m: "))  # height is inserted here, again float used as it most likely won't be a whole number

#weight= 65.0
#height= 1.8

BMI = weight/(height**2)  # formula used here to calculate BMI based on the values that were input earlier
print("Your body mass index is", BMI, "based on the values provided.")