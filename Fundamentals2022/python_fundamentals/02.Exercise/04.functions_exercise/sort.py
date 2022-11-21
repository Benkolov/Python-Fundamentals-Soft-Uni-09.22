def sort(num):
    int_list = []
    for i in num:
        int_list.append(int(i))
    return sorted(int_list)


print(sort(input().split()))