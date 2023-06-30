rows, cols = list(map(int, input().split()))

matrix = []

counter = 0

for _ in range(rows):
    matrix.append(input().split())

for current_row in range(rows-1):
    for current_column in range(cols-1):
        if matrix[current_row][current_column] == matrix[current_row][current_column + 1] == \
                matrix[current_row + 1][current_column] == matrix[current_row + 1][current_column + 1]:
            counter += 1

print(counter)
