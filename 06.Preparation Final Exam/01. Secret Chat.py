message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(":|:")
    current_command = command[0]

    if current_command == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif current_command == "Reverse":
        substr = command[1]

        old_message = message
        message = message.replace(substr, "", 1)

        if old_message == message:
            print("error")
            continue

        substr_list = list(substr)
        substr_list.reverse()
        substr_reversed = "".join(substr_list)

        message += substr_reversed
        print(message)
    elif current_command == "ChangeAll":
        substr = command[1]
        replacement = command[2]
        message = message.replace(substr, replacement)
        print(message)


print(f"You have a new text message: {message}")