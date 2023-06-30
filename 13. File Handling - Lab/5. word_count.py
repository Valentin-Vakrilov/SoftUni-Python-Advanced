words_dict = {}

with open("./words.txt", "r") as file:
    all_words = file.read().split()
    for new_word in all_words:
        words_dict[new_word] = 0

with open("./input.txt", "r") as file:
    for line in file:
        separated_words = line.split()
        for curr_word in separated_words:
            stripped_word = ""
            for index in range(len(curr_word)):
                if curr_word[index].isalpha():
                    stripped_word += curr_word[index].lower()
            if stripped_word in words_dict:
                words_dict[stripped_word] += 1

with open("./output.txt", "w") as file:
    sorted_words_dict = sorted(words_dict.items(), key=lambda x: -x[1])
    for key, value in sorted_words_dict:
        file.write(f"{key} - {value}\n")
