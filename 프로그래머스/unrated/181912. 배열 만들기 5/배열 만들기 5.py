def solution(intStrs, k, s, l):
    result = []
    
    for num_str in intStrs:
        start_index = s
        end_index = s + l

        sub_str = num_str[start_index:end_index]
        num = int(sub_str)
        
        if num > k:
            result.append(num)
    
    return result
