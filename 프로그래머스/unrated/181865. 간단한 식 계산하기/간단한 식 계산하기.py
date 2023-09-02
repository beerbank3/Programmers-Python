def solution(binomial):
    tokens = binomial.split()

    if len(tokens) != 3:
        return "잘못된 입력"

    a = int(tokens[0])
    op = tokens[1]
    b = int(tokens[2])

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    else:
        return "잘못된 연산자"

    return result