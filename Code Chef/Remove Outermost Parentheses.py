def remove_outer_parentheses(s):
    # Write your code here...
    stack = []
    res = ""

    for ch in s:
        if ch == '(':
            if stack:
                res += ch
            stack.append(ch)
        else:
            stack.pop()
            if stack:
                res += ch

    return res