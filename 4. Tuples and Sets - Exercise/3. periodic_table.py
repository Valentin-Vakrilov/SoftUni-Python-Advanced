number_of_lines = int(input())

unique_elements = set()

for line in range(number_of_lines):
    current_line = input().split()
    for element in current_line:
        unique_elements.add(element)

for element in unique_elements:
    print(element)
