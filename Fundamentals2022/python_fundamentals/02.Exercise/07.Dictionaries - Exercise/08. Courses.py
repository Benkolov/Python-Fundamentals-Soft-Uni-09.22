final_data = {}

while True:
    data = input()
    if data == "end":
        break
    courses, student = data.split(" : ")
    if courses not in final_data:
        final_data[courses] = []
        final_data[courses].append(student)
    else:
        final_data[courses] = list(final_data[courses])
        final_data[courses].append(student)

for key, value in final_data.items():
    print(f"{key}: {len(value)}")
    for student_name in value:
        print(f"-- {student_name}")