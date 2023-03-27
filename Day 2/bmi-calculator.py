print("##### BMI Calculator #######\n")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round((weight)/(height**2),3)

print("Your BMI is: " + str(bmi))
print(f"Your BMI is: {bmi}")