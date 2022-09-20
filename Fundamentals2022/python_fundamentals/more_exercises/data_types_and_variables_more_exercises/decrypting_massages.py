key = int(input())
num = int(input())

text = ""

for i in range(1, num + 1):
    current_string = input()
    text += chr(ord(current_string) + key)

print(text)