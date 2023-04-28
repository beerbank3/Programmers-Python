def solution(price, money, count):
    answer = 0
    sum = 0
    for i in range(count+1):
        sum += price*i
    if sum - money > 0:
        answer = sum - money
    return answer