def solution(brown, yellow):
    answer = [0,0]
    for i in range(brown):
        for j in range(brown):
            if i*j == brown+yellow and j >= i and ((j*2)+(i-2)*2)==brown:
                answer = [j,i]
                
    return answer