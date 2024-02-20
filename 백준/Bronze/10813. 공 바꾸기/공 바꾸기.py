N,M = map(int, input().split())
arr = [str(i+1) for i in range(N)] 
for i in range(M):
    x, y = map(int, input().split())
    temp = arr[x-1]
    arr[x-1] = arr[y-1]
    arr[y-1] = temp

print(' '.join(i for i in arr))