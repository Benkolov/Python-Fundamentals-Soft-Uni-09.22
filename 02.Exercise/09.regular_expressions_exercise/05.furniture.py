import re

pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'
total_coast = 0
bought_furniture = []
command = input()
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_coast += int(quantity) * float(price)
    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_coast:.2f}")