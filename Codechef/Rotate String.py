def can_rotate(s, goal):
    #write code here...
    
    return len(s) == len(goal) and goal in (s + s)