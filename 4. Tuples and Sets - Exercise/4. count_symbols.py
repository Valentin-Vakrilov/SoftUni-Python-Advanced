text = input()

chars = set()

for char in text:
    chars.add(f"{char}: {text.count(char)} time/s")

for character in sorted(chars):
    print(character)
