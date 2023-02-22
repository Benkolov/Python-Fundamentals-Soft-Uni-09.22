message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split("|")
    current_command = command[0]

    if current_command == "Move":
        number_of_letters = int(command[1])
        left = message[:number_of_letters]
        right = message[number_of_letters:]
        message = right + left

    elif current_command == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    elif current_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
