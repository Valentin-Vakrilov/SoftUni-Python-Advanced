def even_odd(*args):
    command = args[-1]
    filtered_list = []

    if command == "even":
        filtered_list = [num for num in args[:-1] if num % 2 == 0]
    elif command == "odd":
        filtered_list = [num for num in args[:-1] if num % 2 != 0]

    return filtered_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
