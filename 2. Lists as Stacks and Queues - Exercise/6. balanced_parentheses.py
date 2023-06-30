sequence = input()

balanced_parentheses = True

stack = []

for element in sequence:
    if element == "(" or element == "{" or element == "[":
        stack.append(element)
    elif element == ")":
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            balanced_parentheses = False
            break
    elif element == "}":
        if stack and stack[-1] == "{":
            stack.pop()
        else:
            balanced_parentheses = False
            break
    elif element == "]":
        if stack and stack[-1] == "[":
            stack.pop()
        else:
            balanced_parentheses = False
            break

if balanced_parentheses:
    print("YES")
else:
    print("NO")
