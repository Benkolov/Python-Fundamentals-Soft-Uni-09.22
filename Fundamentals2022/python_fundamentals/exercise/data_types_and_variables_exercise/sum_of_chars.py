number = int(input())

count = 0

for i in range(1, number + 1):
    char = input()
    count += ord(char)

print(f"The sum equals: {count}")
