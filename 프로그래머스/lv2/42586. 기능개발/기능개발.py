def solution(progresses, speeds):
    answer = []
    temp = []
    index = 0
    for i , j in zip(progresses, speeds):
        count = 0
        while i < 100:
            i += j
            count +=1
        temp.append(count)
    while temp:
        count = 0
        if temp[0] <= index:
             while temp and temp[0] <= index:
                temp.pop(0)
                count += 1
        if count != 0:
            answer.append(count)
        index+=1
    return answer