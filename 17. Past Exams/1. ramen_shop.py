from collections import deque

ramen_bowls = list(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while ramen_bowls and customers:
    current_ramen = int(ramen_bowls.pop())
    current_customer = int(customers.popleft())

    if current_ramen > current_customer:
        current_ramen -= current_customer
        ramen_bowls.append(current_ramen)
    elif current_ramen < current_customer:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if len(ramen_bowls) > 0:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen_bowls))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
