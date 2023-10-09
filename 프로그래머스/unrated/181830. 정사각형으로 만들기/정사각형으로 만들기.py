def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])
    

    if num_rows > num_cols:
        for row in arr:
            while len(row) < num_rows:
                row.append(0)

    elif num_cols > num_rows:
        while len(arr) < num_cols:
            arr.append([0] * num_cols)
    
    return arr