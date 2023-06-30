matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append(list(map(int, input().split())))

command = input()

while command != "END":
    current_command = command.split()
    if 0 <= int(current_command[1]) <= matrix_size - 1 and 0 <= int(current_command[2]) <= matrix_size - 1:
        if current_command[0] == "Add":
            matrix[int(current_command[1])][int(current_command[2])] += int(current_command[3])
        elif current_command[0] == "Subtract":
            matrix[int(current_command[1])][int(current_command[2])] -= int(current_command[3])
    else:
        print("Invalid coordinates")

    command = input()

for current_row in matrix:
    print(" ".join(str(num) for num in current_row))
