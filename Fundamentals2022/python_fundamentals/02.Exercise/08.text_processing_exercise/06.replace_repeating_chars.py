text = input()

final_text = [1]

for i in text:

    if final_text[-1] == i:
        pass
    else:
        final_text.append(i)

final_text.remove(1)

print(''.join(final_text))

