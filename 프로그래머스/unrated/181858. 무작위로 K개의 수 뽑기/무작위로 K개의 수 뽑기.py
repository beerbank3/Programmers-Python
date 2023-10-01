def solution(arr, k):
    result = []
    num_set = set()

    for num in arr:
        if num not in num_set:
            result.append(num)
            num_set.add(num)
        
        if len(result) == k:
            break

    while len(result) < k:
        result.append(-1)

    return result