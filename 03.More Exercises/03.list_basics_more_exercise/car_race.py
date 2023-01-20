sequence_of_numbers = input().split()

left_car_time = 0
right_car_time = 0


middle = len(sequence_of_numbers) // 2
left_part = sequence_of_numbers[0:middle]
right_part = sequence_of_numbers[middle + 1::]

for time_left in left_part:
    if int(time_left) == 0:
        left_car_time *= 0.8
    else:
        left_car_time += int(time_left)
for time_right in right_part:
    if int(time_right) == 0:
        right_car_time *= 0.8
    else:
        right_car_time += int(time_right)

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
elif left_car_time > right_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
