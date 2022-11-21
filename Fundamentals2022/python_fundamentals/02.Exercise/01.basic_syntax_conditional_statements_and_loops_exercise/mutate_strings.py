first_string = input()
second_string = input()

last_printed_string = first_string

for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string


# first_string = input()
# second_string = input()
#
# for i in range(len(first_string)):
#      if first_string[i] != second_string[i]:
#          first_string = first_string[:i] +
#          first_string[i:i + 1].replace(first_string[i], second_string[i], 1) +
#          first_string[i + 1:]
#          print(first_string)