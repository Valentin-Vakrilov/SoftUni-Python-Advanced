matrix = []

white_position = ""
black_position = ""

for i in range(8):
    current_row = input().split()
    matrix.append(current_row)

    if "w" in current_row:
        white_position = [i, current_row.index("w")]

    if "b" in current_row:
        black_position = [i, current_row.index("b")]

white_row = white_position[0]
white_col = white_position[1]
black_row = black_position[0]
black_col = black_position[1]

moves_counter = 0

while True:
    if white_row - 1 >= 0:
        if white_row - 1 == black_row and white_col - 1 == black_col and white_col - 1 >= 0:
            print(f"Game over! White win, capture on {chr(97 + white_col - 1) + str(8 - (white_row - 1))}.")
            break
        elif white_row - 1 == black_row and white_col + 1 == black_col and white_col + 1 <= 7:
            print(f"Game over! White win, capture on {chr(97 + white_col + 1) + str(8 - white_row - 1)}.")
            break
        else:
            white_row -= 1
            if white_row == 0:
                print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_col) + '8'}.")
                break

    if black_row + 1 >= 0:
        if black_row + 1 == white_row and black_col - 1 == black_col and black_col - 1 >= 0:
            print(f"Game over! Black win, capture on {chr(97 + white_col - 1) + str(int(black_row + 1))}.")
            break
        elif black_row + 1 == white_row and black_col + 1 == white_col and black_col + 1 <= 7:
            print(f"Game over! Black win, capture on {chr(97 + white_col + 1) + str(int(black_row + 1))}.")
            break
        else:
            black_row += 1
            if black_position == 7:
                print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_col) + '1'}.")
                break
