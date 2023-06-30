sets_length = input().split()

first_set = set()
second_set = set()

first_set_length = int(sets_length[0])
second_set_length = int(sets_length[1])

for number in range(first_set_length):
    current_first_number = int(input())
    first_set.add(current_first_number)

for number in range(second_set_length):
    current_second_number = int(input())
    second_set.add(current_second_number)

for element in first_set.intersection(second_set):
    print(element)
