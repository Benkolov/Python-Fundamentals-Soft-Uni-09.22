import re

count_of_inputs = int(input())

pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for i in range(count_of_inputs):
    command = input()
    matches = re.findall(pattern, command)
    if len(matches) > 0:
        com = matches[0][0]
        message = matches[0][1]
        print(f"{com}:", end=" ")
        for i in message:
            print(ord(i), end=" ")
    else:
        print(f"\nThe message is invalid")
