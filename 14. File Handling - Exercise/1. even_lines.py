symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("./Files/text.txt", "r") as text_file:
    text = text_file.readlines()

for sentence in range(0, len(text), 2):
    current_sentence = text[sentence]
    for symbol in symbols_to_replace:
        current_sentence = current_sentence.replace(symbol, "@")

    print(*current_sentence.split()[::-1])
