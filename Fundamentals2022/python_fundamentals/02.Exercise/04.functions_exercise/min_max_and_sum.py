def min_max_and_sum(a):
    sum_num = 0
    int_list = []
    for i in a:
        sum_num += int(i)
        int_list.append(int(i))
    print(f"The minimum number is {min(int_list)}")
    print(f"The maximum number is {max(int_list)}")
    print(f"The sum number is: {sum_num}")


min_max_and_sum(input().split())


