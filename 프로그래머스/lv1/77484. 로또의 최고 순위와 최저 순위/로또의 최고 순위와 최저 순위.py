def solution(lottos, win_nums):
    answer = [7-lottos.count(0), 7]
    for i in win_nums:
        if i in lottos:
            answer[0] -= 1
            answer[1] -= 1
    
    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6
    return answer