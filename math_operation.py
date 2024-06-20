def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = 0 
    for each in args:
        difference -= each
    return difference

def multiply(*args):
    multiply_result = 1
    for each in args:
        multiply_result *= each
    return multiply_result

print(multiply(5, 4))