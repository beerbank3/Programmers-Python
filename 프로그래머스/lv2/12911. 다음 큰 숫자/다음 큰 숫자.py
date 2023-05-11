def solution(n):
    answer = 0
    num = bin(n)[2:].count(str(1))
    for i in range(n+1,n*2+1):
        if num == bin(i)[2:].count(str(1)):
            answer = i
            break
    return answer