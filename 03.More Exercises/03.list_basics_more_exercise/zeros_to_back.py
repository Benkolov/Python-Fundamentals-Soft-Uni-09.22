command = input().split(", ")

sort_list = list(command)
for i in command:
    if i == "0":
        sort_list.remove("0")
        sort_list.insert(len(sort_list) + 1, "0")

final_list = []
for i in sort_list:
    final_list.append(int(i))

print(final_list)