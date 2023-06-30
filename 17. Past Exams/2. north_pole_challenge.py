rows, cols = list(map(int, input().split(", ")))

matrix = []
position = ""
row = ""
col = ""
collected_all = False

christmas_decorations = 0
gifts = 0
cookies = 0
collected_christmas_decorations = 0
collected_gifts = 0
collected_cookies = 0

for line in range(rows):
    current_row = input().split()
    matrix.append(current_row)

    if "Y" in current_row:
        position = [line, current_row.index("Y")]
        row = position[0]
        col = position[1]

    if "D" in current_row:
        for symbol in current_row:
            if symbol == "D":
                christmas_decorations += 1

    if "G" in current_row:
        for symbol in current_row:
            if symbol == "G":
                gifts += 1

    if "C" in current_row:
        for symbol in current_row:
            if symbol == "C":
                cookies += 1

command = input()

while command != "End" and not collected_all:
    current_command = command.split("-")
    direction = current_command[0]
    steps = int(current_command[1])

    matrix[row][col] = "x"

    if direction == "up":
        for step in range(1, steps+1):
            row -= 1
            if row < 0:
                row = rows - 1
            elif row > rows - 1:
                row = 0

            if matrix[row][col] == "D":
                collected_christmas_decorations += 1
            elif matrix[row][col] == "G":
                collected_gifts += 1
            elif matrix[row][col] == "C":
                collected_cookies += 1

            matrix[row][col] = "x"

    elif direction == "down":
        for step in range(1, steps+1):
            row += 1
            if row < 0:
                row = rows - 1
            elif row > rows - 1:
                row = 0

            if matrix[row][col] == "D":
                collected_christmas_decorations += 1
            elif matrix[row][col] == "G":
                collected_gifts += 1
            elif matrix[row][col] == "C":
                collected_cookies += 1

            matrix[row][col] = "x"

    elif direction == "left":
        for step in range(1, steps+1):
            col -= 1
            if col < 0:
                col = cols - 1
            elif col > cols - 1:
                col = 0

            if matrix[row][col] == "D":
                collected_christmas_decorations += 1
            elif matrix[row][col] == "G":
                collected_gifts += 1
            elif matrix[row][col] == "C":
                collected_cookies += 1

            matrix[row][col] = "x"

    elif direction == "right":
        for step in range(1, steps+1):
            col += 1
            if col < 0:
                col = cols - 1
            elif col > cols - 1:
                col = 0

            if matrix[row][col] == "D":
                collected_christmas_decorations += 1
            elif matrix[row][col] == "G":
                collected_gifts += 1
            elif matrix[row][col] == "C":
                collected_cookies += 1

            matrix[row][col] = "x"

    if christmas_decorations == collected_christmas_decorations and collected_gifts == gifts and \
            collected_cookies == cookies:
        collected_all = True
        break

    command = input()

matrix[row][col] = "Y"

if collected_all:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {collected_christmas_decorations} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")

for i in matrix:
    print(" ".join(map(str, i)))
