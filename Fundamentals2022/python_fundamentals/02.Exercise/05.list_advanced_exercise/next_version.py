version = [int(i) for i in input().split('.')]
version[-1] += 1

for i in range(len(version) - 1, -1, -1):
    if version[i] > 9:
        version[i] = 0
        version[i - 1] += 1


# print(f'{version[0]}.{version[1]}.{version[2]}')
print('.'.join(str(i) for i in version))