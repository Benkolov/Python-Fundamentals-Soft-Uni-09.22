def character_in_range(a, b):
    final_list = []
    for i in range(ord(a) + 1, ord(b)):
        final_list.append(chr(i))

    return " ".join(final_list)


text1 = input()
text2 = input()

print(character_in_range(text1, text2))