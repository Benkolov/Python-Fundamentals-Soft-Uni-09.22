cities = {}
while True:
    data = input()
    if data == "Sail":
        break

    data = data.split("||")
    city = data[0]
    people = int(data[1])
    gold = int(data[2])
    if city not in cities:
        cities[city] = {'people': people, "gold": gold}
    else:
        cities[city]["people"] += people
        cities[city]["gold"] += gold

while True:
    command = input()
    if command == "End":
        break

    command = command.split("=>")
    current_command = command[0]
    city = command[1]
    if current_command == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        cities[city]["people"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]['people'] <= 0 or cities[city]['gold'] <= 0:
            del cities[city]
            print(f'{city} has been wiped off the map!')

    elif current_command == "Prosper":
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            pass
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")


if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    # sorted_result = sorted(cities.items(), key=lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, data in cities.items():
        print(f"{city} -> Population: {data['people']} citizens, Gold: {data['gold']} kg")
