pokemons = list(map(int, input().split()))

count = 0
while len(pokemons) > 0:
    index = int(input())
    number = 0
    if index < 0:
        number = pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index >= len(pokemons):
        number = pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        number = pokemons[index]
        pokemons.pop(index)
    count += number
    for current_index, current_number in enumerate(pokemons):

        if current_number <= number:
            pokemons[current_index] += number
        else:
            pokemons[current_index] -= number


print(count)