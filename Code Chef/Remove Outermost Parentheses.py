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

# def remove_outer_parentheses(s):
#     res = ""
#     count = 0

#     for ch in s:
#         if ch == '(':
#             if count > 0:
#                 res += ch
#             count += 1
#         else:
#             count -= 1
#             if count > 0:
#                 res += ch

#     return res