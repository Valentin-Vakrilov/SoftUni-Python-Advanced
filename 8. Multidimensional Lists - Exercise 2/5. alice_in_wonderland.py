matrix_size = int(input())

matrix = []

alice_position = []
total_teabags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)

    if "A" in current_row:
        alice_position = [row, current_row.index("A")]
        matrix[row][alice_position[1]] = "*"

while total_teabags < 10:
    command = input()

    row = alice_position[0] + directions[command][0]
    col = alice_position[1] + directions[command][1]

    if not (0 <= row < matrix_size and 0 <= col < matrix_size):
        break

    alice_position = [row, col]
    position = matrix[row][col]
    matrix[row][col] = "*"

    if position == "R":
        break

    if position.isdigit():
        total_teabags += int(position)

if total_teabags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for item in matrix:
    print(" ".join(str(num) for num in item))
