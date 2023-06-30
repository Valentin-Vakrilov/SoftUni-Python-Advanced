number_of_commands = int(input())

cars = set()

for command in range(number_of_commands):
    current_command, plate = input().split(", ")
    if current_command == "IN":
        cars.add(plate)
    elif current_command == "OUT":
        cars.remove(plate)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
