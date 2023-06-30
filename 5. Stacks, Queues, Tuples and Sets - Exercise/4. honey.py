from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_bee <= current_nectar:
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            total_honey += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            total_honey += abs(current_bee * current_nectar)
        elif current_symbol == "/":
            if current_nectar > 0:
                total_honey += abs(current_bee / current_nectar)
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
