import math
number = int(input())

is_prime = True

for i in range(1, int(math.sqrt(number) + 1)):
    if number % i == 0:
        is_prime = False
        break

if number == 1:
    is_prime = False


print(is_prime)

