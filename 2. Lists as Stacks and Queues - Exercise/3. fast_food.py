from collections import deque

food_quantity = int(input())

queue = deque()

orders = input().split()

for order in range(len(orders)):
    queue.append(int(orders[order]))

print(max(queue))

while queue:
    current_order = queue.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        queue.appendleft(current_order)
        break

if len(queue) > 0:
    orders_left = ""
    for order_left in range(len(queue)):
        orders_left += str(queue[order_left]) + " "
    print(f"Orders left: {orders_left[:-1]}")
else:
    print("Orders complete")
