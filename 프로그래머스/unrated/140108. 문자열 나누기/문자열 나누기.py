def solution(s):
    answer = 0
    word = ""
    stack = []
    for i in s:
        if not stack:
            word = i
        
        if word == i:
            stack.append(i)
        else:
            stack.pop()
            
        if not stack:
            answer += 1
    if stack:
        answer += 1
    return answer