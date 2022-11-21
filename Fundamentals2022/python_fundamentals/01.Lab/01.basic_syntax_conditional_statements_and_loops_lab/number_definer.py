number = float(input())

result = None

if number == 0:
    result = "zero"
elif 1 <= number <= 1000000:
    result = "positive"
elif 0 < number < 1:
    result = "small positive"
elif number > 1000000:
    result = "large positive"
else:
    if abs(number) < 1:
        result = "small negative"
    elif abs(number) > 1000000:
        result = "large negative"
    else:
        result = "negative"

# print(type(result))
print(result)
