count = int(input())
final_data = {}
for i in range(count):
    student = input()
    grade = float(input())
    if student not in final_data:
        final_data[student] = []
        final_data[student].append(grade)
    else:
        final_data[student].append(grade)


for name, average_grade in final_data.items():
    average_grade = sum(average_grade) / len(average_grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
