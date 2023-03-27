print("Welcome to the rollercoaster!")
height = int(input("Whats your height in cm? "))


if height > 120:
  print("You can ride in the rollercoaster!")
  age = int(input("How old are you? "))
  if age <= 12:
    print("pay $7.")
  elif age <= 18:
    print("pay $10.")
  else:
    print("pay $15.")
else:
  print("Sorry you have to grow taller before you can ride.")