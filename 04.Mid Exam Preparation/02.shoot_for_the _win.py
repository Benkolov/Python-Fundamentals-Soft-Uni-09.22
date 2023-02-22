targets = list(map(int, input().split()))
index = input()

count = 0
while index != "End":
    current_index = int(index)
    if current_index < len(targets):
        for i in range(len(targets)):
            if i != current_index:
                if targets[i] != -1:
                    if targets[i] > targets[current_index]:
                        targets[i] -= targets[current_index]

                    elif targets[i] <= targets[current_index]:
                        targets[i] += targets[current_index]
        targets[current_index] = -1
        count += 1

    index = input()


targets = list(map(str, targets))
targets = " ".join(targets)
print(f"Shot targets: {count} -> {targets}")