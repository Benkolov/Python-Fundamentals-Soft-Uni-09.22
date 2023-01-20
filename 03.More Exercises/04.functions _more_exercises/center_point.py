# import math
#
#
# def center_point(x1, y1, x2, y2):
#     x = 0
#     y = 0
#     if abs(x1) < abs(x2):
#         x = x1
#     elif abs(x1) == abs(x2):
#         x = x1
#     else:
#         x = x2
#     if abs(y1) < abs(y2):
#         y = y1
#     elif abs(y1) == abs(y2):
#         y = y1
#     else:
#         y = y2
#     return f"({math.floor(x)}, {math.floor(y)})"
#
#
# print(center_point(float(input()), float(input()), float(input()), float(input())))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

coord_A = int(x1), int(y1)
coord_B = int(x2), int(y2)
coord_center = 0, 0


def distance(coord):
    d = abs(coord[0]) + abs(coord[1])
    return d


if distance(coord_A) > distance(coord_B):
    print(coord_B)
elif distance(coord_A) < distance(coord_B):
    print(coord_A)
else:
    print(coord_A)