from collections import deque
def solution(numbers, target):
    answer = 0
    number_list = deque()
    for i in numbers:
        if not number_list:
            number_list.append(i)
            number_list.append(-i)
            continue
        for j in range(len(number_list)):
            que_num = number_list.popleft()
            number_list.append(que_num+i)
            number_list.append(que_num-i)
    
    answer = number_list.count(target)
    return answer