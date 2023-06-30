numbers = tuple(map(float, input().split()))

unique_numbers = {}

for element in numbers:
    if element not in unique_numbers:
        unique_numbers[element] = 0
    unique_numbers[element] += 1

for keys, values in unique_numbers.items():
    print(f"{keys} - {values} times")
