def solution(arr):
    answer = []
    for i in arr:
        if 50 <= i and i % 2 == 0:
            answer.append(i/2)
        elif 50 >= i and i % 2 != 0:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer