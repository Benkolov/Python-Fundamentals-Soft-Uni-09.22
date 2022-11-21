current_string = input()
digit = []
text = []
for i in current_string:
    if i.isdigit():
        digit.append(i)
    else:
        text.append(i)

taken_digit = []
skip_digit = []

for index, number in enumerate(digit):
    if index % 2 == 0:
        taken_digit.append(number)
    else:
        skip_digit.append(number)
taken_text = ""
skip_text = ""

for i in range(len(text)):
    taken_text += text[:taken_digit[0]]
    skip_text += text[taken_digit[0]:skip_digit[0]]




