def solution(arr, queries):
    answer = []
    for i, j in queries:
        temp = arr[i] 
        arr[i] = arr[j]
        arr[j] = temp
    
    answer = arr
    return answer