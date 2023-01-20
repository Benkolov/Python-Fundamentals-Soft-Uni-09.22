data = input().split(", ")

while True:
    command = input()
    if command == "End":
        break

    current_command = command.split(" - ")
    action = current_command[0]

    if action == "Add":
        phone = current_command[1]
        if phone not in data:
            data.append(phone)
    elif action == "Remove":
        phone = current_command[1]
        if phone in data:
            data.remove(phone)
    elif action == "Bonus phone":
        old_phone, new_phone = current_command[1].split(":")
        if old_phone in data:
            old_phone_index = data.index(old_phone)
            data.insert(old_phone_index + 1, new_phone)
    elif action == "Last":
        phone = current_command[1]
        if phone in data:
            data.remove(phone)
            data.append(phone)

print(", ".join(data))