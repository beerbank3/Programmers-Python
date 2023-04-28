def solution(s):
    answer = []
    dict = {}
    for i in enumerate(s):
        if dict.get(i[1]) == 0 or dict.get(i[1]):
            answer.append(i[0]-dict.get(i[1]))
            dict.update({i[1]:i[0]})
        else:
            answer.append(-1)
            dict.update({i[1]: i[0]})
    return answer