def perfect_number(num):
    aliquot_sum = 0
    for i in range(1, num):
        if num % i == 0:
            aliquot_sum += i

    if aliquot_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))