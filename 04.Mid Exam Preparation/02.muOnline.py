data = input().split("|")

health = 100
bitcoins = 0
room = 0
is_made_it = True
for current_command in data:
    room += 1
    a = current_command.split()
    command = a[0]
    value = int(a[1])
    if command == "potion":
        if health + value > 100:
            print(f"You healed for {100 - health} hp.")
        else:
            print(f"You healed for {value} hp.")
        health += value
        if health > 100:
            health = 100
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            is_made_it = False
            break

if is_made_it:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
