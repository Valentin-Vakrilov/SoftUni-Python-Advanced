from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

toys_dict = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic_level:
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()

    if current_material == 0 and current_magic_level == 0:
        continue
    elif current_material == 0:
        magic_level.appendleft(current_magic_level)
        continue
    elif current_magic_level == 0:
        materials.append(current_material)
        continue

    total_magic_level = current_material * current_magic_level
    if total_magic_level == 150:
        toys_dict["Doll"] += 1
    elif total_magic_level == 250:
        toys_dict["Wooden train"] += 1
    elif total_magic_level == 300:
        toys_dict["Teddy bear"] += 1
    elif total_magic_level == 400:
        toys_dict["Bicycle"] += 1
    elif total_magic_level < 0:
        materials.append(current_material + current_magic_level)
    elif total_magic_level > 0 and total_magic_level != 150 and total_magic_level != 250 and total_magic_level != 300 \
            and total_magic_level != 400:
        materials.append(current_material + 15)

if toys_dict["Doll"] > 0 and toys_dict["Wooden train"] > 0 or toys_dict["Teddy bear"] > 0 and toys_dict["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for toy in sorted(toys_dict.keys()):
    if toys_dict[toy] > 0:
        print(f"{toy}: {toys_dict[toy]}")
