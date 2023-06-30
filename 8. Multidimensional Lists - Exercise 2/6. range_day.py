row = 5
col = 5

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

total_targets = 0
targets_hit = 0
targets_hit_coordinates = []

for current_row in range(row):
    line = input().split()
    matrix.append(line)

    if "x" in line:
        total_targets += line.count("x")

    if "A" in line:
        position = [current_row, line.index("A")]
        matrix[current_row][position[1]] = "."

number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()

    if current_command[0] == "move":
        direction = current_command[1]
        steps = int(current_command[2])

        curr_row = position[0] + (directions[direction][0] * steps)
        curr_col = position[1] + (directions[direction][1] * steps)

        if 0 <= curr_row < row and 0 <= curr_col < col:
            if matrix[curr_row][curr_col] == ".":
                position = matrix[curr_row][curr_col]
                matrix[curr_row][curr_col] = "A"

    if current_command[0] == "shoot":
        direction = current_command[1]

        curr_row = position[0] + directions[direction][0]
        curr_col = position[1] + directions[direction][1]

        while 0 <= curr_row < row and 0 <= curr_col < col:
            if matrix[curr_row][curr_col] == "x":
                targets_hit += 1
                targets_hit_coordinates.append([curr_row, curr_col])
                matrix[curr_row][curr_col] = "."

                if total_targets == targets_hit:
                    print(f"Training completed! All {targets_hit} targets hit.")
                break

            curr_row += directions[direction][0]
            curr_col += directions[direction][1]

if total_targets > targets_hit:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")

for item in targets_hit_coordinates:
    print(item)
