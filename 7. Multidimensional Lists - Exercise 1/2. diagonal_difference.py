matrix_size = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []

for row in range(matrix_size):
    matrix.append(list(map(int, input().split())))

for index in range(matrix_size):
    primary_diagonal.append(int(matrix[index][index]))
    secondary_diagonal.append(int(matrix[index][matrix_size-1 - index]))

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
