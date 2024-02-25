N,M = map(int, input().split())
arr = list(i for i in range(1,N+1))
for i  in range(M):
    i,j = map(int, input().split())
    i, j = i-1, j
    arr[i:j] = arr[i:j][::-1]
print(*arr)