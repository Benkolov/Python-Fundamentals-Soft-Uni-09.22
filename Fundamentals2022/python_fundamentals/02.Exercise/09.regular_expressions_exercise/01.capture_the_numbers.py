import re
pattern = '\d+'
text = input()

while True:
    if text:
        matches = re.findall(pattern, text)
        if matches:
            print(' '.join(matches), end=" ")
        text = input()
    else:
        break


