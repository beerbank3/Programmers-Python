def solution(name, yearning, photo):
    answer =[]
    for p in enumerate(photo):
        num = 0
        for i , j in zip(name,yearning):
            if i in p[1]:
                num += j
        answer.append(num)
    return answer