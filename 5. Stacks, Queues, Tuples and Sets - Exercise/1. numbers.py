first_sequence = input().split()
second_sequence = input().split()

number_of_lines = int(input())

first_set = set()
second_set = set()

for item in first_sequence:
    first_set.add(item)

for item in second_sequence:
    second_set.add(item)

for line in range(number_of_lines):
    current_line = input()
    if "Add First" in current_line:
        result = current_line.split()[2:]
        for current_number in result:
            first_set.add(current_number)
    elif "Add Second" in current_line:
        result = current_line.split()[2:]
        for current_number in result:
            second_set.add(current_number)
    elif "Remove First" in current_line:
        result = current_line.split()[2:]
        for current_number in result:
            if current_number in first_set:
                first_set.remove(current_number)
    elif "Remove Second" in current_line:
        result = current_line.split()[2:]
        for current_number in result:
            if current_number in second_set:
                second_set.remove(current_number)
    elif "Check Subset" in current_line:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(", ".join(map(str, sorted(map(int, first_set)))))
print(", ".join(map(str, sorted(map(int, second_set)))))
