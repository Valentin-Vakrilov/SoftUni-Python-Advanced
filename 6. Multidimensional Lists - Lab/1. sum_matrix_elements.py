row_len, col_len = map(int, input().split(", "))

matrix = []

total_sum = 0

for row in range(row_len):
    matrix.append(list(map(int, input().split(","))))

for row_element in range(row_len):
    for col_element in range(col_len):
        total_sum += matrix[row_element][col_element]

print(total_sum)
print(matrix)
