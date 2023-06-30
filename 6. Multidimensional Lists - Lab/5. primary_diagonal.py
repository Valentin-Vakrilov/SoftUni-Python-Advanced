matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append(list(map(int, input().split())))

total = 0

for index in range(matrix_size):
    total += matrix[index][index]

print(total)
