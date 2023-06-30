matrix_size = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []

for row in range(matrix_size):
    matrix.append(list(map(str, input().split(", "))))

for current_row in range(matrix_size):
    for current_column in range(matrix_size):
        if current_row == current_column:
            primary_diagonal.append(matrix[current_row][current_column])
            secondary_diagonal.append(matrix[current_row][(matrix_size-1) - current_column])

print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum(map(int, primary_diagonal))}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum(map(int, secondary_diagonal))}")
