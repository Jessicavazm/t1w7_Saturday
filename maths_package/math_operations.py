def multiply(*args):
    multiply_result = 1
    for each in args:
        multiply_result *= each
    return multiply_result

def division(a,b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

print(multiply(5, 4))