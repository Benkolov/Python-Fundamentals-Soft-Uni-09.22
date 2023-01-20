words = input().split()

final = ""

for word in words:
    final += word * len(word)

print(final)