from functools import reduce


def operate(operator, *args):
    result = 0
    if operator == "+":
        result = reduce(lambda x, y: x + y, args)
    elif operator == "-":
        for num in args:
            result = reduce(lambda x, y: x - y, args)
    elif operator == "*":
        result = reduce(lambda x, y: x * y, args)
    elif operator == "/":
        result = reduce(lambda x, y: x / y, args)

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
