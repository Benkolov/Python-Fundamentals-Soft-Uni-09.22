# string = input()
#
# my_list = []
#
# for i in string:
#     if 65 <= ord(i) <= 90:
#         my_list.append(string.index(i))
#
#
# print(my_list)

command = input()
index = []

for i in range(len(command)):
    if command[i].isupper():
        index.append(i)

print(index)