buy_list = {}

while True:
    command = input()
    if command == "buy":
        break

    current_command = command.split()
    product = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])
    if product not in buy_list:
        buy_list[product] = price, quantity
    else:
        buy_list[product] = list(buy_list[product])
        buy_list[product][0] = price
        buy_list[product][1] += quantity

for product_name, total_price in buy_list.items():
    total_price = total_price[0] * total_price[1]
    print(f"{product_name} -> {total_price:.2f}")