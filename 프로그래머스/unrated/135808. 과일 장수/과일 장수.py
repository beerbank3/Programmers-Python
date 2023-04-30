def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i,j in enumerate(score):
        if (i+1) % m == 0:
            answer += j * m
    return answer