line = input().split("|")

result = []

for current_line in line[::-1]:
    result.extend(current_line.split())

print(" ".join(result))
