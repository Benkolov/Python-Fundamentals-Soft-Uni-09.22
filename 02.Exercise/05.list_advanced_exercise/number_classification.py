numbers = input().split(', ')

print(f"Positive: {', '.join(i for i in numbers if int(i) >= 0)}")
print(f"Negative: {', '.join(i for i in numbers if int(i) < 0)}")
print(f"Even: {', '.join(i for i in numbers if int(i) % 2 == 0)}")
print(f"Odd: {', '.join(i for i in numbers if int(i) % 2 != 0)}")
