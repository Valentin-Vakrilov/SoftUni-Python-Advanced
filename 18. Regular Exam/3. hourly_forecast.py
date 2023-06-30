def forecast(*args):
    locations = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for location in args:
        location_name = location[0]
        weather = location[1]

        locations[weather].append(location_name)

    result = ""

    for key, value in locations.items():
        sorted_values = sorted(value)
        for current_value in sorted_values:
            result += f"{current_value} - {key}\n"

    return result


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
