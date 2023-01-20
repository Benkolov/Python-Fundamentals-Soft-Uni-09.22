number = int(input())

shield = []
n = 1
while number > 0:
    a = 2 * (n ** 2)
    if a <= number:
        shield.append(a)
    else:
        shield.append(number)
    number -= a
    n += 1

print(shield)
