from collections import deque

vowels = deque(map(str, input().split()))
consonants = list(map(str, input().split()))

flowers_dict = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

word_found = False

while vowels and consonants:
    if word_found:
        break
    else:
        current_vowel = vowels.popleft()
        current_consonant = consonants.pop()

        for word in flowers_dict.keys():
            flowers_dict[word] = flowers_dict[word].replace(current_vowel, "")
            flowers_dict[word] = flowers_dict[word].replace(current_consonant, "")

            if flowers_dict[word] == "":
                print(f"Word found: {word}")
                word_found = True
                break


if not word_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(map(str, vowels))}")

if consonants:
    print(f"Consonants left: {' '.join(map(str, consonants))}")
