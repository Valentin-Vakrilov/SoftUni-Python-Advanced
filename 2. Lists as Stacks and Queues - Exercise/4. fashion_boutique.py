clothes = input().split()

rack_capacity = int(input())

stack = []

racks = 1

for cloth in range(len(clothes)):
    stack.append(int(clothes[cloth]))

current_sum = 0

while stack:
    current_cloth = stack.pop()
    if current_cloth + current_sum > rack_capacity:
        racks += 1
        stack.append(current_cloth)
        current_sum = 0
    else:
        current_sum += current_cloth

print(racks)
