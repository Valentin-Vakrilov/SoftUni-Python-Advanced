board_size = int(input())

board = []

for row in range(board_size):
    board.append(list(input()))

moves = [
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
]

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_max_attacks_position = []

    for current_row in range(board_size):
        for current_col in range(board_size):
            if board[current_row][current_col] == "K":
                attacks = 0

                for move in moves:
                    move_row = current_row + move[0]
                    move_col = current_col + move[1]

                    if 0 <= move_row < board_size and 0 <= move_col < board_size:
                        if board[move_row][move_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_max_attacks_position = [current_row, current_col]
                    max_attacks = attacks

    if knight_with_max_attacks_position:
        board[knight_with_max_attacks_position[0]][knight_with_max_attacks_position[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
