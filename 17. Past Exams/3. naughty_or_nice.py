def naughty_or_nice_list(kids_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []

    if args:
        for item in args:
            counter = 0
            name = ""
            naughty_or_nice = item[2:]
            for kid in range(len(kids_list)):
                current_kid = kids_list[kid]
                current_item = int(item[0])
                kid_name = int(current_kid[0])
                if current_item == kid_name:
                    counter += 1
                    name = current_kid[1]
                    index = int(kid)
            if counter == 1:
                if naughty_or_nice == "Naughty":
                    naughty_list.append(name)
                    kids_list.pop(index)
                elif naughty_or_nice == "Nice":
                    nice_list.append(name)
                    kids_list.pop(index)

    if kwargs:
        for key in kwargs:
            counter = 0
            naughty_or_nice = ""
            for child in range(len(kids_list)):
                current_child = kids_list[child]
                child_name = current_child[1]
                if key == child_name:
                    counter += 1
                    naughty_or_nice = kwargs[key]
                    index = int(child)
            if counter == 1:
                if naughty_or_nice == "Naughty":
                    naughty_list.append(key)
                    kids_list.pop(index)
                elif naughty_or_nice == "Nice":
                    nice_list.append(key)
                    kids_list.pop(index)

    while kids_list:
        current_kid = kids_list.pop(0)
        not_found_list.append(current_kid[1])

    result = ""

    if len(nice_list) > 0:
        result += f"Nice: {', '.join(nice_list)}\n"

    if len(naughty_list) > 0:
        result += f"Naughty: {', '.join(naughty_list)}\n"

    if len(not_found_list) > 0:
        result += f"Not found: {', '.join(not_found_list)}\n"

    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
