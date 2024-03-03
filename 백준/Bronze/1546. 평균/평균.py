N = int(input())
points = list(map(int, input().split()))
MAX = max(points)
for i  in range(N):
    points[i] = points[i] / MAX * 100

print(sum(points) / N)
