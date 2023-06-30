with open("./Files/text.txt", "r") as text_file:
    text = text_file.readlines()

with open("./Files/output.txt", "a") as new_text_file:
    for line in range(len(text)):
        current_line = text[line]
        letters = 0
        punctuation_marks = 0
        for symbol in current_line:
            if symbol.isalpha():
                letters += 1
            elif symbol == " " or symbol == "\n":
                pass
            else:
                punctuation_marks += 1

        new_text_file.write(f"Line {line+1}: {current_line[:-1]} ({letters})({punctuation_marks})\n")
