matrix_size = int(input())

matrix = []

for rows in range(matrix_size):
    matrix.append(list(map(str, input())))

searched_symbol = input()

searched_symbol_found = False

for current_row in range(matrix_size):
    for current_col in range(matrix_size):
        if matrix[current_row][current_col] == searched_symbol:
            searched_symbol_found = True
            print((current_row, current_col))
            break

    if searched_symbol_found:
        break

if not searched_symbol_found:
    print(f"{searched_symbol} does not occur in the matrix")
