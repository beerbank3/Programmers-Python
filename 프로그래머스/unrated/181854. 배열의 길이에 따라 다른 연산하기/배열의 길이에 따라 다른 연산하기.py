def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        index = 1
    else:
        index = 0
        
    for i in range(index,len(arr),2):
        arr[i] += n
        
    return arr