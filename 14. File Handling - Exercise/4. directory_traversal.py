import os

directory = input()
file_types = {}
result = []

for file in os.listdir(directory):
    current_file = os.path.join(directory, file)

    if os.path.isfile(current_file):
        current_file_split = file.split(".")
        extension = current_file_split[2]
        filename = current_file_split[1]

        if extension not in file_types:
            file_types[extension] = []
        file_types[extension].append(filename)

    elif os.path.isdir(current_file):
        for sub_file in os.listdir(current_file):
            sub_current_file = os.path.join(current_file, sub_file)

            if os.path.isfile(sub_current_file):
                sub_current_file_split = sub_current_file.split(".")
                extension = sub_current_file_split[2]
                filename = sub_current_file_split[1]

                if extension not in file_types:
                    file_types[extension] = []
                filename = filename.split("\\")[2]
                file_types[extension].append(filename)

file_types = sorted(file_types.items(), key=lambda x: x[0])

for keys, values in file_types:
    result.append(f".{keys}\n")

    for value in sorted(values):
        result.append(f"- - - {value}.{keys}\n")

with open("./report.txt", "w") as text_file:
    text_file.write("".join(result))
