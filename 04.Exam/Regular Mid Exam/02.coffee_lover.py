names_of_coffees = input().split()
number_commands = int(input())

for i in range(number_commands):
    command = input().split()
    current_command = command[0]
    if current_command == "Include":
        coffee = command[1]
        names_of_coffees.append(coffee)

    elif current_command == "Remove":
        data = command[1]
        number = int(command[2])
        for k in range(number):
            if data == "first":
                names_of_coffees.pop(0)
            elif data == "last":
                names_of_coffees.pop(-1)
    elif current_command == "Prefer":
        index1 = int(command[1])
        index2 = int(command[2])
        if index1 >= len(names_of_coffees) or index2 >= len(names_of_coffees):
            pass
        else:
            names_of_coffees[index1], names_of_coffees[index2] = names_of_coffees[index2], names_of_coffees[index1]

    elif current_command == "Reverse":
        names_of_coffees.reverse()


print("Coffees:")
print(" ".join(names_of_coffees))


