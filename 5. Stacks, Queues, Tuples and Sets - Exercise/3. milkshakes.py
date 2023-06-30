from collections import deque

chocolate = input().split(", ")
milk_cups = input().split(", ")

chocolate_stack = []
milk_cups_que = deque()

for chocolate_bar in chocolate:
    chocolate_stack.append(int(chocolate_bar))

for milk_cup in milk_cups:
    milk_cups_que.append(int(milk_cup))

milkshakes = 0

while milkshakes < 5 and chocolate_stack and milk_cups_que:
    if chocolate_stack[-1] <= 0 or milk_cups_que[0] <= 0:
        if chocolate_stack[-1] <= 0:
            chocolate_stack.pop()
        else:
            milk_cups_que.popleft()
        continue

    if chocolate_stack[-1] == milk_cups_que[0]:
        milkshakes += 1
        chocolate_stack.pop()
        milk_cups_que.popleft()
    else:
        milk_cups_que.append(milk_cups_que.popleft())
        chocolate_stack[-1] -= 5

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_stack:
    print(f"Chocolate: {', '.join(map(str, chocolate_stack))}")
else:
    print("Chocolate: empty")

if milk_cups_que:
    print(f"Milk: {', '.join(map(str, milk_cups_que))}")
else:
    print("Milk: empty")
