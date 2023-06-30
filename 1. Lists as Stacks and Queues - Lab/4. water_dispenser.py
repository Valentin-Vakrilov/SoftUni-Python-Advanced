from collections import deque

queue = deque()

quantity = int(input())

person = input()

while person != "Start":
    queue.append(person)
    person = input()

command = input()

while command != "End":
    if "refill" in command:
        splitted_command = command.split()
        quantity += int(splitted_command[1])
    else:
        needed_quantity = int(command)
        if len(queue) > 0:
            current_person = queue.popleft()
            if quantity >= needed_quantity:
                quantity -= needed_quantity
                print(f"{current_person} got water")
            else:
                print(f"{current_person} must wait")

    command = input()

print(f"{quantity} liters left")
