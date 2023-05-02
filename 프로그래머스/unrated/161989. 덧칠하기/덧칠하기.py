def solution(n, m, section):
    answer = 0
    paint = 0
    for i in section:
        if paint < i:
            answer += 1
            paint = i + m -1
        
    return answer