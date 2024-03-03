def chessboard(x, y):
    result = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j)%2 == 0:
                if board[i][j] == 'W':
                    result += 1
            else:
                if board[i][j] == 'B':
                    result += 1
    return min(result, 64-result)
    

N, M = map(int, input().split())
board = []
result = 987654321
for _ in range(N):
    board.append(list(input()))

for i in range(N-7):
    for j in range(M-7):
        result = min(result, chessboard(i, j))

print(result)