def solution(n, computers):
  visited = [False] * n
  answer = 0

  for i in range(n):
    if not visited[i]:
      answer += 1
      dfs(i, visited, computers)

  return answer

def dfs(x, visited, computers):
  visited[x] = True

  for y in range(len(computers[x])):
    if computers[x][y] == 1 and not visited[y]:
      dfs(y, visited, computers)