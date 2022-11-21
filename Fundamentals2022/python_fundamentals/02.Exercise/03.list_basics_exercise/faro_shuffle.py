text = input().split()
count = int(input())

for shuffle in range(count):
    final_deck = []
    middle_of_the_deck = len(text) // 2
    left_part = text[0:middle_of_the_deck]
    right_part = text[middle_of_the_deck::]
    for index_of_the_card in range(len(left_part)):
        final_deck.append(left_part[index_of_the_card])
        final_deck.append(right_part[index_of_the_card])
    text = final_deck

print(text)