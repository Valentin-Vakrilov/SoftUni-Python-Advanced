def rectangle(length, width):
    def area():
        return f"Rectangle area: {length * width}"

    def perimeter():
        return f"Rectangle perimeter: {length * 2 + width * 2}"

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return area() + '\n' + perimeter()


print(rectangle(2, 10))
