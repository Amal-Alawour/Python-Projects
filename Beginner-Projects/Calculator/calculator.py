# Simple Calculator Project
# Created by Amal Alawour

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


print("Simple Calculator")
print("----------------")

num1 = float(input("Enter first number: "))
operator = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", add(num1, num2))

elif operator == "-":
    print("Result:", subtract(num1, num2))

elif operator == "*":
    print("Result:", multiply(num1, num2))

elif operator == "/":
    print("Result:", divide(num1, num2))

else:
    print("Invalid operation")
