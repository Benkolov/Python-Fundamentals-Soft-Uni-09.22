number_of_cities = int(input())

total_profit = 0

for i in range(1, number_of_cities + 1):
    name_of_the_city = input()
    income = float(input())
    expenses = float(input())
    if i % 3 == 0 and i % 5 != 0:
        profit = income - expenses * 1.5
        total_profit += profit
    elif i % 5 == 0:
        profit = income * 0.9 - expenses
        total_profit += profit
    else:
        profit = income - expenses
        total_profit += profit
    print(f"In {name_of_the_city} Burger Bus earned {profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")