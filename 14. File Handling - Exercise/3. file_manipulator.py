import os

command = input()

while command != "End":
    current_command = command.split("-")

    if current_command[0] == "Create":
        file = open(f"./Files/{current_command[1]}", "w")
        file.close()

    elif current_command[0] == "Add":
        with open(f"./Files/{current_command[1]}", "a") as file:
            file.write(f"{current_command[2]}\n")

    elif current_command[0] == "Replace":
        try:
            with open(f"./Files/{current_command[1]}", "r") as read_file:
                text = read_file.readlines()

            with open(f"./Files/{current_command[1]}", "w") as write_file:
                for line in range(len(text)):
                    current_line = text[line]
                    current_line = current_line.replace(current_command[2], (current_command[3]))
                    write_file.write(current_line)

        except FileNotFoundError:
            print("An error occurred")

    elif current_command[0] == "Delete":
        try:
            os.remove(f"./Files/{current_command[1]}")

        except FileNotFoundError:
            print("An error occurred")

    command = input()
