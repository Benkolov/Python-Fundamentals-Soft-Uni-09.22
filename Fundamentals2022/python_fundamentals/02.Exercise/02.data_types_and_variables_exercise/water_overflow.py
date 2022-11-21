number = int(input())

capacity = 0

for i in range(1, number + 1):
    current_number = int(input())
    if capacity + current_number > 255:
        print("Insufficient capacity!")
    else:
        capacity += current_number

print(capacity)