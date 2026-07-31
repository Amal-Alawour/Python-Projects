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


def calculator():

    while True:

        print("\nSimple Calculator")
        print("----------------")
        print("Choose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        operator = input("Enter choice: ")

        if operator == "5":
            print("Calculator closed.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Please enter valid numbers.")
            continue


        if operator == "1":
            print("Result:", add(num1, num2))

        elif operator == "2":
            print("Result:", subtract(num1, num2))

        elif operator == "3":
            print("Result:", multiply(num1, num2))

        elif operator == "4":
            print("Result:", divide(num1, num2))

        else:
            print("Invalid operation")


calculator()
