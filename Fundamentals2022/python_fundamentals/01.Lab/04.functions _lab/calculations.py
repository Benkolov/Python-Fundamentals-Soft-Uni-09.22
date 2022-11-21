text = input()
number1 = int(input())
number2 = int(input())


def calculator(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


print(calculator(text, number1, number2))
