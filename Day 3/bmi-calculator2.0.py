print("##### BMI Calculator #######\n")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round((weight)/(height**2),3)

print("Your BMI is: " + str(bmi))
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
  print("underweight")
elif bmi <= 25:
  print("normal")
elif bmi <= 30:
  print("obese")
else:
  print("clinically obese")