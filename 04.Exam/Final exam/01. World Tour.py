trip = input()

while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(":")
    current_command = command[0]

    if current_command == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index <= len(trip):
            trip = trip[:index] + string + trip[index:]
        print(trip)

    elif current_command == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index <= end_index < len(trip):
            trip = trip[:start_index] + trip[end_index + 1:]
        print(trip)

    elif current_command == "Switch":
        old_string = command[1]
        new_string = command[2]
        trip = trip.replace(old_string, new_string)
        print(trip)

print(f"Ready for world tour! Planned stops: {trip}")