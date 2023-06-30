row_len, col_len = list(map(int, input().split(", ")))

matrix = []

for row in range(row_len):
    matrix.append(list(map(int, input().split())))

for col in range(col_len):
    total = 0
    for row in range(row_len):
        total += matrix[row][col]
    print(total)
