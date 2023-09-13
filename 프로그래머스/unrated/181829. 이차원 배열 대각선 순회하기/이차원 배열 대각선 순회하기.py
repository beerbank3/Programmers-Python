def solution(board, k):
    rows = len(board)
    cols = len(board[0])
    total_sum = 0

    for i in range(rows):
        for j in range(cols):
            if i + j <= k:
                total_sum += board[i][j]

    return total_sum