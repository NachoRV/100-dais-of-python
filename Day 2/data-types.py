# Data types
# String Integer float Boolean 

# String:

print("Hello"[4])
print("Hello" + "World")

#Integer

print(123)
print(123 + 1)
print(123_256)
print(123.256)

#Boolean

print(True)
print(False)

# type conversion
string = str(5)
print(type(string))
print(int(string))
print(float(string))

input_number = input("Enter a number of 2 digits: ")
num_one = input_number[0]
num_two = input_number[1]

sum_number = int(num_one) + int(num_two)

print(sum_number)
