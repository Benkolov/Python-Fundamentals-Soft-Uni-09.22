budget = float(input())
one_kg_flour_price = float(input())

breads = 0
colored_eggs_counter = 0

eggs_price = one_kg_flour_price * 0.75
milk_price = (one_kg_flour_price * 1.25) / 4

one_bread_price = eggs_price + one_kg_flour_price + milk_price

while budget >= one_bread_price:
    budget -= one_bread_price
    breads += 1
    colored_eggs_counter += 3
    if breads % 3 == 0:
        colored_eggs_counter -= (breads - 2)


print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")




# def loss_eggs(x):
#     if (x == 0):
#         return 0
#     else:
#         return 3 * x - 2 + loss_eggs(x - 1)
#
#
# budget = float(input())
# flour_price = float(input())
#
# price_per_bread = flour_price * (1 + .75 + 1.25 / 4)
#
# coun_bread = int(budget // price_per_bread)
#
# count_color_eggs = coun_bread * 3 - loss_eggs(int(coun_bread // 3))
#
# money_left = budget - coun_bread * price_per_bread
#
# print(f"You made {coun_bread} loaves of Easter bread! Now you have {count_color_eggs} eggs and {money_left:.2f}BGN left.")