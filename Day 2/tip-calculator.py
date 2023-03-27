print("Welcome to tip calculator\n")
bill = int(input("What was the tal bill? "))
tip = int(input("What % tip would you like  give? "))
people = int(input("How many people o split the will? "))

bill_mas_tip = bill * tip / 100

print(f"Each person should pay {bill_mas_tip/people}")
