import sys
n = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def solution(n):
    answer = 0
    array = [[0] * 100 for _ in range(100)]
    for i,j in n:
        for x in range(i,i+10):
            for y in range(j,j+10):
                array[x][y] = 1
    answer = sum(element == 1 for row in array for element in row)
    return answer


print(solution(data))