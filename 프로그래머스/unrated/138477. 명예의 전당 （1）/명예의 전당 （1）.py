def solution(k, score):
    answer = []
    number = []
    for i in score:
        number.append(i)
        if len(number) == k+1:
            number.remove(min(number))
        answer.append(min(number))
    return answer