
# Welcome message
print("Welcome to the simple calculator!")

# Input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on the operator
if operator == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operator == '/':
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
else:
    print("Invalid operator! Please enter one of +, -, *, /.")

# Goodbye message
print("Thank you for using the simple calculator!")
