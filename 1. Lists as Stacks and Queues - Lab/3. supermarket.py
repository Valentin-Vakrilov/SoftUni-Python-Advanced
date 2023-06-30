from collections import deque

queue = deque()

while True:
    people = input()
    if people == "Paid":
        print('\n'.join(queue))
        queue.clear()
    elif people == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(people)
