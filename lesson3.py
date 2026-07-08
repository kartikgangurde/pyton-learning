#  User Input + Calculations 

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Sum:", first_number + second_number)
print("sub:", first_number - second_number)
print("mul:", first_number * second_number)

if second_number != 0:
    print("div:", first_number / second_number)
else:
    print("div: Cannot divide by zero")
