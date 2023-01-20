def create_plants_data(plants, number):
    for i in range(number):
        data = input().split("<->")
        plant = data[0]
        rarity = data[1]

        if plant not in plants:
            plants[plant] = {'rarity': rarity, 'rating': []}
        else:
            plants[plant]['rarity'] += rarity

    return plants


def additional_plants_data(plants):

    while True:
        command = input().split(': ')
        if command[0] == "Exhibition":
            break

        data = command[1].split(" - ")
        plant = data[0]
        if plant not in plants:
            print('error')
            continue

        if command[0] == "Rate":
            rating = int(data[1])
            plants[plant]['rating'].append(rating)

        elif command[0] == "Update":
            new_rarity = int(data[1])
            plants[plant]['rarity'] = new_rarity

        elif command[0] == "Reset":
            plants[plant]['rating'].clear()

    return plants


def print_function(plants):
    print("Plants for the exhibition:")

    for dict_el in plants:
        if len(plants[dict_el]['rating']) > 0 and sum(plants[dict_el]['rating']) != 0:
            average_rating = sum(plants[dict_el]['rating']) / len(plants[dict_el]['rating'])
        else:
            average_rating = 0
        rarity = plants[dict_el]['rarity']
        print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plant_discovery(number):
    plants = {}

    create_plants_data(plants, number)
    additional_plants_data(plants)
    print_function(plants)


n = int(input())
plant_discovery(n)













