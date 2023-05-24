from collections import Counter
def solution(clothes):
    answer = 1
    c_dict = Counter(j for i,j in clothes)
    for i in c_dict.values():
        answer *= (i+1)
    return answer - 1