def solution(k, tangerine):
    answer = 0
    total = 0
    num_dict = {}
    for i in tangerine:
        if not i in num_dict:
            num_dict.update({i : 1})
        else:
            num_dict.update({i : num_dict[i] +1})
    num_dict = sorted(num_dict.items(), key = lambda item: item[1], reverse=True)
    
    for i,j in num_dict:
        if total < k:
            total += j
            answer += 1
        else:
            break
    return answer