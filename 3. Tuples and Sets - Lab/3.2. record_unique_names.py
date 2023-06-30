number_of_names = int(input())

unique_names = set()

for name in range(number_of_names):
    unique_names.add(input())

for current_name in unique_names:
    print(current_name)
