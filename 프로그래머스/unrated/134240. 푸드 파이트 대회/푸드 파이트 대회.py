def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] // 2 > 0:
            answer += str(i) * int(food[i] // 2)
    answer += '0'+''.join(sorted(answer,reverse = True))
    return answer