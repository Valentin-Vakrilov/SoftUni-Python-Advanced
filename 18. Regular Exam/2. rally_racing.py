size = int(input())

racing_number = input()

car_position = [0, 0]
row = car_position[0]
col = car_position[1]

matrix = []

tunnel_positions = []

for line in range(size):
    current_line = input().split()
    matrix.append(current_line)

    if "T" in current_line:
        tunnel_positions.append([line, current_line.index("T")])

command = input()

passed_kilometers = 0

finished = False

while command != "End" and not finished:
    passed_kilometers += 10

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    if matrix[row][col] == "T":
        passed_kilometers += 20
        matrix[row][col] = "."
        first_tunnel = tunnel_positions.index([row, col])
        tunnel_positions.pop(first_tunnel)
        car_position = tunnel_positions.pop()
        row = car_position[0]
        col = car_position[1]
        matrix[row][col] = "."
    elif matrix[row][col] == "F":
        finished = True
        break

    command = input()

matrix[row][col] = "C"

if finished:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {passed_kilometers} km.")

print(*["".join(row) for row in matrix], sep="\n")
