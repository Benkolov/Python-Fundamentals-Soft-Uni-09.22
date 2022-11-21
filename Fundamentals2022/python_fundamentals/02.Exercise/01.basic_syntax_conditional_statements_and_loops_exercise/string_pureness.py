n = int(input())

for i in range(1, n + 1):
    current_string = input()
    # x = current_string.rfind(".")
    # y = current_string.rfind(",")
    # z = current_string.rfind("_")
    # if x >= 0 or y >= 0 or z >= 0:
    #     print(f"{current_string} is not pure!")
    # else:
    #     print(f"{current_string} is pure.")
    if ',' in current_string or '.' in current_string or '_' in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")