
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

def get_user_input():
    operation = input("Enter operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        print ("Invalid operation!")
        return None, None, None
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return operation, a, b

def main():
    while True:
        operation, num1, num2 = get_user_input()
        result = 0
        if operation is None:
            return 0
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        else:
            result = division(num1, num2)

        print(f"The result is, {result}")

        next_calculation = input("Would you like to perform another calculation? Enter (yes/no): ")
        if next_calculation.lower() != "yes":
            break

main()
