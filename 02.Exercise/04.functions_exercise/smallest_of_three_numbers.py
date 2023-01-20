import sys


def min_count(a, b, c):
    small = sys.maxsize
    if a < small:
        small = a
    if b < small:
        small = b
    if c < small:
        small = c
    return small


print(min_count(int(input()), int(input()), int(input())))
