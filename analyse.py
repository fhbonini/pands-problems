# this program calculates BMI

altura = float(input("Enter the altura: "))
peso = float(input("Enter the peso: "))

bmi = altura * altura / peso

print("Your BMI is ", bmi)
if bmi < 0.035:
    print("Thats ok")
else:
    print("You gonna die")
