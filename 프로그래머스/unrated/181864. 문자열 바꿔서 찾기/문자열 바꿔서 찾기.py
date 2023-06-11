def solution(myString, pat):
    answer = ''
    for i in myString:
        if 'A' == i:
            answer += 'B'
        elif 'B' == i:
            answer += 'A'
    if pat in answer:
        return 1
    return 0