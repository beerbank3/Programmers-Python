def solution(X, Y):
    answer = ''
    for i in range(10):
        i = str(i)
        if min(X.count(i),Y.count(i)) > 0:
            answer += i * min(X.count(i),Y.count(i))

    answer = ''.join(sorted(list(answer),reverse=True))
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer