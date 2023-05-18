def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i,j in enumerate(citations):
        if j >= n-i:
            answer+=1
    return answer