def solution(absolutes, signs):
    answer = 0
    i = 0
    for sign in signs:
        if sign:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        i+= 1
    return answer