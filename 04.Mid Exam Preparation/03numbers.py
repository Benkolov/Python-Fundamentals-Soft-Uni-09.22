def sorted_func(greater_number_than_average_sum):
    top_five_numbers = []
    for num in sorted(greater_number_than_average_sum)[::-1]:
        if len(top_five_numbers) < 5:
            top_five_numbers.append(num)
        else:
            break
    return " ".join([str(num) for num in top_five_numbers])


def numbers_func(num):
    average = sum(num) / len(num)
    greater_numbers = [num for num in num if num > average]

    if greater_numbers:
        print(sorted_func(greater_numbers))
    else:
        print('No')


numbers = list(map(int, input().split()))
numbers_func(numbers)
