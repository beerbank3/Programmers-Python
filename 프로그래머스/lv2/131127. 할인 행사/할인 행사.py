from collections import Counter
def solution(want, number, discount):
    answer = 0
    num = sum(number)
    p_dict = dict(zip(want,number))
    for i in range(len(discount)-num+1):
        d_dict = Counter(discount[i:num+i])
        if p_dict.items() == d_dict.items():
            answer+=1
    return answer