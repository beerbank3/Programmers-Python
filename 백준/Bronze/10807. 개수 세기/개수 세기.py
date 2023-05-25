import sys
a = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))
c = int(sys.stdin.readline().strip())
print(data.count(c))