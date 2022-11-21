events = input().split("|")

energy = 100
coin = 100
is_completed = True

for event in events:
    current_even = event.split("-")
    type_event = current_even[0]
    number = int(current_even[1])
    if type_event == 'rest':
        temporary_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif type_event == "order":
        if energy >= 30:
            coin += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            if energy > 100:
                energy = 100
    else:
        if coin >= number:
            coin -= number
            print(f"You bought {type_event}.")
        else:
            print(f"Closed! Cannot afford {type_event}.")
            is_completed = False
            break

if is_completed:
    print("Day completed!")
    print(f"Coins: {coin}")
    print(f"Energy: {energy}")
