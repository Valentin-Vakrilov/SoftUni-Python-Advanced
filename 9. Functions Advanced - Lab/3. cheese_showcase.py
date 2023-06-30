def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for keys, values in sorted_cheeses:
        sorted_values = sorted(values, reverse=True)
        result += keys + '\n'
        result += '\n'.join(str(num) for num in sorted_values) + '\n'

    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

