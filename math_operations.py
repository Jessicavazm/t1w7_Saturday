def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = args[0] 
    for each in args[1:]:
        difference -= each
    return difference

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