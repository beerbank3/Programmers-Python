def solution(num_list):
    answer = 0
    x = ''
    y = ''
    for i in num_list:
        if i % 2 == 0 :
            x += str(i)
        else:
            y += str(i)
    answer = int(x) + int(y)
    return answer