numbers = input().split(", ")
numbers = list(map(int, numbers))
numbers2 = numbers.copy()
group = 0
while len(numbers2) > 0:
    group += 10
    list_of_numbers = []
    for i in numbers:
        if (group - 10) < int(i) <= group:
            list_of_numbers.append(i)
            numbers2.remove(i)

    print(f"Group of {group}'s: {list_of_numbers}")

