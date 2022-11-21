import re

pattern = r'^%(?P<customer>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^|$%.]*?(?P<price>[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)\$'

total_price = 0
while True:
    command = input()
    if command == "end of shift":
        break
    match = re.search(pattern, command)
    if match:
        customer = match[1]
        product = match[2]
        price = int(match[3]) * float(match[4])
        total_price += price
        print(f"{customer}: {product} - {price:.2f}")

print(f"Total income: {total_price:.2f}")
