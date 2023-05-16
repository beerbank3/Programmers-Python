def solution(A, B):
    answer = 0
    A.sort(reverse =True)
    B.sort(reverse =True)
    n = 0
    for i in A:
        if i < B[n]:
            answer += 1
            n += 1
    
    return answer