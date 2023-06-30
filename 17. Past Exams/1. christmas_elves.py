from collections import deque

elf_energy = deque(map(int, input().split()))
number_of_materials = list(map(int, input().split()))

created_toys = 0
total_used_energy = 0
counter = 0

while elf_energy and number_of_materials:
    current_energy = elf_energy.popleft()
    if current_energy >= 5:
        current_material = number_of_materials.pop()
    else:
        continue

    counter += 1
    if current_energy >= current_material:
        if counter % 3 != 0:
            created_toys += 1
            current_energy -= current_material
            total_used_energy += current_material
            if counter % 5 == 0:
                created_toys -= 1
            else:
                current_energy += 1
            elf_energy.append(current_energy)

        elif counter % 3 == 0:
            current_material *= 2
            if current_energy >= current_material:
                created_toys += 2
                current_energy -= current_material
                total_used_energy += current_material
                if counter % 5 == 0:
                    created_toys -= 2
                else:
                    current_energy += 1
                elf_energy.append(current_energy)
            else:
                number_of_materials.append(int(current_material / 2))
                elf_energy.append(int(current_energy * 2))
    else:
        number_of_materials.append(current_material)
        elf_energy.append(current_energy * 2)

print(f"Toys: {created_toys}")
print(f"Energy: {int(total_used_energy)}")
if elf_energy:
    print(f"Elves left: {', '.join(map(str, elf_energy))}")
if number_of_materials:
    print(f"Boxes left: {', '.join(map(str, number_of_materials))}")
