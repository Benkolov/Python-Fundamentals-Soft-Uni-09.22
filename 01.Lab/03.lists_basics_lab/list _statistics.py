number = int(input())

negatives = list()
positives = list()
sum_of_negatives = 0

for i in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)
        sum_of_negatives += current_number

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum_of_negatives}')