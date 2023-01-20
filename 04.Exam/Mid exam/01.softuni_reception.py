employee_efficiency_per_hour = int(input()) + int(input()) + int(input())
students_count = int(input())

needed_time = 0
count = 0
while students_count != 0:
    if students_count < employee_efficiency_per_hour:
        needed_time += 1
        students_count = 0
    else:
        students_count -= employee_efficiency_per_hour
        needed_time += 1
        count += 1
    if count % 3 == 0 and students_count != 0:
        needed_time += 1


print(f"Time needed: {needed_time}h.")
