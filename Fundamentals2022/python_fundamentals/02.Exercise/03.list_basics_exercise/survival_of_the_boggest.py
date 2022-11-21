nums = input().split(" ")
copy_nums = list(map(int, nums))
count = int(input())

for i in range(1, count + 1):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)


print(", ".join(nums))