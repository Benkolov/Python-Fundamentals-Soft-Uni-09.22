data = list(map(int, input().split("@")))
location = 0

while True:
    command = input()
    if command == "Love!":
        break

    current_command = command.split()
    number = int(current_command[1])
    location = location + number
    if location >= len(data):
        location = 0

    if data[location] > 0:
        data[location] -= 2
        if data[location] == 0:
            print(f"Place {location} has Valentine's day.")
    else:
        print(f"Place {data[location]} already had Valentine's day.")


print(f"Cupid's last position was {location}.")
if sum(data) == 0:
    print("Mission was successful.")
else:
    house_count = 0
    for i in data:
        if i > 0:
            house_count += 1
    print(f"Cupid has failed {house_count} places.")