import re

pattern = r"(@|#)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"

text = input()
mirror_words = []
matches = re.finditer(pattern, text)
count = 0
for match in matches:
    count += 1
    first_group = match.group(2)
    second_group = match.group(5)
    second_group_reversed = second_group[::-1]

    if first_group == second_group_reversed:
        mirror_words.append(f"{first_group} <=> {second_group}")

if count > 0:
    print(f"{count} word pairs found!")
else:
    print("No word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))


