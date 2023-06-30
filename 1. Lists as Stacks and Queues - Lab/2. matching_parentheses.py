expression = input()

stack = []

for index in range(len(expression)):
    symbol = expression[index]
    if symbol == "(":
        stack.append(index)
    elif symbol == ")":
        opening_bracket = stack.pop()
        parentheses = expression[opening_bracket:index+1]
        print(''.join(parentheses))
