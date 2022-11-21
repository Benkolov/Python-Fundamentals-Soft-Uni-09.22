command = input().split(", ")
count_of_beggars = int(input())

final_list = []
counter_of_index = 0
sums_list_as_digits = []

for element in command:
    sums_list_as_digits.append(int(element))

while counter_of_index < count_of_beggars:
    sum_for_current_beggar = 0
    for i in range(counter_of_index, len(sums_list_as_digits), count_of_beggars):
        sum_for_current_beggar += sums_list_as_digits[i]
    counter_of_index += 1
    final_list.append(sum_for_current_beggar)

print(final_list)


# collect = input()
# collectors = int(input())
#
# collect_list = list(map(int, collect.split(", ")))
#
# collector_final = []
#
# for i in range(collectors):
#     middle_list = collect_list[i::collectors]
#     collector_final.append(sum(middle_list))
#
# print(collector_final)








