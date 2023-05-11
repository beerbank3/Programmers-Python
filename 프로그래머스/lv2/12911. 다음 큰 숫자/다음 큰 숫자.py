def solution(n):
    answer = 0
    for i in range(n+1,n*2):
        if bin(n)[2:].count(str(1)) == bin(i)[2:].count(str(1)):
            answer = i
            break
    return answer