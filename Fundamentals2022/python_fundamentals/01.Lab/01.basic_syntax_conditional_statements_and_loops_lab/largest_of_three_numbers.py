import sys

f_num = int(input())
s_num = int(input())
t_num = int(input())

max_number = -sys.maxsize

if f_num > max_number:
    max_number = f_num
if s_num > max_number:
    max_number = s_num
if t_num > max_number:
    max_number = t_num

print(max_number)