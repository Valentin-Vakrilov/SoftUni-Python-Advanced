first_player, second_player = input().split(", ")

matrix = []

for _ in range(6):
    current_row = input().split()
    matrix.append(current_row)

first_player_rest = 0
second_player_rest = 0
iterations = 0

while True:
    coordinates = input()

    if iterations % 2 == 0:
        current_player = first_player
    else:
        current_player = second_player

    iterations += 1

    if current_player == first_player and first_player_rest > 0:
        first_player_rest -= 1
        continue
    elif current_player == second_player and second_player_rest > 0:
        second_player_rest -= 1
        continue

    matrix_coordinates = ""

    for symbol in range(len(coordinates)):
        current_symbol = coordinates[symbol]
        if current_symbol.isdigit():
            matrix_coordinates += current_symbol

    row = int(matrix_coordinates[0])
    col = int(matrix_coordinates[1])

    if matrix[row][col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        if current_player == first_player:
            print(f"{current_player} is out of the game! The winner is {second_player}.")
        else:
            print(f"{current_player} is out of the game! The winner is {first_player}.")
        break
    elif matrix[row][col] == "W":
        if current_player == first_player:
            first_player_rest += 1
            print(f"{current_player} hits a wall and needs to rest.")
        else:
            second_player_rest += 1
            print(f"{current_player} hits a wall and needs to rest.")
