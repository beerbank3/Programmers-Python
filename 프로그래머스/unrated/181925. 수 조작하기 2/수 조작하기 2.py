def solution(numLog):
    result = []
    current_num = 0

    for i in range(len(numLog)):
        diff = numLog[i] - current_num

        if diff == 1:
            result.append("w")
        elif diff == -1:
            result.append("s")
        elif diff == 10:
            result.append("d")
        elif diff == -10:
            result.append("a")
        
        current_num = numLog[i]

    return ''.join(result)