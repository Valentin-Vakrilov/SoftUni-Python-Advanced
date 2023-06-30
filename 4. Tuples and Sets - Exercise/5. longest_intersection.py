number_of_lines = int(input())

longest_intersection = set()

for line in range(number_of_lines):
    current_line = input().split("-")
    first_set = set()
    second_set = set()

    first_range = current_line[0].split(",")
    first_range_start = int(first_range[0])
    first_range_end = int(first_range[1])
    for number in range(first_range_start, first_range_end+1):
        first_set.add(number)

    second_range = current_line[1].split(",")
    second_range_start = int(second_range[0])
    second_range_end = int(second_range[1])
    for number in range(second_range_start, second_range_end+1):
        second_set.add(number)

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {[num for num in longest_intersection]} with length {len(longest_intersection)}")
