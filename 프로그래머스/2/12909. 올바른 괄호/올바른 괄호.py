def solution(s):
    stack = []

    for b in s:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) == 0: 
                return False
            stack.pop()
            
    if len(stack) == 0:
        return True
    else:
        return False