# this program calculates BMI body mass index

height = float(input("Enter the height in cm: "))
weight = float(input("Enter the weight: "))

bmi = (weight) / (height * height)

print("Your BMI is ", (bmi*10000))
if bmi < 0.0025:
    print("Thats ok")
else:
    print("You gonna die")

