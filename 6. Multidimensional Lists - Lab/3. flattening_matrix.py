rows = int(input())

matrix = []

for _ in range(rows):
    matrix.extend(list(map(int, input().split(", "))))

print(matrix)
