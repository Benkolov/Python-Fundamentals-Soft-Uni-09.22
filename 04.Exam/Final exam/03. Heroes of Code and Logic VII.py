number = int(input())

info_heroes = {}

for i in range(number):
    info = input().split()
    hero = info[0]
    hit_points = int(info[1])
    mana_points = int(info[2])
    info_heroes[hero] = {"hit points": hit_points, "mana points": mana_points}

while True:
    command = input()
    if command == "End":
        break

    command = command.split(" - ")
    current_command = command[0]
    hero = command[1]
    if current_command == "CastSpell":
        mp_needed = int(command[2])
        spell = command[3]
        if info_heroes[hero]["mana points"] >= mp_needed:
            info_heroes[hero]["mana points"] -= mp_needed
            print(f"{hero} has successfully cast {spell} and now has {info_heroes[hero]['mana points']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif current_command == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        info_heroes[hero]["hit points"] -= damage
        if info_heroes[hero]["hit points"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {info_heroes[hero]['hit points']} HP left!")
        else:
            del info_heroes[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif current_command == "Recharge":
        amount = int(command[2])
        old_mp = info_heroes[hero]['mana points']
        info_heroes[hero]['mana points'] += amount

        if info_heroes[hero]['mana points'] > 200:
            print(f"{hero} recharged for {200 - old_mp} MP!")
            info_heroes[hero]['mana points'] = 200
        else:
            print(f"{hero} recharged for {amount} MP!")

    elif current_command == "Heal":
        amount = int(command[2])
        old_hp = info_heroes[hero]['hit points']
        info_heroes[hero]['hit points'] += amount
        if info_heroes[hero]['hit points'] > 100:

            print(f"{hero} healed for {100 - old_hp} HP!")
            info_heroes[hero]['hit points'] = 100
        else:
            print(f"{hero} healed for {amount} HP!")

for heroes, data in info_heroes.items():
    print(f"{heroes}")
    print(f"  HP: {data['hit points']}")
    print(f"  MP: {data['mana points']}")
