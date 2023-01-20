import math

number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())

total_bonus = 0
max_student_attendances = 0

for i in range(1, number_of_the_students + 1):
    student_attendances = int(input())
    if student_attendances > max_student_attendances:
        max_student_attendances = student_attendances
    bonus = student_attendances / number_of_the_lectures * (5 + additional_bonus)
    if bonus > total_bonus:
        total_bonus = bonus


print(f"Max Bonus: {math.ceil(total_bonus)}.")
print(f"The student has attended {max_student_attendances} lectures.")
