people = int(input())
number_of_lift = list(map(int, input().split()))

for wagon in range(len(number_of_lift)):
    if people > 3:
        current_people = abs(4 - int(number_of_lift[wagon]))
        people -= current_people
        number_of_lift[wagon] += current_people
    else:

        number_of_lift[wagon] += people
        people = 0

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

elif sum(number_of_lift) != len(number_of_lift) * 4:
    print("The lift has empty spots!")


number_of_lift = list(map(str, number_of_lift))
print(" ".join(number_of_lift))

