data = input().split()
command = input()

while command != "3:1":
    current_command = command.split()
    if current_command[0] == 'merge':
        start = int(current_command[1])
        end = int(current_command[2])
        if start < 0:
            start = 0
        if end > len(data) - 1:
            end = len(data) - 1
        for index, string in enumerate(data):
            if index in range(start + 1, end + 1):
                data[start] += data[index]
        for index in range(end, start, - 1):
            data.pop(index)
    elif current_command[0] == 'divide':
        index = int(current_command[1])
        partitions = int(current_command[2])
        if partitions > len(data[index]):
            step = 1
        else:
            step = len(data[index]) // partitions
        divide_part = data.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                data.insert(index, divide_part[start::])
                break
            else:
                data.insert(index, divide_part[start: start + step:])
                start += step
                index += 1
    command = input()

print(" ".join(data))