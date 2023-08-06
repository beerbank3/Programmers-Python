def solution(n):
    answer = [n]
    num = n
    while num != 1:
        if num % 2 == 0:
            answer.append(num/2)
            num = num / 2
        else:
            answer.append((num*3)+1)
            num = (num * 3) + 1
    return answer