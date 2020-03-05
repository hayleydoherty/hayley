# this programme is used to calculate a persons BMI

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

#weight= 65.0
#height= 1.8

BMI = weight/(height**2)
print("Your body mass index is", BMI, "based on the values provided.")