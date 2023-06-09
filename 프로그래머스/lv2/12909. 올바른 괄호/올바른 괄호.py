def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append("(")
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        answer = False
    return answer