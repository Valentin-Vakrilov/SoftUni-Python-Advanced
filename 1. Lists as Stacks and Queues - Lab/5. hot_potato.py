from collections import deque

queue = deque()

kids = input().split()

while len(kids) > 0:
    current_kid = kids.pop()
    queue.appendleft(current_kid)

toss = int(input())

counter = 1

while len(queue) > 1:
    removed_kid = queue.popleft()
    if counter == toss:
        print(f"Removed {removed_kid}")
        counter = 1
    else:
        counter += 1
        queue.append(removed_kid)

print(f"Last is {queue.popleft()}")
