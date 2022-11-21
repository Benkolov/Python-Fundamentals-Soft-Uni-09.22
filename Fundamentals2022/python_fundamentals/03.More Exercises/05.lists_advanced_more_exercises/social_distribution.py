people = list(map(int, input().split(",")))
min_sum = int(input())

is_equal = True

for i in range(len(people)):
    max_number = max(people)
    max_index = people.index(max_number)
    if people[i] < min_sum:
        diff = min_sum - people[i]
        people[i] += diff
        people[max_index] -= diff

if min(people) < min_sum:
    is_equal = False

if is_equal:
    print(people)
else:
    print("No equal distribution possible")