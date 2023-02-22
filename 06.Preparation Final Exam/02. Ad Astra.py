import re

text = input()
pattern = r'\#([A-Z a-z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|([A-Z a-z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
result = re.findall(pattern, text)
calories = 0

items = []

for item in result:
    current_item = [el for el in item if el != '']
    items.append(current_item)
    calories += int(current_item[2])

number_of_days = int(calories / 2000)
print(f'You have food to last you for: {number_of_days} days!')

for data in items:
    product = data[0]
    date = data[1]
    current_calories = data[2]
    print(f'Item: {product}, Best before: {date}, Nutrition: {current_calories}')