sequences1 = input().split(', ')
sequences2 = input().split(', ')

# sequences = []
#
# for i in sequences1:
#     for k in sequences2:
#         if i in k and not i in sequences:
#             sequences.append(i)
#             break

sequences = [x for x in sequences1 if any(x in w for w in sequences2)]
print(sequences)

