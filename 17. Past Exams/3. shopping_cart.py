def shopping_cart(*args):
    products = {"Soup": [], "Pizza": [], "Dessert": []}

    for element in args:
        if element == "Stop":
            break

        if element[0] == "Soup" and int(len(products["Soup"]) < 3) and element[1] not in products["Soup"]:
            products["Soup"].append(element[1])
        elif element[0] == "Pizza" and int(len(products["Pizza"]) < 4) and element[1] not in products["Pizza"]:
            products["Pizza"].append(element[1])
        elif element[0] == "Dessert" and int(len(products["Dessert"]) < 2) and element[1] not in products["Dessert"]:
            products["Dessert"].append(element[1])

    result = ""

    if len(products["Soup"]) == 0 and len(products["Pizza"]) == 0 and len(products["Dessert"]) == 0:
        result = "No products in the cart!"
    else:
        sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))

        for key, value in sorted_products:
            result += f"{key}:\n"
            sorted_values = sorted(value)
            for current_value in sorted_values:
                result += f" - {current_value}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
