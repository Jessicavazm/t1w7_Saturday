# This way you can import all functions inside math_operations and use them calling the module_name.function_name(). Here you import using IMPORT.
import math_operations

num1 = 15
num2 = 7

# You can keep adding  arguments and it will work because num1 and num2 are variables and the rest args are default.
result_add = math_operations.add(num1,num2, 1, 1, 1, 1)
print(result_add)

result_subtract = math_operations.subtract(num2, num1)
print(result_subtract)

result_multiply = math_operations.multiply(num1,num2)
print(result_multiply)

result_divide = math_operations.division(num1,num2)
print(result_divide)

# Another way to import, this way you don't need to type the (math_operations.), you can only type the function name, and you can also only import what you need, you don't need to import all the functions if not needed. Here you import using FROM and IMPORT. 

print("--------")
from math_operations import add, subtract, multiply, division
result_add = add(num1, num2)
print(result_add)

result_subtract = subtract(num1,num2)
print(result_subtract)

# Python's pre-defined modules, it's a good pratice to import all functions in the same line

import math, random

num1 = math.pow(3, 4)
print(num1)

num2 = math.sqrt(64)
print(num2)

# this gives you a random number, inside parameters you have start,stop and step values.
random_value = random.randrange(1, 10)
print(random_value)