N,M = map(int, input().split())
arr = ['0' for i in range(N)] 
for i in range(M):
    x, y, z = map(int, input().split())
    for i in range(x-1, y):
        arr[i] = str(z)
print(' '.join(i for i in arr))