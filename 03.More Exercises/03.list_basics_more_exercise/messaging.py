sequence_of_numbers = input().split(" ")
text = input()

message = []

for i in sequence_of_numbers:
    current_sum = 0
    for k in i:
        current_sum += int(k)

    current_sum %= len(text)

    message.append(text[current_sum])
    text = text.replace(text[current_sum], '', 1)

print(''.join(message))

