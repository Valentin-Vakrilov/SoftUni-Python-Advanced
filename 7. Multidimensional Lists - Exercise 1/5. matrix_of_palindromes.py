rows, cols = list(map(int, input().split()))

for current_row in range(rows):
    palindrome_letter = 97 + current_row
    row = []
    for current_column in range(cols):
        middle_letter = palindrome_letter + current_column
        row.append(chr(palindrome_letter) + chr(middle_letter) + chr(palindrome_letter))

    print(" ".join(list(map(str, row))))
