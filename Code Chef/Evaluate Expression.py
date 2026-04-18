t = int(input())

while t:
    t -= 1
    
    n = int(input())
    expr = input()
    
    stack = []
    
    for ch in expr:
        
        # If operand → push
        if ch.isdigit():
            stack.append(int(ch))
        
        else:
            a = stack.pop()
            b = stack.pop()
            
            if ch == '+':
                stack.append(b + a)
            elif ch == '-':
                stack.append(b - a)
            elif ch == '*':
                stack.append(b * a)
            elif ch == '/':
                stack.append(b // a)   # integer division
    
    # Final result
    print(stack[-1])