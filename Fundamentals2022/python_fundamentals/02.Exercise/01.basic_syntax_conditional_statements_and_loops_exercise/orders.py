number_of_orders = int(input())

total_price = 0

for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_need_per_day = int(input())
    price_coffee = (days * capsules_need_per_day) * price_per_capsule
    if not 0.01 <= price_per_capsule <= 100 or not 1 <= days <= 31 or not 1 <= capsules_need_per_day <= 2000:
        continue
    else:
        total_price += price_coffee
        print(f"The price for the coffee is: ${price_coffee:.2f}")

print(f"Total: ${total_price:.2f}")