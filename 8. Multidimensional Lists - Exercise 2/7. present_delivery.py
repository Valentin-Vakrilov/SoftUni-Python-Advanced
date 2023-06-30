total_presents = int(input())
rows = int(input())

matrix = []
nice_kids = 0
nice_kids_received_presents = 0
santa_position = ""
row = ""
col = ""

for line in range(rows):
    current_line = input().split()
    matrix.append(current_line)

    if "S" in current_line:
        santa_position = (line, current_line.index("S"))
        row = santa_position[0]
        col = santa_position[1]

    if "V" in current_line:
        nice_kids += current_line.count("V")

command = input()

while command != "Christmas morning" and total_presents > 0:
    matrix[row][col] = "-"
    if command == "up":
        row -= 1
        if matrix[row][col] == "V":
            total_presents -= 1
            nice_kids_received_presents += 1
        elif matrix[row][col] == "C":
            matrix[row][col] = "-"
            if total_presents > 0 and matrix[row-1][col] == "V" or matrix[row-1][col] == "X":
                total_presents -= 1
                if matrix[row-1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row-1][col] = "-"
            if total_presents > 0 and matrix[row+1][col] == "V" or matrix[row+1][col] == "X":
                total_presents -= 1
                if matrix[row+1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row+1][col] = "-"
            if total_presents > 0 and matrix[row][col-1] == "V" or matrix[row][col-1] == "X":
                total_presents -= 1
                if matrix[row][col-1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col-1] = "-"
            if total_presents > 0 and matrix[row][col+1] == "V" or matrix[row][col+1] == "X":
                total_presents -= 1
                if matrix[row][col+1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col+1] = "-"
        matrix[row][col] = "-"

    elif command == "down":
        row += 1
        if matrix[row][col] == "V":
            total_presents -= 1
            nice_kids_received_presents += 1
        elif matrix[row][col] == "C":
            matrix[row][col] = "-"
            if total_presents > 0 and matrix[row-1][col] == "V" or matrix[row-1][col] == "X":
                total_presents -= 1
                if matrix[row-1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row-1][col] = "-"
            if total_presents > 0 and matrix[row + 1][col] == "V" or matrix[row + 1][col] == "X":
                total_presents -= 1
                if matrix[row+1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row+1][col] = "-"
            if total_presents > 0 and matrix[row][col-1] == "V" or matrix[row][col-1] == "X":
                total_presents -= 1
                if matrix[row][col-1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col-1] = "-"
            if total_presents > 0 and matrix[row][col+1] == "V" or matrix[row][col+1] == "X":
                total_presents -= 1
                if matrix[row][col+1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col+1] = "-"
        matrix[row][col] = "-"

    elif command == "left":
        col -= 1
        if matrix[row][col] == "V":
            total_presents -= 1
            nice_kids_received_presents += 1
        elif matrix[row][col] == "C":
            matrix[row][col] = "-"
            if total_presents > 0 and matrix[row-1][col] == "V" or matrix[row-1][col] == "X":
                total_presents -= 1
                if matrix[row-1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row-1][col] = "-"
            if total_presents > 0 and matrix[row+1][col] == "V" or matrix[row+1][col] == "X":
                total_presents -= 1
                if matrix[row+1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row+1][col] = "-"
            if total_presents > 0 and matrix[row][col-1] == "V" or matrix[row][col-1] == "X":
                total_presents -= 1
                if matrix[row][col-1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col-1] = "-"
            if total_presents > 0 and matrix[row][col + 1] == "V" or matrix[row][col + 1] == "X":
                total_presents -= 1
                if matrix[row][col+1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col+1] = "-"
        matrix[row][col] = "-"

    elif command == "right":
        col += 1
        if matrix[row][col] == "V":
            total_presents -= 1
            nice_kids_received_presents += 1
        elif matrix[row][col] == "C":
            matrix[row][col] = "-"
            if total_presents > 0 and matrix[row-1][col] == "V" or matrix[row-1][col] == "X":
                total_presents -= 1
                if matrix[row-1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row-1][col] = "-"
            if total_presents > 0 and matrix[row+1][col] == "V" or matrix[row+1][col] == "X":
                total_presents -= 1
                if matrix[row+1][col] == "V":
                    nice_kids_received_presents += 1
                matrix[row+1][col] = "-"
            if total_presents > 0 and matrix[row][col-1] == "V" or matrix[row][col-1] == "X":
                total_presents -= 1
                if matrix[row][col-1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col-1] = "-"
            if total_presents > 0 and matrix[row][col+1] == "V" or matrix[row][col+1] == "X":
                total_presents -= 1
                if matrix[row][col+1] == "V":
                    nice_kids_received_presents += 1
                matrix[row][col+1] = "-"
        matrix[row][col] = "-"

    if total_presents == 0:
        break

    command = input()

matrix[row][col] = "S"

if nice_kids - nice_kids_received_presents != 0:
    print("Santa ran out of presents!")

for i in matrix:
    print(" ".join(map(str, i)))

if nice_kids - nice_kids_received_presents == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_received_presents} nice kid/s.")
