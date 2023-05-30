def solution(n, control):
    answer = n
    for i in control:
        if "w" == i:
            answer += 1
        elif "s" == i:
            answer -= 1
        elif "d" == i:
            answer +=10
        elif "a" == i:
            answer -= 10
    return answer