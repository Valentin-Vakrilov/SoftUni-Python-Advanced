def words_sorting(*args):
    words_dict = {}

    values_sum = 0

    for word in args:
        if word not in words_dict:
            words_dict[word] = 0
        for letter in word:
            words_dict[word] += ord(letter)
            values_sum += ord(letter)

    if values_sum % 2 == 0:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])

    result = ""

    for words, values in sorted_words:
        result += f"{words} - {values}\n"

    return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
