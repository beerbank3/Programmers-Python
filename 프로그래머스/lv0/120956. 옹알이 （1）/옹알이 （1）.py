import re
def solution(babbling):
    regex = re.compile(r'^(aya|ye|woo|ma)+$')
    answer = 0
    for i in babbling:
        if regex.match(i):
            answer += 1
    return answer