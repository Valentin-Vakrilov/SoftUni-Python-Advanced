rows, cols = list(map(int, input().split()))

matrix = []

for _ in range(rows):
    matrix.append(list(map(str, input().split())))

while True:
    command = input().split()

    if command[0] == "END":
        break

    if command[0] == "swap" and len(command) == 5 \
    and int(command[1]) <= rows and int(command[3]) <= rows\
    and int(command[2]) <= cols and int(command[4]) <= cols\
    and int(command[1]) >= 0 and int(command[2]) >= 0 and int(command[3]) >= 0 and int(command[4]) >= 0:
        point_one = matrix[int(command[1])][int(command[2])]
        point_two = matrix[int(command[3])][int(command[4])]
        matrix[int(command[3])][int(command[4])] = point_one
        matrix[int(command[1])][int(command[2])] = point_two
        for row in matrix:
            print(" ".join(list(map(str, row))))

    else:
        print("Invalid input!")
