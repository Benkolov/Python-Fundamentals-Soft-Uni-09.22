import math


def factorial_division(num1, num2):
    x = math.factorial(num1)
    y = math.factorial(num2)
    z = x / y
    print(f"{z:.2f}")


factorial_division(int(input()), int(input()))