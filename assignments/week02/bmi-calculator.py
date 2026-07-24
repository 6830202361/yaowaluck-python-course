# BMI Calculator

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("BMI:", format(bmi, ".1f"))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal weight")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")