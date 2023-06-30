number_of_names = int(input())

names = []

for name in range(number_of_names):
    current_name = input()
    names.append(current_name)

unique = {name for name in names}

for name in unique:
    print(name)
