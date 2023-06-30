from collections import deque

eggs = deque(input().split(", "))
paper = list(map(str, input().split(", ")))

filled_boxes = 0

while eggs and paper:
    current_egg = int(eggs.popleft())

    if current_egg > 0:
        if current_egg == 13:
            paper[0], paper[-1] = paper[-1], paper[0]
        else:
            current_paper = int(paper.pop())
            if current_egg + current_paper <= 50:
                filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(eggs)}")
elif paper:
    print(f"Pieces of paper left: {', '.join(paper)}")
