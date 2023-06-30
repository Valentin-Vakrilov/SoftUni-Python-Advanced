from collections import deque

seats = list(map(str, input().split(", ")))

first_sequence = deque(map(int, input().split(", ")))
second_sequence = list(map(int, input().split(", ")))

matched_seats = []
rotations = 0

while rotations < 10 and len(matched_seats) < 3:
    rotations += 1

    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    letter = chr(first_number + second_number)

    first_combination = str(first_number) + letter
    second_combination = str(second_number) + letter

    if first_combination in seats and first_combination not in matched_seats:
        matched_seats.append(first_combination)
    elif second_combination in seats and second_combination not in matched_seats:
        matched_seats.append(second_combination)
    else:
        first_sequence.append(first_number)
        second_sequence.insert(0, second_number)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
