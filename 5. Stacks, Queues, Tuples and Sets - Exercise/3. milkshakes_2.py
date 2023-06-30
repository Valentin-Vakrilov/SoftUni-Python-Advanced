from collections import deque

chocolates = list(map(int, input().split(", ")))
milk = deque(map(int, input().split(", ")))

milkshakes = 0

while milkshakes < 5 and chocolates and milk:
    below_zero = False

    if chocolates[-1] <= 0:
        chocolates.pop()
        below_zero = True

    if milk[0] <= 0:
        milk.popleft()
        below_zero = True

    if below_zero:
        continue

    if chocolates[-1] == milk[0]:
        milkshakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        chocolates[-1] -= 5
        milk.append(milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
