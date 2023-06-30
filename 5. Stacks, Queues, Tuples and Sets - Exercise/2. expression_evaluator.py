from collections import deque

expression = input().split()

numbers = deque()

for symbol in expression:
    if symbol.lstrip("-").isnumeric():
        numbers.append(int(symbol))
    else:
        if symbol == "*":
            while len(numbers) > 1:
                result = numbers.popleft() * numbers.popleft()
                numbers.appendleft(result)
        elif symbol == "+":
            while len(numbers) > 1:
                result = numbers.popleft() + numbers.popleft()
                numbers.appendleft(result)
        elif symbol == "-":
            while len(numbers) > 1:
                result = numbers.popleft() - numbers.popleft()
                numbers.appendleft(result)
        elif symbol == "/":
            while len(numbers) > 1:
                result = int(numbers.popleft() / numbers.popleft())
                numbers.appendleft(result)

print(numbers.popleft())
