import re
def solution(dartResult):
    answer = []
    pattern = '[0-9]{1,2}(D|S|T)(#|\*|)'
    a = re.finditer(pattern,dartResult)
    num = 0
    for i in a:
        num = int(re.search('[0-9]{1,2}',i.group()).group())
        for j in i.group():
            if 'D' in j:
                num **= 2
                continue
            if 'T' in j:
                num **= 3
                continue
            if '*' in j:
                num *= 2
                if len(answer) > 0:
                    answer[-1] *= 2
                continue
            if '#' in j:
                num *= -1
        answer.append(num)
    
    return sum(answer)