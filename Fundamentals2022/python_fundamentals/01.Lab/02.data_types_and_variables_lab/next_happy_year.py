from itertools import permutations
number = tuple(map(int, input()))
myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))


for digit in list(myperm):
    if digit > number:
        result = ''.join(str(x) for x in digit)
        print(result)
        break


# year = int(input())
#
# is_happy_year = False
#
# while not is_happy_year:
#     year += 1
#     str_year = str(year)
#     set_year = set(str_year)
#     # for i in range(len(str_year)):
#     #     set_year.add(str_year[i])
#     is_happy_year = len(str_year) == len(set_year)
#
# print(year)

