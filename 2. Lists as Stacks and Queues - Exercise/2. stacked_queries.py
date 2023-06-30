number_of_inputs = int(input())

stack = []

for current_input in range(number_of_inputs):
    current_line = input().split()
    if current_line[0] == "1":
        stack.append(int(current_line[1]))
    elif current_line[0] == "2":
        if stack:
            stack.pop()
    elif current_line[0] == "3":
        if stack:
            print(max(stack))
    elif current_line[0] == "4":
        if stack:
            print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))
