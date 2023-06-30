matrix_size = int(input())

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

bunny_position = []
best_direction = None
best_path = []
max_collected_eggs = 0

for row in range(matrix_size):
    current_row = input().split()

    if "B" in current_row:
        bunny_pos = [row, current_row.index("B")]

    matrix.append(current_row)

for key, values in directions.items():
    row, col = [(bunny_pos[0] + values[0]), (bunny_pos[1] + values[1])]
    path = []
    collected_eggs = 0

    while 0 <= row < matrix_size and 0 <= col < matrix_size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += values[0]
        col += values[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = path
        best_direction = key

print(best_direction)
for item in best_path:
    print(item)
print(max_collected_eggs)
