data = input()
final_data = ''
for i in data:
    final_data += chr(ord(i) + 3)

print(final_data)