number = int(input())

car_dict = {}

for i in range(number):
    cars = input().split("|")
    car = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])
    car_dict[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    current_command = command[0]
    car = command[1]
    if current_command == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > car_dict[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car]['fuel'] -= fuel
            car_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car_dict[car]['mileage'] > 100000:
            del car_dict[car]
            print(f"Time to sell the {car}!")

    elif current_command == "Refuel":
        fuel = int(command[2])
        a = car_dict[car]["fuel"]
        car_dict[car]['fuel'] += fuel
        if car_dict[car]['fuel'] > 75:
            car_dict[car]['fuel'] = 75
            print(f"{car} refueled with {75 - a} liters")
        else:
            print(f"{car} refueled with {fuel} liters")

    elif current_command == "Revert":
        kilometers = int(command[2])
        car_dict[car]['mileage'] -= kilometers
        if car_dict[car]['mileage'] < 10000:
            car_dict[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, data in car_dict.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")

