string = input().split()

stack = []

while string:
    stack.append(string.pop())

print(' '.join(stack))
