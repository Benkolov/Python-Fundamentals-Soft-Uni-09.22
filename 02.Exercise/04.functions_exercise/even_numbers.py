def even_numbers(num):
    if int(num) % 2 != 0:
        return False
    else:
        return True


even = filter(even_numbers, input().split())
even_list = []
for n in even:
    even_list.append(int(n))

print(even_list)