def start_spring(**kwargs):
    types = {}

    for key, value in kwargs.items():
        if value not in types:
            types[value] = []
        types[value].append(key)

    result = ""

    types_sorted = sorted(types.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in types_sorted:
        sorted_values = sorted(value)
        result += f"{key}:\n"
        for value in sorted_values:
            result += f"-{value}\n"

    return result.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
