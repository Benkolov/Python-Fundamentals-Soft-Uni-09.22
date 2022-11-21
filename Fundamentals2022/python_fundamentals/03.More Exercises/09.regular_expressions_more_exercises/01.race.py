import re

pattern_name = r'(?P<name>[A-Za-z])'
pattern_digit = r'(?P<digit>[0-9])'

players = input().split(", ")
info = {}
while True:
    command = input()
    if command == 'end of race':
        break

    name = ''.join(re.findall(pattern_name, command))
    digit = re.findall(pattern_digit, command)
    digit = sum([int(i) for i in digit])
    if name in players:
        if name not in info:
            info[name] = digit
        else:
            info[name] += digit
    else:
        pass

sorted_info = sorted(info.items(), key=lambda k: -k[1])
print(f"1st place: {sorted_info[0][0]}")
print(f"2nd place: {sorted_info[1][0]}")
print(f"3rd place: {sorted_info[2][0]}")



