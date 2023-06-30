import sys

rows, cols = list(map(int, input().split()))

matrix = []
sub_matrix = []
max_sum = -sys.maxsize
current_sum = 0

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for current_row in range(rows-2):
    for current_col in range(cols-2):
        first_row = list(map(int, [matrix[current_row][current_col], matrix[current_row][current_col + 1],
                                   matrix[current_row][current_col + 2]]))
        second_row = list(map(int, [matrix[current_row + 1][current_col], matrix[current_row + 1][current_col + 1],
                                    matrix[current_row + 1][current_col + 2]]))
        third_row = list(map(int, [matrix[current_row + 2][current_col], matrix[current_row + 2][current_col + 1],
                             matrix[current_row + 2][current_col + 2]]))
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for row in sub_matrix:
    print(" ".join(list(map(str, row))))
