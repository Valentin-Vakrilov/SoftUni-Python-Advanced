matrix = []

for line in range(6):
    current_line = input().split()
    matrix.append(current_line)

position = input()
row = int(position[1])
col = int(position[4])

command = input()

while command != "Stop":
    current_command = command.split(", ")

    command_type = current_command[0]
    direction = current_command[1]

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    if command_type == "Create":
        value = current_command[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value
    elif command_type == "Update":
        value = current_command[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value
    elif command_type == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    elif command_type == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])

    command = input()

for line in matrix:
    print(*line)
