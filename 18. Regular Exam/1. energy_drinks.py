from collections import deque

caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

total_caffeine = 300
caffeine_taken = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    current_sum = current_caffeine * current_energy_drink

    if current_sum <= total_caffeine:
        caffeine_taken += current_sum
        total_caffeine -= current_sum
    else:
        energy_drinks.append(current_energy_drink)
        if caffeine_taken >= 30:
            caffeine_taken -= 30
            total_caffeine += 30
        else:
            caffeine_taken = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_taken} mg caffeine.")
