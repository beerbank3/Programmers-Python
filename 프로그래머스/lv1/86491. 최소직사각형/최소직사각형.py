def solution(sizes):
    answer = 0
    x = 0
    y = 0
    for i in sizes:
        if i[1] > i[0]:
            temp = i[0]
            i[0] = i[1]
            i[1] = temp
        if i[0] > x:
            x = i[0]
        if i[1] > y:
            y = i[1]
    answer = x * y
    return answer