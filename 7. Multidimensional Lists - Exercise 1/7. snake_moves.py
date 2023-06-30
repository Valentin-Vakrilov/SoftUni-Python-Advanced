rows, cols = list(map(int, input().split()))

string = input()
matrix = []
index_counter = 0

for current_row in range(rows):
    row = ""
    for current_col in range(cols):
        row += string[index_counter % len(string)]
        index_counter += 1

    if current_row % 2 == 0:
        matrix.append(row)
    else:
        matrix.append(row[::-1])

for item in matrix:
    print("".join(list(map(str, item))))
