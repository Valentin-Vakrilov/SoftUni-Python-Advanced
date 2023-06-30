matrix = []

water_deposit = False
metal_deposit = False
concrete_deposit = False

for rows in range(6):
    current_row = input().split()
    matrix.append(current_row)

    if "E" in current_row:
        position = [rows, current_row.index("E")]

row = int(position[0])
col = int(position[1])

commands = input().split(", ")

while commands:
    current_command = commands.pop(0)

    if current_command == "up":
        row -= 1
    elif current_command == "down":
        row += 1
    elif current_command == "left":
        col -= 1
    elif current_command == "right":
        col += 1

    if row < 0:
        row = 5
    elif row > 5:
        row = 0

    if col < 0:
        col = 5
    if col > 5:
        col = 0

    if matrix[row][col] == "W":
        water_deposit = True
        print(f"Water deposit found at {(row, col)}")
    elif matrix[row][col] == "M":
        metal_deposit = True
        print(f"Metal deposit found at {(row, col)}")
    elif matrix[row][col] == "C":
        concrete_deposit = True
        print(f"Concrete deposit found at {(row, col)}")
    elif matrix[row][col] == "R":
        print(f"Rover got broken at {(row, col)}")
        break

if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
