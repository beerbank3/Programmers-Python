total = int(input())
N = int(input())
for i in range(N):
    a, b= map(int, input().split())
    total -= a * b
print('Yes' if total == 0 else 'No')

