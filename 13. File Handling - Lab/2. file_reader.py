file_path = "./numbers.txt"

file = open(file_path, "r")

result = 0

for number in file:
    result += int(number)

print(result)
