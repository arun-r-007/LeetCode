def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    if op == "^":
        return 3
    return 0

def infix_to_postfix(expr):
    stack = []
    output = ""

    for ch in expr:
        if ch.isalnum():
            output += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:
            while stack and (
                precedence(stack[-1]) > precedence(ch) or
                (precedence(stack[-1]) == precedence(ch) and ch != '^')
            ):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


# main
t = int(input())
while t:
    t -= 1
    expr = input()
    print(infix_to_postfix(expr))