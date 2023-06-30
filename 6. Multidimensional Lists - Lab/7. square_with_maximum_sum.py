rows, cols = list(map(int, input().split(", ")))

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split(", "))))

max_sum = 0
current_sum = 0
first_row = ""
first_row_plus_one = ""
first_col = ""
first_col_plus_one = ""

for current_row in range(rows):
    for current_col in range(cols):
        if current_col + 1 in range(cols) and current_row + 1 in range(rows):
            current_sum = matrix[current_row][current_col] + matrix[current_row][current_col + 1] + \
                           matrix[current_row + 1][current_col] + matrix[current_row + 1][current_col + 1]
            if current_sum > max_sum:
                max_sum = current_sum
                first_row = matrix[current_row][current_col]
                first_row_plus_one = matrix[current_row][current_col + 1]
                first_col = matrix[current_row + 1][current_col]
                first_col_plus_one = matrix[current_row + 1][current_col + 1]

print(first_row, end=" ")
print(first_row_plus_one)
print(first_col, end=" ")
print(first_col_plus_one)
print(max_sum)
