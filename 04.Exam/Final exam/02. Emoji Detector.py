import re

pattern = r'(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)'
pattern_number = r'\d'

text = input()

all_numbers_in_text_as_strings = re.findall(pattern_number, text)
all_numbers_as_integer = [int(num_str) for num_str in all_numbers_in_text_as_strings]

threshold = 1
for num in all_numbers_as_integer:
    threshold *= num
print(f"Cool threshold: {threshold}")
emojis_to_print = []
emoji_count = 0
for match in re.finditer(pattern, text):
    emoji_count += 1
    data = match.groupdict()
    emoji = data['emoji']
    emoji_coolness = sum([ord(letter) for letter in emoji])
    if emoji_coolness >= threshold:
        emojis_to_print.append(f"{data['surr']}{data['emoji']}{data['surr']}")

print(f'{emoji_count} emojis found in the text. The cool ones are:')

# print("\n".join(emojis_to_print))
for emoji in emojis_to_print:
    print(emoji)



