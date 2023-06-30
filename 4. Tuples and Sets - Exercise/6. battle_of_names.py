number_of_names = int(input())

odd_set = set()
even_set = set()

for name in range(1, number_of_names+1):
    current_name = input()
    total_sum = 0
    for char in current_name:
        total_sum += ord(char)

    divided_result = int(total_sum / name)

    if divided_result % 2 == 0:
        even_set.add(divided_result)
    else:
        odd_set.add(divided_result)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

if odd_set_sum == even_set_sum:
    result = odd_set.union(even_set)
elif odd_set_sum > even_set_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(", ".join(str(num) for num in result))
