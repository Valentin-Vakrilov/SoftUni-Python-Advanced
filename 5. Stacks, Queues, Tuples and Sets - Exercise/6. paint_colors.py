from collections import deque

sequence = deque(input().split())

main_colors = "red", "yellow", "blue"
secondary_colors = "orange", "purple", "green"

colors = []

while sequence:
    if len(sequence) > 1:
        first = sequence.popleft()
        second = sequence.pop()
        first_combination = first + second
        second_combination = second + first
        if first_combination in main_colors or first_combination in secondary_colors:
            colors.append(first_combination)
        elif second_combination in main_colors or second_combination in secondary_colors:
            colors.append(second_combination)
        else:
            first = first[:-1]
            second = second[:-1]
            if first:
                sequence.insert(len(sequence) // 2, first)
            if second:
                sequence.insert(len(sequence) // 2, second)
    else:
        first = sequence.popleft()
        if first in main_colors or first in secondary_colors:
            colors.append(first)

for colour in colors:
    if "orange" in colors:
        if "red" not in colors or "yellow" not in colors:
            colors.remove("orange")
    if "purple" in colors:
        if "red" not in colors or "blue" not in colors:
            colors.remove("purple")
    if "green" in colors:
        if "yellow" not in colors or "blue" not in colors:
            colors.remove("green")

print(colors)
