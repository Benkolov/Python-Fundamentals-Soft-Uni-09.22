data = input().split("!")


while True:
    command = input()
    if command == "Go Shopping!":
        break

    command = command.split()
    if len(command) == 3:
        current_command = command[0]
        item = command[1]
        new_item = command[2]
    else:
        current_command = command[0]
        item = command[1]
    if current_command == "Urgent":
        if item not in data:
            data.insert(0, item)
    elif current_command == 'Unnecessary':
        if item in data:
            data.remove(item)
    elif current_command == 'Correct':

        if item in data:
            item_index = data.index(item)
            data.pop(item_index)
            data.insert(item_index, new_item)
    elif current_command == 'Rearrange':
        if item in data:
            data.remove(item)
            data.append(item)


print(", ".join(data))