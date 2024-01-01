from collections import deque

def solution(s):
    s_queue = deque(s)
    brackets = []
    
    while s_queue:
        temp = s_queue.popleft()
        if brackets and brackets[-1] == '(' and temp == ')':
            brackets.pop()
        else:
            brackets.append(temp)
    
    if brackets:
        return False
    else:
        return True
