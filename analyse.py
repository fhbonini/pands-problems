# this program calculates BMI

altura = float(input("Enter the altura: "))
peso = float(input("Enter the peso: "))

bmi = altura * altura / peso

print("Your BMI is ", bmi)
print(if(bmi >= 0.03,"ok vc vai viver"))
