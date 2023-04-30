def solution(N, stages):
    answer = []
    number_count= []
    number_sum = {}
    for i in range(1,N+2):
        number_count.append(stages.count(i))
    
    for a, b in enumerate(number_count):
        if b > 0:
            number_sum.update({a+1:b / sum(number_count[a:])})

    if number_sum.get(N+1):
        del(number_sum[N+1])
    number_sum = sorted(number_sum.items(), key = lambda item : item[1], reverse=True)
    for key , value in number_sum:
        answer.append(key)
    for num in range(1,N+1):
        if not answer.count(num):
            answer.append(num)
    return answer