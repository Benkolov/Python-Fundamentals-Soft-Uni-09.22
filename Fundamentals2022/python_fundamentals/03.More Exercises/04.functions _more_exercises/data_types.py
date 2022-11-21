def data_types(a, b):
    if a == "int":
        return int(b) * 2
    elif a == "real":
        return f'{float(b) * 1.5:.2f}'
    else:
        return f'${b}$'


print(data_types(input(), input()))